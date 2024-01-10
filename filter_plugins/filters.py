#!/usr/bin/python3
import itertools

def extrElem(aList,pattern1,pattern2):
    result = list(itertools.takewhile(lambda x: pattern2 not in x, 
        itertools.dropwhile(lambda x: pattern1 not in x, aList)))
    return(result)

class FilterModule(object):
    def filters(self):
        return {
            'extract_element': extrElem 
        }