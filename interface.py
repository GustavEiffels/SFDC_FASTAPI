from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import Response

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message":"Hello from fast API"}


@app.get("/favicon.ico", include_in_schema=False) 
async def get_favicon():
    return Response(content="", media_type="image/x-icon")