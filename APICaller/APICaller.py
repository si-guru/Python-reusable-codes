"""
Name        :   APICaller
Usage       :   Calls a Web-API using the provided input and will return the
                response in JSON format
Reusability :   -
Author      :   AVM-Automation-SGO
Created on  :   08/10/2018
---------------------------------------------------------------------------------
Change Log: Recent Modification in TOP
---------------------------------------------------------------------------------
Date        Modified By     Version              Modification
---------------------------------------------------------------------------------
08/10/2018  DomainBOTS          1.00                 Initial Code
"""
# python modules
import sys
import json
import requests
from requests.auth import HTTPBasicAuth

# 3rd party modules
from requests_ntlm import HttpNtlmAuth  # requires cryptography and ntlm-auth

# Custom Modules
from .. import Globals

if(not Globals.setting):
    Globals.start()

setting = Globals.setting
logger = setting['Logger']
ipc_object = setting['IPC_Object']


def data_string_to_json(data):
    if(not data == ()):
        if(not isinstance(data, str)):
            data = data[0]
        if(data.strip() == ""):
            data = []
        else:
            if(data[0] == '"'):
                data = data.replace('"', "")
            data = (data).replace("'", '"')
            data = json.loads((data))
    print(data)
    return data


def main_function(
        request_url, auth_username=None, auth_password=None, proxy_url=None,
        proxy_username=None, proxy_password=None, method=None, *args, **kwargs
        ):

    data = kwargs['data']

    if(not method):
        method = 'get'

    # Basic Checks
    if(not (proxy_url == "")):
        if(not proxy_username):
            print("WARNING - Proxy auth not provided")

    if(request_url == ""):
        print("Request URL not provided")
        sys.exit()

    # Set headers for access
    headers = {
                "Content-Type": "application/json",
                "Accept": "application/json"
            }

    # Extracting proxies
    is_multiple_proxy = (';' in proxy_url)
    http_proxy = ""
    https_proxy = ""
    if(is_multiple_proxy):
        index = proxy_url.index(';')

        proxy = (proxy_url[0:index])
        if('http:' in proxy):
            http_proxy = str(
                        "http://" + proxy_username + ":" + proxy_password + 
                        "@" + proxy[7:]
                        )
        if('https:' in proxy):
            https_proxy = str(
                        "https://" + proxy_username + ":" + proxy_password +
                        "@" + proxy[8:]
                        )

        proxy = (proxy_url[index+1:])
        if('http:' in proxy):
            http_proxy = str(
                        "http://" + proxy_username + ":" + proxy_password + 
                        "@" + proxy[7:]
                        )
        if('https:' in proxy):
            https_proxy = str(
                        "https://" + proxy_username + ":" + proxy_password +
                        "@" + proxy[8:]
                        )

    else:
        proxy = proxy_url
        if('http:' in proxy):
            http_proxy = str(
                        "http://" + proxy_username + ":" + proxy_password + 
                        "@" + proxy[7:]
                        )
        if('https:' in proxy):
            https_proxy = str(
                        "https://" + proxy_username + ":" + proxy_password +
                        "@" + proxy[8:]
                        )

    # Set Proxies
    proxies = {
        'http': http_proxy,
        'https': https_proxy
    }

    # Basic Auth method
    auth = (auth_username, auth_password)

    # auth= HTTPBasicAuth(auth_username, auth_password)

    # auth= HttpNtlmAuth(auth_username, auth_password)

    # Response from site 
    if(method == 'get'):
        response = requests.get(
                    url=request_url, proxies=proxies, auth=auth,
                    headers=headers, params=data
                    )
    elif (method == 'post'):
        response = requests.post(
                    url=request_url, proxies=proxies, auth=auth,
                    headers=headers, json=data
                    )
    json_output = []

    if(response.status_code == 200):
        json_output = (response.json())
    return json_output


if __name__ == '__main__':

    try:
        request_url = sys.argv[1]
        auth_username = sys.argv[2]
        auth_password = sys.argv[3]
        proxy_url = sys.argv[4]
        proxy_username = sys.argv[5]
        proxy_password = sys.argv[6]
        # data = (*sys.argv[7:],)
        data = []
        data = data_string_to_json(data)
    except:
        print("Please Enter all valid Arguments")
        sys.exit()

    args = []
    response = main_function(
                request_url, auth_username=auth_username,
                auth_password=auth_password, proxy_url=proxy_url,
                proxy_username=proxy_username, proxy_password=proxy_password,
                method=None, args=args, data=data
                )
    print(response)
