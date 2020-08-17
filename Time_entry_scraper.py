#Web_Scraper for tffrs notes

import xlwt
from xlwt import Workbook

"""
To think about:
- Web scraper or API query
- Deal with incorrect data on Tffrs, IAAF, Athletic.net, other websites
- Small differences in spelling of name,
- Club or unattached athletes might not have a profile with their PRs

API (Application Program Interface): An API is a set of methods and tools
that allows one’s to query and retrieve data dynamically.
Reddit, Spotify, Twitter, Facebook, and many other companies provide free
APIs that enable developers to access the information they store on their
servers; others charge for access to their APIs.

Web Scraping: A lot of data isn’t accessible through data sets or
APIs but rather exists on the internet as Web pages.

- possibly take the lowest PR from many websites, search all variations of name
- Search by team and find closest matching name

- After every athlete search--> put into table unless User says Clear
"""



#Ask for user input (Name and coach's time entry) (Maybe have a main function)
def display_menu():
    """ prints a menu of options
    """  
    print()
    print('(0) Create New Table')
    print('(1) Search an athlete')
    print('(2) Print/Export/View? current table')
    print('(3) Quit')
    print()


#Scraper:
    #From Athletic.net, Tffrs, IAAF
    #If no value is found, return N/A & dont go on to next functions
def scraper(athlete, distance, entry_time):
    """Scrapes 3 websites to search for athlete PR"""





#Find smallest value of the three websites MIN
def min_PR(tffrs_entry, a_n_entry, IAAF_entry):
    """Finds the fastest time between the 3 websites"""



#Average the smallest val of the three websites and the coach's entry
def average_time(PR, entry):
    """averages the scraped PR and the coach's entry"""
    #FIND SIMPLER WAY
    PR_list= PR.split(';', ':', '.')
    entry_list = entry.split(':', ';', '.')

    for i in range(len(PR_list)):
        PR_list[i]=int(PR_list[i]) #Now list of integers

    for j in range(len(entry_list)):
        entry_list[i]=int(entry_list[i]) # List of integers

    #Convert to seconds
    #Average
    #Convert back to minute/seconds
        
        



#CREATE TABLE FUNCTION (create an excel sheet?)
def create_table(table_name):
    """May go to an excel spreadsheet and create the names of columns
        as NAME, DISTANCE, AVERAGE TIME"""
    wb= Workbook()

    sheet1 = wb.add_sheet(table_name)
    sheet1.write(1,0, 'Athlete name')
    sheet1.write(1, 1, 'Distance')
    sheet1.write(1,2, 'Average time')

    wb.save(table_name + '.xls')
    



#ADD VAL TO TABLE FUNCTION (insert values into excel sheet)
def insert_val(athlete, distance, average_time):
    """inserts the data into excel(?) in respective columns"""

    

#VIEW TABLE FUNCTION (Go to that excel sheet)
def view_table():
    """Pulls up the current excel spreadsheet"""



#MAIN Function
def main():
    """ the main user-interaction loop
    """

    while True:
        print()
       # print_matrix(matrix)       Possibly print table of finished names?
        display_menu()
        print('**You must create a new table before the first athlete search**')
        choice = int(input('Enter your choice: '))

        if choice ==0:
            #Call function that creates a table
            title= str(input('Name of table: ')
            create_table(title)

        elif choice == 1:
            a= str(input('Athlete Name (ie. Angela Castronuovo): '))
            d= int(input('Race Distance (ie. 3000): '))
            t= str(input('Entry time (ie. 4:07.0): '))
            #USE THIS INFO FOR WEB SCRAPING
            #call webscraper, call MIN, call average, put val into table
                
        
        elif choice ==2:
            #Call function to view current table
            view_table()
            
        elif choice ==3:
            break
        else:
            print('Invalid choice. Try again.')
            
        
