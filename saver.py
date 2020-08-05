a = []

def add(card):
	global a
	a.append(card)

def check(card):
	for i in range(0, len(a)):
		if a[i] == card:
			return True
		else:
			return False


if __name__ == '__main__':
	add('туз пики')
	add('8 черви')
	print(a)