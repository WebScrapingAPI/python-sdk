from requests import request, Response
from urllib.parse import urlencode

class WebScrapingApiClient:
    api_url = 'https://api.webscrapingapi.com/v1'

    def __init__(self, api_key: str):
        self.api_key = api_key       
        
    def request(self, method: str, url: str, params: dict = None, data: dict = None, headers: dict = None, **kwargs) -> Response:
        if not params:
            params = {}

        params['api_key'] = self.api_key
        params['url'] = url
        
        if headers:
            params['keep_headers'] = 1
        else:
            headers = {}

        full_api_url = self.api_url + '?' + urlencode(params)

        return request(method, full_api_url, data=data, headers=headers, **kwargs)

    def get(self, url: str, params: dict = None, headers: dict = None, **kwargs) -> Response:
        return self.request('GET', url, params=params, headers=headers, **kwargs)

    def post(self, url: str, params: dict = None, data: dict = None, headers: dict = None, **kwargs) -> Response:
        return self.request('POST', url, params=params, data=data, headers=headers, **kwargs)