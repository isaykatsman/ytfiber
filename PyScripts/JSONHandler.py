import sys, os, errno
import selenium
import json
from pprint import pprint

#input: bookmark folder name
#-> output: array of bookmark urls and bookmark link names
folder_name = 'YTFiberDL'

data_file = open('/home/isaykatsman/.config/google-chrome/Default/Bookmarks', 'r')

data = json.load(data_file)

#list folders by finding all children of bookmark_bar that have element 'children'
num_children_of_bookmark_bar = len(data['roots']['bookmark_bar']['children'])

#see how many children book_mark bar has
print 'Bookmark bar has ' + str(len(data['roots']['bookmark_bar']['children'])) + ' children'

#print all folders
print 'All bookmark folders:'
for i in range(0, num_children_of_bookmark_bar):
    #this is if child of bookmark_bar isn't a folder
    try:
        folder_elements = data['roots']['bookmark_bar']['children'][i]['children']

        #if above didn't give error, then must be folder so print foldername
        print data['roots']['bookmark_bar']['children'][i]['name']
    except KeyError:
        a = 1
        #do nothing print 'Not a folder'

#once user selects bookmark folder in wx gui, and clicks run, we simply get url data of each child of folder
#data['roots']['bookmark_bar']['children'][i]['children'][0]['url']