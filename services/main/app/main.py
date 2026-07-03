from fastapi import FastAPI
from app.api.v1 import router
from app.controllers.v0 import stub_controller

app = FastAPI(title="Python Microservice")
app.include_router(router)


@app.get("/")
async def health():
    return await stub_controller.get_root_info()


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return await stub_controller.get_item_by_id(item_id)
