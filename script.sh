#!/bin/bash

# 检查参数数量是否正确
if [ "$#" -ne 2 ]; then
    echo "使用方法: $0 <搜索文件> <搜索内容>"
    exit 1
fi

search_file="$1"
search_content="$2"
output_file="search_results.txt"

# 检查文件是否存在
if [ ! -f "$search_file" ]; then
    echo "错误: 文件 '$search_file' 不存在"
    exit 1
fi

# 清空或创建输出文件
> "$output_file"

echo "正在文件 '$search_file' 中搜索 '$search_content'..."
echo "搜索结果:"

# 使用 grep 搜索内容，并显示行号
grep -n "$search_content" "$search_file" | while read -r line; do
    # 输出到控制台
    echo "$line"
    # 写入到文件
    echo "$line" >> "$output_file"
done

echo "搜索结果已保存到 '$output_file'"
