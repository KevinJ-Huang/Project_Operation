 
with open('1.txt') as f_obj:		
	lines = f_obj.readlines()
 
with open('2.txt') as g_obj:		
	contents = g_obj.readlines()
 
with open('3.txt', 'w') as t_obj:		
 
	all_feature = [line.strip() + ',' + content for line, content in zip(lines, contents)]		
 

	for a_f in all_feature:
		t_obj.write(a_f)
 
print('Finished!')
