'''
This module demonstrates how to use python built-in module requests
'''
import requests


def requests_usage():
    '''
    This function demonstrates how to work with requests, e.g. make requests, check status_code,
    get response as plain text or as json object converted into python dict, pass parameters
    '''
    url0 = 'https://httpbin.org/get'
    req0 = requests.get(url0)
    print(f'Status for {url0}: {req0.status_code}')
    print('req0.text (type', type(req0.text), '): ', req0.text)
    print('req0.json() (type', type(req0.json()), '): ', req0.json())

    bad_url = 'https://httpbin.org/status/404'
    bad_req = requests.get(bad_url)
    print(f'Status for {bad_url}: {bad_req.status_code}')

    # two alternatives on how to pass parameters into request
    payload = {'key1': 'value1', 'key2': 'value2'}
    req1 = requests.get('https://httpbin.org/get', params=payload)
    req2 = requests.get(f'https://httpbin.org/get?key1={payload["key1"]}&key2={payload["key2"]}')
    print(req1.url)
    print(req2.url)
    print(f'Are the two links indentical? {req1.url == req2.url}')


if __name__ == '__main__':
    requests_usage()
