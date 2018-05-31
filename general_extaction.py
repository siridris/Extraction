#this code contains a general agorithm for all the extaction
#the parts
print" trying out something spectacular"
from sys import argv
#run the arguments in the command prompt
script, in_file, snd_a, snd_b, sD_a, sD_b, rcv_ab, timeing, t_diff  = argv
#getting the all "snd" lines from the log
#*************************************************************************************
def get_line(file_name, find_word1, find_word2):

	lines = [] #create a list for appending
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
def get_files_in (in_file, find_word1,find_word2, snd_a):

	filtererd_lines = get_all_lines(in_file, find_word1, find_word2)
	joinliens = '\n'.join(filtererd_lines)
	open(snd_a, 'w').write(joinliens) #writing and joining the list to a file
	return snd_a
#exracting out specific lines
A = get_files_in(in_file, "PSnd", "snd", snd_a)
f_file = open(A)
t_file = open ('snd_a', 'w')
for a in f_file:
	t_file.write(a.split()[2] + '\n')
t_file.close()
f_file.close()
def to_list():
	gone=[]
	cope = open('snd_a', 'r')
	for line in cope.readlines():
		ball = line[3:15]
		#bball, time..
		gone.append(ball)
		
	return gone

resu= to_list()	
with open(snd_a, 'w') as f:# i want to read and write at the same time
	su_m= len(resu)# the length of list
	print "total message sent is : %d " %su_m
	f.write ("the total number is {}\n".format(su_m))
	f.write('\n'.join(map(str, resu)))
with open(snd_a ,'r') as f:
	content = f.read()
	count = content.count("FFFF")#counting broadcast messages
	print "the number of broadcast message is: %d" %count	
unicast = su_m-count	#counting unicast messages
print "the unicast message is:%d" %unicast
print su_m, count, unicast
#getting the all "Sd" lines from the log
#*************************************************************************************
def get_line(file_name, find_word1, find_word2):

	lines = [] #create a list for appending
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
def get_files_in (in_file, find_word1,find_word2, sD_a):

	filtererd_lines = get_all_lines(in_file, find_word1, find_word2)
	joinliens = '\n'.join(filtererd_lines)
	open(sD_a, 'w').write(joinliens)
	return sD_a
#further extraction of sD lines 
A = get_files_in(in_file, "PSnd", "sD", sD_a)
f_file = open(A)
t_file = open ('sD_a', 'w')
for a in f_file:
	t_file.write(a.split()[2] + '\n') #writing result extracted
t_file.close()
f_file.close()
def to_list():
	gone=[]
	cope = open('sD_a', 'r')
	for line in cope.readlines():
		ball = line[4:10] #cutting out only sd lines
		gone.append(ball)
	return gone
resu= to_list()	
#write the results to a file
with open(sD_b, 'w') as f:
	s= len(resu) # the length of list
	print"delivered message is :%d"  %s
	f.write ("the total number is {}\n".format(s))
	f.write('\n'.join(map(str, resu)))
Snd_diff= su_m-s
print "the snd diff is %d" %Snd_diff
#getting the all "Rcv" lines from the log
#*************************************************************************************
def get_line(file_name, f1, f2, f3, f4, f5,f6,f7,f8,f9,f10,f11,f12,f13):
	lines = [] #creating a list to be appended
	for line in file_name.strip().split('\n'):
		if f1 in line:
			lines.append(line)
		elif f2 in line:
			lines.append(line)
		elif f3 in line:
			lines.append(line)
		elif f4 in line:
			lines.append(line)
		elif f5 in line:
			lines.append(line)
		elif f6 in line:
			lines.append(line)
		elif f7 in line:
			lines.append(line)
		elif f8 in line:
			lines.append(line)
		elif f9 in line:
			lines.append(line)
		elif f10 in line:
			lines.append(line)
		elif f11 in line:
			lines.append(line)
		elif f12 in line:
			lines.append(line)
		elif f13 in line:
			lines.append(line)			
		else:
			pass
	return lines
def get_all_lines(f_name, f1, f2, f3, f4, f5,f6,f7,f8,f9,f10,f11,f12,f13):

	f_content = open(f_name, 'r').read() #open a file
	return get_line(f_content,f1, f2, f3, f4, f5,f6,f7,f8,f9,f10,f11,f12,f13)

