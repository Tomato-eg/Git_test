# python3.11
# -*- coding: utf-8 -*-
# ---
# @Software: 
# @File: test_requests.py
# @Author: Tomato
# @Time: 1月 03, 2024
# ---

import json
import requests
from requests import Timeout, RequestException


class RequestLog:
    def __init__(self):
        """
        初始化User-Agent
        """
        self.headers = {
            'User-Agent':
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                'Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0'
        }

    def get(self, url, params):
        try:
            r = requests.get(url, params=params, headers=self.headers)
            r.encoding = 'UTF-8'
            if r.status_code == 200:
                json_response = json.loads(r.text)
                return {'code': 0,
                        'result': json_response}
            else:
                return {'code': 1, 'result': '接口请求失败,返回状态码: %s' % str(r.status_code)}
        except Timeout as e:
            return {'code': 2, 'result': '请求超时:%s' % e}
        except RequestException as e:
            return {'code': 3, 'result': '请求异常:%s' % e}
        except Exception as e:
            return {'code': 4, 'result': 'get请求错误,错误原因:%s' % e}
