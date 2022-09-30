
# constant value for search without mileage
SEARCH_QUERY = "SELECT year, make, model, listing_price, listing_mileage, dealer_name, dealer_street FROM `database`.`carsdb`WHERE make=%s AND model=%s AND YEAR=%s;"

# constant value for  searching with mileage
SEARCH_QUERY_MILEAGE = "SELECT year, make, model, listing_price, listing_mileage, dealer_name, dealer_street FROM `database`.`carsdb`WHERE make=%s AND model=%s AND YEAR=%s AND listing_mileage BETWEEN %s AND %s;"

MILEAGE_DIFF = 1000