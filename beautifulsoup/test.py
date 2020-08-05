from base import extract_pages, extract_jobs
from save import save_to_csv

last_page = extract_pages()

jobs = extract_jobs(last_page)

save_to_csv(jobs)