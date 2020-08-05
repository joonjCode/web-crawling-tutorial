import requests
from bs4 import BeautifulSoup

URL = 'https://kr.indeed.com/jobs?q=python&l=seoul'

def extract_pages():
    page = requests.get(URL)

    # Check for requsts 
    # Expecting 200
    # print(page)

    soup = BeautifulSoup(page.content, 'html.parser')
    pag = soup.find('div', {'class':'pagination'})
    links = pag.find_all('a')
    # print(pages)

    pages = []
    for link in links[:-1]:
        # pages.append(link.find('span').string)
        pages.append(int(link.string))
    # Get the last page
    max_page = pages[-1]

    return max_page


def extract_job(result):
    title = result.find('h2', {'class':'title'}).text.strip()
    # print(title)
    company = result.find('span', {'class':'company'})
    if company.find('a') is not None:
        company = str(company.find('a').string).strip()
    else:
        company = str(company.string).strip()

    location = result.find('span',{'class':'location'})
    if location is None:
        location = result.find('div',{'class':'location'}).string
    else:
        location = location.string

    job_id = result['data-jk']

    return {'title':title, 'company':company, 'location':location, 'link':f'https://www.indeed.com/viewjob?jk={job_id}'}

def extract_jobs(max_page):
    jobs = []
    for page in range(max_page):
        result = requests.get(f'{URL}&start={page*10}')   
        soup = BeautifulSoup(result.text, 'html.parser')
        results = soup.find_all('div', {'class':'jobsearch-SerpJobCard'})

        for result in results:
            job = extract_job(result)
            jobs.append(job)

    return jobs