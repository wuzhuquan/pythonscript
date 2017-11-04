import requests
import json
import http.cookiejar, urllib.request
from urllib.parse import urlencode

def getcookie():
    #生成cookie
    cookiejar = http.cookiejar.CookieJar()
    urlOpener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookiejar))
    values = {
        'JSESSIONID': '913895A30C4E9117933522391F3FD273'
    }
    cookiedata = urlencode(values)
    return cookiedata
	

headers = {
    'Accept':'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding':'gzip, deflate, sdch',
    'Accept-Language':'zh-CN,zh;q=0.8',
    'Connection':'keep-alive',
    'Cookie': getcookie(),
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36',
    'X-Requested-With':'XMLHttpRequest'
}
url = 'http://192.168.1.100:9880/spa-manager/api/v2/project/list'
detail = {'clubId':'871666660254158848'}
r = requests.get(url,headers=headers,params=detail)
json_response = r.text
print(json_response)

