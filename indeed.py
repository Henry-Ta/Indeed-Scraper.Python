import requests
from bs4 import BeautifulSoup
import pandas as pd

#----------------------------Scap whole page
URL="https://ca.indeed.com/jobs?q=internship&l=Vancouver,+BC&jt=internship&fromage=3"
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

# print(page.status_code)

# print(soup.prettify())

# print(list(soup.children))

# for item in (list(soup.children)):
    # print(item)
    # print(type(item))

#-----------Option 1-------------------Extract <head>, <body>
# html = list(soup.children)[2]    

# print(list(html.children))
# print(html.prettify())

# head = list(html.children)[1]
# body = list(html.children)[3]

# print(head.prettify())
# print(body.prettify())

#------------<head>

#------------<body>
# print(list(body.children))

#*** p = list(body.children)[1] 
#*** p.get_text()

# print(type(p))
# print(type(p.get_text()))

#-----------Option 2-----------------Find all
data = soup.find_all("div",{"data-tn-component":"organicJob"})

title = soup.find_all("h2",{"class":"title"})
company = soup.find_all("span",{"class":"company"})
location = soup.find_all("span",{"class":"location accessible-contrast-color-location"})
difficulty = soup.find_all("span",{"class":"iaLabel iaIconActive"})
date = soup.find_all("span",{"class":"date"})
salary = soup.find_all("span",{"class":"salaryText"})

# p = soup.find('p')    # Return the first instance
# p = soup.find_all('p')
# p_class= soup.find_all('p',class_='outer-text')
# p_id = soup.find_all('p',id="first")

# print(type(data))
print(list(data))
print(len(data))
# print(salary[0].get_text())
# print(p_class)
# print(p_id)

#----------------------------------Search by CSS selectors
#*** p = soup.select("div p")

# print(p)

#------------Example---------------Weather Data
# seven_day = soup.find(id="seven-day-forecast")
# forecast_items = seven_day.find_all(class_="tombstone-container")
# tonight = forecast_items[0]

# print(seven_day.prettify())
# print(list(forecast_items))
# print(tonight.prettify())

# period = tonight.find(class_="period-name").get_text()
# short_desc = tonight.find(class_="short-desc").get_text()
# temp = tonight.find(class_="temp").get_text()

# print(period)
# print(short_desc)
# print(temp)

# img = tonight.find("img")
# img_desc = img['title']

# print(img)
# print(img_desc)

# period_tags = seven_day.select(".tombstone-container .period-name")
# periods = [pt.get_text() for pt in period_tags]

# print(period_tags)
# print(periods)

# short_descs = [sd.get_text() for sd in seven_day.select(".tombstone-container .short-desc")]
# temps = [t.get_text() for t in seven_day.select(".tombstone-container .temp")]
# descs = [d["title"] for d in seven_day.select(".tombstone-container img")]

# print(short_descs)
# print(temps)
# print(descs)

#--------------------------- Pandas Dataframe
# weather = pd.DataFrame({
    # "period": periods,
    # "short_desc": short_descs,
    # "temp": temps,
    # "desc": descs
# })

# print(weather)

#-------------------------- Extract Detail


#---------------------------Indeed
#----------Tree
#<body>
#<table id="resultsBody" class="centered"
#<tbody id="resultsBodyContent"
#<table id="pageContent" class="serpContainerMinHeight"
#<div class:"jobsearch-serpjobcard unifiedrow row result clickcard"
