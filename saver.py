a = []

def add(card):
	global a
	a.append(card)

def check(card):
	global a
	for i in range(0, len(a)):
		if a[i] == card:
			return True

def clear():
	global a
	a = []


if __name__ == '__main__':
	add('туз пики')
	add('8 черви')
	print(a)
	print('8 черви найдено? - ', check('8 черви'))