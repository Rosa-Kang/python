#딕셔너리와 셋은 순서가 없기 때문에 인덱싱을 지원하지 않는다. 따라서 인덱싱을 위해서는 리스트나 튜플로 변환후 해야 한다.
#교집합

s1 = set([1,2,3,4,5,6])
s2 = set([4,5,7,9,0,11])

#교집합
s1 & s2 
{4,5}
s1.intersection(s2)
{4,5}

#합집합
s1 | s2
s1.union(s2)
{0,1,2,3,4,5,6,7,9,11} #중복값은 한번만, 순서가 없어 작은 값이 먼저온다

#차집합
s1 - s2
s1.difference(s2)

#추가하기
s1.add(x)
s1.update([4,5,6])
s1.remove(2)