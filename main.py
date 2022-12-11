from amazon_spd import selenium_spd
from api import amazon_spd_api

# uvicorn run
if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app=amazon_spd_api.app, port=8000)