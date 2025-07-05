import urllib
from datetime import datetime

import execjs

import scrapy
from scrapy import cmdline
from scrapy.http import HtmlResponse

class ZhihuSpider(scrapy.Spider):
    name = 'zhihu_spider'

    # allowed_domains = ['m.qingting.fm']
    start_urls = ['https://zhihu.com/']
    cookies = {
        "_zap": "a151f011-0efd-402d-82bb-63e7def6b5e3",
        "d_c0": "ATCSzTbe1xiPTtvwldcuQDzEc7yQczUbxog=|1719583518",
        "__snaker__id": "1ZiWvADqW7hOm34T",
        "q_c1": "007f0ed3d6b847f6b6146e1e9ce7655e|1719583526000|1719583526000",
        "_xsrf": "VnM9zYPL0Rgzft96z3b0Vg0LtqvRwq6D",
        "gdxidpyhxdE": "zgsg4UxhKn58kxacYXclEJ2%5Cj3Xn%5CE7Sh6TMzon0RPSU55%2FpjXbMlZPTjwLgmh2YdK1ok0kjrbUrfOeb4tkyj9J%5CYGYLbmTszKCtwhrs8QgsQBNloJyPvuekCi%5Cs9bSu182rThSnRqO63OOwY5jlas%5CyRU%2BRNvQ5rYtLfwavpHjWHD%2BV%3A1745251725231",
        "captcha_session_v2": "2|1:0|10:1745250834|18:captcha_session_v2|88:V3lCV3RsRk5OSUx5K1V2bXZ6elZjU21kakRiVlRyWDh0TC9TbmtjRnRqcE5ESThSdWUvZUVSZ1QrMHNLVktFUQ==|03805153ce2cc91961ee7f18c95a7b5361a59cfc43351716c3b73eff8d792014",
        "captcha_ticket_v2": "2|1:0|10:1745250841|17:captcha_ticket_v2|728:eyJ2YWxpZGF0ZSI6IkNOMzFfZkZIT3hQR3pTYjBCR1JtbUVuOG53TkVYVzE4YzYxKk5wZ2JxLmNKYUFmYlgzTUp3Lk1PS2VnTGV5KlRaY1JQZC5oM2RETWJEVGlsUWRxWU1hb1Eua1F5cXZ6WkVnbV9oMF9BWllQU2lDY1hSTVZFVmZBS3gwWEZVWjhwaDkyaFFXRm9wa2lMM1J2b0VNTkFCUVZiVC51eEtWaUExckFXRDNRUTJTQ1F1SEJBdzR0dG9VKkZXbV9wclUuZUFDTW5XYjBYdlVlaUtWcTJSNlhXZ0p4a204RXlaSUl3UnlqRlBjSnBEOXp4WFUqUzJZbU4qSndEVTlBWnIqNHFpRVZ1TWRBcEgwMXRET1l5bHRTTm5hcm1qa1ptMzFaOXFISHVOT3QwTmtPUVhhU2Q2S3AqNipVb0NhXzFrZkJQaGM0bXFPWnNQdW1aVURsUm53QVoqNVJ4cVR3MmQqakhDc2d4andNSl9sdk1mTXZ1aG9yMjVNbyo4M1ZvSzAuUzJ6bHdsRWRIRlplUjE1bWR2KkFOTnZSWXUwMlB3WllLaTJCbEI4WVUxNFUwVF9rMnA0UFJOa2hTc3hWemN5YlptcThzMVNXeGZlcTZTTTZoVmdFamhTemJ0cVlONVZjRDU0OWwzVEdMMWhDVHpyQzF0aldEQ05NWXBiZENheDZSUHE2NXlEX1NPT1k3N192X2lfMSJ9|52deedab981db9438ec4dd1cb50d322493e147b1f487e65f78c0435be613380d",
        "z_c0": "2|1:0|10:1745250842|4:z_c0|92:Mi4xckMwTUF3QUFBQUFCTUpMTk50N1hHQ1lBQUFCZ0FsVk5Hcmp6YUFBRHR1d0ZsR0hrckhOVk1KNjVHTFN0VFRrV2NR|5a7abab116b19ebe2f8f3a3c5445c49918ca4080850a2565844c717bca48006a",
        "BEC": "684e706569bf16169217bb2a788786f3",
        "Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49": "1745250583,1745278129,1745363046,1745466838",
        "HMACCOUNT": "11F3EEC15F332D20",
        "tst": "r",
        "SESSIONID": "G58xoYfEdNHY5ODnJcHEUuYG5vDPZ3pnkGJZhSARBFf",
        "JOID": "Ul0VBEi3fpazmZa_K0N9QgRCYO8x9U6pz_XK3GnQNdvtqNr-QGHJnNyflr0osc-cP7fM66O0NOhpXcnqnFrIftw=",
        "osd": "Vl4VAE-zfZa3npK8K0d6RgdCZOg19k6tyPHJ3G3XMdjtrN36Q2HNm9iclrkvtcycO7DI6KOwM-xqXc3tmFnIets=",
        "__zse_ck": "004_goM2xktpZ3IXlQo8zVG1IYPi6VM8jWsfpmzDYRwPr8HgTi8z/Wy4zF5PzwSyAfjUXpFHG4DlPGQK1vj1IzAftUuyaXvLRDN1zjk2WLnONSc/LvwSCKnGv/48FVqj76NC-kXhyCKgXxWtWUc2nstoCS9pIbb+l1gUT6QD0DCeYgXzxZRx69NVcxtWRpr4iODsm9WluYCB1M8B+wSSqYmlkFiLCFe4s+B3DrToEPTugAXUraOMKRnICBGSApiHEsSsskMPomQxqAj1NfbvHeTc/WD0SaUnS/1K5HcKkLfB+vQ0=",
        "Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49": "1745468651"
    }

    headers = {
        'accept': '*/*',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'cache-control': 'no-cache',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': 'https://www.zhihu.com/question/277135177/answer/4386444671',
        'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
        'x-requested-with': 'fetch',
        'x-zse-93': '101_3_3.0',
        'x-zse-96': '2.0_d/4QImsYXt3VlmC9Sf4iGxVtGMYfA4Ncf/M4gn7XWLDJApzPny9okyZyIrH8RNzY',
        "x-zst-81": "3_2.0aR_sn77yn6O92wOB8hPZnQr0EMYxc4f18wNBUgpTQ6nxERFZs0Y0-4Lm-h3_tufIwJS8gcxTgJS_AuPZNcXCTwxI78YxEM20s4PGDwN8gGcYAupMWufIoLVqr4gxrRPOI0cY7HL8qun9g93mFukyigcmebS_FwOYPRP0E4rZUrN9DDom3hnynAUMnAVPF_PhaueTF_NLc8HOaBXfxrSYhrSM8BgsSJHKHheqeTXOpcNOQGeY5wXqoiCLxUgsJqcTVMo0Iuc8SMXMXbLC7gxKLhUC3vO8tgo9tCSMTUOqUBouIg3Mug29ZCoqb0cYFvg0YHN1cQr0agHKECS0TUNGLBHqSqSOS7VLMckqNwNLrh3VSuY_kJxmCg_ze6x8bCL8nhxfHvpLSTgsbTC_1cefDcN1pcLmXg2fM9FLYUwmceNBcipGbBO9NgrVJDop68p9FvH1J7uBQvgsWgxLyvOZiJpMJhxY0Bcfmh3mWJSC68Xs"
    }
    # 手动构建翻页的url
    def start_requests(self):
        url = "https://www.zhihu.com/api/v4/questions/277135177/feeds?"
        params = {
            "include": "data[*].is_normal,admin_closed_comment,reward_info,is_collapsed,annotation_action,annotation_detail,collapse_reason,is_sticky,collapsed_by,suggest_edit,comment_count,can_comment,content,editable_content,attachment,voteup_count,reshipment_settings,comment_permission,created_time,updated_time,review_info,relevant_info,question,excerpt,is_labeled,paid_info,paid_info_content,reaction_instruction,relationship.is_authorized,is_author,voting,is_thanked,is_nothelp;data[*].author.follower_count,vip_info,kvip_info,badge[*].topics;data[*].settings.table_of_content.enabled",
            "limit": "500",
            "offset": "0",
            "order": "default",
            "platform": "desktop",
            "session_id": "1745364620148165106",
            "ws_qiangzhisafe": "0"
        }
        encoded_params = url + urllib.parse.urlencode(params)
        # print(encoded_params)
        # print(encoded_params)
        ctll = execjs.compile(open('zhihu.js', encoding='utf-8').read())
        result = ctll.call('get_x_zse_96', encoded_params, self.headers["x-zst-81"])
        self.headers["x-zse-96"] = str(result)
        yield scrapy.Request(url=encoded_params, headers=self.headers, cookies=self.cookies, callback=self.parse)

    def parse(self, response: HtmlResponse, **kwargs):
        next = response.json()['paging']['next']
        datas = response.json()['data']
        for data in datas:
            item = dict()
            cursor_ = data.get('cursor')
            excerpt = data['target']['excerpt']
            content = data['target']['content']
            created_time = data['target']['created_time']
            author_id = data['target']['id']
            voteup_count = data['target']['voteup_count']
            item['cursor_'] = cursor_
            item['excerpt'] = excerpt
            item['content'] = content
            item['created_time'] = str(self.parse_time(created_time))
            item['author_id'] = author_id
            item['voteup_count'] = voteup_count
            # print(item)
            yield item
            ctll = execjs.compile(open('zhihu.js', encoding='utf-8').read())
            result = ctll.call('get_x_zse_96', str(next), self.headers['x-zst-81'])
            self.headers['x-zse-96'] = str(result)
        while True:
            if next == "" or next == []:
                break
            yield scrapy.Request(next, headers=self.headers, cookies=self.cookies, callback=self.parse)

    def parse_time(self,timestamp):
        # 给定的时间戳
        # 将时间戳转换为 datetime 对象
        dt_object = datetime.utcfromtimestamp(timestamp)
        # 打印结果，格式化为 '年-月-日 时:分:秒'
        formatted_date = dt_object.strftime('%Y-%m-%d %H:%M:%S')
        return formatted_date


if __name__ == '__main__':
    cmdline.execute('scrapy crawl zhihu_spider'.split())
