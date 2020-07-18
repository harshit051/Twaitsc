#pip install requests
#pip install bs4
#pip install lxml
import requests
import bs4

country_name=input('Enter Country Name')
def Covid19_data(country):
  res=requests.get('https://www.worldometers.info/coronavirus/#countries')
  s=bs4.BeautifulSoup(res.text,'lxml')
  index=-1
  data=s.select('tr td')

  for i in range(len(data)):
    if data[i].text==country:
      index=i
      break
  
  for i in range(8):
    if i==0:
      print("Country Name: "+str(data[i+index].text))
    elif i==1:
      print("Total Case: "+str(data[i+index].text))
    elif i==2:
      print("New Case: "+str(data[i+index].text))
    elif i==3:
      print("Total Deaths: "+str(data[i+index].text))
    elif i==4:
      print("New Deaths: "+str(data[i+index].text))
    elif i==5:
      print("Total Recovered: "+str(data[i+index].text))
    elif i==6:
      print("Active Cases: "+str(data[i+index].text))
    elif i==7:
      print("Serious, Critical: "+str(data[i+index].text))



Covid19_data(country_name)
