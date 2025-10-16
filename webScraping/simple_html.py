from bs4 import BeautifulSoup
SIMPLE_HTML = '''
<html>
    <head></head>
    <body>
    <h1>This is a titles</h1>
    <p class="subtitle"> Lorem ipsum ... </p>
    <p> Here's another p without a class </p>
    <ui>
    <li>Rolf</li>
    <li>Charlies</li>
    <li>Jen</li>
    <li>Jose</li>
    </ui>
    </body>
<html>
'''

simple_soup = BeautifulSoup(SIMPLE_HTML,'html.parser')

def find_title():
    h1 = simple_soup.find('h1')
    return h1.string
print(find_title())

def find_list_items():
    list_items = simple_soup.find_all('li')
    for item in list_items:
        print(item.string)
find_list_items()

def find_subtitle():
    paragraph = simple_soup.find('p',{'class':'subtitle'})
    print(paragraph.string)
find_subtitle()

def find_other_paragraph():
    paragraph = simple_soup.find_all('p')
    print(paragraph)
    other_paragraph = [p for p in paragraph if 'subtitle' not in p.attrs.get('class',[])]
    print(other_paragraph)

find_other_paragraph()