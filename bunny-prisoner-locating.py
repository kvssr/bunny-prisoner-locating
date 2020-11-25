def solution(x, y):
	
	xinc = 2
	yinc = x
	
	result = 1
	
	for a in range(1,x):
		result += xinc
		xinc += 1
		
	for b in range(1,y):
		result += yinc
		yinc += 1

	return result
