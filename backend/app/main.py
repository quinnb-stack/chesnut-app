from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"I kiss na gad po ako babyyyyy :(((("}
