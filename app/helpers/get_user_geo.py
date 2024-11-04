# import requests
#
#
# def get_address(ip: str):
#     response = requests.get(url=f"http://ip-api.com/json/{ip}")
#     content = response.json()
#     data = {
#         "country": content["country"],
#         "region": content["regionName"],
#         "city": content["city"],
#     }
#
#     return data
