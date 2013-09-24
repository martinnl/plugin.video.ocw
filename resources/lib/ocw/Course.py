'''
Created on 24 sep 2013

@author: martinnl
'''

class Course(object):
    '''
    classdocs
    '''


    def __init__(self, coursename, progress, url):
        '''
        Constructor
        '''
        self.coursename = coursename
        self.progress = progress
        self.url = url
        