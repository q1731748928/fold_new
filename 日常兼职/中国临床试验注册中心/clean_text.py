with open("showproj.html?proj=267713.txt", 'r') as f:
    tt = f.read()
lines = str(tt).split('\n')
for i, line in enumerate(lines, 1):  # enumerate 从1开始计数行号
    # 注册号
    print(f"第{i}行: {line}")
    if i == 1:
        print(f"第{i}行: 注册号：{line}")

    if i == 2:
        print(f"第{i}行: {line}")

    if i == 4:
        print(f"第{i}行: 注册号状态：{line}")

    if i == 6:
        print(f"第{i}行: 注册题目：{line}")
    # 申请注册联系人
    if i == 10:
        print(f"第{i}行: 申请注册联系人：{line}")
    # 研究负责人
    if i == 12:
        print(f"第{i}行: 研究负责人：{line}")
    #
    if i == 16:
        print(f"第{i}行: 申请注册联系人电话：{line}")
    #
    if i == 23:
        print(f"第{i}行: 申请注册联系人电子邮件：{line}")
    #
    if i == 27:
        print(f"第{i}行: 申请单位网址(自愿提供)：{line}")
    #
    if i == 31:
        print(f"第{i}行: 申请注册联系人通讯地址：{line}")
    #
    if i == 39:
        print(f"第{i}行: 申请人所在单位：{line}")
    # 是否获伦理委员会批准：
    if i == 41:
        print(f"第{i}行: 是否获伦理委员会批准：{line}")
    #
    if i == 46:
        print(f"第{i}行: 批准本研究的伦理委员会名称：{line}")
    #
    if i == 48:
        print(f"第{i}行: 伦理委员会批准日期：{line}")
    #
    if i == 51:
        print(f"第{i}行: 研究实施负责（组长）单位：{line}")
    #
    if i == 55:
        print(f"第{i}行: 试验主办单位：{line}")












