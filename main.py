print('---------')
print("|       |")
print("|       |")
print("|       |")
print("---------")
m = [[" ", " ", " ", " "], [" ", " ", " ", " "], [" ", " ", " ", " "], [" ", " ", " ", " "]]
q = 1
while True:
	count_x = m[1].count('X') + m[2].count('X') + m[3].count('X')
	count_o = m[1].count('O') + m[2].count('O') + m[3].count('O')
	count_ = m[1].count(' ') + m[2].count(' ') + m[3].count(' ')
	win = 0

	# when game impossible

	a = list(input("Enter the coordinates: "))
	y = a[0]
	x = a[2]
	while not a[0].isdecimal() or not a[2].isdecimal:
		print("You should enter numbers!")
		a = list(input("Enter the coordinates: "))
		y = a[0]
		x = a[2]
	while int(y) > 3 or int(y) < 1 or int(x) > 3 or int(x) < 1:
		print("Coordinates should be from 1 to 3!")
		a = list(input("Enter the coordinates: "))
		y = a[0]
		x = a[2]
	while m[int(y)][int(x)] != " ":
		print("This cell is occupied! Choose another one!")
		a = list(input("Enter the coordinates: "))
		y = a[0]
		x = a[2]
	if q % 2 == 1:
		m[int(y)][int(x)] = "X"
	else:
		m[int(y)][int(x)] = "O"
	q = q + 1
	print('---------')
	print('| ' + m[1][1] + ' ' + m[1][2] + ' ' + m[1][3] + ' |')
	print('| ' + m[2][1] + ' ' + m[2][2] + ' ' + m[2][3] + ' |')
	print('| ' + m[3][1] + ' ' + m[3][2] + ' ' + m[3][3] + ' |')
	print('---------')
	if count_x - count_o >= 2:
		pass
	elif count_o - count_x >= 2:
		pass
	elif (m[1][1] == m[1][2] == m[1][3]) and (m[2][1] == m[2][2] == m[2][3]):
		pass
	elif (m[1][1] == m[1][2] == m[1][3]) and (m[3][1] == m[3][2] == m[3][3]):
		pass
	elif (m[2][1] == m[2][2] == m[2][3]) and (m[3][1] == m[3][2] == m[3][3]):
		pass
	elif (m[1][1] == m[2][1] == m[3][1]) and (m[1][2] == m[3][2] == m[2][2]):
		pass
	elif (m[2][1] == m[1][1] == m[3][1]) and (m[1][3] == m[2][3] == m[3][3]):
		pass
	elif (m[1][2] == m[2][2] == m[3][2]) and (m[1][3] == m[2][3] == m[3][3]):
		pass

	# when x or o win
	elif ((m[1][1] != ' ') and (m[1][1] == m[1][2]) and (m[1][2] == m[1][3])):
		win = 1
		print(m[1][1], 'wins')
		break
	elif ((m[2][1] != ' ') and (m[2][1] == m[2][2]) and (m[2][2] == m[2][3])):
		win = 1
		print(m[2][1], 'wins')
		break
	elif ((m[3][1] != ' ') and (m[3][1] == m[3][2]) and (m[3][2] == m[3][3])):
		win = 1
		print(m[3][1], 'wins')
		break
	elif ((m[1][1] != ' ') and (m[1][1] == m[2][1]) and (m[2][1] == m[3][1])):
		win = 1
		print(m[1][1], 'wins')
		break
	elif ((m[1][2] != ' ') and (m[1][2] == m[2][2]) and (m[1][2] == m[3][2])):
		win = 1
		print(m[1][2], 'wins')
		break
	elif ((m[1][3] != ' ') and (m[1][3] == m[2][3]) and (m[2][3] == m[3][3])):
		win = 1
		print(m[1][3], 'wins')
		break
	elif ((m[1][1] != ' ') and (m[1][1] == m[2][2]) and (m[2][2] == m[3][3])):
		win = 1
		print(m[1][1], 'wins')
		break
	elif ((m[3][1] != ' ') and (m[3][1] == m[2][2]) and (m[2][2] == m[1][3])):
		win = 1
		print(m[3][1], 'wins')
		break
	elif win == 0 and count_ == 0:
		print("Draw")
		break
	if q == 10:
		print("Draw")
		break
