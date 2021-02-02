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

from env_var import *
from DNACenter import *

DNACenterLab = DNACenter(username=DNAC_USER, password=DNAC_PASS, base_url=DNAC_URL)


def start():
    devices = DNACenterLab.get_devices()
    for dev in devices:
        device_id = "deivceId"
        print("For device: %s-%s" % (dev["hostname"], device_id))

        keyword = "service" #"name-server"
        print("Here is configuration for: %s" % keyword)
        DNACenterLab.get_device_config(dev["id"], keyword)

        search_for = "xxx"
        print("Search for: %s" % search_for)
        DNACenterLab.check_config(dev["id"], search_for)
        exit()


start()
