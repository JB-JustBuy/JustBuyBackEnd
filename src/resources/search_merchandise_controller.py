from flask_login import login_required
from flask_restful import Resource, request, reqparse
from src.resources.auth import login_required
from redis import Redis
from rq import Queue
from src.services.best_plan_service import BestPlanService
import json


class SearchByUrlController(Resource):
    def __init__(self, ):
        self.result = None

    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('job_id')
        args = parser.parse_args()
        print('job_id:', args['job_id'])
        redis = Redis()
        queue = Queue('Just-Buy-Queue', connection=redis)
        fetched_job = queue.fetch_job(args['job_id'])

        job_json = json.dumps(fetched_job.to_dict(), indent=2, default=str)
        print(job_json)
        if fetched_job.get_status() == "finished":
            return {'result': fetched_job.result}, 200
        elif fetched_job.get_status() == "failed":
            print(fetched_job.exc_info)
            return {'status': fetched_job.get_status()}
        else:
            return {'status': fetched_job.get_status()}

    # the vserion using rq worker and redis
    def post(self):
        # process font end paras
        rp = reqparse.RequestParser()
        rp.add_argument('urls', required=True, action='append', help='Urls is required')
        args = rp.parse_args()
        # call scrapy to search the same product
        service = BestPlanService(args['urls'], 'familiar')

        # init queue and worker
        redis = Redis()
        queue = Queue('Just-Buy-Queue', connection=redis)
        job = queue.enqueue(service.plan)
        return {'job_id': job.get_id()}, 200

