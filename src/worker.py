# from src.entities.scrapy_model import Scrapy
# from redis import Redis
# from rq import Queue, Worker
# from rq.local import LocalStack

#
# class JustBuyWorker:
#     def __init__(self):
#         self.driver = Scrapy.get_driver()
#         self._driver_stack = LocalStack()
#
#     def get_driver(self):
#         # driver = self._driver_stack.top
#         # if not driver:
#         #     raise Exception('Run outside of worker context')
#
#         return self.driver
#
#     # init queue and worker
#     def work(self, burst=False, logging_level='INFO'):
#         self._driver_stack.push(self.driver)
#         redis = Redis()
#         q = Queue('Just-Buy-Queue', connection=redis)
#         worker = Worker([q], connection=redis)
#         worker.work(burst=burst, logging_level=logging_level)

import os
import redis
from rq import Worker, Queue, Connection

listen = ["Just-Buy-Queue"]

redis_url = os.getenv('REDISTOGO_URL', 'redis://localhost:6379')

conn = redis.from_url(redis_url)


def work_except_handle(job, exc_type, exc_value, traceback):
    print("Exception handler handle job id: {}".format(job.id))
    print(" exception type&value", exc_type, exc_value)


if __name__ == '__main__':
    with Connection(conn):
        worker = Worker(list(map(Queue, listen)), exception_handlers=[work_except_handle])
        worker.work()
