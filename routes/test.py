from fastapi import APIRouter
from apis import test

router = APIRouter(
  prefix="/test"
)

@router.get("/")
async def test_1():
  res = await test.get_test_db()
  return {"res": res}

@router.get("/user/{user_id}")
async def test_get_user(user_id:int):
  res = await test.get_test_user_db(userId=user_id)
  return {"res": res}