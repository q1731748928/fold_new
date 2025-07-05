import requests


headers = {
    "accept": "*/*",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
    "cache-control": "no-cache",
    "content-type": "application/json",
    "nyt-app-type": "project-vi",
    "nyt-app-version": "0.0.5",
    "nyt-token": "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAs+/oUCTBmD/cLdmcecrnBMHiU/pxQCn2DDyaPKUOXxi4p0uUSZQzsuq1pJ1m5z1i0YGPd1U1OeGHAChWtqoxC7bFMCXcwnE1oyui9G1uobgpm1GdhtwkR7ta7akVTcsF8zxiXx7DNXIPd2nIJFH83rmkZueKrC4JVaNzjvD+Z03piLn5bHWU6+w+rA+kyJtGgZNTXKyPh6EC6o5N+rknNMG5+CdTq35p8f99WjFawSvYgP9V64kgckbTbtdJ6YhVP58TnuYgr12urtwnIqWP9KSJ1e5vmgf3tunMqWNm6+AnsqNj8mCLdCuc5cEB74CwUeQcP2HQQmbCddBy2y0mEwIDAQAB",
    "origin": "https://www.nytimes.com",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://www.nytimes.com/",
    "sec-ch-ua": "\"Chromium\";v=\"134\", \"Not:A-Brand\";v=\"24\", \"Google Chrome\";v=\"134\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
    "x-nyt-internal-meter-override": "undefined"
}

url = "https://samizdat-graphql.nytimes.com/graphql/v2"
params = {
    "operationName": "CollectionsQuery",
    "variables": "{\"id\":\"/news-event/ukraine-russia\",\"first\":10,\"exclusionMode\":\"HIGHLIGHTS_AND_EMBEDDED\",\"isFetchMore\":false,\"isTranslatable\":false,\"isEspanol\":false,\"highlightsListUri\":\"nyt://per/personalized-list/__null__\",\"highlightsListFirst\":0,\"hasHighlightsList\":false}",
    "extensions": "{\"persistedQuery\":{\"version\":1,\"sha256Hash\":\"1f99120a11e94dd62a9474f68ee1255537ee3cf7eac20a0377819edb2fa1fef7\"}}"
}
response = requests.get(url, headers=headers, params=params)

print(response.text)
print(response)