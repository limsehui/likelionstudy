wintable={
	'가위':'보'
	'바위':'가위'
	'보':'바위'
}

def rsp(mine, yours):
	if mine == yours:
		return 'draw'
	elif wintable[mine] == yours:
		return 'win'
	else:
		return 'lose'
		
result =rsp('가위', '바위')


messages ={
	'win':'이겼다'
	'draw':'비겼네'
	'lose':'졌어...'
	}

print(result)

"""
딕셔너리란
여러 값을 저장해 두고 필요한 값을 꺼내 쓰는 기능
이름표를 이용하여 값을 꺼내 사용
사용할 때는 리스트와 비슷한 방식
"""