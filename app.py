from flask import Flask, render_template, request, Response
import json
from controller.dbhandler import DBHandler
from controller.utils import calculateAvg, get_vehicle_list_as_dict, round_nearest_100

db = DBHandler()

application = Flask(__name__, template_folder="view")

@application.route('/')
def home():
    return render_template("index.html")

# this is an api endpoint, it only accepts GET method
# Input : Year, Make, Model, Mileage (Optional parameter)
# Output : JSON Array
@application.route('/search', methods=['GET'])
def search():
    try:
        year = request.args["year"]
        make = request.args["make"]
        model = request.args["model"]
        mileage = request.args["mileage"]

        result = []

        # checking if mileage value is provided  

        if mileage == "":
            result = db.search(year, make, model)
        else:
            result = db.searchMileage(year, make, model, int(mileage))

        # if no vehicle is found then this data is returned

        if(len(result) < 1):
            return Response(json.dumps({"success": False, "error":"No vehicle found with given input data."}), mimetype='application/json')

        # Limit only first 100 vehicles
        vehicles = get_vehicle_list_as_dict(result, 100)

        # rounding up the value to its nearest 100
        est = round_nearest_100(calculateAvg(result))
        
        response = {"success": True, "error": ""}
        response["estimation"] = int(est)
        response["vehicles"] = vehicles


        return Response(json.dumps(response), mimetype='application/json')

    # exception handeling

    except Exception as e:
        print(e)
        return Response(json.dumps({"success": False, "error":"Error"}), mimetype='application/json')

if __name__ == '__main__':
   application.run()