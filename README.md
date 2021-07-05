# WebScrapingApi Python SDK

WebScrapingApi is an API that allows scraping websites while using rotating proxies to prevent bans. This SDK for Python makes the usage of the API easier to implement in any project you have.

## Installation

Run the following command in the main folder of your project:

```
pip install webscrapingapi
```

## API Key

To use the API and the SDK you will need a API Key. You can get one by registering at [WebScrapingApi](https://app.webscrapingapi.com/register)

## Usage

Using the SDK it's quite easy. You can check out the code from example.py to make things more clear.
An example of a GET call to the API is the following:

```
from webscrapingapi import WebScrapingApiClient

client = WebScrapingApiClient(api_key='YOUR_API_KEY')

response = client.get('https://webscrapingapi.com', params={
    'render_js': 0,
    'proxy_type': 'datacenter',
    'device': 'desktop',
}, headers={
    'authorization': 'bearer test'
})
```

For a better understanding of the parameters, please check out [our documentation](https://docs.webscrapingapi.com/#request-parameters)


