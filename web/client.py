# import requests
# from django.core.serializers import json
#
# url = 'http://127.0.0.1:8000/api/'  # django api路径
#
# parms = {
#     'name': '客户端',  # <span style="color:#ff0000;">发送给服务器的内容</span>
# }
#
# headers = {  # 请求头 是<span style="color:#ff0000;">浏览器正常的</span>就行 就这里弄了一天 - -！
#     'User-agent': 'none/ofyourbusiness',
#     'Spam': 'Eggs'
# }
#
# resp = requests.post(url, data=parms, headers=headers)  # <span style="color:#ff0000;">发送请求</span>
#
# # Decoded text returned by the request
# text = resp.text
# print(json.loads(text))

