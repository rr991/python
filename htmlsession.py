# 1. 建立Session:

from requests_html import HTMLSession
session = HTMLSession()
 

# 2. 打开Url检查返回码

mainPage = session.get("https://blog.csdn.net/chunyexiyu/")
if (mainPage.status_code == 404):
        print("url open failed: {}".format(mainPage.url))
        sys.exit()     

 

# 3. 查找内容并检查返回内容

articleElement = mainPage.html.find("#mainBox > main > div.article-list", first=True)
if (articleElement == None):
        print("article empty");

 

# 4. 获取Element内容中的信息(文本/链接)

print(articleElement.text)
for url in articleElement.links:
 

# 5. 保保存网页内容bin

      file = open("output.text", "w", encoding="utf-8")
      file.write(articleElement.text)
      # file.close()

 

# 6. 保存网页内容bin

      file = open("output.html", "wb")
      file.write(mainPage.html.raw_html)
      file.close()

