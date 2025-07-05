import requests


headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "priority": "u=0, i",
    "sec-ch-ua": "\"Chromium\";v=\"136\", \"Google Chrome\";v=\"136\", \"Not.A/Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "none",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
}
cookies = {
    "sid": "5fb615934cf84132816efbbf5c24374a27f9b67c",
    "PCID": "31120665385442638836007",
    "overrideAbTestGroup": "%5B%5D",
    "MARKETID": "31120665385442638836007",
    "x-coupang-accept-language": "ko-KR",
    "x-coupang-target-market": "KR",
    "bm_ss": "ab8e18ef4e",
    "bm_so": "B4711012E284419B5E727F2578A8526326322B5BA2A869944F2FB51CA43D842C~YAAQB6InF+QMEoWWAQAA2+hYwgPYt04OncP56aUBYILWIXOEdhiv6lRhoAfDNAZkuNglxyjjfFvHZ9LLUtuS/ilB3UVibTZnNIeLr+EXwKYv++tUddb+kuPKeqRkH39OIGq6hpg3BKPdhGs9XlvgbhKqzW9SNCEZNEhi2kS+v2aFVqFMewogcBEBFfFjokQGwHbbDWzIDyw0dbkFMhaBVi2yDlVFjYYEGMHEE+qgbwWHt/rbeTWW+o3ucTdUk9fva8NGGgyw7sRW/KXVykz6r8HDuMhuc26gfQX8GvbwmmkTzSE+R8ioScSIAz8rrBNviK6djn2S0okL8QxIRP800uS2i4kyZ2UMoEY/FVYxbY39vk/m73oJWpPlhI4CVqbuvbj4dhvSGzw/aD0d6L+6UwIOON/KrxKRcndPxbrcv5y6Vdo8gmKxi+tLovjCPxWdRYFZ/jMuHKuJuu5wfAzaZw==",
    "bm_sz": "71DECE528BA1FB34B7582887B7C6B2CE~YAAQB6InF+UMEoWWAQAA2+hYwhsbpIkwOsF9bqSDZjLMkmB8zedgo2AFFzRhLBISSi4fybUT2Tv/KRMUL8S9oSGm82WooLD0bvp25Z26O3PXvL3qEjTMJ5LUDQ441Udhhu9swrrLplrVl2rGtQhI/VqyPQG4h6NKdNzbX2SOHrx4NgY7KjbHNMo4rP1gIoVgSoaSeAIivfzTxJGoPT/EzE+e0+Opf4jqaPt9KjA0EY5736xAurU0Z5cIW/CvVlpuGcNfNu/RlPSdKszu+DJIPxOTdVOpjjUAXfeLbJzwf/Ao17jxLD82xu/NeEr6cNbhEWW7gCXu9llvt6s0lFUCxn49+Yxl3dQe/DcQtvWMIRXs7FFTFbq3xzR63IzAb03V0rJQNDfURYUZEdWiIz3aFQ==~4404532~4468786",
    "web-session-id": "0a8cbec3-7448-45b6-b1dc-f003ad763109",
    "bm_lso": "B4711012E284419B5E727F2578A8526326322B5BA2A869944F2FB51CA43D842C~YAAQB6InF+QMEoWWAQAA2+hYwgPYt04OncP56aUBYILWIXOEdhiv6lRhoAfDNAZkuNglxyjjfFvHZ9LLUtuS/ilB3UVibTZnNIeLr+EXwKYv++tUddb+kuPKeqRkH39OIGq6hpg3BKPdhGs9XlvgbhKqzW9SNCEZNEhi2kS+v2aFVqFMewogcBEBFfFjokQGwHbbDWzIDyw0dbkFMhaBVi2yDlVFjYYEGMHEE+qgbwWHt/rbeTWW+o3ucTdUk9fva8NGGgyw7sRW/KXVykz6r8HDuMhuc26gfQX8GvbwmmkTzSE+R8ioScSIAz8rrBNviK6djn2S0okL8QxIRP800uS2i4kyZ2UMoEY/FVYxbY39vk/m73oJWpPlhI4CVqbuvbj4dhvSGzw/aD0d6L+6UwIOON/KrxKRcndPxbrcv5y6Vdo8gmKxi+tLovjCPxWdRYFZ/jMuHKuJuu5wfAzaZw==^1747017328218",
    "_abck": "B521F828D473DD2624B1CAE71866FB3F~0~YAAQB6InF/gMEoWWAQAAzO9Ywg2H38YqphtIMMbGhXf6Mj8mL4nVpa6ycwyoeKty4p189Jlrp/Vok163yuel5ykoKi1EIgOlDWgBDb+GLmrq1JbKd2+Hu+dlYbI4nzgK6nDGHH6wgr/bWBV45e6M9rUoubwKGOtAnidL5/VOs2dIPgNRjb7gmBaJNUPMXvYfjUntbthm/IbR0QhUADhp4xf5ytqOYMdpqHClopKB329T8dKGARlPAZLKD4ajrCQbiLd+2pupZpncfplfE3D4703eoxGbMX14kuVJaW0LKR9duqQ/Rm57/cZYqk5DqyXkveQbcDW8OdoZUfJCkJrH1zyT7ziwi+jZrKdxsgUZa37Y9YTGPMTF9LQ8AdykL2SioZqImbatdTZ0V5VK69mLJD6ni1ji+5aqKRTMDtjtp4HJ4lU7Pr7CKi3MGiVw5XZk0sErBfZ+QdZeQwsTcAOFdVlWm4ZoHYNVWX9lYQvAoDtiphxYEZOLHYSAcAE91JiFw/S/r2Kk17Z8FHgWZLbC+a54nzryvmGmoUrQhc5JS8RnamqJ6rAlcTnnzN5+MjFfsyvuOzDhk/aw7LoKMZcEIFqjxr3X~-1~||0||~-1",
    "ak_bmsc": "05F039A326F746D09A7FD45366792F9E~000000000000000000000000000000~YAAQB6InF/0MEoWWAQAA/fBYwhuVzpxPouzaaT1J4atcGoYDiOZ9DRBv5Y5VHWhVGHg+5uRzGV1J1wTWmluPHSuCW79ImFPpPnxIjTT4Z8DhnhbJgdidn7zyX7qdyOJH3dzEhPO95jzeOoOpmKHsSvRBkQWaMqQy5YFtrk3B+jmdnb+9b0CwzUDVxhHEXm55nu07q8J0P8MOXLw++1EozO6nKzLvcBl4XrMrvYRFPt/HI97QE6im4aIrmF2d6v57ugd+4n590jMm3xh6BOdBHMwXBw21XKhOCXvgHEIfImADx7A/8BZ9AkmtdVHvHEgfz/NZzeCIQSGSHyikeSP4ru/zxyYpKXx07+SGQXlfK+zmdAf7cYHuFgxtSHqd1s+MxpJofgJxA1CkVe50LAY2hdMv4E4FTQTjwRWvsQAGgRFz8icOHzNo7qbPOfvpwLyX+Cw6Kig2A8jAOd4+LXE=",
    "bm_s": "YAAQB6InFwoNEoWWAQAAMvNYwgOEsZgaAUuoDyKbvPbKTjdwCAWRMJPrDqhY782s8+hR6t3cq9vnPmWdyAJXh63JNoDgQkQAPsRyT4SuLgSSyZjb4/NncX5s/0bN36qVBu5FVVNQjcmRjZTVvGAeG/f+r73GE4CaV9qcueE6KYTBy1AC7yvwHlpRpKj5e5LhnOPmLkT056JOX1VD+a0TTR1Sd4EZ8ytJVj6xxsERYvlGNHp9r4yD+Sq4nqEWM+h1xEh9GrLUT2BGdH6S7RquEDNPVG0TYPJCoorALkRR4n5m1owR/RaNGyNp/CJx5TosvIia5lfwTLoTy3sd+0FgFmexHZhuvPU5lpAMmJ0bfSBjBd/GIeKJlEEf4uyJqoMU0XIOI+LxMLlJatbwBiBxH+/8V3DygGYF5fQLJPjy7wDoWOfHsR8p281byBpyK3UHSWFsTglbPIkOZ2ei51XKRM6Ka6bA8OhvN5SvdT1vq/zAHMknV1uGRTMSMPfljotQrgEBqJjF4m1CilA4c5dNU8T0W1262OysX5uyPUadrBkjffY6B6Q=",
    "cto_bundle": "X91N9F9HNm9HbzNHRFY1TE5MWlBDRTFWS1VWaEpUR2pGTWhraUJkdmZtSm00VjBYMnNMNWpBWlZWTDRuMlZtTm1RWXVMUUFiSUtnJTJGRG1TT3hZcVNwVVh2dGppekQlMkZ3ZkMxdTlSMW04YW85bGJJbmlyVU9ia0Y3dW1lU3F5RkNVVWthJTJGSiUyQlphSmZyeDVGOCUyRk0wcGdhYVVoQzZCQyUyRjdYOGJhYnZkUlFDMUxWZG5aSnBCJTJGbjFHVXdmN0hkaVdlNDI3ZUtUcFR1c0RzQSUyQnF0RzBOaVlYNGpWTm5EOEs0cmpHRjRKZUh0SDF2TE5wTlRzVlJmQk4lMkJBeXBzYUNaRzZueWpYYVRM",
    "bm_sv": "D540C2681745A5F3664427AF35995EBD~YAAQB6InFw0NEoWWAQAAO/RYwhsYQ6ExvfQhTi5Oa1广东翻页（不能动）.pyEGKNAFGO4rnSEpXnHy9RtVR2Z7389O6zawIANg3HQaBpyEzv8M+KKLcGIs+3A+2iNSJYjXnWRjWzfpBCm+P6INOkweH5KDHpWe05sswZBQ9oM/mBJPQx5ki7jckzoh23fT4rS20tJ2YORkIWv4XYuNkyV2cmjK0AW+qV5Zd+/vAqdaXTG3t6QqcQ1yy+5TBpfNc1qzVHkoVCZfa+a/nziADA==~1",
    "_fbp": "fb.1.1747017329620.677545779782614693",
    "baby-isWide": "wide"
}
url = "https://www.coupang.com/"
response = requests.get(url, headers=headers, cookies=cookies)

print(response.text)
print(response)