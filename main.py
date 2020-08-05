import random
mast = ['черви', 'буби', 'пики', 'крести']
imaje = ['туз', 'валет', 'дама', 'король']

def ochki(num):
	if (num > 10):
		if num-10 == 1:
			return(str(num-10) + ' очко')
		elif (num-10 > 1) and (num-10 < 5):
			return(str(num-10) + ' очка')
		else:
			return(str(num-10) + ' очков')
	else:
		if num == 1:
			return(str(num) + ' очко')
		elif (num > 1) and (num < 5):
			return(str(num) + ' очка')
		else:
			return(str(num) + ' очков')


def randomcart():
	mast_n = random.randint(0,3)
	card = random.randint(2, 14)
	if (card > 10):
		return(imaje[card-11] + ' ' + mast[mast_n] + ' (' + ochki(card) + ')')
		return(ochki(card))
	else:
		return(str(card) + ' ' + mast[mast_n] + ' (' + ochki(card) + ')')
if __name__ == '__main__':
	print(randomcart())