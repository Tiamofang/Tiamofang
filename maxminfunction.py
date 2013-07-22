Python 2.7.3 (default, Apr 10 2012, 23:24:47) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.

>>> ================================ RESTART ================================
>>> def maxnum(List):
	index=0
	while index+1<len(List):
		if List[index]<List[index+1]:
			larger=List[index+1]
		else:
			larger=List[index]
		index+=1
	return larger

>>> maxnum([2,4,2,4,5,6])
6
>>> maxnum([3,3,3])
3
>>> def minnum(List):
	index=0
	while index+1<len(List):
		if List[index]>List[index+1]:
			smaller=List[index+1]
		else:
			smaller=List[index]
		index+=1
	return smaller

>>> minnum([2,3,4,1,4])
1

>>> def length(S):
	count=0
	for s in S:
		count+=1
	return count

>>> length('adfasdfasdf')
11
>>> 
