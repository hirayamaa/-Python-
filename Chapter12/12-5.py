import requests
import bs4

res = requests.get('https://nostarch.com')
res.raise_for_status()
no_starch_soup = bs4.BeautifulSoup(res.text, 'html.parser')
print(type(no_starch_soup))

example_file = open('example.html')
example_soup = bs4.BeautifulSoup(example_file, 'html.parser')
elems = example_soup.select('#author')
print(type(elems))
print(len(elems))
print(elems[0].getText())
print(elems[0])

p_elems = example_soup.select('p')
for p in p_elems:
    print(str(p) + '\n')
    print(p.getText)

