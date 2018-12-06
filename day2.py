with open('./day2_input.txt', 'r') as file:
	twos = 0
	threes = 0
	lines = []
	for line in file:
		#----Part1----
		sorted_line = sorted(line)
		two = True
		three = True
		while len(sorted_line) > 0 and (two or three):
			n = sorted_line.count(sorted_line[0])
			if two and n == 2:
				twos += 1
				two = False
			elif three and n == 3:
				threes += 1
				three = False
			del sorted_line[0:n]

		#----Part2----
		lines.append(line)

	row_len = len(lines[0])
	common = ''
	for i in range(len(lines)):
		for j in range(i+1, len(lines)):
			for n in range(row_len):
				if lines[i][0:n] == lines[j][0:n] and lines[i][n+1:] == lines[j][n+1:]:
					common = lines[i][0:n] + lines[i][n+1:]

	checksum = twos * threes

	print('Checksum: ' + str(checksum))
	print('Common: ' + common)


