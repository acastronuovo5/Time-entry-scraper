import urllib
from bs4 import BeautifulSoup

page = urllib.urlopen("https://www.bu.edu/hub/hub-courses/philosophical-aesthetic-and-historical-interpretation/")
page1 = urllib.urlopen("http://www.bu.edu/hub/hub-courses/scientific-and-social-inquiry/")
page2 = urllib.urlopen("http://www.bu.edu/hub/hub-courses/quantitative-reasoning/")
page3 = urllib.urlopen("http://www.bu.edu/hub/hub-courses/diversity-civic-engagement-and-global-citizenship/")
page4 = urllib.urlopen("http://www.bu.edu/hub/hub-courses/communication/")
page5 = urllib.urlopen("http://www.bu.edu/hub/hub-courses/intellectual-toolkit/")
soup = BeautifulSoup(page)
soup1 = BeautifulSoup(page1)
soup2 = BeautifulSoup(page2)
soup3 = BeautifulSoup(page3)
soup4 = BeautifulSoup(page4)
soup5 = BeautifulSoup(page5)

#hublist = []

hubs = soup.findAll('h2', {"class", "bu_collapsible"})

#for hubname in hubs:
 #   hublist.append(hubname.string)

#print(k)
#for hub in credit:
 #   k.append(hub)   

#credit = [$0 for tag in soup.html.findAll('h2',{'class':'::before'})]
#print(credit)
k = {}
for hub in hubs:
    key = hub.string
    titles = hub.next_sibling.findAll('h3', {'class': 'cf-course-title'})
    b = []
    for course in titles:
        b.append(course.text)
    k[key] = b
#print([name.encode('ascii') for name in k])

hubs = soup1.findAll('h2',{'class','bu_collapsible'})
for hub in hubs:
    key = hub.string
    titles = hub.next_sibling.findAll('h3', {'class': 'cf-course-title'})
    b = []
    for course in titles:
        b.append(course.text)
    k[key] = b

hubs = soup2.findAll('h2',{'class','bu_collapsible'})
for hub in hubs:
    key = hub.string
    titles = hub.next_sibling.findAll('h3', {'class': 'cf-course-title'})
    b = []
    for course in titles:
        b.append(course.text)
    k[key] = b

hubs = soup3.findAll('h2',{'class','bu_collapsible'})
for hub in hubs:
    key = hub.string
    titles = hub.next_sibling.findAll('h3', {'class': 'cf-course-title'})
    b = []
    for course in titles:
        b.append(course.text)
    k[key] = b

hubs = soup4.findAll('h2',{'class','bu_collapsible'})
for hub in hubs:
    key = hub.string
    titles = hub.next_sibling.findAll('h3', {'class': 'cf-course-title'})
    b = []
    for course in titles:
        b.append(course.text)
    k[key] = b

hubs = soup5.findAll('h2',{'class','bu_collapsible'})
for hub in hubs:
    key = hub.string
    titles = hub.next_sibling.findAll('h3', {'class': 'cf-course-title'})
    b = []
    for course in titles:
        b.append(course.text)
    k[key] = b
print(k)

