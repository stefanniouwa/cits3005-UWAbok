import requests
import lxml
import re
import json
from bs4 import BeautifulSoup

#set url and headers
url = "https://handbooks.uwa.edu.au/unitdetails?code="
headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
}

#unit codes is a textfile containing the 8 character unit codes, 1 to a line.
#test only with small lists of units (e.g. CITS units)
codes=open('unit-codes.txt','r')

#the unit currently being crawled
code = codes.readline().strip()

#the dictionary of units.
units = {}

while code:
  print(code)
  page = requests.get(url+code, headers = headers)

  soup = BeautifulSoup(page.content, 'lxml')
  #put all data into units dictionary

  data = json.loads('{'+''.join(re.findall(r'(".*)',str(list(soup.find_all('script'))[4])))+'}')

  unit = {}
  unit['code'] = data['fsCode']
  unit['title'] = data['fsCourseTitle']
  unit['school'] = data['fsSchool']
  unit['board_of_examiners'] = data['fsBoe']
  unit['delivery_mode'] = data['fsDelivery']
  unit['level'] = code[4]

  #Assume the relevant fields are contained in dictionary lists
  #(which is mostly true).
  for key, value in list(zip(soup.find_all("dt"),soup.find_all("dd"))):
    key = key.get_text().strip().lower()
    #Description is a text file (html characters are stripped out)
    if key == 'description':
      unit[key] = value.get_text()
    #credit is a number (remove "points")  
    elif key == 'credit':
      unit[key.lower()] = value.get_text().strip()[0:-7]
    #correct? doesn't seem to be widely used?  
    elif key == 'offering':
      offer = {}
      for row in value.find_all('tbody tr'):
        for h, d in list(zip(value.find_all('thead th'), row.find_all('td'))):
          offer[h.get_text().strip()] = d.get_text().strip()
      unit[key] = offer
    #Find Majors in which the course appears (note, only name, not code is given.  
    elif key == 'details for undergraduate courses':
      majors = value.find('li').get_text().strip()
      unit['majors'] = re.findall(r'([A-Z][^;]*)',majors[5:-16])
    #Extract list of outcomes using a regexp  
    elif key == 'outcomes':
      outcomes = value.get_text().strip()
      unit[key] = re.findall(r'\d\)([^\(;]*)', outcomes)
    #Extract description of assessment items  
    elif key == 'assessment':  
      assessments = value.get_text().strip()
      unit[key] = re.findall(r'\d\)([^\(;.]*)', assessments)
    #find Unit Coordinator name  
    elif key == 'unit coordinator':
      unit['coordinator'] = value.get_text().strip()
    #find Notes  
    elif key == 'note':
      unit[key] = value.get_text().strip()
    #find description of contact hours with class type and time per week (working?)  
    elif key == 'contact hours':
      classes = {}
      for d,h in list(zip(value.find_all('i'), re.findall(r'(\d)',value.get_text()))):
        classes[d.get_text()] = h
      unit['contact'] = classes 
    #find prerequisites. Format is vague, should probably convert to CNF.  
    elif key == 'unit rules':#deeply unsatisfactory. Should aim to capture the Boolean rules here. Will accept as disjunct. Also, advisable prior study...!!!
      for k, v in list(zip(value.find_all('dt'), value.find_all('dd'))):
        k = k.get_text().strip().lower()
        if k == 'incompatibilities':
          unit[k] = list(map(lambda x: x.get_text().strip(), v.find_all('a')))
        elif k == 'advisable prior study':  
          unit['advisable_prior_study'] = list(map(lambda x: x.get_text().strip(), v.find_all('a')))
        elif k == 'prerequisites':
          unit[k+'_text'] = v.get_text()
          conjunct = str(v).split('<em>and</em>')
          unit[k+'_cnf'] = []
          for c in conjunct:
            disjunct = c.split('<em>or</em>')
            dis = []
            for d in disjunct:
              us = re.findall(r'(\w{4}\d{4})',d)
              if us:
                dis.append(us[0])
            if dis:
              unit[k+'_cnf'].append(dis)

    #textbooks    
    elif key == 'Texts':
      unit['texts'] = list(map(lambda x: x.get_text().strip(), value.find_all('p')))
  units[code] = unit
  code = codes.readline().strip()

codes.close()
out = open('units.json', 'w')
#write to file with indent set to 2.
json.dump(units,out,indent=2)