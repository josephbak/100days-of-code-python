from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")

# print(response.text)
yc_web_page = response.text
soup = BeautifulSoup(yc_web_page, "html.parser")
# # print(soup.title)
# # for link in soup.find_all("a", "titlelink"):
# #     print(link.get_text())
#
# print(soup.find(name="a", class_="titlelink").getText())

# article_tag = soup.find(name="a", class_="titlelink")
# print(article_tag)
# article_text = article_tag.getText()
# print(article_text)
# article_link = article_tag.get("href")
# print(article_link)
# article_upvote = soup.find(name="span", class_="score").getText()
# print(article_upvote)

articles = soup.find_all(name="a", class_="titlelink")
article_texts = []
article_links = []
for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

# print(article_texts)
# print(article_links)
print(article_upvotes)

largest_number = max(article_upvotes)
largest_index = article_upvotes.index(largest_number)
print(largest_index)
print(article_texts[largest_index])
print(article_links[largest_index])






















#
#
# with open("website.html") as file:
#     contents = file.read()
#
#
# soup = BeautifulSoup(contents, "html.parser")
# # print(soup.title)
# # print(soup.title.string)
# # print(soup.prettify())
# # print(type(soup.li))
#
#
# all_anchor_tags = soup.find_all(name="a")
# # print(all_anchor_tags)
#
# # for tag in all_anchor_tags:
# #     print(tag.getText())
# #     print(tag.get("href"))
#
#
#
# heading = soup.find(name="h1", id="name")
# print(heading)
#
#
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.get("class"))
#
# h3_heading = soup.find_all("h3", class_ = "heading")
# print(h3_heading)
#
# name = soup.select_one(selector="#name")
# print(name)
#
# headings = soup.select(".heading")
# print(headings)