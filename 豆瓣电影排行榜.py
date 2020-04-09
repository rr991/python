from requests_html import HTMLSession
session=HTMLSession()
url='https://movie.douban.com/top250'
r = session.get(url)
film_ranks = r.html.find('ol.grid_view>li')
# print(film_ranks)
# int(type(film_ranks))
# print(r.html.html)
for f in film_ranks:
    f_title = f.xpath('.//div[@class="hd"]/a/span[@class="title"]/text()')[0]
    print(f_title)
    f_actor = f.xpath('.//div[@class="bd"]/p/text()')[0].strip()
    print(f_actor)
    f_score = f.xpath('.//div[@class="star"]/span[@class="rating_num"]/text()')[0].strip()
    print(f_score)
    print('\n')
