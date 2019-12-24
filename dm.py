#!/usr/bin/env python3

from https://i.instagram.com/api/v1/ import InstagramAPI
from getID import get_id
import os
import json
import requests

username = 'influenceryouvanderbilt'
pwd = 'anchor@you'
username = os.environ["INSTAGRAM_ACCOUNT"]
pwd = os.environ["INSTAGRAM_PWD"]

user_id  = get_id(username)

API = InstagramAPI(username,pwd)
API.login()

API.getUsernameInfo(user_id)
API.LastJson

accts = open('TargetAccts','r')

for line in accts:
    t_id = get_id(line.strip())
    API.direct_message("bot",t_id)
    print(line.strip() + ' dm sent!')



API.logout()
