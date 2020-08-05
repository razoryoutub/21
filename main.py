import random
import os
import time
import saver
mast = ['черви', 'буби', 'пики', 'крести']
imaje = ['туз', 'валет', 'дама', 'король']
os.system('cls')
print('для взятия карт нажимайте "enter"(ввод)')
print('для завершения набора введите что-то и нажмите "enter"(ввод)')
input(': ')


def continiue():
	global q_cards
	global u_cards
	global u_sum
	global q_sum
	global cp
	global cp_u
	q_cards = ""
	u_cards = ""
	u_sum = 0
	q_sum = 0
	cp = True
	cp_u = ""
	gameloop()


def ochki(num):
	if num >= 10 and num < 20:
		return((str(num) + ' очков'))
	elif num >= 20:
		if int(str(num)[-1]) == 1:
			return(str(num) + ' очко')
		elif int((str(num)[-1])) > 1 and int(str(num)[-1]) < 5:
			return(str(num) + ' очка')
		else:
			return(str(num) + ' очков')
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
		return(imaje[card-11] + ' ' + mast[mast_n] + ' ' + str(card-10))
	else:
		return(str(card) + ' ' + mast[mast_n] + ' ' + str(card))

def q_game():
	global q_cards
	global q_sum
	os.system('cls')
	print('ваша сумма: ' + str(ochki(u_sum)))
	print('первая карта крупье: ' + q_cards[0:-2])
	print('Крупье берет карты...')
	while True:
		global cp	
		if q_sum < 21 and cp:
			time.sleep(2)
			if q_sum < 15:
				q_cards += randomcart()
				q_sum += int(q_cards.split()[-1])
				q_cards = q_cards[0:-2] + ' | '
				print(q_cards.split()[-3] + ' ' + q_cards.split()[-2])
			else: 
				if random.randint(1,100) >= 65:
					q_cards += randomcart()
					q_sum += int(q_cards.split()[-1])
					q_cards = q_cards[0:-2] + ' | '
					print(q_cards.split()[-3] + ' ' + q_cards.split()[-2])
				else:
					cp = False
		else:
			time.sleep(3)
			os.system('cls')
			if int(u_sum) > int(q_sum) or int(q_sum)>21:
				print('Вы выиграли!')
			elif int(u_sum) < int(q_sum) or (int(q_sum)==21 and  (int(u_sum) != int(q_sum))):
				print('Вы проиграли')
			elif int(u_sum) == int(q_sum):
				print('Вы  проиграли!')
				print('(При одинаковом количестве очков побеждает крупье!)')
			print('Ваши карты: ' + u_cards[0:-2] + ' --сумма: ' + str(u_sum))
			print('Карты крупье: ' + q_cards[0:-2] + ' --сумма: ' + str(q_sum))
			global cp_u
			while (cp_u != 'y') and (cp_u != 'n'):
				cp_u = input('Продолжим?[y/n]: ')
			if cp_u == 'y':
				continiue()
			else:
				exit()



def gameloop():
	global u_sum
	global q_cards
	global u_cards
	global q_sum
	os.system('cls')
	if q_cards == "":
		q_cards += randomcart()
		q_sum += int(q_cards.split()[-1])
		q_cards = q_cards[0:-2] + ' | '
	u_cards += randomcart()
	u_sum += int(u_cards.split()[-1])
	print('Карта крупье: {0} \n\nВаши карты: {1}'.format(q_cards[0:-2], u_cards[0:-2]))
	print('Сумма ваших очков: ' + str(ochki(u_sum)))
	u_cards = u_cards[0:-2] + ' | '
	if u_sum == 21:
		os.system('cls')
		print('Вы набрали 21!')
		time.sleep(1)
		q_game()
	elif u_sum > 21:
		time.sleep(1)
		os.system('cls')
		print('Вы проиграли!')
		print('Ваши карты:\n' + u_cards)
		global cp_u
		while cp_u != 'y' and cp_u != 'n':
			cp_u = input('Продолжим?[y/n]: ')
		if cp_u == 'y':
			continiue()
		else:
			exit()
	cont = input(': ')
	if cont == "":
		gameloop()
	else:
		q_game()


if __name__ == '__main__':
	q_cards = ""
	u_cards = ""
	u_sum = 0
	q_sum = 0
	cp = True
	cp_u = ""
	gameloop()