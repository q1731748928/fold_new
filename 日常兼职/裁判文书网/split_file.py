import os


def split_file(input_file, target_size_mb=500):
    target_size_bytes = target_size_mb * 1024 * 1024  # 目标文件大小（字节）

    with open(input_file, "r", encoding="utf-8") as f:
        chunk = []
        current_size = 0
        file_count = 1

        for line in f:
            # 计算当前行的字节数
            current_size += len(line.encode('utf-8'))
            chunk.append(line)

            # 如果当前文件大小超过目标大小，保存并开始新的文件
            if current_size >= target_size_bytes:
                with open(f"chunk_{file_count}.txt", "w", encoding="utf-8") as out:
                    out.writelines(chunk)
                file_count += 1
                chunk = []
                current_size = 0

        # 如果最后一部分内容没有满目标大小，仍然保存
        if chunk:
            with open(f"chunk_{file_count}.txt", "w", encoding="utf-8") as out:
                out.writelines(chunk)


# 调用函数进行文件分割
split_file("/Users/hejie/PycharmProjects/turing_exec/日常兼职/裁判文书网/data_1 96万.txt")
