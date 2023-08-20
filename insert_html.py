from bs4 import BeautifulSoup
import info # import info.py to extract data from database


'''
purpose for the python file is to insert data from the database to html
refresh only when update file

'''


#inject code for beautiful soup

#reference for course

# course_na, course_description, pre_requisite, link_for_more, icon_class

course_na, course_description, pre_requisite, link_for_more, icon_class = "","","","",""


#template for dynamically insert html element
inject_code = """

 <div class="course-card">
        
        
        <h2 class="title">{course_na}
          
            <span class="material-icons">
                {icon_class}
            </span>
        </h2>
        
        <p class="description">{course_description}</p>
        <p class = "pre-requisite">{pre_requisite}</p>
      
        <a class="link-for-more" href={link_for_more}>Link for more</a>
        
        
        
 </div>



"""

#update july 29- able to connect database and inject html code!!

def format_code(el) -> str:
    # get info from the database and insert as html document
  
    #retrieve database record and insert into the file
     
    # el in order:
    # course_na, course_description, pre_requisite, link_for_more, icon_class
        
    new = inject_code.format(course_na = el[0], icon_class = el[4], pre_requisite = el[2], course_description =  el[1],  link_for_more = el[3])
    return new
        

def clear_info(target):
     #clear all info
          for div in target.find_all("div", {'class': 'course-card'}):
              div.decompose()


def insert_info():
    '''insert code'''
    with open("./templates/info.html", encoding='utf8') as file:
        soup = BeautifulSoup(file, "html.parser")
        print(soup)
        target = soup.find("section", {'class':'all-course-content'})
        clear_info(target) # clear html to re-insert html 


        print(info.get_record())

       # get record from the database to display all info
        for course in info.get_record():
             
       
        
          # insert target and parse code beautiful soup
          ## course_na, course_description, pre_requisite, link_for_more, icon_class
          
           div_class= format_code(course)

           # aug 1 works! -> just some html error
           target.append(BeautifulSoup(div_class, 'html.parser'))
        # alter file and add the new course class
        with open("./templates/info.html", "wb") as file:
           file.write(soup.prettify("utf-8"))
        
  



def insert_search_record(key:str):
        '''
        to insert search record into the search result
        
        '''
        with open("./templates/info.html", encoding='utf8') as file:
           soup = BeautifulSoup(file, "html.parser")
          
           target = soup.find("section", {'class':'search-result'})
        clear_info(target)
         # clear html to re-insert html 

       # get record from the database to display all info
        for course in info.filter_record(key):
             
       
        
          # insert target and parse code beautiful soup
          ## course_na, course_description, pre_requisite, link_for_more, icon_class
          
           div_class= format_code(course)

           # aug 1 works! -> just some html error
           target.append(BeautifulSoup(div_class, 'html.parser'))
         


    # alter file and add the new course class
        with open("./templates/info.html", "wb") as file:
           file.write(soup.prettify("utf-8"))
        
        
    
        
#insert_info()
    


