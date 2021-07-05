from unittest import mock

import pytest

from webscrapingapi import WebScrapingApiClient

@pytest.fixture(scope='module')
def client():
    return WebScrapingApiClient(api_key='API_KEY')


@mock.patch('webscrapingapi.client.request')
def test_get(mock_request, client):
    '''It should make a GET request with the url and API key'''
    client.get('https://httpbin.org')

    mock_request.assert_called_with(
        'GET',
        'https://api.webscrapingapi.com/v1'
        '?api_key=API_KEY&url=https%3A%2F%2Fhttpbin.org',
        data=None,
        headers={},
    )


@mock.patch('webscrapingapi.client.request')
def test_get_with_params(mock_request, client):
    '''It should add parameters to the url'''
    client.get('https://httpbin.org', params={'render_js': 1})

    mock_request.assert_called_with(
        'GET',
        'https://api.webscrapingapi.com/v1'
        '?render_js=1&api_key=API_KEY&url=https%3A%2F%2Fhttpbin.org',
        data=None,
        headers={},
    )


@mock.patch('webscrapingapi.client.request')
def test_get_with_headers(mock_request, client):
    '''It should send headers in the request and set keep_headers to 1'''
    client.get('https://httpbin.org', headers={'Content-Type': 'text/html; charset=utf-8'})

    mock_request.assert_called_with(
        'GET',
        'https://api.webscrapingapi.com/v1'
        '?api_key=API_KEY&url=https%3A%2F%2Fhttpbin.org&keep_headers=1',
        data=None,
        headers={'Content-Type': 'text/html; charset=utf-8'},
    )


@mock.patch('webscrapingapi.client.request')
def test_post(mock_request, client):
    '''It should make a POST request with some data'''
    client.post('https://httpbin.org', data={'KEY_1': 'VALUE_1'})

    mock_request.assert_called_with(
        'POST',
        'https://api.webscrapingapi.com/v1?api_key=API_KEY&url=https%3A%2F%2Fhttpbin.org',
        data={'KEY_1': 'VALUE_1'},
        headers={}
    )