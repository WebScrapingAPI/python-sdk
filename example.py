from webscrapingapi import WebScrapingApiClient

client = WebScrapingApiClient(api_key='76SxogX9jwYmIoCl3D1QpYdWgcgIuwSF')

response = client.get('https://webscrapingapi.com', params={
    'render_js': 0,
    'proxy_type': 'datacenter',
    'device': 'desktop',
}, headers={
    'authorization': 'bearer test'
})

print(response.status_code)
print(response.content);