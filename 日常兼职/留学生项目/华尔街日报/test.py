keywords = {
    "AAPL": [
        "apple", "iphone", "aapl", "macbook", "ipad", "ios",
        "apple inc", "apple earnings", "apple revenue", "tim cook"
    ],
    "MSFT": [
        "microsoft", "msft", "windows", "office", "azure", "xbox",
        "microsoft corp", "satya nadella", "microsoft earnings", "microsoft cloud"
    ],
    "GOOGL": [
        "alphabet", "google", "googl", "android", "youtube", "chrome", "google cloud",
        "google earnings", "alphabet inc", "sundar pichai", "waymo"
    ]
}

def find_parent_company(keyword):
    # 遍历字典，检查关键词是否在某个公司下
    for parent_company, keywords_list in keywords.items():
        if keyword.lower() in [k.lower() for k in keywords_list]:  # 不区分大小写比较
            return parent_company
    return None  # 如果没有找到对应的母公司

# 测试
keyword = input("请输入一个关键词: ")  # 输入关键词
parent_company = find_parent_company(keyword)

if parent_company:
    print(f"关键词 '{keyword}' 的母公司是: {parent_company}")
else:
    print(f"没有找到关键词 '{keyword}' 的母公司。")