import config
from flask import Flask, jsonify
from occupancy import get_rooms

APP = Flask(__name__)

@APP.route('/', methods=['GET'])
def occupancy():
    print("CALLED!")
    result = get_rooms()
    response  = jsonify(result)
    response.headers.add(
        "Access-Control-Allow-Origin", 
        "http://localhost:3000"
    )
    return response

if __name__ == "__main__":
    APP.run(port=config.port)
