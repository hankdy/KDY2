from  bs4 import BeautifulSoup
import requests

url = "http://127.0.0.1:5500/hello.html"
response = requests.get(url)

html = response.text
# print(html)

soup = BeautifulSoup(html, 'html.parser')

h1 = soup.find('h1')  # 가장 먼저 찾은 HTML 태그 <h1>
print(h1.text)

all_p = soup.find_all('p') # 모든 HTML 태그 <p>
for p in all_p:
    print(p.text)

