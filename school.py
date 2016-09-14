from bs4 import BeautifulSoup
from time import sleep
import urllib.request
from random import randrange
from string import ascii_uppercase

class School:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.students = []
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
            student_set = soup.find_all('ul')[1].find_all('li')
            for s in student_set:
                student_name = s.find('a').contents[0]
                student_link = s.find('a').get('href')
                student = Student(student_name, student_link)
                students.append(student)
    
        self.students = students
        

class Student:
    def __init__(self, name, id):
        self.tokens = self.parse_name(name)
        self.name = self.tokens[0]
        self.class_info = self.tokens[1]
        self.id = id
         
    def parse_name(self, n):
        class_info = n[n.find("(")+1:n.find(")")]
        name = n.split("(")[0]
        return name, class_info

def get_schools(url):
    doc = open(url).read()

    soup = BeautifulSoup(doc, 'html.parser')
    schools = soup.find_all('a')

    schoollist = []

    for school in schools:
        schoolname = school.contents[0].replace('\n','')
        ID = school.get('href').replace("/lectio/", "").replace("/default.aspx", "")
        schoollist.append((schoolname, ID))
        print("Downloaded " + schoolname + "\n")
        sleep(randrange(5,15))

    return schoollist


def main():
    print("Hello World")
    
if __name__=="__main__":
    main()
