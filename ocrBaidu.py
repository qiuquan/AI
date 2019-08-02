# -*- coding: UTF-8 -*-

# --https://ai.baidu.com/docs#/OCR-Python-SDK/07883957--接口文档

from aip import AipOcr

# 定义常量
APP_ID = '16938377'
API_KEY = 'e2IC26RZBbHFGwEZ0X1ZuyF8'
SECRET_KEY = 'WZvHp8EsyB7tTgyR1pd1GXrNuHhHhOZD'

# 初始化文字识别分类器
aipOcr=AipOcr(APP_ID, API_KEY, SECRET_KEY)

# 读取图片
filePath = "1.jpg"

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

# 定义参数变量
options = {
    'detect_direction': 'true',
    'language_type': 'CHN_ENG',
}

print(get_file_content(filePath))

# 网络图片文字文字识别接口
result = aipOcr.webImage(get_file_content(filePath),options)

# 如果图片是url 调用示例如下
# result = apiOcr.webImage('http://www.xxxxxx.com/img.jpg')

for i in result.keys():
    if i == 'words_result':
        print(result[i])
        for j in result[i]:
            #print(j)
            for k in j.keys():
                print(j[k])


