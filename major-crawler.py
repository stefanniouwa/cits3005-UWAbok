import requests
import lxml
import re
import json
from bs4 import BeautifulSoup

#set url and headers
url = "https://handbooks.uwa.edu.au/majordetails?code="
headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
}

#unit codes is a textfile containing the 8 character unit codes, 1 to a line.
#test only with small lists of units (e.g. CITS units)
codes=open('major-codes.txt','r')

#the major currently being crawled
code = codes.readline().strip()

#the dictionary of majors.
majors = {}

while code:
  page = requests.get(url+code, headers = headers)

  soup = BeautifulSoup(page.content, 'lxml')
  #put all data into majors dictionary

  data = json.loads('{'+''.join(re.findall(r'(".*)',str(list(soup.find_all('script'))[4])))+'}')

  major = {}
  major['code'] = data['fsCode']
  major['title'] = data['fsCourseTitle']
  major['school'] = data['fsSchool']
  major['board_of_examiners'] = data['fsBoe']
  major['delivery_mode'] = data['fsDelivery']

  #Assume the relevant fields are contained in dictionary lists
  #(which is mostly true).
  overview = soup.find('dl')

  for key, value in list(zip(overview.find_all("dt"),overview.find_all("dd"))):
    key = key.get_text().strip()
    #Description is a text file (html characters are stripped out)
    if key == 'Description':
      major[key.lower()] = value.get_text()
    #credit is a number (remove "points")  
    elif key == 'Outcomes':
      outcomes = value.get_text().strip()
      major[key.lower()] = re.findall(r'\d\)([^\(;]*)', outcomes)
    elif key == 'Prerequisites':
      major[key.lower()] = value.get_text().strip()[0:-7]
    #correct? doesn't seem to be widely used?  
    elif key == 'Courses':
      major[key.lower()] = list(map(lambda x: x.get_text().strip()[0:5], value.find_all("strong")))

  major['bridging'] = []
  major['units'] = []

  #need <h5 bridging -> /table/div as a string then units = beautifulsoup(text, 'lxml')
  bridge_source = re.findall(r'class="bridging">.*?(<table.*?</table>)',str(page.content))
  for bridge_set in bridge_source:
    bridging_units = BeautifulSoup(bridge_set, 'lxml')
    cells = list(bridging_units.select('tr td'))
    count = 1
    while count < len(cells):
      major['bridging'].append(cells[count].find('a').get_text().strip())
      count+=4

#No good way to extract electives here
  core_source = re.findall(r'class="dsm">.*?(<table.*?</table>)',str(page.content))
  for core_set in core_source:
    core_units = BeautifulSoup(core_set, 'lxml')
    cells = list(core_units.select('tr td'))
    count = 1
    while count < len(cells):
      major['units'].append(cells[count].find('a').get_text().strip())
      count+=4

  majors[code] = major
  code = codes.readline().strip()

codes.close()
out = open('majors.json', 'w')
#write to file with indent set to 2.
json.dump(majors,out,indent=2)