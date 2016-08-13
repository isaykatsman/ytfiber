import sys, os, errno
import selenium
import json
import getpass
from pprint import pprint
import wx
from urllib import urlopen
from lxml import etree
import collections

#input: bookmark folder name
#-> output: array of bookmark urls and bookmark link names
folder_name = 'YTFiberDL'

data_file = open('/home/isaykatsman/.config/google-chrome-unstable/Default/Bookmarks', 'r')
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
print os.name
print getpass.getuser()

#load json from string
s = '{"text":"lolextractme"}'
data = json.loads(s)

print data['text']

#dialog analytics scraping test
url = 'https://www.youtube.com/watch?v=73tGe3JE5IU'

#aggregate keywords
keywords = []

#scrape keywords from yt urls and aggregate in list
f = urlopen(url).read()
tree = etree.HTML(f)
string_keys = tree.xpath( "//meta[@name='keywords']" )[0].get("content")
keywords.extend(string_keys.split(", "))
print keywords
keywords.extend(['30'])
print keywords

#aggregate count with collections count
counter = collections.Counter(keywords)
print counter

#get most common
most_common = counter.most_common(3)
print 'Most common: ' + most_common[0][0] + ' ' + most_common[1][0] + ' ' + most_common[2][0]

#display analytics results
#app = wx.App()
#dlg = wx.MessageDialog(None, 'This is a multiline comment regarding \n analytics and stuff \n this is cool and dank', 'Analytics', wx.OK)
#dlg.ShowModal()
#dlg.Destroy()