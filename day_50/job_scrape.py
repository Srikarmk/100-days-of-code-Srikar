from bs4 import BeautifulSoup
import requests
import time 

def findJob():
    url_text=requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python&txtLocation=').text

    soup=BeautifulSoup(url_text,'lxml')
    jobs=soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

    for index, job in enumerate(jobs):
        posted=job.find('span',class_='sim-posted').span.text
        if 'few' in posted:
            company=job.find('h3',class_='joblist-comp-name').text
            company="".join(company.split())
            skills=job.find('span',class_='srp-skills').text

            position=job.find('strong',class_='blkclor').text
            skills="".join(skills.split())
            
            with open(f'jobs/{index}.txt','w') as file:
                details=file.write(f'''Company: {company}
                Position: {position}
                Skills Required: {skills}
                Posted : {posted}
                ''')
                print(f"File {index} Saved !")


if __name__=="__main__":
    findJob()
    timeWait=10
    print(f"Waiting for {timeWait} minutes")
    time.sleep(timeWait*60)