# 准备工作

1. 登陆github.com并注册个人账户
2. 创建一个公开的repo

# 开发内容

## 1. python测试

### 1.1 scrapy爬取测试

1. 通过 scrapy 实现网页信息爬取和采集。
2. 通过提供的列表页网址采集到详情页的信息。
3. 爬取结果存成一份 JSON文档。
4. JSON文档要求：  
   主要信息：
   - 标题（title）
   - 价格(price)
   - 颜色(color)
   - 尺码(size)
   - 网站货号(sku)
   - 详情(details)
   - 大图的URL (img_urls)
   - 其它字段随意
5. 抓取前48个
6. 要爬取的地址：
   - 网站: https://www.nike.com.cn/
   - 列表页网址: https://www.nike.com.cn/w/

## 2. 算法

**题目：**  
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

**Example 1:**
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

text

**Constraints:**
- 2 <= nums.length <= 10⁴
- -10⁹ <= nums[i] <= 10⁹
- -10⁹ <= target <= 10⁹
- Only one valid answer exists.

## 3. linux

**任务：**  
编写一个shell脚本(linux)，功能如下:

在给定文件中搜索指定内容，并将搜索结果(含内容出现的行号)保存到新的文件中，同时结果输出到控制台。
