from core.redis_config import redis_config

async def get_test_db():
  return {"test": "test1"}

async def get_test_user_db(userId):
  rd = redis_config()
  # user_db = rd.get(userId)
  return {"user_id": userId}
