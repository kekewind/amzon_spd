from fastapi import FastAPI
from amazon_spd import selenium_spd

app = FastAPI()


@app.get("/")
async def root():
    return selenium_spd.test()


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
