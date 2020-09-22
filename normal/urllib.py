from urllib import request
from urllib import parse
import requests

post_ulr = 'http://httpbin.org/post'
get_url = 'http://httpbin.org/get?name=wyc1856'
encode_type = 'utf-8'

payload = bytes(parse.urlencode({"name": "wyc1856"}), encoding=encode_type)
# post_response = request.urlopen(post_ulr, data=payload, timeout=1)
# print(post_response.read().decode(encode_type))
#
# get_response = request.urlopen(get_url, timeout=1)
# print(get_response.read().decode(encode_type))

response = requests.get(get_url)
print(response.text)

response = requests.post(post_ulr, data=payload)
print(response.text)
