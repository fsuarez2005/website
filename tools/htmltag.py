#!/usr/bin/env python3

__all__ = ['Tag']


import html

class Tag:
    def __init__(self,name,*content,tags=[]):
        self.name = name
        self.content = content
        self.tags = tags
    
    
    def __str__(self):
        output = ""
        
        output += f"<{self.name}>"
        
        for e in self.content:
            output+= str(e)
        
        output += f"</{self.name}>"
        
        
        return output





import unittest
    
class TestTag(unittest.TestCase):
    def test_c(self):
        t = Tag('html',Tag('h1'))
        
        print(t)

if __name__ == '__main__':
    unittest.main()


