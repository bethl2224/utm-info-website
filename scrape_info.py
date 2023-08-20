from bs4 import BeautifulSoup
import info # import info.py to extract data from database
import requests # get request
import pandas
import extract_course
'''
purpose for the python file is to scrape info and insert into the database

'''



#TODO generate list of link_for_more and icon
#for each class!!!
#using csv file



# reference
course_link = "https://utm.calendar.utoronto.ca/course/"

#TODO 
# we can use pandas and numpy to dynamically scrape data into csv file
# need to generate a csv file with course name corresponding with link, icon_class
#use probably pandas or csv file

course_name = ["csc108h5,csc148h5,mat102h5, csc207h5, mat135h5, mat136h5, csc236h5"]





def find_title(soup) -> str:
    #scrape title
    title = soup.find('h1', {'class': 'page-title'})
    

    return str(title.contents) # get the content string

def find_description(soup) -> str:
    # scrape course description
    '''find course description'''
    content = soup.find('section', {'class': 'w3-block w3-block-wrapper block-system block-system-main-block'})

    #find the description
    description = content.find('div', {'class':'w3-bar-item field__item'})
    return description.text


def find_prerequisite(soup) -> str:
    # scrape prerequisite
    content = soup.find('div', {'class':'w3-row field field--name-field-prerequisite field--type-text-long field--label-inline clearfix'})
    if content: # might not be prerequisite
       prerequsite = content.find('div', {'class': 'w3-bar-item field__item'})
    else:
        return ""
    return prerequsite.text[:-1]
 

#link_for_more = "https://www.cs.toronto.edu/~quellan/courses/csc108/lectures.shtml"

# successful 



def insert_course_info(course_na, link_for_more, icon) -> None:
    # scrape course_info and insert into database


    response = requests.get(course_link + course_na)
    #print(response.text)
    soup = BeautifulSoup(response.text, 'html.parser')
    #print(soup)
    course_na = find_title(soup)

    course_description = find_description(soup)
    pre_requisite = find_prerequisite(soup)
            
    # save scrape info into the database
    info.insert_record(course_na, course_description, pre_requisite, link_for_more, icon)
    # use panda to find the icon we want to insert

    
# test july 29 - successfull!!
#info.clear_table() -> reset table if necessary
#insert_course_info()

#where we insert all data
def insert_all_info() -> None:
    all_course_data = extract_course.return_info()


    for course, link, icon in zip(all_course_data[0],all_course_data[1], all_course_data[2] ):
        insert_course_info(course, link,icon)


#insert_all_info()





