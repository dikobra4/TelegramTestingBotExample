import os
from pytest import fixture
from dotenv import load_dotenv

from bot.redis_controller import RedisController

load_dotenv()


@fixture(scope='function')
def tester_bot():
    redis = RedisController(
        host=os.getenv("REDIS_HOST"),
        port=int(os.getenv("REDIS_PORT"))
    )
    redis.clear_all()
    yield redis
    redis.clear_all()
