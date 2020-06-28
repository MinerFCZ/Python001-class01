# 作业一：
#
# 安装并使用 requests、bs4 库，爬取猫眼电影（）的前 10 个电影名称、电影类型和上映时间，
# 并以 UTF-8 字符集保存到 csv 格式的文件中

import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

url = 'https://m.maoyan.com/#movie/classic'

user_agent = 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Mobile Safari/537.36'

cookie = 'lxsdk_cuid=172f8655508c8-0b7c2e34487bb5-31617402-1aeaa0-172f8655509c8; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1593305290,1593306295; __mta=209484077.1593305290267.1593306456952.1593306708379.10; uuid_n_v=v1; iuuid=6A770690B8DD11EA9BBABBBB31B3B9ACB0CD4F6FB91249B48EB407DD5F7AB956; webp=true; ci=30%2C%E6%B7%B1%E5%9C%B3; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22172f88207ab75b-03b63323e0c112-73236134-349920-172f88207ac7a9%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%22172f88207ab75b-03b63323e0c112-73236134-349920-172f88207ac7a9%22%7D; _last_page=c_dmLad; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1593307171; _lxsdk=6A770690B8DD11EA9BBABBBB31B3B9ACB0CD4F6FB91249B48EB407DD5F7AB956; __mta=209484077.1593305290267.1593306708379.1593307172384.11; _lxsdk_s=172f8655509-342-4cc-3f5%7C%7C31'

headers = {'user-agent': user_agent, 'cookie': cookie}

response = requests.get(url, headers=headers)

bs_info = bs(response.text, 'html.parser')

movies = []

count = 0

for div_tags in bs_info.find_all('div', attrs={'class': 'classic-movies-list'}):
    for a_tag in div_tags.find_all('a'):
        movie_info = {}
        movie_info['href'] = 'https://m.maoyan.com' + a_tag.get('href')
        movie_info['title'] = a_tag.find('div', attrs={'class': 'title'}).text
        movie_info['actors'] = a_tag.find('div', attrs={'class': 'actors'}).text
        movie_info['show_time'] = a_tag.find('div', attrs={'class': 'show-info'}).text[0:10]
        movies.append(movie_info)
        count += 1
        if count >= 10:
            break

movies_df = pd.DataFrame(data=movies)

movies_df.to_csv('./week01_01.csv', encoding='utf8', index=False, header=False)

