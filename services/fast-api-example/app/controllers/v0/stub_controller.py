from fastapi import HTTPException


async def get_root_info():
    return {"service": "python-stub", "version": "v0", "status": "active"}


async def get_item_by_id(item_id: int):
    if item_id <= 0:
        raise HTTPException(status_code=400, detail="Invalid ID")
    return {"item_id": item_id, "data": "stub_data"}
