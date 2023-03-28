from redis.client import Redis


class RedisController:
    request_queue = 'request_messages'
    response_queue = 'response_messages'

    def __init__(self, host: str, port: int):
        self.redis = Redis(host=host, port=port, db=0)

    def send_message(self, text: str):
        self.redis.rpush(self.request_queue, text)

    def get_last_message(self):
        message = self.redis.rpop(self.response_queue).decode()
        return message

    def clear_all(self):
        self.redis.delete(self.response_queue)
        self.redis.delete(self.request_queue)
