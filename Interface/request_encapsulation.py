# -*- coding: utf-8 -*-
# @Time    :
# @Author  : Tomato
# @Site    :
# @File    : request_encapsulation.py
from Public.test_requests import Requ


class RequestEncapsulation:
    def __init__(self, method, url, params):
        """
        初始化参数
        :param method: 方法
        :param url: 地址
        :param params: 参数
        """
        self.method = method
        self.url = url
        self.params = params
        self.custom_request = Requ

    def request_method(self):
        if self.method == "GET":
            self.response = self.custom_request.get(self.url, self.params)
        elif self.method == "POST":
            self.response = self.custom_request.post(url=self.url, params=self.params)
        elif self.method == "PUT":
            self.response = self.custom_request.put(url=self.url, params=self.params)
        elif self.method == "DELETE":
            self.response = self.custom_request.delete(url=self.url, params=self.params)
        return self.response

    def get_json_data(self):
        json_data = self.request_method()
        return json_data

