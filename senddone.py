#getting the all "Sd" lines from the log
print" trying out something spectacular"
from sys import argv

script, in_file, out_file, total_f = argv

def get_line(file_name, find_word1, find_word2):

	lines = []#create a list for appending
	for line in file_name.strip().split('\n'):
		if find_word1 in line:
			if find_word2 in line:
				lines.append(line)
	return lines
#open a file to save the list
def get_all_lines(f_name, find_word1, find_word2):

	f_content = open(f_name, 'r').read()
	return get_line(f_content,find_word1, find_word2)
#write all the exracted lines in the file opemned
def get_files_in (in_file, find_word1,find_word2, out_file):

	filtererd_lines = get_all_lines(in_file, find_word1, find_word2)
	joinliens = '\n'.join(filtererd_lines)
	open(out_file, 'w').write(joinliens) #writing result extracted
	return out_file
#further extraction of sD lines 
A = get_files_in(in_file, "PSnd", "sD", out_file)


f_file = open(A)
t_file = open ('out_file', 'w')

for a in f_file:
	t_file.write(a.split()[2] + '\n') #writing result extracted
t_file.close()
f_file.close()

def to_list():
	gone=[]
	cope = open('out_file', 'r')
	for line in cope.readlines():
		ball = line[4:10] #cutting out only sd lines
		gone.append(ball)
		
	return gone
resu= to_list()	
#write the results to a file
with open(total_f, 'w') as f:
	s= len(resu) # the length of list
	print"delivered message is :%d"  %s
	f.write ("the total number is {}\n".format(s))
	f.write('\n'.join(map(str, resu)))
