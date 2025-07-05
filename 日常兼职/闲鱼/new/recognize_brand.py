import re

import re

# 假设品牌列表
brands = ["华为", "小米", "联想", "中兴", "OPPO", "vivo", "一加", "魅族", "锤子", "诺基亚", "TCL", "海信", "创维", "海尔", "紫米", "步步高", "大疆", "360", "黑鲨", "坚果", "乐视", "科大讯飞", "华硕", "苹果", "三星", "索尼", "戴尔", "惠普", "微软", "英特尔", "尼康", "佳能", "LG", "雷蛇", "HTC", "飞利浦", "博世", "西部数据", "赛米控", "Siemens", "特斯拉", "亚马逊", "富士", "松下", "摩托罗拉", "高通", "雷神", "AMD", "英伟达"]

# 将品牌中的数字0替换为字母O，以避免误差
pattern = r'|'.join(re.escape(brand.replace('0', 'O')) for brand in brands)



# 处理大小写，忽略数字0与字母O的差异
def extract_brands(title):
    matches = re.findall(pattern, title, flags=re.IGNORECASE)
    if matches:
        return matches
    else:
        return None  # 或者返回 []





# 待匹配的标题
title = "ViV0，y81，3+32G内存，功能完好，插卡可用，看好在 拍，二手物品出售不退不换"
result = extract_brands(title)
if result is not None:
    print(f"匹配到的品牌: {result[0]}")
else:
    print("没有匹配到品牌")