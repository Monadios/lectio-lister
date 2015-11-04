from bs4 import BeautifulSoup
import urllib.request
import json

def get_schools(url):
    doc = open(url).read()
    soup = BeautifulSoup(doc, 'html.parser')
    schools = soup.find_all('a')
    return schools


schooltuple = []
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

def get_student(letter):
    baseurl = 'https://www.lectio.dk/lectio/557/FindSkema.aspx?type=elev&forbogstav='
    link = urllib.request.urlopen(baseurl + letter).read()
    soup = BeautifulSoup(link, 'html.parser')
    students = []
    for x in soup.find_all('ul')[1].find_all('li'):
        students.append((x.find('a').contents[0],
    parse_studentID(x.find('a').get('href'))))

    return students
    
if __name__ == '__main__':
    charset = [list(range(ord('a'), ord('z'))), 230, 229, 248]
    doc = urllib.request.urlopen(
        'https://www.lectio.dk/lectio/557/FindSkema.aspx?type=elev').read()
    soup = BeautifulSoup(doc, 'html.parser')
    
