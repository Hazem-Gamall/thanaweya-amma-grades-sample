import requests
from bs4 import BeautifulSoup

url = 'https://natiga.dostor.org/Home/Result'

for i in range(14100,89900): #collect seating numbers in this range
    data = {'seating_no':i}
    x = requests.post(url, data = data)
    print(x.reason)

    if(x.status_code != 200):
        continue
    soup = BeautifulSoup(x.text, 'html.parser')

    with open('natega.txt','a') as f:
        for p in soup.find_all('li',{"class":"nav-item"}):
            f.write(p.get_text())
        f.write('\n\n')

