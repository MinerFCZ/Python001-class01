import requests
import pymysql
from bs4 import BeautifulSoup as bs


def get_movie_comment():

    header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
        'Host': 'movie.douban.com',
        'Referer': 'https://movie.douban.com/subject/26871906/?tag=%E7%83%AD%E9%97%A8&from=gaia',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Cookie': '"118282"; bid=PNGCklCdEOo; __utma=30149280.1687312380.1596361133.1596361133.1596361133.1; __utmc=30149280; __utmz=30149280.1596361133.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utma=223695111.1368341988.1596361134.1596361134.1596361134.1; __utmc=223695111; __utmz=223695111.1596361134.1.1.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1596361134%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; ap_v=0,6.0; __yadk_uid=GErX62cNiAHCGXQ23XCFNIHpBh3nGOkU; _vwo_uuid_v2=DAF907ACE9752525DB83D943FE9ADD37E|55da037bb12350c298270f9a5de318d8; __gads=ID=38678e1df400416a-221ff39fc3c2007e:T=1596361147:RT=1596361147:S=ALNI_MZcfV8IgfbLC5iJT2jCGl9R166bVg; _pk_id.100001.4cf6=731ecb754b7d9980.1596361134.1.1596361202.1596361134.'
    }

    response = requests.get('https://movie.douban.com/subject/26871906/reviews', headers=header)

    bs_info = bs(response.text, 'html.parser')

    comments = []

    for review in bs_info.find_all('div', attrs={'class': 'main review-item'}):
        comment = {}
        user_name = review.find('a', attrs={'class': 'name'}).text
        rating = None
        if review.find('span', attrs={'class': 'main-title-rating'}) is not None:
            span = review.find('span', attrs={'class': 'main-title-rating'})
            start = span.attrs['class'][0]
            rating = int(int(start.replace('allstar', '')) / 10)
        comment_time = review.find('span', attrs={'class': 'main-meta'}).text
        short_content = review.find('div', attrs={'class': 'short-content'}).text
        comment['movie_id'] = '26871906'
        comment['user_name'] = user_name
        comment['rating'] = rating
        comment['comment_time'] = comment_time
        comment['short_content'] = short_content
        comments.append(comment)

    return comments


def save_to_mysql(comments):
    conn = pymysql.connect(host='localhost',
                           port=3306,
                           user='root',
                           password='root',
                           database='geek_bang_train',
                           charset='utf8mb4'
                           )
    items = [
        (comment['movie_id'], comment['user_name'], comment['rating'], comment['comment_time'], comment['short_content']) for comment in
        comments
    ]

    try:
        with conn.cursor() as cursor:
            sql = "INSERT INTO douban_movie_comment (movie_id, user_name, rating,comment_time,short_content) VALUES (%s, %s, %s, %s, %s)"
            cursor.executemany(sql, items)
        conn.commit()
    finally:
        conn.close()


if __name__ == '__main__':
    comments = get_movie_comment()
    # print(comments)
    save_to_mysql(comments)
