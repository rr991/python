from requests_html import HTMLSession
session = HTMLSession()

# r = session.get('https://python.org/')
# about = r.html.find('#about', first=True)

# r = session.get('https://www.cnblogs.com/')
# about = r.html.find('#nav_menu>a')
# # about = r.html.find('#nav_menu>a', first=True)
#
# # print(about.attrs['id'])
# # print(type(about.attrs['id']))
# for aa in about:
#     print(aa.text)
#     print(aa.absolute_links)
#     print('\n')

r = session.get('https://www.cnblogs.com/')
about = r.html.find('.post_item_body')
# print(about)
# print(type(news))
for aa in about:
    print(aa.text)
    print(aa.absolute_links)
    print('\n')

