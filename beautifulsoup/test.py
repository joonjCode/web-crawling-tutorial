import requests
from bs4 import BeautifulSoup

URL = 'https://kr.indeed.com/jobs?q=python&l=seoul'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
print(soup)

for job_elem in job_elems:
    # Each job_elem is a new BeautifulSoup object.
    # You can use the same methods on it as you did before.
    title_elem = job_elem.find('h2', class_='title')
    company_elem = job_elem.find('div', class_='company')
    location_elem = job_elem.find('div', class_='location')
		# For error checking 
    if None in (title_elem, company_elem, location_elem):
        continue
    print(title_elem)
    print(company_elem)
    print(location_elem)
    print()

python_jobs = results.find_all('h2',
                               string=lambda text: "python" in text.lower())

for p_job in python_jobs:
    link = p_job.find('a')['href']
    print(p_job.text.strip())
    print(f"Apply here: {link}\n")