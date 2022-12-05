import requests
from bs4 import BeautifulSoup
import csv


#-------------------------------------------------------
'''simple html phaser, using beautifulsoup find elements'''

# with open('simple.html') as html_file:
#     soup = BeautifulSoup(html_file, 'lxml')  #file, phaser
    
# print(soup.prettify())

'''find value'''
# match = soup.title.text
# match = soup.find('div', class_='footer')
# print(match) 
# article = soup.find('div', class_='article')
# print(article)
# headline = article.h2.a.text
# print(headline)
# summary = article.p.text
# print(summary)

# for article in soup.find_all('div', class_='article'):
#     headline = article.h2.a.text
#     print(headline)
#     summary = article.p.text
#     print(summary)

#------------------------------------------------------------
'''real website screping'''

source = requests.get('http://coreyms.com').text
soup = BeautifulSoup(source, 'lxml')
# print(soup.prettify())
csv_file = open('cms_scrape.csv', 'w', encoding='utf-8')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline', 'summary', 'vidio_link'])

for article in soup.find_all('article'):
    #print(article.prettify())
    headline = article.h2.a.text
    print(headline)
    summary = article.find('div', class_='entry-content').p.text
    print(summary)
    try:
        vid_scr = article.find('iframe', class_='youtube-player')['src']
        # print(vid_scr)
        vid_id = vid_scr.split('/')[4]
        vid_id = vid_id.split('?')[0]
        #print(vid_id)
        yt_link = f'https://youtube.com/watch?v={vid_id}'
    except Exception as e:
        yt_link = None
    print(yt_link)
    print()
    csv_writer.writerow([headline, summary, yt_link])

csv_file.close()