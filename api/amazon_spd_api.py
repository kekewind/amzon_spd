from fastapi import FastAPI
from amazon_spd import selenium_spd

app = FastAPI()


@app.get("/")
async def root():
    test = []
    for i in selenium_spd.test():
        test.append(i.text)
    return test


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


def add(x: int, y: int):
    return x + y
