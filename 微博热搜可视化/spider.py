import requests
import csv
from bs4 import BeautifulSoup as BS
import time
def get_data(url, headers):
    response = requests.get(url = url, headers = headers)
    #print(response.status_code)
    response.encoding = "utf_8_sig"
    soup = BS(response.text, "html.parser")
    #print(soup)
    div_content = soup.find('section', {'class': 'list'})
    #print(div_content)
    t = 1 # 去掉置顶
    list_t = []
    List = []
    #flag = 0
    for item in div_content.find_all("li"):
        if(t == 1):
            t = 0
            continue
        #print(item.find("em").string)#hotness
        #print(item.find("a").get("href"))#url
        #print("***")
        #print(item)
        #if(item.find("i")):
        #    print(item.find("i").get("class")[1])
        #else:
        #    print("None")
        #print(item.find("a").get("href").split("rank=")[1][0])
        #根据关键字打印排名之后的内容，然后只输出第一个字符，即排名
        #print("*****")
        #print(item.span.contents[0])
        #print(type(item.find("span").get_text()))
        #print(item.find("a").get("href").split("rank=")[1].split("&")[0])#.get_text()[1])
        #flag += 1
        #if flag == 15:
        #    break
        #rank = item.find("a").get("href").split("rank=")[1].split("&")[0]
        rank = item.find("strong").string
        subject = item.span.contents[0]
        hotness = item.find("em").string
        if(item.find("i")):
            sign = item.find("i").get("class")[1]
        else:
            sign = 'None'
        current_time = time.strftime("%Y-%m-%d %H:%M")
        print(rank)
        list_t = [subject, rank, hotness, sign, current_time]
        #print(list_t)
        List.append(list_t)
    return List

def store(List):#"D:\code\weibo.csv"
    with open('D:/code/12_23.csv', 'a', encoding = "utf_8_sig", newline = "") as file:
        writer = csv.writer(file)
        for item in List:
            writer.writerow(item)
        file.close()

url = 'https://s.weibo.com/top/summary?cate=realtimehot'
# 请求头
'''headers = {
	'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Mobile Safari/537.36',
	'Host': 's.weibo.com',
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
	'Accept-Encoding': 'gzip, deflate, br',
	# 定期更换Cookie
	'Cookie': 'SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9W5ThXi6g0XiDC_TD8UQ-6oo; SUB=_2AkMUxJoMf8NxqwFRmP8WxG_nZIt0zADEieKimGvXJRMxHRl-yj92qmEEtRB6P0S041uftaI5dG9DOvSuqXGCeHbbhtED; _s_tentry=passport.weibo.com; Apache=2299625611123.144.1670911291558; SINAGLOBAL=2299625611123.144.1670911291558; ULV=1670911291563:1:1:1:2299625611123.144.1670911291558:'}'''
headers = {
	'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0.0; SM-G955U Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36 Edg/108.0.0.0',
	'Host': 's.weibo.com',
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
	'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
	'Accept-Encoding': 'gzip, deflate, br',
	'Cookie': 'SINAGLOBAL=2299625611123.144.1670911291558; SCF=Avg3iCW-ED4m2pzB66A7ImFVKQWSnoFyWTyyTpIV5-myioEvnlRNKvWQUkdMH2HnXW_SV3anYPaPHeKZ7PPv4H4.; _s_tentry=login.sina.com.cn; UOR=,,login.sina.com.cn; Apache=7944884108670.651.1673095191377; ULV=1673095191381:7:1:1:7944884108670.651.1673095191377:1671877799055; SUBP=0033WrSXqPxfM72wWs9jqgMF55529P9D9WWnIk5-4AY84YsqY2zR.rRZ5JpVF02f1KqESozRe0-p; SUB=_2AkMU5f-TdcPxrAZVkPsSyWjgaYVH-jynMJZlAn7uJhMyAxh77gkuqSVutBF-XBoKYLDdOFmpzyCYkJj_BnT_W_O5; login_sid_t=a7f2054c6ffe77a59ca4e2b308eea0d2; cross_origin_proto=SSL'}
List = get_data(url, headers)
store(List)