from fastapi import FastAPI

from .herbal import herbal

app = FastAPI()


@app.get("/")
def read_root():
    return {"Nothing here"}


app.mount("/herbal", herbal.app)
