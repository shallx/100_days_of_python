from bs4 import BeautifulSoup

with open("website.html", encoding="utf8") as file:
    contents = file.read()

soup = BeautifulSoup(contents, 'html.parser')


soup.prettify() # have to be printed

html_title = soup.title
title_tag_name = soup.title.name
title_content = soup.title.string
first_a_tag = soup.a
all_anchor_tags = soup.find_all(name="a")

for tag in all_anchor_tags:
    anchor_tag_content = tag.getText() 
    anchor_tag_href = tag.get("href") 
    
heading_by_id = soup.find(name="h1", id="name")
single_heading_by_class = soup.find(name="h3", class_="heading")
class_of_an_element = single_heading_by_class.get("class")
finding_by_nested_selector = soup.select_one(selector="p a")
query_selector_single = soup.select_one("#name")
query_selector_multiple = soup.select_one(".heading")