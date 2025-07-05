import requests
from bs4 import BeautifulSoup
import pandas as pd
import pymysql
from datetime import datetime
import random
import re
import time

# ==== 全局配置 ====
headers = {
    'User-Agent': random.choice([
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0'
    ]),
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br'
}

hot_keywords = ["人工智能", "经济", "关税"]  # 可扩展关键词
all_news = []  # 存储新闻数据

# ==== 通用工具函数 ====
def normalize_time(raw_time):
    """标准化时间格式"""
    try:
        # 替换中文日期单位
        normalized = raw_time.replace('年', '-').replace('月', '-').replace('日', ' ').replace('时', ':').replace('分', '')
        # 提取时间成分
        time_match = re.search(
            r'(?P<year>\d{4})[-/]?(?P<month>\d{1,2})[-/]?(?P<day>\d{1,2})[^\d]*(?P<hour>\d{1,2}):?(?P<minute>\d{2})?',
            normalized
        )
        if time_match:
            components = time_match.groupdict()
            # 补全默认值
            components['minute'] = components['minute'] or '00'
            return f"{components['year']}-{components['month']:0>2}-{components['day']:0>2} " \
                   f"{components['hour']:0>2}:{components['minute']:0>2}"
        return raw_time.strip()[:16]  # 保留原始格式前16字符
    except:
        return "未知"

# ==== 网易新闻抓取 ====
def fetch_163_news(keyword):
    print(f"🔍 正在抓取网易新闻：关键词【{keyword}】")
    base_url = "https://news.163.com/"
    try:
        resp = requests.get(base_url, headers=headers, timeout=15)
        soup = BeautifulSoup(resp.text, 'lxml')

        for a in soup.find_all("a", href=True):
            title = a.get_text(strip=True)
            href = a['href']
            if keyword in title and href.startswith("http") and "163.com" in href:
                try:
                    # 动态请求头
                    article_headers = {
                        **headers,
                        'Referer': base_url,
                        'Sec-Fetch-Dest': 'document'
                    }
                    
                    # 带重试机制的请求
                    article = requests.get(href, headers=article_headers, timeout=20)
                    article.encoding = 'utf-8'
                    article_soup = BeautifulSoup(article.text, 'lxml')

                    # 改进的时间提取
                    time_tag = article_soup.find("div", class_="post_time_source") or \
                              article_soup.find("span", class_="time")
                    pub_time = "未知"
                    if time_tag:
                        raw_time = re.sub(r'\s+', ' ', time_tag.text.strip())
                        pub_time = normalize_time(raw_time.split('来源:')[0])

                    # 增强的正文提取
                    content_div = article_soup.find("div", class_="post_body") or \
                                 article_soup.find("div", {"id": "content"})
                    
                    full_text = "无正文内容"
                    if content_div:
                        # 清理广告和干扰元素
                        [ad.decompose() for ad in content_div.select(".gg200x300, .ep-source, .ad-wrap, script")]
                        paragraphs = content_div.select("p:not([class]):not([style])")
                        filtered_paragraphs = [p.get_text(strip=True) for p in paragraphs if len(p.text.strip()) > 15]
                        full_text = "\n".join(filtered_paragraphs) if filtered_paragraphs else "无有效正文内容"

                    all_news.append({
                        "网站": "网易新闻",
                        "标题": title[:200],  # 限制标题长度
                        "链接": href,
                        "关键词": keyword,
                        "抓取时间": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        "发布时间": pub_time,
                        "正文": full_text[:5000]  # 限制正文长度
                    })

                except Exception as e:
                    print(f"[子错误] 网易解析失败：{str(e)[:60]}...")
    except Exception as e:
        print(f"[错误] 抓取网易失败：{str(e)[:60]}...")

