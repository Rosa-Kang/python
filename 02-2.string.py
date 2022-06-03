#multistring.py

from ctypes import pointer
import string
from xml.dom.minidom import CharacterData


print("=" * 50)
print("My Program")
print("=" * 50)

# "Life is too short, You need Python"
# \a
# \b
# \000
# \n
# \t
# \\
# \'
# \"
# \r
# \f
%s string
%c Character
%d Integer
%f Floating-point
%o Octal
%x 16진수
%% Literal%

a= "hobby"
a.count('b')
# 2
a.find('b')
# 2
a.index('y')
# 4
",".join('abcd')
# 'a,b,c,d'
",".join['a', 'b', 'c', 'd']
# 'a,b,c,d'
c="Hi"
c.lower()
c.upper()

b=" hi "
b.lstrip()  #l means left
# "hi "
b.rstrip()
# " hi"

e="Life it too short"
e.split()
# ["Life", "is", "too", "short"]
f = ["a : b : c : d"]
f.split(:)
# ['a ', 'b ', 'c ', 'd']