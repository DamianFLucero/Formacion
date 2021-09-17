

personas = [
			['nico',24],
			['pedro',27],
			['maria',30],
			['clara',22],
			['franco',24],
			['lucia',28]
			]
contador = 1
for i in personas:
	print(contador, "-", i[0], end=" ")
	print(i[1], "años")
	contador+=1