import math

# function to calculate average vehicle price
def calculateAvg(vehicles):
    est = 0
    for x in vehicles:
            try:
                est += int(x[3])
            except:
                pass
    return est / len(vehicles)

# function to round estimated price to nearst 100
#     
def round_nearest_100(num):
    return math.ceil(num / 100) * 100

# function to limit vehicle to only first 100

def get_vehicle_list(result, limit):
    vehicles = []
    i = 0
    for x in result:
            if i >= limit:
                break
            vehicles.append({"year": x[0], "make": x[1], "model": x[2], "price":x[3], "mileage":x[4], "dealer_name": x[5], "dealer_street": x[6]})
            i += 1
    return vehicles