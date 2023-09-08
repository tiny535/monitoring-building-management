import React, { useEffect, useState } from "react";
import "./App.css";
import Header from "./components/Header";
import { Button, Input, Space, Table } from "antd";
import { SearchOutlined } from "@ant-design/icons";
import { useRef } from "react";
import Indicator from "./components/Indicator/Indicator";
function App() {
  const searchInput = useRef(null);
  const convertToData = (value, index) => {
    const percent = Math.round((value.currentOccupancy / value.capacity) * 100);
    return {
      ...value,
      key: index,
      percentageFilled: `${percent}%`,
      bulb: <Indicator percentageFilled={percent} />
    };
  };
  const [intervalTimer, setIntervalTimer] = useState(null);
  const [dataSource, setDataSource] = useState([]);
  const [isLoading, setIsLoading] = useState(true);
  useEffect(() => {
    const url = "http://localhost:8080";
    const fetchDataSource = async () => {
      const data = await fetch(url, { method: "GET", mode: "cors" });
      const json = await data.json();
      if (isLoading) {
        setIsLoading(false);
      }
      setDataSource([...json].map((value, index) => convertToData(value, index)));
    };
    fetchDataSource();
    if (intervalTimer) {
      return;
    }
    const intervalId = setInterval(fetchDataSource, 300000);
    setIntervalTimer(intervalId);
  }, []);
  
  const handleReset = (clearFilters, confirm) => {
    clearFilters();
    confirm();
  };
  const getColumnSearchProps = (dataIndex) => ({
    filterDropdown: ({ setSelectedKeys, selectedKeys, confirm, clearFilters }) => (
      <div
        style={{
          padding: 8,
        }}
        onKeyDown={(e) => e.stopPropagation()}
      >
        <Input
          ref={searchInput}
          placeholder={`Search ${dataIndex}`}
          value={selectedKeys[0]}
          onChange={(e) => setSelectedKeys(e.target.value ? [e.target.value] : [])}
          onPressEnter={confirm}
          style={{
            marginBottom: 8,
            display: "block",
          }}
        />
        <Space>
          <Button
            type="primary"
            onClick={confirm}
            icon={<SearchOutlined />}
            size="small"
            style={{
              width: 90,
            }}
          >
            Search
          </Button>
          <Button
            onClick={() => clearFilters && handleReset(clearFilters, confirm)}
            size="small"
            style={{
              width: 90,
            }}
          >
            Reset
          </Button>
        </Space>
      </div>
    ),
    filterIcon: (filtered) => (
      <SearchOutlined
        style={{
          color: filtered ? "#1677ff" : undefined,
        }}
      />
    ),
    onFilter: (value, record) =>
      record[dataIndex].toString().toLowerCase().includes(value.toLowerCase()),
    onFilterDropdownOpenChange: (visible) => {
      if (visible) {
        setTimeout(() => searchInput.current?.select(), 100);
      }
    },
  });
  const columns = [
    {
      title: "Building Name",
      dataIndex: "buildingName",
      key: "building-name",
      sorter: (a, b) => a.buildingName.localeCompare(b.buildingName),
      ...getColumnSearchProps("buildingName"),
    },
    {
      title: "Building Code",
      dataIndex: "buildingCode",
      key: "building-code",
      sorter: (a, b) => a.buildingCode.localeCompare(b.buildingCode),
      ...getColumnSearchProps("buildingCode"),
    },
    {
      title: "Room Name",
      dataIndex: "roomName",
      key: "room-name",
      sorter: (a, b) => a.roomName.localeCompare(b.roomName),
      ...getColumnSearchProps("roomName"),
    },
    {
      title: "Capacity",
      dataIndex: "capacity",
      key: "capacity",
    },
    {
      title: "Current Occupancy",
      dataIndex: "currentOccupancy",
      key: "current-occupancy",
    },
    {
      title: "Percentage Filled",
      dataIndex: "percentageFilled",
      key: "percentage-filled",
    },
    {
      title: "Indicator",
      dataIndex: "bulb",
      key: "bulb",
    },
  ];
  return (
    <div className="App">
      <Header />
      <Table
        columns={columns}
        dataSource={dataSource}
        loading={isLoading}
      />
    </div>
  );
}
export default App;