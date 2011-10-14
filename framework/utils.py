'''
Created on 11.09.2011

@author: josh
'''
def as_iterable(object):
    try: 
        iter(object)
        return object
    except TypeError: 
        return (object)

    
    
