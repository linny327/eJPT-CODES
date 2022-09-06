"""
module is a file that contains source code, their main purpose is to
group python functions and objects in order to organize larger projects.
NB we can also import c++ object files in addition to python
"""

#my_double module
#create my_double.py module

import my_double
#from my_double import c then print(c)

print(my_double.c) # using object defined within the imported module
print(my_double.my_double(8))
print(my_double.__doc__)#printing the documentation of the module and the funx
print(my_double.my_double.__doc__)