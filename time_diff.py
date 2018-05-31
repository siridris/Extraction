#using datetine
import datetime
from sys import argv

script, in_file, out_file, t_diff = argv

print" trying out something spectacular"

def get_line(file_name, find_word1, find_word2):

	lines = [] #a list
	for line in file_name.strip().split('\n'):
		if find_word1 in line:
			lines.append(line)
		elif find_word2 in line:
			lines.append(line)
		else:
			pass
	return lines #append back to list
#open a file to save list
def get_all_lines(f_name, find_word1, find_word2):

	f_content = open(f_name, 'r').read()
	return get_line(f_content,find_word1, find_word2)
#joining lists and writing to the file
def get_files_in (in_file, find_word1,find_word2, out_file):

	filtererd_lines = get_all_lines(in_file, find_word1, find_word2)
	joinliens = '\n'.join(filtererd_lines)
	open(out_file, 'w').write(joinliens)
	return out_file
#from the result, extacting all radio start and stop time, 
def extract(in_file, find_word1,find_word2, out_file1,out_file2):
	f_file = open(get_files_in(in_file, find_word1,find_word2, out_file1))
	t_file = open ('out_file2', 'w')
	for a in f_file:
		t_file.write(a.split()[0] + '\n')#spilting list
	t_file.close()
	f_file.close()
	return 'out_file2'
C= extract(in_file, "RStrtD", "RStpD", out_file,"N_save.txt")
#extracing the time seperately 
def A():
	times= []
	imp = open(C, "r")
	for line in imp.readlines():
		times.append(line)
	return times
result = A()
time_convered = map(
	lambda x: datetime.datetime.strptime(x, '%Y-%m-%dT%H:%M:%S.%fZ\n'), # convert time to datetime for easy calculation
	result
	)
diffs = []
for i in range(0,len(result), 2):
    diffs.append((time_convered[i+1]-time_convered[i]).total_seconds()) #subtracte the start time of radio from the off time of radio
with open(t_diff, "w+") as f:
    s = sum(diffs)
    f.write("sum = {}\n".format(s)) #format function in python..
    f.write("\n".join(map(str, diffs)))#join the result
print s
