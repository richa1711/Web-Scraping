from bs4 import BeautifulSoup
import requests
from lxml import html
import codecs
import pandas as pd

#page=requests.get('https://summerofcode.withgoogle.com/projects/?sp-page=65#!')
#soup=BeautifulSoup(page,'lxml')
#print(soup)

with codecs.open('source2.html', 'r', encoding='utf-8', errors='ignore') as fdata:
    soup=BeautifulSoup(fdata,'lxml')

#print(soup)
#taking out body out of whole code
#x=body.find('li',class_='project-card')          
#y=x.find('div',class_='project-card__right-header-content')

n=int(input("Enter the number of lectures you want to scrap\n"))

week_list=[]
lecture_list=[]
links_list=[]
all_weeks=[]
body=soup.find('body')
f=0
for each_week in body.find_all('div',class_='weekDetailsBox'):
    k=0
    for i in each_week.find_all('div',class_='lectureInfoBoxText'):
      k+=1
       
    for x in range(k):
        all_weeks.append('Week '+str(f))
    f+=1

i=0
for lecture in body.find_all_next('div',class_='lectureInfoBoxText'):
    if(i<n):
        lecture_list.append(lecture.text.replace('\r\n','').strip())
        i+=1

print(lecture_list)




k=0
for link in body.find_all('div',class_="lectureItem completeRowLectureColorWatched"):
    if(k<n):
        y="https://hello.iitk.ac.in/mth102aa/"+link.a['href']
        links_list.append(y)
        k+=1


actual_week_list=[]
for i in range(n):
    week_list.append(all_weeks[i])
    
#print(week_list)
#print(links_list)
#print(lecture_list)

data = {'Week': week_list, 'Lecture_name': lecture_list, 'Lecture_links': links_list}  
       
df = pd.DataFrame(data) 
    
# saving the dataframe 
df.to_csv('mookit.csv')
