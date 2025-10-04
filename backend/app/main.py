from fastapi import FastAPI

from .herbal import herbal
from .smes import smes

app = FastAPI()


@app.get("/")
def read_root():
    return {"Nothing here"}


app.mount("/herbal", herbal.app)
app.mount("/smes", smes.app)
