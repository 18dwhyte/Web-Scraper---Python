
import requests
from bs4 import BeautifulSoup
import pandas as pd

#Web Scraper
def extract(page):
    headers = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'}
    url = f'https://www.indeed.com/jobs?q=Junior%20Software%20Engineer&start={page}&vjk=8ac24243da6a8b03'
    r = requests.get(url, headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup


def transform(soup):
    divs = soup.find_all('div', class_ = 'slider_container')
    for item in divs:
        title = item.find('a').text.strip()
        company = item.find('span', class_ = 'companyName').text
        try:
            salary = item.find('span', class_ = "icl-u-xs-mr--xs").text
        except:
            salary = ''
        summary = item.find('div', {'class' : 'job-snippet'}).text

        job = {
            'title': title,
            'company': company,
            'salary': salary,
            'summary': summary
        }

        joblist.append(job)
    return

joblist = []
for i in range(0,40, 10):
    print(f'Getting page, {i}')
    c = extract(10)
    transform(c)

#creates a csv file with jobs
df = pd.DataFrame(joblist)
print(df.head())
df.to_csv('jobs.csv')