import csv
from bs4 import BeautifulSoup

filename_in = 'text_5_var_24'
filename_out = 'res5.csv'
data = []

with open(filename_in, encoding='utf-8') as f_in:
    lines = f_in.readlines()
html = ''
for line in lines:
    html += line

soup = BeautifulSoup(html, 'html.parser')

rows = soup.find_all('tr')

for i in range(1, len(rows)):
    tds = rows[i].find_all('td')
    item = {
        'Company': tds[0].text,
        'Contact': tds[1].text,
        'Country': tds[2].text,
        'Price': tds[3].text,
        'Item': tds[4].text
    }
    data.append(item)

with open(filename_out, 'w', encoding='utf-8', newline='') as f_out:
    writer = csv.writer(f_out)
    for row in data:
        writer.writerow(row.values())


