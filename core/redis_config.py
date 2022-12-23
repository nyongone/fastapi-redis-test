import redis

def redis_config():
  try:
    REDIS_HOST = str = "localhost"
    REDIS_PORT = int = 6379
    REDIS_DB = int = 0
    rd = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)
  except:
    print("Connection Failed")