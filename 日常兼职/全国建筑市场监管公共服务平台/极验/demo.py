def generate_values(x, y):
    # 根据对应关系生成 x_gen 和 y_gen
    x_gen = x * 3
    y_gen = y * 3
    return x_gen, y_gen

# 测试函数
real_values = [(14, 10), (156, 9), (279, 200), (68, 267), (280, 278)]
for x, y in real_values:
    x_gen, y_gen = generate_values(x, y)
    print(f"真实值: x,y ({x}, {y})  生成值: x,y({x_gen}, {y_gen})")
