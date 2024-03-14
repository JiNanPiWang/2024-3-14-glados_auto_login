import requests

# 创建一个会话对象
session = requests.Session()

# 签到URL
sign_in_url = 'https://glados.rocks/api/user/checkin'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'
}

# 在登录并签到后，从浏览器的开发者工具中复制的cookie
cookies = {
    'cookie_name':
        'koa:sess=eyJ1c2VySWQiOjIxOTQ1OSwiX2V4cGlyZSI6MTcyMzU5NjE1MDc0MSwiX21heEFnZSI6MjU5MjAwMDAwMDB9; koa:sess.sig=tpRbExwOqTO0PssXig1xgWio3lw; _gid=GA1.2.238316004.1710379807; _gat_gtag_UA_104464600_2=1; _ga_CZFVKMNT9J=GS1.1.1710382018.13.1.1710382019.0.0.0; _ga=GA1.1.912722861.1697675900'
}

response = session.post(sign_in_url, headers=headers, cookies=cookies)

print(response.text)

# 检查签到是否成功，可以根据返回的响应内容来判断
# if response.status_code == 200:
#     print("签到成功！")
# else:
#     print("签到失败。")