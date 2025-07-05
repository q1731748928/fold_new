const fetch = require('node-fetch');
fetch("https://gleami.apps.fao.org/animals_selection", {
  "headers": {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
    "cache-control": "no-cache",
    "content-type": "application/x-www-form-urlencoded",
    "pragma": "no-cache",
    "priority": "u=0, i",
    "sec-ch-ua": "\"Chromium\";v=\"136\", \"Google Chrome\";v=\"136\", \"Not.A/Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "cookie": "csrftoken=ccoCJveqBKM6jADPOelm9k69VfXRF8Hzo6NTWZsUl1tDLxkxBc21l1Up7obG9lVv; sessionid=9gyopkur38k1hecaix79jxom3dhpp9k6; _ga=GA1.1.1163173444.1747796148; _ga_D1DDJEPMCW=GS2.1.s1747796148$o1$g1$t1747799271$j0$l0$h0",
    "Referer": "https://gleami.apps.fao.org/animals_selection",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": "productionsys=2_3&animalproductionsysproduct=2_3_1&animalproductionsysproduct=2_3_2&productionsys=2_4&animalproductionsysproduct=2_4_1&animalproductionsysproduct=2_4_2&productionsys=3_5&animalproductionsysproduct=3_5_1&animalproductionsysproduct=3_5_2&productionsys=3_6&animalproductionsysproduct=3_6_1&animalproductionsysproduct=3_6_2&productionsys=4_7&animalproductionsysproduct=4_7_1&animalproductionsysproduct=4_7_2&productionsys=4_8&animalproductionsysproduct=4_8_1&animalproductionsysproduct=4_8_2&productionsys=5_9&animalproductionsysproduct=5_9_3&productionsys=5_10&animalproductionsysproduct=5_10_1&productionsys=5_11&animalproductionsysproduct=5_11_3&productionsys=6_12&animalproductionsysproduct=6_12_1&productionsys=6_13&animalproductionsysproduct=6_13_1&productionsys=6_14&animalproductionsysproduct=6_14_1&csrfmiddlewaretoken=A25xGVDb6Uaz90dKxdgLyiKQFh3baM7iMWuOTpRFQbR6BXUskbXqKZy6Rqh0EZle",
  "method": "POST"
});