'''
Created on 25 sep 2013

@author: martinnl
'''

from resources.lib.ocw.Course import Course

class User(object):
    '''
    classdocs
    '''


    def __init__(self, name):
        '''
        Constructor
        '''
        self.name = name
    
    def getCurrentCourses(self):
        asicCourse = Course('ASIC', 0.5, '/asic')
        fpgaCourse = Course('FPGA', 0.2, '/fpga')
        
        return [asicCourse, fpgaCourse]
        