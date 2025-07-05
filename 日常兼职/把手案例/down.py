import requests


headers = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
    "authentication": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJuYmYiOjE3NDgzMTM2MTcsImNyZWRlbnRpYWxzIjoiJDJhJDEwJExSVkVMQUFvWlpybFRaQ2FDc1paWU9KQWx0UW10SzFqdm5aWGh6bGtoLnpqL0JUMmh3ZXNLIiwibmlja25hbWUiOiJUUkFOU1BBUkVOVCIsImlkIjoiMTUxMjk5IiwidHlwZSI6IjEiLCJleHAiOjE3NDgzMTU0MTcsImlhdCI6MTc0ODMxMzYxN30.Odnr-DgOElrpRkfVvxoqXy-Eo0_tE6Ykx1BqitajYRg",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://www.lawsdata.com/",
    "sec-ch-ua": "\"Chromium\";v=\"136\", \"Google Chrome\";v=\"136\", \"Not.A/Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36",
    "x-requested-with": "XMLHttpRequest"
}
url = "https://www.lawsdata.com/sweet/compass-instrument/export/wordForInstrument/681aca68c76cc24ac8cba816"
params = {
    "": ""
}
response = requests.get(url, headers=headers, params=params)

print(response.text)
print(response)