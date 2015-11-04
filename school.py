from bs4 import BeautifulSoup
import urllib.request
import json

def get_schools(url):
    doc = open(url).read()
    soup = BeautifulSoup(doc, 'html.parser')
    schools = soup.find_all('a')

    schoollist = []

    for school in schools:
        schoolname = school.contents[0].replace('\n','')
        ID = school.get(
            'href').replace("/lectio/", "").replace("/default.aspx", "")
        schoollist.append((schoolname, ID))

    return schoollist
    

baseurl = 'http://www.lectio.dk/'
studenturl = 'http://www.lectio.dk/lectio/557/SkemaNy.aspx?type=elev&elevid='
schools = get_schools('skole.html')


##########################################################
# def make_school_tuple():                               #
#     for school in schools:                             #
#         schooltuple.append(                            #
#             (''.join(school.contents[0].splitlines()), #
#              school.get('href')))                      #
##########################################################


def parse_studentID(info):
    sid = info.replace('/lectio/557/SkemaNy.aspx?type=elev&elevid=', "")
    return sid

def get_student(school_id, letter):
    url = '%slectio/%/FindSkema.aspx?type=elev&forbogstav=%s' % baseurl,
    school_id, letter
    link = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(link, 'html.parser')
    students = []

    for x in soup.find_all('ul')[1].find_all('li'):
        students.append((x.find('a').contents[0],
    parse_studentID(x.find('a').get('href'))))

    return students
    
def dump_schools(file_name):
    with open(file_name,'a') as f:
        for school in get_schools('skole.html'):
            f.write(school[0] + ',' + school[1] + '\n')

if __name__ == '__main__':
    charset = [list(range(ord('a'), ord('z'))), 230, 229, 248]
#    doc = urllib.request.urlopen(
 #       'https://www.lectio.dk/lectio/557/FindSkema.aspx?type=elev').read()
  #  soup = BeautifulSoup(doc, 'html.parser')
