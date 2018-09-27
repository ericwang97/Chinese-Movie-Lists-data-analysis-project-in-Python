# -*- coding: utf-8 -*-
import codecs
import csv
import re
import requests
from bs4 import BeautifulSoup


def getHTML(url):
    r = requests.get(url)
    return r.content

def llist(list1):
    for mm in list1:
        mm = int(mm)
    return mm

def llist2(list2):
    for k in list2:
        k = float(k)
    return k

def parseHTML(html):
    soup = BeautifulSoup(html, 'html.parser')
    genre = soup.title.string
    movie1 = soup.body.find('div', attrs={'id': 'wrapper'})
    movie2 = soup.body.find('div', attrs={'class': 'article'})
    movie3 = movie2.find('div', attrs={'class': ''})
    movie4 = movie3.find_all('table', attrs={'width':'100%','class': ''})#非常繁复，有没有再简化的方法？
    movie_list = []
    for info in movie4:
        name = info.get_text()
        info1 = info.find('a', attrs={'class': ''})
        name1 = info1.get_text()
        if re.search(r'\d+', name) != None:
            time1 = re.findall(r'\d{4}\-\d{2}', name)  # 正则提取数字
            year1 = re.findall(r'\d{4}', str(time1))
            year = llist(year1)
        elif re.search(r'\d+', name) == None:
            year = None

        info2 = info.find('div', attrs={'class': 'star clearfix'})
        info3 = info2.get_text()
        if re.match(r'\n\n\d', info3) != None:
            peo1 = re.findall(r'\d{2,6}', info3)
            peo = llist(peo1)
        elif re.match(r'\n\d', info3) == None:
            peo = None
        if re.match(r'\n\n\d', info3) != None:
            score1 = re.findall(r'\d\.\d', info3)
            score = llist2(score1)  # 正则提出来带[]和引号，要去掉！
        elif re.match(r'\n\d', info3) == None:
            score = None

        movie_list.append([genre,name1,year,score,peo])

    return movie_list  # 修改

def writeCSV(file_name, data_list):
    with codecs.open(file_name, 'w+') as f:
        writer = csv.writer(f)
        writer.writerow(["genre",'name',"time","score","people"])#write要有标题就这样
        for data in data_list:
            writer.writerow(data)


data_list = []

url = 'https://movie.douban.com/tag/科幻?start=2720&type=T'    #这个url的构造规律性太强了！
html = getHTML(url)
data_list = parseHTML(html) # list拼接
print(data_list)

#出现encode问题，是print出问题。
#有时候请求太久卡到一半肯定是出了问题
#有没有必要封装成类？
#







