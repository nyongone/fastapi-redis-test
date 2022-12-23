from fastapi import FastAPI
from routes.test import router as router_test

app = FastAPI()
app.include_router(router_test)

@app.get("/")
def index():
  return {"message": "Hello World!"}