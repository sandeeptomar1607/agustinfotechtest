

import time
import logging

from django.https import HttpRequest, HttpResponse

logger = logging.getLogger(__name__)


class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request: Httprequest):

        start_time = time.perf_counter()
        response = self.get_response(request)
        end_time = time.perf_counter()
        execution_time_taken = end_time 

        logger.info("Tie Taken:", execution_time_taken)

        return response

        