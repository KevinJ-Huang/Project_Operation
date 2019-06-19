import os
import random
out = open("DPED_hunhe_res.txt",'w')
lines=[]
with open("DPED_hunhe.txt", 'r') as infile:
	for line in infile:
		lines.append(line)
random.shuffle(lines)
for line in lines:
	out.write(line)
infile.close()
out.close()
