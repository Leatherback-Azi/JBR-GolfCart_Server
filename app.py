import config
from flask import Flask, send_file, request

app = Flask(__name__)
VERSION_NO_ROUTE = config.Setup.version_no_route

def make_response(status, detail, data, base_response=config.Response.BASE_RESPONSE):
    try:
        base_response['status'] = int(status)
        base_response['detail'] = str(detail)
        base_response['data'] = dict(data)
        return base_response
    except (KeyError, ValueError):
        print("\n=======================================\n")
        print("RESPONSE ERR, GOT WRONG DATA")
        print("\n=======================================\n")


@app.route(VERSION_NO_ROUTE + '/map_image', methods=["GET"])
def get_map_image():
    return send_file(config.Setup.map_image_route, mimetype='image/' + config.Setup.map_image_fomat)

@app.route(VERSION_NO_ROUTE + '/user/robot/map/location/', methods=["GET"])
def get_robots_coordinate():
    coordinate_curr = {
        "robots": [
            {
                "id": 1,
                "x_pos": 12.7,
                "y_pos": 15.4
            }
        ]
    }
    return make_response(200, "OK", coordinate_curr)


@app.route(VERSION_NO_ROUTE + '/user/robot/map/location/destination/', methods=["GET", "PUT"])
class robots_destination_coordinate():
    def get(self):
        coordinate_dest = {
            "robots": [
                {
                    "id": 1,
                    "x_pos": 12.7,
                    "y_pos": 15.4
                }
            ]
        }
        return make_response(200, "OK", coordinate_dest)
    def put(self):
        coordinate = request.json.get()
        # CODE HERE
        return make_response(200, "OK")


@app.route(VERSION_NO_ROUTE + '/user/robot/battery/', methods=["GET"])
def get_robots_battery():
    battery_stats = {
        "robots": [
            {
                "id": 1,
                "battery": 97
            }
        ]
    }
    return make_response(200, "OK", battery_stats)


@app.route(VERSION_NO_ROUTE + '/user/robot/power/', methods=['PUT'])
class control_robot_power():
    def put(self):
        return make_response(200, "OK")


if __name__ == '__main__':
    app.run()
