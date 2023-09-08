import React from "react";
import classnames from "classnames";
import { BulbFilled } from "@ant-design/icons";
import PropTypes from "prop-types";
import "./Indicator.css";

const Indicator = ({ percentageFilled }) => {
  const className = {
    "bulb": true
  };
  let colourClass = "green";
  if (percentageFilled >= 50) {
    colourClass = "yellow";
  }
    
  if (percentageFilled >= 75) {
    colourClass = "red";
  }
  className[colourClass] = true;
  return <div className={classnames(className)}>
    <BulbFilled />
  </div>;
};

Indicator.propTypes = {
  percentageFilled: PropTypes.number,
};

export default Indicator;