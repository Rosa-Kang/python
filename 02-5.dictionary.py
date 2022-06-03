#hash or associative array
from calendar import c

#딕셔너리와 셋은 순서가 없기 때문에 인덱싱을 지원하지 않는다. 따라서 인덱싱을 위해서는 리스트나 튜플로 변환후 해야 한다.
a ={a:'a'}
a[2] = 'b'
a = {1:'a', 2:'b'}

#key가 dictionary 안에 있는 지 확인하기 위해서는
c={'name':'pey', 'phoe': '6044445050', 'birth':'1118'}
'name' in c
true