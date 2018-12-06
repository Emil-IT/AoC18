with open('./day1_input.txt', 'r') as file:
	data = []
	for line in file:
			if line[0] == '+':
				data.append(int(line[1:]))
			if line[0] == '-':
				data.append(-int(line[1:]))
	freq = 0
	seen_freqs = [0]
	itteration = 0
	while True:
		#print('Itteration: ' + str(itteration))
		if(itteration%1 == 0):
			print(str(itteration) + ', ' + str(len(seen_freqs)))
		for change in data:
			freq += change

			if freq in seen_freqs:
				print('Repeated frequency: ' + str(freq))
				quit()
			else:
				seen_freqs.append(freq)
				#print(len(seen_freqs))

		itteration += 1

		print(freq)
		#print(seen_freqs)
