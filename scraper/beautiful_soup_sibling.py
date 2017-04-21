from bs4 import BeautifulSoup
sibling_soup = BeautifulSoup("<a><b>text1</b><c>text2</c></b></a>","html5lib")
# <html>
#  <body>
#   <a>
#    <b>
#     text1
#    </b>
#    <c>
#     text2
#    </c>
#   </a>
#  </body>
# </html>
print(sibling_soup.c.previous_sibling)

#=============================================================================================

html_doc = """
<html><head><title>The Dormouse's story</title></head>

<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
soup = BeautifulSoup(html_doc,"html5lib")
#print(sibling_soup.a.next_siblings)
for nextsiblings in soup.a.next_siblings:
    print(nextsiblings)
    
"""
children
descendants
parents
next_siblings
previous_siblings
都要用for 才能把每個 sideways 都走一遍
"""