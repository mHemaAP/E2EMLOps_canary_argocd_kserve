
import requests
import json

url_1 = "http://a82f89a5c4cc847b7ba40070efce3746-1537257378.ap-south-1.elb.amazonaws.com/v1/models/sports-classifier:predict"

with open("input.json") as f:
    payload = json.load(f)


headers_1 = {"Host": "sports-classifier.default.emlo.tsai", "Content-Type": "application/json"}


response_1 = requests.request("POST", url_1, headers=headers_1, json=payload)


print(response_1.headers)
print(response_1.status_code)
print(response_1.json())

"""
ajith@LAPTOP-OVJI4T62:~/mlops/course/emlo_play/emlo4-s18/E2EMLOps/K8SDeploy/eks-cluster-config$ python3 test_kserver_sports_2.py 
{'content-length': '55', 'content-type': 'application/json', 'date': 'Sun, 04 May 2025 15:20:53 GMT', 'server': 'istio-envoy', 'x-envoy-upstream-service-time': '61'}
200
{'predictions': [{'nascar racing': 0.01726987212896347}]}
"""

"""
provided output

{'content-length': '77', 'content-type': 'application/json', 'date': 'Sun, 04 May 2025 15:36:37 GMT', 'server': 'istio-envoy', 'x-envoy-upstream-service-time': '109'}
200
{'predictions': [{'class': 'nascar racing', 'probability': 0.01726987212896347}]}

"""