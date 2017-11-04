import log_config
import json
import http.client,mimetypes
from urllib.parse import urlencode
import random
import time
import re
import os,sys

logging = log_config.getlogger()

def interfaceTest(num,api_purpose,api_host,request_url,request_data,check_point,request_method,request_data_type,session):  
    headers = {'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
               'X-Requested-With':'XMLHttpRequest',
               'Connection':'keep-alive',
               'Referer':'http://' + api_host,
               'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36'}
    if session is not None:
        headers['Cookie'] = 'session=' + session
        if request_data_type == 'File':
            headers['Content-Type'] = 'multipart/form-data;boundary=----WebKitFormBoundaryDf9uRfwb8uzv1eNe;charset=UTF-8'
        elif request_data_type == 'Data':
            headers['Content-Type'] = 'text/plain; charset=UTF-8'

    conn = http.client.HTTPConnection(api_host)
    if request_method == 'POST':
        conn.request('POST',request_url,request_data,headers=headers)
    elif request_method == 'GET':
        conn.request('GET',request_url+'?'+request_data,headers=headers)
    else:
        logging.error(num + ' ' + api_purpose + ' HTTP请求方法错误，请确认[Request Method]字段是否正确！！！')
        return 400,request_method
    response = conn.getresponse()
    status = response.status
    resp = response.read()
    if status == 200:
        resp = resp.decode('utf-8')
        if re.search(check_point,str(resp)):
            logging.info(num + ' ' + api_purpose + ' 成功, ' + str(status) + ', ' + str(resp))
            return status,json.loads(resp)
        else:
            logging.error(num + ' ' + api_purpose + ' 失败！！！, [ ' + str(status) + ' ], ' + str(resp))
            return 2001,resp
    else:
        logging.error(num + ' ' + api_purpose + ' 失败！！！, [ ' + str(status) + ' ], ' + str(resp))
        return status,resp.decode('utf-8')

if __name__ == '__main__':
    main()
