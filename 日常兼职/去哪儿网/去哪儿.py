import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import random
import re
import os
import urllib.parse

# 设置请求头模拟浏览器访问
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Referer': 'https://travel.qunar.com/'
}


def get_guide_urls(page_num):
    url = f"https://travel.qunar.com/travelbook/list.htm?page={page_num}&order=hot_heat"
    try:
        print(f"Requesting URL: {url}")
        response = requests.get(url, headers=headers, timeout=15)
        response.encoding = 'utf-8'  # 确保正确编码

        if response.status_code != 200:
            print(f"Failed to get page {page_num}, status code: {response.status_code}")
            return []

        soup = BeautifulSoup(response.text, 'html.parser')

        # 尝试多种可能的选择器
        guide_list = soup.find('ul', class_='b_strategy_list')
        if not guide_list:
            print("Couldn't find 'b_strategy_list', trying alternative selectors")
            guide_list = soup.find('ul', class_='list_item')

        if not guide_list:
            print(f"No guide list found on page {page_num} with any selector")
            return []

        guides = guide_list.find_all('li')
        urls = []

        for guide in guides:
            # 尝试多种可能的选择器找到链接
            a_tag = guide.find('a', class_='tit')
            if not a_tag:
                a_tag = guide.find('a', class_='title')
            if not a_tag:
                a_tag = guide.find('h2').find('a') if guide.find('h2') else None

            if a_tag and 'href' in a_tag.attrs:
                guide_url = urllib.parse.urljoin('https://travel.qunar.com', a_tag['href'])
                urls.append(guide_url)
                print(f"Found guide: {a_tag.text.strip() if a_tag.text else 'No title'} - {guide_url}")

        print(f"Found {len(urls)} guides on page {page_num}")
        return urls
    except Exception as e:
        print(f"Error getting guide URLs from page {page_num}: {e}")
        return []


