# 导入数据请求模块  --> 第三方模块 需要 在cmd里面 pip install requests
import requests
# 导入数据解析模块  --> 第三方模块 需要 在cmd里面 pip install parsel
import parsel
# 导入正则模块 --> 内置模块 不需要安装
import re
# 导入文件操作模块 --> 内置模块 不需要安装
import os.path

# 构建翻页range,-1表示倒序
for page in range(1, 0, -1):
    print(f'正在采集第{page}页的数据内容==========================================================')
    # 我的壁纸收藏的 url 地址，官方网址：https://wallhaven.cc/
    url = f'https://wallhaven.cc/user/roydon/favorites/1347075?page={page}'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36'
    }
    response = requests.get(url=url, headers=headers)
    selector = parsel.Selector(response.text)
    href = selector.css('.thumb-listing-page ul li .thumb .preview::attr(href)').getall()
    print(len(href))
    print(href)
    for index in href:
        index_url = index
        index_data = requests.get(url=index_url, headers=headers).text
        index_selector = parsel.Selector(index_data)
        img_url = index_selector.css('#main #showcase .scrollbox img::attr(src)').get()
        print(img_url)

        file = f'E:\\wallpaperBorn\\favorites\\第{page}页\\'
        # 如果没有这个文件夹
        if not os.path.exists(file):
            os.makedirs(file)
        img_content = requests.get(url=img_url, headers=headers).content
        # 保存图片
        with open(file + img_url[-10:], mode='wb') as f:
            f.write(img_content)
        print('ok哒')
