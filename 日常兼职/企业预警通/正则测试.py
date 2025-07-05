import re

text = "(截止最新，债券存量规模0.00亿元，债券1只。)"
# 匹配存量规模
scale_pattern = r'债券存量规模(\d+\.?\d*)亿元'
# 匹配债券数量
count_pattern = r'债券(\d+)只'

scale_match = re.search(scale_pattern, text)
count_match = re.search(count_pattern, text)

if scale_match:
    scale = scale_match.group(1)
else:
    scale = None

if count_match:
    count = count_match.group(1)
else:
    count = None

print(f"存量规模: {scale}")
print(f"债券数量: {count}")

# 匹配存量规模
scale_pattern = r'债券存量规模(\d+\.?\d*)亿元'
scale_match = re.search(scale_pattern, message)

if scale_match:
    scale = float(scale_match.group(1))
    if scale > 0.00:
        print(f"债券存量规模: {scale}亿元")
        continuous_creditors_right = f'{scale}亿元'
    else:
        print("债券存量规模为 0.00 亿元，不输出。")
else:
    print("未找到债券存量规模信息。")