def extract_guide_data(url):
    try:
        print(f"Extracting data from: {url}")
        response = requests.get(url, headers=headers, timeout=15)
        response.encoding = 'utf-8'  # 确保正确编码

        if response.status_code != 200:
            print(f"Failed to get {url}, status code: {response.status_code}")
            return None

        soup = BeautifulSoup(response.text, 'html.parser')
        data = {}

        # 攻略标题 - 尝试多种选择器
        title_elem = soup.find('h1', class_='booktitle')
        if not title_elem:
            title_elem = soup.find('h1', class_='title')
        if not title_elem:
            title_elem = soup.find('h1')
        data['title'] = title_elem.text.strip() if title_elem else None

        # 用户名 - 尝试多种选择器
        author_elem = soup.find('span', class_='user_name')
        if not author_elem:
            author_elem = soup.find('a', class_='author_name')
        if not author_elem:
            author_info = soup.find('div', class_='c_author_name') or soup.find('div', class_='author')
            author_elem = author_info.find('a') if author_info else None
        data['username'] = author_elem.text.strip() if author_elem else None

        # 途径路线
        route_elem = soup.find('div', class_='places')
        if not route_elem:
            route_elem = soup.find('div', class_='route')
        if not route_elem:
            route_info = soup.find('div', {'data-reactid': re.compile(r'.*places.*')})
            route_elem = route_info if route_info else None
        data['route'] = route_elem.text.strip() if route_elem else None

        # 行程内容
        content_div = soup.find('div', class_='b_panel_content')
        if not content_div:
            content_div = soup.find('div', class_='content')
        if not content_div:
            content_div = soup.find('div', class_='b_notes_content')
        data['itinerary'] = content_div.text[:200].strip() if content_div else None

        # 出发日期
        date_pattern = re.compile('出发时间|出行时间|旅行时间')
        date_elem = None
        for elem in soup.find_all('li', class_='item'):
            if elem.text and date_pattern.search(elem.text):
                date_elem = elem
                break

        if date_elem:
            value_span = date_elem.find('span', class_='value')
            data['departure_date'] = value_span.text.strip() if value_span else date_elem.text.replace('出发时间',
                                                                                                       '').replace(
                '出行时间', '').replace('旅行时间', '').strip()
        else:
            date_div = soup.find('div', text=date_pattern)
            if date_div:
                next_elem = date_div.find_next()
                data['departure_date'] = next_elem.text.strip() if next_elem else None
            else:
                data['departure_date'] = None

        # 行程天数
        days_pattern = re.compile('出行天数|行程天数|旅行天数')
        days_elem = None
        for elem in soup.find_all('li', class_='item'):
            if elem.text and days_pattern.search(elem.text):
                days_elem = elem
                break

        if days_elem:
            value_span = days_elem.find('span', class_='value')
            data['days'] = value_span.text.strip() if value_span else days_elem.text.replace('出行天数', '').replace(
                '行程天数', '').replace('旅行天数', '').strip()
        else:
            days_div = soup.find('div', text=days_pattern)
            if days_div:
                next_elem = days_div.find_next()
                data['days'] = next_elem.text.strip() if next_elem else None
            else:
                # 尝试从标题或内容中提取天数
                days_match = re.search(r'\d+[天日]', data['title'] if data['title'] else '')
                if not days_match and data['itinerary']:
                    days_match = re.search(r'\d+[天日]', data['itinerary'])
                data['days'] = days_match.group(0) if days_match else None

        # 人物标签和玩法标签
        tags_div = soup.find('div', class_='tags')
        if not tags_div:
            # 尝试找到所有可能的标签元素
            tag_elems = soup.find_all('span', class_='tag') or soup.find_all('a', class_='tag')
            if tag_elems:
                tags = [tag.text.strip() for tag in tag_elems if tag.text.strip()]
                data['tags'] = ', '.join(tags)
            else:
                data['tags'] = None
        else:
            data['tags'] = tags_div.text.strip()

        # 人均费用
        cost_pattern = re.compile('人均花费|人均消费|人均开销|费用')
        cost_elem = None
        for elem in soup.find_all('li', class_='item'):
            if elem.text and cost_pattern.search(elem.text):
                cost_elem = elem
                break

        if cost_elem:
            value_span = cost_elem.find('span', class_='value')
            data['cost'] = value_span.text.strip() if value_span else cost_elem.text.replace('人均花费', '').replace(
                '人均消费', '').replace('人均开销', '').replace('费用', '').strip()
        else:
            cost_div = soup.find('div', text=cost_pattern)
            if cost_div:
                next_elem = cost_div.find_next()
                data['cost'] = next_elem.text.strip() if next_elem else None
            else:
                # 尝试从内容中提取费用信息
                if data['itinerary']:
                    cost_match = re.search(r'\d+元|\d+\.\d+元|\d+块|\d+\.\d+块|\d+人民币|\d+\.\d+人民币',
                                           data['itinerary'])
                    data['cost'] = cost_match.group(0) if cost_match else None
                else:
                    data['cost'] = None

        # 照片数量
        all_imgs = soup.find_all('img')
        content_imgs = []
        if content_div:
            content_imgs = content_div.find_all('img')
        data['photo_count'] = len(content_imgs) if content_imgs else len(all_imgs)

        # 文字内容 (摘要)
        if content_div:
            text_content = content_div.text.strip()
            # 移除过长的空白
            text_content = re.sub(r'\s+', ' ', text_content)
            data['text_content'] = text_content[:300] if text_content else None
        else:
            data['text_content'] = None

        # 图片内容 (第一张照片的URL)
        img_elem = None
        if content_div:
            img_elem = content_div.find('img')
        if not img_elem:
            img_elem = soup.find('img', class_='cover') or soup.find('img')

        if img_elem and 'src' in img_elem.attrs:
            img_src = img_elem['src']
            # 确保是完整URL
            if not img_src.startswith('http'):
                img_src = urllib.parse.urljoin('https://travel.qunar.com', img_src)
            data['image_content'] = img_src
        else:
            data['image_content'] = None

        # 统计数据
        # 观看数
        view_pattern = re.compile('浏览|查看|阅读')
        views_elem = soup.find('span', class_=lambda c: c and 'view' in c) or soup.find('span', text=view_pattern)
        data['views'] = views_elem.text.strip() if views_elem else None

        # 点赞数
        like_pattern = re.compile('赞|点赞|顶')
        likes_elem = soup.find('span', class_=lambda c: c and ('like' in c or 'ding' in c)) or soup.find('span',
                                                                                                         text=like_pattern)
        data['likes'] = likes_elem.text.strip() if likes_elem else None

        # 收藏数
        fav_pattern = re.compile('收藏|珍藏')
        favs_elem = soup.find('span', class_=lambda c: c and ('collect' in c or 'fav' in c)) or soup.find('span',
                                                                                                          text=fav_pattern)
        data['favorites'] = favs_elem.text.strip() if favs_elem else None

        # 分享数
        share_pattern = re.compile('分享')
        share_elem = soup.find('span', class_=lambda c: c and 'share' in c) or soup.find('span', text=share_pattern)
        data['shares'] = share_elem.text.strip() if share_elem else None

        # 评论数量和内容
        comment_pattern = re.compile('评论')
        comment_elem = soup.find('span', class_=lambda c: c and 'comment' in c) or soup.find('span',
                                                                                             text=comment_pattern)
        data['comments'] = comment_elem.text.strip() if comment_elem else None

        # 记录爬取成功的URL
        data['url'] = url

        # 记录日志
        print(f"Successfully extracted data for: {data['title']}")
        return data
    except Exception as e:
        print(f"Error extracting data from {url}: {e}")
        return None


