from sklearn import linear_model
import numpy as np

from model.vehicle import Vehicle

class Estimator:
    def estimate(vehicles, mileage):
        sorted_vehicles = sorted(vehicles, key=lambda k: k[4])
        reg = linear_model.LinearRegression()
        mileage_list = []
        price_list = []
        for vehicle in sorted_vehicles:
            mileage_list.append(vehicle[4])
            price_list.append(vehicle[3])
        
        x = np.array(mileage_list)
        y = np.array(price_list)

        reg.fit(x.reshape(-1, 1), y)
        est = reg.predict([[int(mileage)]])
        return est[0]
