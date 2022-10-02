import requests, json

#unit testing functions

def test_homepage():
    res = requests.get('http://localhost:5000')
    assert res.status_code == 200
    print("test_homepage OK")

def test_api_search():
    res = requests.get('http://localhost:5000/search?year=2009&make=audi&model=a3&mileage=')
    assert res.status_code == 200
    resJson = json.loads(res.text)
    assert resJson["success"] == True
    print("test_api_search OK")

if __name__ == "__main__":
    test_homepage()
    test_api_search()
    