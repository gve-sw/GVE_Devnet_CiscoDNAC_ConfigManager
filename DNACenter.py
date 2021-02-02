"""
Copyright (c) 2020 Cisco and/or its affiliates.
This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.1 (the "License"). You may obtain a copy of the
License at
               https://developer.cisco.com/docs/licenses
All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.
"""

import re

import requests
import urllib3
from requests.auth import HTTPBasicAuth


class DNACenter(object):

    def __init__(self, username, password, base_url):
        self.username = username
        self.password = password
        self.base_url = base_url

        self.__auth_token = self.__get_auth_token()

    def __get_auth_token(self):
        url = '{0}/dna/system/api/v1/auth/token'.format(self.base_url)
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        r = requests.post(url, auth=HTTPBasicAuth(self.username, self.password), verify=False)
        if r.status_code == 200:
            response = r.json()
            return response['Token']
        else:
            raise Exception(r.status_code)

    def __dna_headers(self):
        return {'Content-Type': 'application/json', 'x-auth-token': self.__auth_token}

    def get_devices(self):
        url = '%s/dna/intent/api/v1/network-device' % (self.base_url)
        r = requests.get(url, headers=self.__dna_headers(), verify=False)
        if r.status_code == 200 or 202:
            resp = r.json()["response"]
            return resp
        else:
            return False

    def get_device_config(self, device_id, keyword):
        url = '%s/dna/intent/api/v1/network-device/%s/config' % (self.base_url, device_id)
        r = requests.get(url, headers=self.__dna_headers(), verify=False)
        if r.status_code == 200 or 202:
            device_config = r.json()["response"]
            try:
                keyword = r'%s([^!]+)' % keyword
                config = re.search(keyword, device_config).group(1)
                print(config)
                return config
            except:
                print("Doesn't contain the string match")
                return False
        return False

    def check_config(self, device_id, keyword):
        url = '%s/dna/intent/api/v1/network-device/%s/config' % (self.base_url, device_id)
        r = requests.get(url, headers=self.__dna_headers(), verify=False)
        if r.status_code == 200 or 202:
            device_config = r.json()["response"]
            if keyword in device_config:
                print("Configuration contains: ", keyword)
                return True
            else:
                print("Configuration DOES NOT contains: ", keyword)
        return False

