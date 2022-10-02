SEARCH_QUERY = "SELECT year, make, model, listing_price, listing_mileage, dealer_name, dealer_street FROM `searchtool_database`.`carsdb`WHERE make=%s AND model=%s AND YEAR=%s;"
SEARCH_QUERY_MILEAGE = "SELECT year, make, model, listing_price, listing_mileage, dealer_name, dealer_street FROM `searchtool_database`.`carsdb`WHERE make=%s AND model=%s AND YEAR=%s AND listing_mileage BETWEEN %s AND %s;"

MILEAGE_DIFF = 1000