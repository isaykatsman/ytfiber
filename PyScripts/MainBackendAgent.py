import sys, os, random
#import mechanize
from selenium import webdriver
import time
import json
import getpass

#ytfiber backend
#currently works on both linux and windows

#inputs
destination_path = '/home/isaykatsman/Desktop/client_destination'
folder_name = 'YTFiberDL'

#first parse the folder in chrome data
#data file is platform dependent
#select data file based on os, as well as current user
data_file = ''
current_user = getpass.getuser() #
if os.name == 'posix':
    data_file = open('/home/' + current_user + '/.config/google-chrome-unstable/Default/Bookmarks', 'r')
elif os.name == 'nt':
    data_file = open('C:/Users/' + current_user + '/AppData/Local/Google/Chrome/User Data/Default', 'r')

data = json.load(data_file)

#list folders by finding all children of bookmark_bar that have element 'children'
num_children_of_bookmark_bar = len(data['roots']['bookmark_bar']['children'])

#see how many children book_mark bar has
print 'Bookmark bar has ' + str(len(data['roots']['bookmark_bar']['children'])) + ' children'

#store bookmark info for url
folder_urls = []
folder_url_names = []

#print all folders
print 'Obtaining Necessary bookmark urls'
for i in range(0, num_children_of_bookmark_bar):
    #this is if child of bookmark_bar isn't a folder
    try:
        folder_elements = data['roots']['bookmark_bar']['children'][i]['children']

        #if above didn't give error, then must be folder so check foldername
        #print data['roots']['bookmark_bar']['children'][i]['name']
        if data['roots']['bookmark_bar']['children'][i]['name'] == folder_name:
            num_urls = len(data['roots']['bookmark_bar']['children'][i]['children'])
            print 'Selected folder has ' + str(num_urls) + ' children'
            for j in range(0,num_urls):
                #log some information
                print 'Title: ' + data['roots']['bookmark_bar']['children'][i]['children'][j]['name'] +\
                      ' URL: ' + data['roots']['bookmark_bar']['children'][i]['children'][j]['url']
                #actually add what is necessary
                folder_urls.append(data['roots']['bookmark_bar']['children'][i]['children'][j]['url'])
                folder_url_names.append(data['roots']['bookmark_bar']['children'][i]['children'][j]['name'])
    except KeyError:
        a = 1
        #do nothing print 'Not a folder'

#now go ahead and actually do the downloading

#start scraping/downloading process
chromeOptions = webdriver.ChromeOptions()
prefs = {"download.default_directory" : destination_path}
chromeOptions.add_experimental_option("prefs",prefs)
chromedriver = './chromedriver'
driver = webdriver.Chrome(executable_path=chromedriver, chrome_options=chromeOptions)

#stealth mode, for deployment - make browser head invisible
driver.set_window_size(0, 0)
driver.set_window_position(2000, 0)

os.environ['webdriver.chrome.driver'] = chromedriver
driver.get("http://mp3fiber.com")

#go through each url and download
for i in range(0, len(folder_urls)):
    line = folder_urls[i]
    print line
    old_url = driver.current_url #save this current url

    #fill out link
    vidlink = driver.find_element_by_name('videoURL')
    vidlink.send_keys(line)

    # now click on link
    print "will now download"
    link = driver.find_element_by_class_name('submit')#driver.find_element_by_name('submit')
    time.sleep(1)
    link.click() #necessary in most instances, sometimes might cause error so comment it out

    #now waiting to download
    print "now waiting as external download to fiber server occurs"
    time.sleep(3)
    # now when finished, should be able to click Download
    time_old = int(time.time())
    time_accum = 0

    #TODO: timeouts ~1 out of 60 times, fix is to wait until element is clickable, check bookmarks for selenium tut
    while True:
        time.sleep(1)
        if driver.current_url != old_url:
            print "fetching download link"
            link = driver.find_element_by_link_text('Download Now!')
            print "right before download"
            time.sleep(1)
            link.click()
            print "clicked and pausing"
            #pause a bit for download to take place
            time.sleep(5)

            break

        #check if frozen, then reload page and go to next
        time_accum = int(time.time()) - time_old
        if time_accum > 600: #more than ten minutes
            print "Skipping!!!"
            #reload original page
            driver.get("http://mp3fiber.com")
            break
    #found and clicked url


#finally, close file
data_file.close()

#quite browser
driver.quit()