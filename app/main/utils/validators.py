"""
validate request api_key, request body schema 
"""
import logging
from flask import request, abort, Response
from pydantic import BaseModel
from typing import Callable, Any
from dotenv import load_dotenv
from functools import wraps
import json
import os 


load_dotenv()
API_KEY = os.environ.get('API_KEY')


def valiate_request_body(schema:BaseModel) -> Callable:
    """ a decorator to validate request using pydantic schema"""
    def decorator(request_func:Callable):
        @wraps(request_func)
        def wrapper(*args,**kwargs):
            try:
                print(f"request.is_json:{request.is_json}")
                if not request.is_json:
                   abort(400, description='Request does not contain JSON data')
                print(f"requestrequest: {request.json}")
                # validate schema here 
                data = schema(**request.json)
                return request_func(*args,**kwargs)
            except Exception as e:
                logging.error(f"Validating request failed >> {e}")
                abort(500, description=str(e))

        return wrapper  
    return decorator


def validate_api_key(request_func):
    """ check if provided request header apikey is valid """
    @wraps(request_func)
    def wrapper(*args,**kwargs):

        if 'Api-Key' not in request.headers:
            abort(403, description='Missing API key') # forbidden
        if API_KEY != request.headers['Api-Key']:
            abort(403, description='Invalid API key')
        return request_func(*args,**kwargs)
    return wrapper




def custom_response(data:Any, status_code:int) -> Response:
    """ create custom http response """

    if  isinstance(data,dict):
        data = json.dumps(data)
    response = Response(response=str(data), status=status_code, content_type='application/json')
    return response


