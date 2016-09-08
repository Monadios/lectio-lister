from bs4 import BeautifulSoup
from time import sleep
import urllib.request
from string import ascii_uppercase

class School:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.students = self.get_students()
        self.student_url = 'http://www.lectio.dk/' + 'lectio/557/SkemaNy.aspx?type=elev&elevid='
    
    def make_url(self, letter):
        return 'http://www.lectio.dk/' + 'lectio/' + self.id + '/FindSkema.aspx?type=elev&forbogstav=' + letter

    def letter_range(self, f,l,al = ascii_uppercase):
        for x in al[al.index(f):al.index(l)+1]:
            yield x
        
    def get_students(self):
        students = []
        letters = self.letter_range('A', 'Z')
        for letter in letters:
            url = self.make_url(letter)
            link = urllib.request.urlopen(url).read()
            soup = BeautifulSoup(link, 'html.parser')

            for x in soup.find_all('ul')[1].find_all('li'):
                student_link = (x.find('a').contents[0], x.find('a').get('href'))
                students.append(student_link)
    
        return students
        

def get_schools(url):
    doc = open(url).read()

    soup = BeautifulSoup(doc, 'html.parser')
    schools = soup.find_all('a')

    schoollist = []

    for school in schools:
        schoolname = school.contents[0].replace('\n','')
        ID = school.get('href').replace("/lectio/", "").replace("/default.aspx", "")
        schoollist.append((schoolname, ID))

    return schoollist
    

schoollist = []

for line in open('skoler.csv').readlines()[0:-1]:
    schoolname = line.split(',')[0]
    schoolID = line.split(',')[1]
    schoollist.append((schoolname, schoolID[:-1]))

def main():
    print("Hello World")
    
if __name__=="__main__":
    main()
