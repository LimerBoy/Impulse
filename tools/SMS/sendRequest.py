import json
import requests
import tools.SMS.numberTools as numberTools
import tools.SMS.randomData as randomData

# Read services file
def getServices(file = 'tools/SMS/services.json'):
    with open(file, 'r') as services:
        return json.load(services)["services"]

# Read proxy list
def getProxys(file = 'tools/SMS/proxy.json'):
    with open(file, 'r') as proxys:
        return json.load(proxys)["proxy"]

# Get domain by big url
def getDomain(url):
    return url.split('/')[2]

# Service class
# parseData, SendSMS
class Service:
    def __init__(self, service):
        self.service = service
        self.proxy = getProxys()
        self.timeout = 10

    # Parse string
    def parseData(self, phone):
        payload = None
        # Check for 'data'
        try:
            dataType = "data"
            payload = self.service["data"]
        except KeyError:
            pass
        # Check for 'json'
        try:
            dataType = "json"
            payload = self.service["json"]
        except KeyError:
            pass
        # If payload is clean
        if not payload:
            payload = json.dumps({"url": self.service["url"]})
            dataType = "url"
        # Replace %phone%, etc.. to data
        for old, new in {
            "\'": "\"",
            "%phone%": phone,
            "%phone5%": numberTools.transformPhone(phone, 5),
            "%name%":  randomData.random_name(),
            "%email%": randomData.random_email(),
            "%password%": randomData.random_password()
            }.items():
            payload = payload.replace(old, new)
        return (json.loads(payload), dataType)
    
    # Send message
    def sendMessage(self, phone):
        url = self.service["url"]
        #print("Sending message.. | URL: (" + getDomain(url) + ") >> STATUS:", end = " ")
        payload, dataType = self.parseData(phone)

        # Headers for request
        headers = {
            "X-Requested-With": "XMLHttpRequest",
            "Connection": "keep-alive",
            "Pragma": "no-cache",
            "Cache-Control": "no-cache",
            "Accept-Encoding": "gzip, deflate, br",
            "User-agent": randomData.random_useragent()
            }

        # Add custom headers
        try:
            customHeaders = self.service["headers"]
        except KeyError:
            pass
        else:
            for key, value in json.loads(customHeaders.replace("\'", "\"")).items():
                headers[key] = value

        # Create suffixes
        okay  = " Service (" + getDomain(url) + ") >> Message sent!"
        error = " Service (" + getDomain(url) + ") >> Failed to sent message!"

        try:
            # If data type is 'json'
            if dataType == "json":
                r = requests.post(url, json = payload, timeout = self.timeout, headers = headers, proxies = self.proxy)
            # If data type is 'data'
            elif dataType == "data":
                r = requests.post(url, data = payload, timeout = self.timeout, headers = headers, proxies = self.proxy)
            elif dataType == "url":
                r = requests.post(payload["url"], timeout = self.timeout, headers = headers, proxies = self.proxy)

            # Check status
            if r.status_code == 200:
                print("[SUCCESS]" + okay)
            elif r.status_code == 429:
                print("[TOO MANY REQUESTS]" + error)
            else:
                #print(r.text)
                print("[" + str(r.status_code) + "]" + error)
            
            return r.status_code

        except (requests.exceptions.ReadTimeout, requests.exceptions.ConnectTimeout):
            print("[CONNECTION TIMED OUT]" + error)
        except (requests.exceptions.ConnectionError):
            print("[CONNECTION ERROR]" + error)