def get_files_in (in_file, f1, f2, f3, f4, f5,f6,f7,f8,f9,f10,f11,f12,f13, rcv_ab):

	filtererd_lines = get_all_lines(in_file, f1, f2, f3, f4, f5,f6,f7,f8,f9,f10,f11,f12,f13)
	joinliens = '\n'.join(filtererd_lines)
	with open(rcv_ab, 'w') as f:
		f.write(joinliens) #joining lines and writing results to a file
	return rcv_ab
Bob = get_files_in(in_file, "Rcv<-PTRNG", "Rcv<-JFACK","Rcv<-DYHM", "Rcv<-RUA", "Rcv<-Alv", "Rcv<-BIDNV", "Rcv<-IHY", "Rcv<-SFY", "Rcv<-SR", "Rcv<-INYP", "Rcv<-CO", "Rcv<-CnclPshp", "Rcv<-PR",rcv_ab)	#keywords to be extacred
# makeing a new defination to count received messages
def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1
	
C_1 = file_len(Bob)
#writing all lines in the file and joining them
def get_files_in (in_file, f1, f2, f3, f4, f5,f6,f7,f8,f9,f10,f11,f12,f13, rcv_ab):

	filtererd_lines = get_all_lines(in_file, f1, f2, f3, f4, f5,f6,f7,f8,f9,f10,f11,f12,f13)
	joinliens = '\n'.join(filtererd_lines)
	with open(rcv_ab, 'w') as f:
		f.write("the total numbers is :{}\n".format(C_1))
		f.write(joinliens)
	return rcv_ab
#result on screen
print"received messages are %d" %C_1
time = get_files_in(in_file, "Rcv<-PTRNG", "Rcv<-JFACK","Rcv<-DYHM", "Rcv<-RUA", "Rcv<-Alv", "Rcv<-BIDNV", "Rcv<-IHY", "Rcv<-SFY", "Rcv<-SR", "Rcv<-INYP", "Rcv<-CO", "Rcv<-CnclPshp", "Rcv<-PR",  rcv_ab)
#getting the all "time difference i.e radio on and off" lines from the log
#*************************************************************************************
#using datetine 
import datetime
def get_line(file_name, find_word1, find_word2):
    lines = [] #a list
    temp = ""

    for line in file_name.strip().split('\n'):
        if find_word1 in line and not temp:
            temp = line
        elif find_word2 in line and temp:
                lines.append(temp)
                lines.append(line)
                temp = ""
        else:
            pass
    return lines#append back to list
#open a file to save list
def get_all_lines(f_name, find_word1, find_word2):

	f_content = open(f_name, 'r').read()
	return get_line(f_content,find_word1, find_word2)
#joining lists and writing to the file
def get_files_in (in_file, find_word1,find_word2, timeing):

	filtererd_lines = get_all_lines(in_file, find_word1, find_word2)
	joinliens = '\n'.join(filtererd_lines)
	open(timeing, 'w').write(joinliens)
	return timeing
#from the result, extacting all radio start and stop time, 
def extract(in_file, find_word1,find_word2, timeing1,timeing2):
	f_file = open(get_files_in(in_file, find_word1,find_word2, timeing1))
	t_file = open ('timeing2', 'w')

	for a in f_file:
		t_file.write(a.split()[0] + '\n') #spilting list 
	t_file.close()
	f_file.close()
	return 'timeing2'
C= extract(in_file, "RStrtD", "RStpD", timeing,"N_save.txt")
#extracing the time seperately 
def A():
	times= []
	imp = open(C, "r")
	for line in imp.readlines():
		times.append(line)
	return times
result = A()
time_convered = map(
	lambda x: datetime.datetime.strptime(x, '%Y-%m-%dT%H:%M:%S.%fZ\n'),# convert time to datetime for easy calculation
	result
	)
diffs = []
for i in range(0,len(result), 2):
    diffs.append((time_convered[i+1]-time_convered[i]).total_seconds()) #subtracte the start time of radio from the off time of radio
with open(t_diff, "w+") as f:
	len_ght= len(diffs)
	f.write("total number of on off is = {}\n".format(len_ght)) #format function in python..
	some = sum(diffs)
	f.write("sum = {}\n".format(some)) #format function in python..
	f.write("\n".join(map(str, diffs))) #join the result
#***********************************************************************************
#finish part
print "the total time here is : %d" %some
print "snd,	broadcast,	unicats,	Sd,	snd-Sd,		rcv,		timedif,   timetotal"  #final result on screen 
print su_m,count,unicast,s,Snd_diff,C_1,some,len_ght
