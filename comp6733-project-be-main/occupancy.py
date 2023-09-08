'''
- This code should be run from the base of the repository (../comp6733-project-be)
'''
from reconciliation import reconcilation
import random

def get_rooms():
    """
    Return Type: 
    [
      {
        buildingName: String,
        buildingCode: String,
        roomName: String,
        capacity: Integer,
        currentOccupancy: Integer,
      }
    ]
    """
    
    occupancy = reconcilation()
    return [
 {
     "buildingName": "Demo Building",
     "buildingCode": "DB01",
     "roomName": "Demo Room",
     "capacity": 18,
     "currentOccupancy": occupancy
 },
 {
   "buildingName": "AGSM",
   "buildingCode": " G27",
   "roomName": " AGSM Hugh Dixson Theatre",
   "capacity": 56,
   "currentOccupancy": random.randint(0, 56)
 },
 {
   "buildingName": "AGSM",
   "buildingCode": " G27",
   "roomName": " Pioneer International Theatre",
   "capacity": 57,
   "currentOccupancy": random.randint(0, 57)
 },
 {
   "buildingName": "AGSM",
   "buildingCode": " G27",
   "roomName": " AGSM Boral Theatre",
   "capacity": 52,
   "currentOccupancy": random.randint(0, 52)
 },
 {
   "buildingName": "AGSM",
   "buildingCode": " G27",
   "roomName": " AGSM Colonial Theatre",
   "capacity": 43,
   "currentOccupancy": random.randint(0, 43)
 },
 {
   "buildingName": "AGSM",
   "buildingCode": " G27",
   "roomName": " John B Reid Theatre",
   "capacity": 131,
   "currentOccupancy": random.randint(0, 131)
 },
 {
   "buildingName": "AGSM",
   "buildingCode": " G27",
   "roomName": " AGSM LG06",
   "capacity": 30,
   "currentOccupancy": random.randint(0, 30)
 },
 {
   "buildingName": "AGSM",
   "buildingCode": " G27",
   "roomName": " AGSM LG07",
   "capacity": 30,
   "currentOccupancy": random.randint(0, 30)
 },
 {
   "buildingName": "Ainsworth Building",
   "buildingCode": " J17",
   "roomName": " Ainsworth 101",
   "capacity": 50,
   "currentOccupancy": random.randint(0, 50)
 },
 {
   "buildingName": "Ainsworth Building",
   "buildingCode": " J17",
   "roomName": " Ainsworth 102",
   "capacity": 100,
   "currentOccupancy": random.randint(0, 100)
 },
 {
   "buildingName": "Ainsworth Building",
   "buildingCode": " J17",
   "roomName": " Ainsworth 201",
   "capacity": 50,
   "currentOccupancy": random.randint(0, 50)
 },
 {
   "buildingName": "Ainsworth Building",
   "buildingCode": " J17",
   "roomName": " Ainsworth 202",
   "capacity": 100,
   "currentOccupancy": random.randint(0, 100)
 },
 {
   "buildingName": "Ainsworth Building",
   "buildingCode": " J17",
   "roomName": " Ainsworth G01",
   "capacity": 50,
   "currentOccupancy": random.randint(0, 50)
 },
 {
   "buildingName": "Ainsworth Building",
   "buildingCode": " J17",
   "roomName": " Ainsworth G02",
   "capacity": 100,
   "currentOccupancy": random.randint(0, 100)
 },
 {
   "buildingName": "Ainsworth Building",
   "buildingCode": " J17",
   "roomName": " Ainsworth G03",
   "capacity": 350,
   "currentOccupancy": random.randint(0, 350)
 },
 {
   "buildingName": "Anita B. Lawrence Centre",
   "buildingCode": " H13",
   "roomName": " H13 Lawrence East 1040",
   "capacity": 56,
   "currentOccupancy": random.randint(0, 56)
 },
 {
   "buildingName": "Anita B. Lawrence Centre",
   "buildingCode": " H13",
   "roomName": " H13 Lawrence East 1041",
   "capacity": 48,
   "currentOccupancy": random.randint(0, 48)
 },
 {
   "buildingName": "Anita B. Lawrence Centre",
   "buildingCode": " H13",
   "roomName": " H13 Lawrence East 1042",
   "capacity": 48,
   "currentOccupancy": random.randint(0, 48)
 },
 {
   "buildingName": "Anita B. Lawrence Centre",
   "buildingCode": " H13",
   "roomName": " H13 Lawrence East 1040",
   "capacity": 48,
   "currentOccupancy": random.randint(0, 48)
 },
 {
   "buildingName": "Anita B. Lawrence Centre",
   "buildingCode": " H13",
   "roomName": " H13 Lawrence West 2035",
   "capacity": 26,
   "currentOccupancy": random.randint(0, 26)
 },
 {
   "buildingName": "Anita B. Lawrence Centre",
   "buildingCode": " H13",
   "roomName": " H13 Lawrence East 2060",
   "capacity": 48,
   "currentOccupancy": random.randint(0, 48)
 },
 {
   "buildingName": "Anita B. Lawrence Centre",
   "buildingCode": " H13",
   "roomName": " H13 Lawrence East 2061",
   "capacity": 48,
   "currentOccupancy": random.randint(0, 48)
 },
 {
   "buildingName": "Anita B. Lawrence Centre",
   "buildingCode": " H13",
   "roomName": " H13 Lawrence East 2062",
   "capacity": 48,
   "currentOccupancy": random.randint(0, 48)
 },
 {
   "buildingName": "Anita B. Lawrence Centre",
   "buildingCode": " H13",
   "roomName": " H13 Lawrence East 2063",
   "capacity": 48,
   "currentOccupancy": random.randint(0, 48)
 },
 {
   "buildingName": "Anita B. Lawrence Centre",
   "buildingCode": " H13",
   "roomName": " H13 Lawrence West 3037",
   "capacity": 26,
   "currentOccupancy": random.randint(0, 26)
 },
 {
   "buildingName": "Anita B. Lawrence Centre",
   "buildingCode": " H13",
   "roomName": " H13 Lawrence West 4034",
   "capacity": 26,
   "currentOccupancy": random.randint(0, 26)
 },
 {
   "buildingName": "Anita B. Lawrence Centre",
   "buildingCode": " H13",
   "roomName": " H13 Lawrence West 4037",
   "capacity": 26,
   "currentOccupancy": random.randint(0, 26)
 },
 {
   "buildingName": "Anita B. Lawrence Centre",
   "buildingCode": " H13",
   "roomName": " H13 Lawrence Theatre",
   "capacity": 117,
   "currentOccupancy": random.randint(0, 117)
 },
 {
   "buildingName": "Anita B. Lawrence Centre",
   "buildingCode": " H13",
   "roomName": " H13 Lawrence West M010",
   "capacity": 44,
   "currentOccupancy": random.randint(0, 44)
 },
 {
   "buildingName": "Anita B. Lawrence Centre",
   "buildingCode": " H13",
   "roomName": " H13 Lawrence East M032",
   "capacity": 89,
   "currentOccupancy": random.randint(0, 89)
 },
 {
   "buildingName": "Biological Sciences (North)",
   "buildingCode": " D26",
   "roomName": " Bioscience G07",
   "capacity": 63,
   "currentOccupancy": random.randint(0, 63)
 },
 {
   "buildingName": "Blockhouse",
   "buildingCode": " G6",
   "roomName": " Blockhouse G13",
   "capacity": 38,
   "currentOccupancy": random.randint(0, 38)
 },
 {
   "buildingName": "Blockhouse",
   "buildingCode": " G6",
   "roomName": " Blockhouse G14",
   "capacity": 38,
   "currentOccupancy": random.randint(0, 38)
 },
 {
   "buildingName": "Blockhouse",
   "buildingCode": " G6",
   "roomName": " Blockhouse G15",
   "capacity": 38,
   "currentOccupancy": random.randint(0, 38)
 },
 {
   "buildingName": "Blockhouse",
   "buildingCode": " G6",
   "roomName": " Blockhouse G16",
   "capacity": 38,
   "currentOccupancy": random.randint(0, 38)
 },
 {
   "buildingName": "Blockhouse",
   "buildingCode": " G6",
   "roomName": " Blockhouse G6",
   "capacity": 38,
   "currentOccupancy": random.randint(0, 38)
 },
 {
   "buildingName": "Civil Engineering Building",
   "buildingCode": " H20",
   "roomName": " Civil Engineering 101",
   "capacity": 118,
   "currentOccupancy": random.randint(0, 118)
 },
 {
   "buildingName": "Civil Engineering Building",
   "buildingCode": " H20",
   "roomName": " Civil Engineering 102",
   "capacity": 53,
   "currentOccupancy": random.randint(0, 53)
 },
 {
   "buildingName": "Civil Engineering Building",
   "buildingCode": " H20",
   "roomName": " Civil Engineering 109",
   "capacity": 108,
   "currentOccupancy": random.randint(0, 108)
 },
 {
   "buildingName": "Civil Engineering Building",
   "buildingCode": " H20",
   "roomName": " Civil Engineering 701",
   "capacity": 56,
   "currentOccupancy": random.randint(0, 56)
 },
 {
   "buildingName": "Civil Engineering Building",
   "buildingCode": " H20",
   "roomName": " Civil Engineering G1",
   "capacity": 106,
   "currentOccupancy": random.randint(0, 106)
 },
 {
   "buildingName": "Civil Engineering Building",
   "buildingCode": " H20",
   "roomName": " Civil Engineering G6",
   "capacity": 36,
   "currentOccupancy": random.randint(0, 36)
 },
 {
   "buildingName": "Civil Engineering Building",
   "buildingCode": " H20",
   "roomName": " Civil Engineering G8",
   "capacity": 64,
   "currentOccupancy": random.randint(0, 64)
 },
 {
   "buildingName": "Colombo Building",
   "buildingCode": " B16",
   "roomName": " Colombo LG01",
   "capacity": 48,
   "currentOccupancy": random.randint(0, 48)
 },
 {
   "buildingName": "Colombo Building",
   "buildingCode": " B16",
   "roomName": " Colombo LG02",
   "capacity": 56,
   "currentOccupancy": random.randint(0, 56)
 },
 {
   "buildingName": "Colombo Building",
   "buildingCode": " B16",
   "roomName": " Colombo Theatre A",
   "capacity": 223,
   "currentOccupancy": random.randint(0, 223)
 },
 {
   "buildingName": "Colombo Building",
   "buildingCode": " B16",
   "roomName": " Colombo Theatre B",
   "capacity": 154,
   "currentOccupancy": random.randint(0, 154)
 },
 {
   "buildingName": "Colombo Building",
   "buildingCode": " B16",
   "roomName": " Colombo Theatre C",
   "capacity": 154,
   "currentOccupancy": random.randint(0, 154)
 },
 {
   "buildingName": "Electrical Engineering Building",
   "buildingCode": " G17",
   "roomName": " Electrical Engineering G03",
   "capacity": 54,
   "currentOccupancy": random.randint(0, 54)
 },
 {
   "buildingName": "Electrical Engineering Building",
   "buildingCode": " G17",
   "roomName": " Electrical Engineering G04",
   "capacity": 48,
   "currentOccupancy": random.randint(0, 48)
 },
 {
   "buildingName": "Electrical Engineering Building",
   "buildingCode": " G17",
   "roomName": " Electrical Engineering G09",
   "capacity": 54,
   "currentOccupancy": random.randint(0, 54)
 },
 {
   "buildingName": "Electrical Engineering Building",
   "buildingCode": " G17",
   "roomName": " Electrical Engineering G10",
   "capacity": 54,
   "currentOccupancy": random.randint(0, 54)
 },
 {
   "buildingName": "Electrical Engineering Building",
   "buildingCode": " G17",
   "roomName": " Electrical Engineering G22",
   "capacity": 148,
   "currentOccupancy": random.randint(0, 148)
 },
 {
   "buildingName": "Electrical Engineering Building",
   "buildingCode": " G17",
   "roomName": " Electrical Engineering G23",
   "capacity": 148,
   "currentOccupancy": random.randint(0, 148)
 },
 {
   "buildingName": "Goldstein Hall",
   "buildingCode": " D16",
   "roomName": " Goldstein G01",
   "capacity": 38,
   "currentOccupancy": random.randint(0, 38)
 },
 {
   "buildingName": "Goldstein Hall",
   "buildingCode": " D16",
   "roomName": " Goldstein G02",
   "capacity": 30,
   "currentOccupancy": random.randint(0, 30)
 },
 {
   "buildingName": "Goldstein Hall",
   "buildingCode": " D16",
   "roomName": " Goldstein G03",
   "capacity": 40,
   "currentOccupancy": random.randint(0, 40)
 },
 {
   "buildingName": "Goldstein Hall",
   "buildingCode": " D16",
   "roomName": " Goldstein G04",
   "capacity": 18,
   "currentOccupancy": random.randint(0, 18)
 },
 {
   "buildingName": "Goldstein Hall",
   "buildingCode": " D16",
   "roomName": " Goldstein G05",
   "capacity": 24,
   "currentOccupancy": random.randint(0, 24)
 },
 {
   "buildingName": "Goldstein Hall",
   "buildingCode": " D16",
   "roomName": " Goldstein G06",
   "capacity": 28,
   "currentOccupancy": random.randint(0, 28)
 },
 {
   "buildingName": "Goldstein Hall",
   "buildingCode": " D16",
   "roomName": " Goldstein G07",
   "capacity": 24,
   "currentOccupancy": random.randint(0, 24)
 },
 {
   "buildingName": "Goldstein Hall",
   "buildingCode": " D16",
   "roomName": " Goldstein G09",
   "capacity": 42,
   "currentOccupancy": random.randint(0, 42)
 },
 {
   "buildingName": "John Goodsell Building",
   "buildingCode": " F20",
   "roomName": " John Goodsell LG19",
   "capacity": 42,
   "currentOccupancy": random.randint(0, 42)
 },
 {
   "buildingName": "John Goodsell Building",
   "buildingCode": " F20",
   "roomName": " John Goodsell LG21",
   "capacity": 42,
   "currentOccupancy": random.randint(0, 42)
 },
 {
   "buildingName": "John Niland Scientia",
   "buildingCode": " G19",
   "roomName": " Ritchie Theatre",
   "capacity": 266,
   "currentOccupancy": random.randint(0, 266)
 },
 {
   "buildingName": "June Griffith Building",
   "buildingCode": " F10",
   "roomName": " F10 June Griffith M10",
   "capacity": 98,
   "currentOccupancy": random.randint(0, 98)
 },
 {
   "buildingName": "June Griffith Building",
   "buildingCode": " F10",
   "roomName": " F10 June Griffith M11",
   "capacity": 97,
   "currentOccupancy": random.randint(0, 97)
 },
 {
   "buildingName": "June Griffith Building",
   "buildingCode": " F10",
   "roomName": " F10 June Griffith M17",
   "capacity": 253,
   "currentOccupancy": random.randint(0, 253)
 },
 {
   "buildingName": "June Griffith Building",
   "buildingCode": " F10",
   "roomName": " F10 June Griffith M18",
   "capacity": 205,
   "currentOccupancy": random.randint(0, 205)
 },
 {
   "buildingName": "Keith Burrows Theatre",
   "buildingCode": " J14",
   "roomName": " Keith Burrows Theatre",
   "capacity": 438,
   "currentOccupancy": random.randint(0, 438)
 },
 {
   "buildingName": "Law Building",
   "buildingCode": " F8",
   "roomName": " Law Building 101",
   "capacity": 44,
   "currentOccupancy": random.randint(0, 44)
 },
 {
   "buildingName": "Law Building",
   "buildingCode": " F8",
   "roomName": " Law Building 111",
   "capacity": 32,
   "currentOccupancy": random.randint(0, 32)
 },
 {
   "buildingName": "Law Building",
   "buildingCode": " F8",
   "roomName": " Law Building 162",
   "capacity": 44,
   "currentOccupancy": random.randint(0, 44)
 },
 {
   "buildingName": "Law Building",
   "buildingCode": " F8",
   "roomName": " Law Building 163",
   "capacity": 44,
   "currentOccupancy": random.randint(0, 44)
 },
 {
   "buildingName": "Law Building",
   "buildingCode": " F8",
   "roomName": " Law Building 201",
   "capacity": 44,
   "currentOccupancy": random.randint(0, 44)
 },
 {
   "buildingName": "Law Building",
   "buildingCode": " F8",
   "roomName": " Law Building 202",
   "capacity": 44,
   "currentOccupancy": random.randint(0, 44)
 },
 {
   "buildingName": "Law Building",
   "buildingCode": " F8",
   "roomName": " Law Building 203",
   "capacity": 56,
   "currentOccupancy": random.randint(0, 56)
 },
 {
   "buildingName": "Law Building",
   "buildingCode": " F8",
   "roomName": " Law Building 275",
   "capacity": 44,
   "currentOccupancy": random.randint(0, 44)
 },
 {
   "buildingName": "Law Building",
   "buildingCode": " F8",
   "roomName": " Law Building 276",
   "capacity": 44,
   "currentOccupancy": random.randint(0, 44)
 },
 {
   "buildingName": "Law Building",
   "buildingCode": " F8",
   "roomName": " Law Building 301",
   "capacity": 44,
   "currentOccupancy": random.randint(0, 44)
 },
 {
   "buildingName": "Law Building",
   "buildingCode": " F8",
   "roomName": " Law Building 302",
   "capacity": 44,
   "currentOccupancy": random.randint(0, 44)
 },
 {
   "buildingName": "Law Building",
   "buildingCode": " F8",
   "roomName": " Law Building 388",
   "capacity": 44,
   "currentOccupancy": random.randint(0, 44)
 },
 {
   "buildingName": "Law Building",
   "buildingCode": " F8",
   "roomName": " Law Building 389",
   "capacity": 44,
   "currentOccupancy": random.randint(0, 44)
 },
 {
   "buildingName": "Law Building",
   "buildingCode": " F8",
   "roomName": " Law Theatre G02",
   "capacity": 90,
   "currentOccupancy": random.randint(0, 90)
 },
 {
   "buildingName": "Law Building",
   "buildingCode": " F8",
   "roomName": " Law Theatre G04",
   "capacity": 347,
   "currentOccupancy": random.randint(0, 347)
 },
 {
   "buildingName": "Law Building",
   "buildingCode": " F8",
   "roomName": " Law Library G17",
   "capacity": 44,
   "currentOccupancy": random.randint(0, 44)
 },
 {
   "buildingName": "Law Building",
   "buildingCode": " F8",
   "roomName": " Law Theatre G23",
   "capacity": 90,
   "currentOccupancy": random.randint(0, 90)
 },
 {
   "buildingName": "Library Stage 2",
   "buildingCode": " F21",
   "roomName": " Library 176A",
   "capacity": 24,
   "currentOccupancy": random.randint(0, 24)
 },
 {
   "buildingName": "Library Stage 2",
   "buildingCode": " F21",
   "roomName": " Library 176B",
   "capacity": 24,
   "currentOccupancy": random.randint(0, 24)
 },
 {
   "buildingName": "Mathews Building",
   "buildingCode": " F23",
   "roomName": " Mathews 101",
   "capacity": 56,
   "currentOccupancy": random.randint(0, 56)
 },
 {
   "buildingName": "Mathews Building",
   "buildingCode": " F23",
   "roomName": " Mathews 102",
   "capacity": 56,
   "currentOccupancy": random.randint(0, 56)
 },
 {
   "buildingName": "Mathews Building",
   "buildingCode": " F23",
   "roomName": " Mathews 103",
   "capacity": 84,
   "currentOccupancy": random.randint(0, 84)
 },
 {
   "buildingName": "Mathews Building",
   "buildingCode": " F23",
   "roomName": " Mathews 104",
   "capacity": 54,
   "currentOccupancy": random.randint(0, 54)
 },
 {
   "buildingName": "Mathews Building",
   "buildingCode": " F23",
   "roomName": " Mathews 105",
   "capacity": 54,
   "currentOccupancy": random.randint(0, 54)
 },
 {
   "buildingName": "Mathews Building",
   "buildingCode": " F23",
   "roomName": " Mathews 106",
   "capacity": 40,
   "currentOccupancy": random.randint(0, 40)
 },
 {
   "buildingName": "Mathews Building",
   "buildingCode": " F23",
   "roomName": " Mathews 107",
   "capacity": 32,
   "currentOccupancy": random.randint(0, 32)
 },
 {
   "buildingName": "Mathews Building",
   "buildingCode": " F23",
   "roomName": " Mathews 108",
   "capacity": 40,
   "currentOccupancy": random.randint(0, 40)
 },
 {
   "buildingName": "Mathews Building",
   "buildingCode": " F23",
   "roomName": " Mathews 214",
   "capacity": 72,
   "currentOccupancy": random.randint(0, 72)
 },
 {
   "buildingName": "Mathews Building",
   "buildingCode": " F23",
   "roomName": " Mathews 226",
   "capacity": 38,
   "currentOccupancy": random.randint(0, 38)
 },
 {
   "buildingName": "Mathews Building",
   "buildingCode": " F23",
   "roomName": " Mathews 227",
   "capacity": 42,
   "currentOccupancy": random.randint(0, 42)
 },
 {
   "buildingName": "Mathews Building",
   "buildingCode": " F23",
   "roomName": " Mathews 228",
   "capacity": 42,
   "currentOccupancy": random.randint(0, 42)
 },
 {
   "buildingName": "Mathews Building",
   "buildingCode": " F23",
   "roomName": " Mathews 230",
   "capacity": 48,
   "currentOccupancy": random.randint(0, 48)
 },
 {
   "buildingName": "Mathews Building",
   "buildingCode": " F23",
   "roomName": " Mathews 231",
   "capacity": 48,
   "currentOccupancy": random.randint(0, 48)
 },
 {
   "buildingName": "Mathews Building",
   "buildingCode": " F23",
   "roomName": " Mathews 232",
   "capacity": 38,
   "currentOccupancy": random.randint(0, 38)
 },
 {
   "buildingName": "Mathews Building",
   "buildingCode": " F23",
   "roomName": " Mathews 301",
   "capacity": 16,
   "currentOccupancy": random.randint(0, 16)
 },
 {
   "buildingName": "Mathews Building",
   "buildingCode": " F23",
   "roomName": " Mathews 302",
   "capacity": 22,
   "currentOccupancy": random.randint(0, 22)
 },
 {
   "buildingName": "Mathews Building",
   "buildingCode": " F23",
   "roomName": " Mathews 303",
   "capacity": 22,
   "currentOccupancy": random.randint(0, 22)
 },
 {
   "buildingName": "Mathews Building",
   "buildingCode": " F23",
   "roomName": " Mathews 306",
   "capacity": 28,
   "currentOccupancy": random.randint(0, 28)
 },
 {
   "buildingName": "Mathews Building",
   "buildingCode": " F23",
   "roomName": " Mathews 307",
   "capacity": 44,
   "currentOccupancy": random.randint(0, 44)
 },
 {
   "buildingName": "Mathews Building",
   "buildingCode": " F23",
   "roomName": " Mathews 308",
   "capacity": 30,
   "currentOccupancy": random.randint(0, 30)
 },
 {
   "buildingName": "Mathews Building",
   "buildingCode": " F23",
   "roomName": " Mathews 309",
   "capacity": 34,
   "currentOccupancy": random.randint(0, 34)
 },
 {
   "buildingName": "Mathews Building",
   "buildingCode": " F23",
   "roomName": " Mathews 310",
   "capacity": 48,
   "currentOccupancy": random.randint(0, 48)
 },
 {
   "buildingName": "Mathews Building",
   "buildingCode": " F23",
   "roomName": " Mathews 311",
   "capacity": 24,
   "currentOccupancy": random.randint(0, 24)
 },
 {
   "buildingName": "Mathews Building",
   "buildingCode": " F23",
   "roomName": " Mathews 312",
   "capacity": 44,
   "currentOccupancy": random.randint(0, 44)
 },
 {
   "buildingName": "Mathews Building",
   "buildingCode": " F23",
   "roomName": " Mathews 313",
   "capacity": 18,
   "currentOccupancy": random.randint(0, 18)
 },
 {
   "buildingName": "Mathews Theatres",
   "buildingCode": " D23",
   "roomName": " Mathews Theatre A",
   "capacity": 472,
   "currentOccupancy": random.randint(0, 472)
 },
 {
   "buildingName": "Mathews Theatres",
   "buildingCode": " D23",
   "roomName": " Mathews Theatre B",
   "capacity": 246,
   "currentOccupancy": random.randint(0, 246)
 },
 {
   "buildingName": "Mathews Theatres",
   "buildingCode": " D23",
   "roomName": " Mathews Theatre C",
   "capacity": 110,
   "currentOccupancy": random.randint(0, 110)
 },
 {
   "buildingName": "Mathews Theatres",
   "buildingCode": " D23",
   "roomName": " Mathews Theatre D",
   "capacity": 110,
   "currentOccupancy": random.randint(0, 110)
 },
 {
   "buildingName": "Morven Brown Building",
   "buildingCode": " C20",
   "roomName": " Morven Brown G5",
   "capacity": 26,
   "currentOccupancy": random.randint(0, 26)
 },
 {
   "buildingName": "Morven Brown Building",
   "buildingCode": " C20",
   "roomName": " Morven Brown G6",
   "capacity": 42,
   "currentOccupancy": random.randint(0, 42)
 },
 {
   "buildingName": "Morven Brown Building",
   "buildingCode": " C20",
   "roomName": " Morven Brown LG2",
   "capacity": 32,
   "currentOccupancy": random.randint(0, 32)
 },
 {
   "buildingName": "Morven Brown Building",
   "buildingCode": " C20",
   "roomName": " Morven Brown LG30",
   "capacity": 24,
   "currentOccupancy": random.randint(0, 24)
 },
 {
   "buildingName": "Newton Building",
   "buildingCode": " J12",
   "roomName": " Newton 306",
   "capacity": 26,
   "currentOccupancy": random.randint(0, 26)
 },
 {
   "buildingName": "Newton Building",
   "buildingCode": " J12",
   "roomName": " Newton 307",
   "capacity": 30,
   "currentOccupancy": random.randint(0, 30)
 },
 {
   "buildingName": "Old Main Building",
   "buildingCode": " K15",
   "roomName": " Old Main Building 149",
   "capacity": 149,
   "currentOccupancy": random.randint(0, 149)
 },
 {
   "buildingName": "Old Main Building",
   "buildingCode": " K15",
   "roomName": " Old Main Building 150",
   "capacity": 50,
   "currentOccupancy": random.randint(0, 50)
 },
 {
   "buildingName": "Old Main Building",
   "buildingCode": " K15",
   "roomName": " Old Main Building 151",
   "capacity": 38,
   "currentOccupancy": random.randint(0, 38)
 },
 {
   "buildingName": "Old Main Building",
   "buildingCode": " K15",
   "roomName": " Old Main Building 229",
   "capacity": 100,
   "currentOccupancy": random.randint(0, 100)
 },
 {
   "buildingName": "Old Main Building",
   "buildingCode": " K15",
   "roomName": " Old Main Building 230",
   "capacity": 100,
   "currentOccupancy": random.randint(0, 100)
 },
 {
   "buildingName": "Old Main Building",
   "buildingCode": " K15",
   "roomName": " Old Main Building G31",
   "capacity": 111,
   "currentOccupancy": random.randint(0, 111)
 },
 {
   "buildingName": "Old Main Building",
   "buildingCode": " K15",
   "roomName": " Old Main Building G32",
   "capacity": 74,
   "currentOccupancy": random.randint(0, 74)
 },
 {
   "buildingName": "Patricia O'Shane Building",
   "buildingCode": " E19",
   "roomName": " E19 Patricia O’Shane 103",
   "capacity": 231,
   "currentOccupancy": random.randint(0, 231)
 },
 {
   "buildingName": "Patricia O'Shane Building",
   "buildingCode": " E19",
   "roomName": " E19 Patricia O’Shane 104",
   "capacity": 497,
   "currentOccupancy": random.randint(0, 497)
 },
 {
   "buildingName": "Patricia O'Shane Building",
   "buildingCode": " E19",
   "roomName": " E19 Patricia O’Shane 105",
   "capacity": 231,
   "currentOccupancy": random.randint(0, 231)
 },
 {
   "buildingName": "Patricia O'Shane Building",
   "buildingCode": " E19",
   "roomName": " E19 Patricia O’Shane G02",
   "capacity": 113,
   "currentOccupancy": random.randint(0, 113)
 },
 {
   "buildingName": "Patricia O'Shane Building",
   "buildingCode": " E19",
   "roomName": " E19 Patricia O’Shane G03",
   "capacity": 112,
   "currentOccupancy": random.randint(0, 112)
 },
 {
   "buildingName": "Patricia O'Shane Building",
   "buildingCode": " E19",
   "roomName": " E19 Patricia O’Shane G04",
   "capacity": 102,
   "currentOccupancy": random.randint(0, 102)
 },
 {
   "buildingName": "Patricia O'Shane Building",
   "buildingCode": " E19",
   "roomName": " E19 Patricia O’Shane G05",
   "capacity": 112,
   "currentOccupancy": random.randint(0, 112)
 },
 {
   "buildingName": "Patricia O'Shane Building",
   "buildingCode": " E19",
   "roomName": " E19 Patricia O’Shane G06",
   "capacity": 113,
   "currentOccupancy": random.randint(0, 113)
 },
 {
   "buildingName": "Physics Theatre",
   "buildingCode": " K14",
   "roomName": " Physics Theatre",
   "capacity": 369,
   "currentOccupancy": random.randint(0, 369)
 },
 {
   "buildingName": "Quadrangle Building",
   "buildingCode": " E15",
   "roomName": " Quadrangle 1001",
   "capacity": 28,
   "currentOccupancy": random.randint(0, 28)
 },
 {
   "buildingName": "Quadrangle Building",
   "buildingCode": " E15",
   "roomName": " Macauley Theatre",
   "capacity": 114,
   "currentOccupancy": random.randint(0, 114)
 },
 {
   "buildingName": "Quadrangle Building",
   "buildingCode": " E15",
   "roomName": " Quadrangle 1042",
   "capacity": 22,
   "currentOccupancy": random.randint(0, 22)
 },
 {
   "buildingName": "Quadrangle Building",
   "buildingCode": " E15",
   "roomName": " Quadrangle 1043",
   "capacity": 60,
   "currentOccupancy": random.randint(0, 60)
 },
 {
   "buildingName": "Quadrangle Building",
   "buildingCode": " E15",
   "roomName": " Quadrangle 1045",
   "capacity": 30,
   "currentOccupancy": random.randint(0, 30)
 },
 {
   "buildingName": "Quadrangle Building",
   "buildingCode": " E15",
   "roomName": " Quadrangle 1046",
   "capacity": 30,
   "currentOccupancy": random.randint(0, 30)
 },
 {
   "buildingName": "Quadrangle Building",
   "buildingCode": " E15",
   "roomName": " Quadrangle 1047",
   "capacity": 30,
   "currentOccupancy": random.randint(0, 30)
 },
 {
   "buildingName": "Quadrangle Building",
   "buildingCode": " E15",
   "roomName": " Quadrangle 1048",
   "capacity": 30,
   "currentOccupancy": random.randint(0, 30)
 },
 {
   "buildingName": "Quadrangle Building",
   "buildingCode": " E15",
   "roomName": " Quadrangle 1049",
   "capacity": 20,
   "currentOccupancy": random.randint(0, 20)
 },
 {
   "buildingName": "Quadrangle Building",
   "buildingCode": " E15",
   "roomName": " Quadrangle G025",
   "capacity": 30,
   "currentOccupancy": random.randint(0, 30)
 },
 {
   "buildingName": "Quadrangle Building",
   "buildingCode": " E15",
   "roomName": " Quadrangle G026",
   "capacity": 30,
   "currentOccupancy": random.randint(0, 30)
 },
 {
   "buildingName": "Quadrangle Building",
   "buildingCode": " E15",
   "roomName": " Quadrangle G027",
   "capacity": 26,
   "currentOccupancy": random.randint(0, 26)
 },
 {
   "buildingName": "Quadrangle Building",
   "buildingCode": " E15",
   "roomName": " Quadrangle G031",
   "capacity": 52,
   "currentOccupancy": random.randint(0, 52)
 },
 {
   "buildingName": "Quadrangle Building",
   "buildingCode": " E15",
   "roomName": " Quadrangle G032",
   "capacity": 58,
   "currentOccupancy": random.randint(0, 58)
 },
 {
   "buildingName": "Quadrangle Building",
   "buildingCode": " E15",
   "roomName": " Quadrangle G033",
   "capacity": 10,
   "currentOccupancy": random.randint(0, 10)
 },
 {
   "buildingName": "Quadrangle Building",
   "buildingCode": " E15",
   "roomName": " Quadrangle G034",
   "capacity": 60,
   "currentOccupancy": random.randint(0, 60)
 },
 {
   "buildingName": "Quadrangle Building",
   "buildingCode": " E15",
   "roomName": " Quadrangle G040",
   "capacity": 40,
   "currentOccupancy": random.randint(0, 5402)
 },
 {
   "buildingName": "Quadrangle Building",
   "buildingCode": " E15",
   "roomName": " Quadrangle G042",
   "capacity": 22,
   "currentOccupancy": random.randint(0, 22)
 },
 {
   "buildingName": "Quadrangle Building",
   "buildingCode": " E15",
   "roomName": " Quadrangle G044",
   "capacity": 51,
   "currentOccupancy": random.randint(0, 51)
 },
 {
   "buildingName": "Quadrangle Building",
   "buildingCode": " E15",
   "roomName": " Quadrangle G045",
   "capacity": 51,
   "currentOccupancy": random.randint(0, 51)
 },
 {
   "buildingName": "Quadrangle Building",
   "buildingCode": " E15",
   "roomName": " Quadrangle G046",
   "capacity": 30,
   "currentOccupancy": random.randint(0, 30)
 },
 {
   "buildingName": "Quadrangle Building",
   "buildingCode": " E15",
   "roomName": " Quadrangle G047",
   "capacity": 30,
   "currentOccupancy": random.randint(0, 30)
 },
 {
   "buildingName": "Quadrangle Building",
   "buildingCode": " E15",
   "roomName": " Quadrangle G048",
   "capacity": 20,
   "currentOccupancy": random.randint(0, 20)
 },
 {
   "buildingName": "Quadrangle Building",
   "buildingCode": " E15",
   "roomName": " Quadrangle G052",
   "capacity": 26,
   "currentOccupancy": random.randint(0, 26)
 },
 {
   "buildingName": "Quadrangle Building",
   "buildingCode": " E15",
   "roomName": " Quadrangle G053",
   "capacity": 44,
   "currentOccupancy": random.randint(0, 44)
 },
 {
   "buildingName": "Quadrangle Building",
   "buildingCode": " E15",
   "roomName": " Quadrangle G054",
   "capacity": 34,
   "currentOccupancy": random.randint(0, 34)
 },
 {
   "buildingName": "Quadrangle Building",
   "buildingCode": " E15",
   "roomName": " Quadrangle G055",
   "capacity": 18,
   "currentOccupancy": random.randint(0, 18)
 },
 {
   "buildingName": "Rex Vowels Theatre",
   "buildingCode": " F17",
   "roomName": " Rex Vowels Theatre",
   "capacity": 292,
   "currentOccupancy": random.randint(0, 292)
 },
 {
   "buildingName": "Rupert Myers Building",
   "buildingCode": " M15",
   "roomName": " Rupert Myers Theatre",
   "capacity": 114,
   "currentOccupancy": random.randint(0, 114)
 },
 {
   "buildingName": "Science & Engineering Building",
   "buildingCode": " E8",
   "roomName": " Science & Engineering B24",
   "capacity": 32,
   "currentOccupancy": random.randint(0, 32)
 },
 {
   "buildingName": "Science & Engineering Building",
   "buildingCode": " E8",
   "roomName": " Science & Engineering B25",
   "capacity": 40,
   "currentOccupancy": random.randint(0, 40)
 },
 {
   "buildingName": "Science & Engineering Building",
   "buildingCode": " E8",
   "roomName": " Science & Engineering B26",
   "capacity": 48,
   "currentOccupancy": random.randint(0, 48)
 },
 {
   "buildingName": "Science & Engineering Building",
   "buildingCode": " E8",
   "roomName": " Science & Engineering B27",
   "capacity": 32,
   "currentOccupancy": random.randint(0, 32)
 },
 {
   "buildingName": "Science & Engineering Building",
   "buildingCode": " E8",
   "roomName": " Science & Engineering G02",
   "capacity": 44,
   "currentOccupancy": random.randint(0, 44)
 },
 {
   "buildingName": "Science & Engineering Building",
   "buildingCode": " E8",
   "roomName": " Science & Engineering G05",
   "capacity": 68,
   "currentOccupancy": random.randint(0, 68)
 },
 {
   "buildingName": "Science & Engineering Building",
   "buildingCode": " E8",
   "roomName": " Science & Engineering G07",
   "capacity": 68,
   "currentOccupancy": random.randint(0, 68)
 },
 {
   "buildingName": "Science Theatre",
   "buildingCode": " F13",
   "roomName": " Science Theatre",
   "capacity": 460,
   "currentOccupancy": random.randint(0, 460)
 },
 {
   "buildingName": "Sir John Clancy Auditorium",
   "buildingCode": " C24",
   "roomName": " Sir John Clancy Auditorium",
   "capacity": 945,
   "currentOccupancy": random.randint(0, 945)
 },
 {
   "buildingName": "Squarehouse",
   "buildingCode": " E4",
   "roomName": " Squarehouse 114",
   "capacity": 40,
   "currentOccupancy": random.randint(0, 40)
 },
 {
   "buildingName": "Squarehouse",
   "buildingCode": " E4",
   "roomName": " Squarehouse 115",
   "capacity": 38,
   "currentOccupancy": random.randint(0, 38)
 },
 {
   "buildingName": "Squarehouse",
   "buildingCode": " E4",
   "roomName": " Squarehouse 203",
   "capacity": 30,
   "currentOccupancy": random.randint(0, 30)
 },
 {
   "buildingName": "Squarehouse",
   "buildingCode": " E4",
   "roomName": " Squarehouse 205",
   "capacity": 20,
   "currentOccupancy": random.randint(0, 20)
 },
 {
   "buildingName": "Squarehouse",
   "buildingCode": " E4",
   "roomName": " Squarehouse 206",
   "capacity": 30,
   "currentOccupancy": random.randint(0, 30)
 },
 {
   "buildingName": "Squarehouse",
   "buildingCode": " E4",
   "roomName": " Squarehouse 207",
   "capacity": 24,
   "currentOccupancy": random.randint(0, 24)
 },
 {
   "buildingName": "Squarehouse",
   "buildingCode": " E4",
   "roomName": " Squarehouse 208",
   "capacity": 24,
   "currentOccupancy": random.randint(0, 24)
 },
 {
   "buildingName": "Squarehouse",
   "buildingCode": " E4",
   "roomName": " Squarehouse 211",
   "capacity": 18,
   "currentOccupancy": random.randint(0, 18)
 },
 {
   "buildingName": "Squarehouse",
   "buildingCode": " E4",
   "roomName": " Squarehouse 214",
   "capacity": 24,
   "currentOccupancy": random.randint(0, 24)
 },
 {
   "buildingName": "Squarehouse",
   "buildingCode": " E4",
   "roomName": " Squarehouse 215",
   "capacity": 24,
   "currentOccupancy": random.randint(0, 24)
 },
 {
   "buildingName": "Squarehouse",
   "buildingCode": " E4",
   "roomName": " Squarehouse 217",
   "capacity": 18,
   "currentOccupancy": random.randint(0, 18)
 },
 {
   "buildingName": "Squarehouse",
   "buildingCode": " E4",
   "roomName": " Squarehouse 218",
   "capacity": 24,
   "currentOccupancy": random.randint(0, 24)
 },
 {
   "buildingName": "Tyree Energy Technology",
   "buildingCode": " H6",
   "roomName": " Tyree Energy Technology G16",
   "capacity": 180,
   "currentOccupancy": random.randint(0, 180)
 },
 {
   "buildingName": "Tyree Energy Technology",
   "buildingCode": " H6",
   "roomName": " Michael Hintze Theatre",
   "capacity": 84,
   "currentOccupancy": random.randint(0, 84)
 },
 {
   "buildingName": "Tyree Energy Technology",
   "buildingCode": " H6",
   "roomName": " Tyree Energy Technology LG05",
   "capacity": 84,
   "currentOccupancy": random.randint(0, 84)
 },
 {
   "buildingName": "Tyree Energy Technology",
   "buildingCode": " H6",
   "roomName": " Tyree Energy Technology LG07",
   "capacity": 84,
   "currentOccupancy": random.randint(0, 84)
 },
 {
   "buildingName": "UNSW Business School",
   "buildingCode": " E12",
   "roomName": " UNSW Business School 105",
   "capacity": 38,
   "currentOccupancy": random.randint(0, 38)
 },
 {
   "buildingName": "UNSW Business School",
   "buildingCode": " E12",
   "roomName": " UNSW Business School 107",
   "capacity": 28,
   "currentOccupancy": random.randint(0, 28)
 },
 {
   "buildingName": "UNSW Business School",
   "buildingCode": " E12",
   "roomName": " UNSW Business School 114",
   "capacity": 28,
   "currentOccupancy": random.randint(0, 28)
 },
 {
   "buildingName": "UNSW Business School",
   "buildingCode": " E12",
   "roomName": " UNSW Business School 115",
   "capacity": 53,
   "currentOccupancy": random.randint(0, 53)
 },
 {
   "buildingName": "UNSW Business School",
   "buildingCode": " E12",
   "roomName": " UNSW Business School 118",
   "capacity": 28,
   "currentOccupancy": random.randint(0, 28)
 },
 {
   "buildingName": "UNSW Business School",
   "buildingCode": " E12",
   "roomName": " UNSW Business School 119",
   "capacity": 53,
   "currentOccupancy": random.randint(0, 53)
 },
 {
   "buildingName": "UNSW Business School",
   "buildingCode": " E12",
   "roomName": " UNSW Business School 130",
   "capacity": 38,
   "currentOccupancy": random.randint(0, 38)
 },
 {
   "buildingName": "UNSW Business School",
   "buildingCode": " E12",
   "roomName": " UNSW Business School 205",
   "capacity": 38,
   "currentOccupancy": random.randint(0, 38)
 },
 {
   "buildingName": "UNSW Business School",
   "buildingCode": " E12",
   "roomName": " UNSW Business School 207",
   "capacity": 28,
   "currentOccupancy": random.randint(0, 28)
 },
 {
   "buildingName": "UNSW Business School",
   "buildingCode": " E12",
   "roomName": " UNSW Business School 215",
   "capacity": 28,
   "currentOccupancy": random.randint(0, 28)
 },
 {
   "buildingName": "UNSW Business School",
   "buildingCode": " E12",
   "roomName": " UNSW Business School 216",
   "capacity": 53,
   "currentOccupancy": random.randint(0, 53)
 },
 {
   "buildingName": "UNSW Business School",
   "buildingCode": " E12",
   "roomName": " UNSW Business School 219",
   "capacity": 28,
   "currentOccupancy": random.randint(0, 28)
 },
 {
   "buildingName": "UNSW Business School",
   "buildingCode": " E12",
   "roomName": " UNSW Business School 220",
   "capacity": 53,
   "currentOccupancy": random.randint(0, 53)
 },
 {
   "buildingName": "UNSW Business School",
   "buildingCode": " E12",
   "roomName": " UNSW Business School 232",
   "capacity": 38,
   "currentOccupancy": random.randint(0, 38)
 },
 {
   "buildingName": "Vallentine Annexe",
   "buildingCode": " H22",
   "roomName": " Vallentine Annexe 121",
   "capacity": 109,
   "currentOccupancy": random.randint(0, 109)
 },
 {
   "buildingName": "Webster Building",
   "buildingCode": " G14",
   "roomName": " New South Global Theatre",
   "capacity": 225,
   "currentOccupancy": random.randint(0, 225)
 },
 {
   "buildingName": "Webster Building",
   "buildingCode": " G14",
   "roomName": " Webster 250",
   "capacity": 42,
   "currentOccupancy": random.randint(0, 42)
 },
 {
   "buildingName": "Webster Building",
   "buildingCode": " G14",
   "roomName": " Webster 251",
   "capacity": 40,
   "currentOccupancy": random.randint(0, 40)
 },
 {
   "buildingName": "Webster Building",
   "buildingCode": " G14",
   "roomName": " Webster 252",
   "capacity": 24,
   "currentOccupancy": random.randint(0, 24)
 },
 {
   "buildingName": "Webster Building",
   "buildingCode": " G14",
   "roomName": " Webster 256",
   "capacity": 60,
   "currentOccupancy": random.randint(0, 60)
 },
 {
   "buildingName": "Webster Building",
   "buildingCode": " G14",
   "roomName": " Webster 302",
   "capacity": 36,
   "currentOccupancy": random.randint(0, 36)
 },
 {
   "buildingName": "Webster Theatres",
   "buildingCode": " G15",
   "roomName": " Webster Theatre A",
   "capacity": 180,
   "currentOccupancy": random.randint(0, 180)
 },
 {
   "buildingName": "Webster Theatres",
   "buildingCode": " G15",
   "roomName": " Webster Theatre B",
   "capacity": 189,
   "currentOccupancy": random.randint(0, 189)
 }
]

# if __name__ == "__main__":
#     print(get_rooms())