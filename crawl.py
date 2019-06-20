import requests
from bs4 import BeautifulSoup
import csv


def get_html():
    # 爬取数据的网址
    url = 'https://zz.58.com/pinpaigongyu/pn/{page}/?minprice=2000_3000'
    # 初始化页码
    page = 0
    # 打开re.csv文件，如果没有就创建一个，并设置写入模式
    csv_file = open('zzzf.csv', 'w', encoding='utf_8_sig', newline='')
    # 创建writer对象
    writer = csv.writer(csv_file, dialect='excel')
    # 循环所有页面
    while True:
        page += 1
        # 抓取目标页面
        response = requests.get(url.format(page=page))
        response.encoding = 'utf-8'     # 设置编码格式
        # 创建一个BeautifulSoup对象，获取页面正文
        html = BeautifulSoup(response.text, 'html.parser')
        # 获取当前页面的房子信息
        house_list = html.select(".list > li")
        print("正在下载网页", url.format(page=page))
        page_a_list = html.find('div', class_='paper')   # 查看页面中是否有切换页面的按钮
        if page_a_list is not None:     # 存在切换页面的按钮
            page_a_list = page_a_list.select('span')        # 查找关于按钮名称的代码
            str_page = str(page_a_list)     # 将代码转换成字符串类型
            if '<span>下一页</span>' in str_page:      # 判断是否有下一页按钮
                write_file(house_list, writer)      # 如果有就写入收据并循环下一页
            else:       # 否则就写入当前页的数据 跳出循环
                write_file(house_list, writer)
                # 关闭文件
                csv_file.close()
                break
        else:       # 当前页面没有切换页面按钮就写入当前页面数据，跳出循环
            write_file(house_list, writer)
            # 关闭文件
            csv_file.close()
            break


def write_file(house_list, writer):
        # 遍历房子信息
        for house in house_list:
            if house is not None:
                # 获取房子标题
                house_title = house.find('div', class_='img').img.get('alt')
                # 对标题进行分隔
                house_info_list = house_title.split()
                # 获取房子位置
                house_location = house_info_list[1]
                # 获取房子链接地址
                house_url = house.select("a")[0]["href"]
                # 写入一行数据
                writer.writerow([house_title, house_location, house_url])


get_html()




