from fastapi import FastAPI

app = FastAPI()


@app.get("/parse")
async def root():
    return {"message": "get"}

@app.post("/parse")
async def rootpost():
    return {"message": "post"}

