# import requests
#
#
# def get_address(ip: str):
#     response = requests.get(url=f"http://ip-api.com/json/{ip}").json()
#
#     data = {
#         "country": response.get("country"),
#         "region": response.get("regionName"),
#         "city": response.get("city"),
#     }
#
#     return data
