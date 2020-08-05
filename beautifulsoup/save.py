import csv

'''
Try to use 
with open('jobs.csv', 'w') as f:
    fields = ['title','company','location','link']
    w = csv.DictWriter(f,fieldnames = fields)

    w.wirteheader()
    w.writerow()        
'''
def save_to_csv(jobs):
    file = open('indeed_python_jobs.csv', mode = 'w', encoding='utf8')
    writer = csv.writer(file)
    writer.writerow(['title', 'company',  'location','link'])
    for job in jobs:
        writer.writerow(list(job.values()))

    return 