# 主爬虫逻辑
all_data = []
max_pages = 50  # 增加页面数以确保获取足够数据
min_data_required = 120  # 目标数据量

for page in range(1, max_pages + 1):
    print(f"\n{'=' * 50}\nProcessing page {page}...\n{'=' * 50}")
    urls = get_guide_urls(page)

    if not urls:
        print(f"No URLs found on page {page}, trying next page...")
        continue

    for url in urls:
        try:
            print(f"\nProcessing URL: {url}")
            data = extract_guide_data(url)

            if data:
                all_data.append(data)
                print(f"Successfully extracted data. Total collected: {len(all_data)}")
            else:
                print(f"Failed to extract data from {url}")

            # 随机延迟，避免请求过于频繁
            delay = random.uniform(3, 7)
            print(f"Waiting for {delay:.2f} seconds...")
            time.sleep(delay)

        except Exception as e:
            print(f"Error processing {url}: {e}")

        # 检查是否已收集足够数据
        if len(all_data) >= min_data_required:
            print(f"Reached target data count: {len(all_data)}")
            break

    if len(all_data) >= min_data_required:
        print(f"Reached target data count: {len(all_data)}. Stopping.")
        break

    # 页面间延迟
    page_delay = random.uniform(5, 10)
    print(f"Finished page {page}. Waiting {page_delay:.2f} seconds before next page...")
    time.sleep(page_delay)

# 数据预处理
print(f"\nData collection complete. Collected {len(all_data)} raw entries.")
print("Processing data...")

if all_data:
    # 创建DataFrame
    df = pd.DataFrame(all_data)

    # 删除完全重复的行
    initial_count = len(df)
    df = df.drop_duplicates()
    print(f"Removed {initial_count - len(df)} completely duplicate entries.")

    # 删除标题和用户名重复的行
    pre_dedup_count = len(df)
    df = df.drop_duplicates(subset=['title', 'username'], keep='first')
    print(f"Removed {pre_dedup_count - len(df)} entries with duplicate titles and usernames.")

    # 处理缺失值
    print("\nMissing value counts before filling:")
    for column in df.columns:
        null_count = df[column].isna().sum()
        if null_count > 0:
            print(f"Column '{column}' has {null_count} missing values.")

    # 填充缺失值
    df = df.fillna({
        'title': 'Unknown Title',
        'username': 'Anonymous User',
        'route': 'Not Specified',
        'itinerary': 'Not Available',
        'departure_date': 'Unknown',
        'days': 'Not Specified',
        'tags': 'No Tags',
        'cost': 'Not Specified',
        'text_content': 'No Content',
        'image_content': 'No Image',
        'views': '0',
        'likes': '0',
        'favorites': '0',
        'shares': '0',
        'comments': '0'
    })


    # 数值列处理 - 确保数值列为数值类型
    # 从统计数据中提取数字
    def extract_number(text):
        if pd.isna(text):
            return 0
        # 提取数字部分
        match = re.search(r'\d+', str(text))
        if match:
            return int(match.group())
        return 0


    # 处理统计类列
    for col in ['views', 'likes', 'favorites', 'shares', 'comments']:
        if col in df.columns:
            df[col] = df[col].apply(extract_number)

    # 确保photo_count为整数
    if 'photo_count' in df.columns:
        df['photo_count'] = pd.to_numeric(df['photo_count'], errors='coerce').fillna(0).astype(int)


    # 提取天数为数字
    def extract_days(text):
        if pd.isna(text):
            return None
        # 提取数字部分
        match = re.search(r'\d+', str(text))
        if match:
            return int(match.group())
        return None


    if 'days' in df.columns:
        df['trip_days'] = df['days'].apply(extract_days)
        df['trip_days'] = pd.to_numeric(df['trip_days'], errors='coerce').fillna(0).astype(int)

    # 将数值型的列转换为整数
    numeric_cols = ['photo_count', 'views', 'likes', 'favorites', 'shares', 'comments', 'trip_days']
    for col in numeric_cols:
        if col in df.columns:
            df[col] = df[col].astype(int)

    # 检查处理后的数据量
    final_count = len(df)
    print(f"\nFinal dataset contains {final_count} entries.")

    if final_count < 100:
        print(f"Warning: Only collected {final_count} unique entries, which is less than the required 100.")
    else:
        print(f"Successfully collected {final_count} unique entries, meeting the requirement of at least 100 entries.")

    # 保存到CSV文件
    output_file = 'travel_guides.csv'
    df.to_csv(output_file, index=False, encoding='utf-8-sig')
    print(f"Data saved to {output_file}")

    # 显示数据集的信息
    print("\nDataset information:")
    print(df.info())
    print("\nSample data (first 5 rows):")
    print(df[['title', 'username', 'route', 'days', 'cost', 'photo_count', 'views', 'likes']].head())
else:
    print("No data collected. Please check the website structure or network connection and try again.")