# ==== 央视新闻抓取 ====
def fetch_sina_news(keyword):
    print(f"🔍 正在抓取央视新闻：关键词【{keyword}】")
    base_url = "https://news.cctv.com/china/"
    params = {
        'q': keyword,
        'c': 'news',
        'range': 'title',
        'num': 20,
        'col': '1_7',
        '_': str(int(time.time() * 1000)),  # 防缓存
        'callback': 'jsonp_callback'
    }
    
    try:
        resp = requests.get(base_url, params=params, headers=headers, timeout=20)
        resp.encoding = 'utf-8'
        soup = BeautifulSoup(resp.text, 'lxml')

        news_found = False
        
        for item in soup.select('.result'):
            try:
                title_tag = item.select_one('h2 a')
                if not title_tag:
                    continue
                
                title = title_tag.text.strip()
                href = title_tag['href']
                
                # 多层时间提取
                time_container = item.select_one('.fgray, .source, .time-source')
                pub_time = "未知"
                if time_container:
                    time_text = ' '.join(time_container.stripped_strings)
                    pub_time = normalize_time(time_text)

                # 动态请求头
                article_headers = {
                    **headers,
                    'Referer': base_url,
                    'Upgrade-Insecure-Requests': '1'
                }
                
                # 带超时重试的请求
                article = requests.get(href, headers=article_headers, timeout=(5, 20))
                article.encoding = article.apparent_encoding
                article_soup = BeautifulSoup(article.text, 'lxml')
                
                # 多策略正文提取
                content_div = article_soup.select_one('.article-content') or \
                             article_soup.find('div', {'id': 'artibody'}) or \
                             article_soup.find('div', {'class': 'article'})
                
                full_text = "无正文内容"
                if content_div:
                    # 清理干扰内容
                    [s.decompose() for s in content_div.select('.hidden, .article-editor, .article-keywords, .comment, iframe')]
                    paragraphs = content_div.select('p:not([style*="display:none"]):not(.article-keywords)')
                    valid_paragraphs = [p.text.strip() for p in paragraphs if 15 < len(p.text.strip()) < 500]
                    full_text = '\n'.join(valid_paragraphs) if valid_paragraphs else "无有效正文内容"

                all_news.append({
                    "网站": "新浪新闻",
                    "标题": title[:200],
                    "链接": href,
                    "关键词": keyword,
                    "抓取时间": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "发布时间": pub_time,
                    "正文": full_text[:5000]
                })
                news_found = True

            except Exception as e:
                print(f"[子错误] 央视解析失败：{str(e)[:60]}...")

        if not news_found:
            print(f"⚠️ 没有找到央视新闻：关键词【{keyword}】")

    except Exception as e:
        print(f"[错误] 抓取央视失败：{str(e)[:60]}...")

# ==== 数据存储 ====
def save_to_mysql(data_list):
    try:
        conn = pymysql.connect(
            host='localhost',
            user='root',
            password='xzxz083083',
            database='news_db',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )
        
        with conn.cursor() as cursor:
            # 创建表（带去重索引）
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS hot_news (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    网站 VARCHAR(100) NOT NULL,
                    标题 VARCHAR(200) NOT NULL,
                    链接 VARCHAR(500) UNIQUE,  -- 链接唯一索引
                    关键词 VARCHAR(50) NOT NULL,
                    抓取时间 DATETIME NOT NULL,
                    发布时间 VARCHAR(20),
                    正文 TEXT,
                    INDEX idx_keyword (关键词),
                    INDEX idx_source (网站)
                ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
            """)
            
            # 批量插入（忽略重复链接）
            sql = """INSERT IGNORE INTO hot_news 
                    (网站, 标题, 链接, 关键词, 抓取时间, 发布时间, 正文)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)"""
            batch_data = [
                (item['网站'], item['标题'], item['链接'], item['关键词'],
                 item['抓取时间'], item['发布时间'], item['正文'])
                for item in data_list
            ]
            cursor.executemany(sql, batch_data)
            
        conn.commit()
        print(f"✅ 成功插入 {cursor.rowcount} 条数据到MySQL")

    except Exception as e:
        print(f"❌ 数据库操作失败：{str(e)[:200]}")
    finally:
        if conn:
            conn.close()

# ==== 主程序 ====
if __name__ == "__main__":
    # 执行抓取任务
    for keyword in hot_keywords:
        fetch_sina_news(keyword)
        fetch_163_news(keyword)
        time.sleep(random.uniform(1, 3))  # 随机延迟防封禁

    # 数据处理
    if not all_news:
        print("⚠️ 没有抓取到任何新闻")
    else:
        # 数据清洗
        df = (
            pd.DataFrame(all_news)
            .drop_duplicates(subset=['链接'], keep='last')
            .sort_values('发布时间', ascending=False)
        )
        
        # 文件存储
        df.to_csv("hot_news.csv", index=False, encoding="utf-8-sig")
        df.to_json("hot_news.json", orient="records", force_ascii=False, indent=2)
        print(f"📁 已保存 {len(df)} CSV.JSON")
        
        # 数据库存储（可选）
        #if not df.empty:
           #save_to_mysql(df.to_dict('records'))
