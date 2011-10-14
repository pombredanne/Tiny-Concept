'''
Created on 28.08.2011

@author: josh
'''

mediatypes_to_filetypes = {"text/html":"html",
                           "application/xhtml+xml":"xhtml",
                           "application/xml":"xml"}

def parse_accept_header(accept):
    """Parse the Accept header *accept*, returning a list with pairs of
    (media_type, q_value), ordered by q values.
    """
    values = [y.split(";") for y in [x for x in accept.split(",") ]]
    result = [(z[0], len(z) == 2 and float(z[1].lstrip().split("=", 1)[1]) 
                                 or 1.0) 
                    for z in values]
    
    result.sort(lambda x, y: -cmp(x[1], y[1]))
    
    return result

