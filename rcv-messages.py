#getting the all "Rcv" lines from the log
from sys import argv
script, in_file, out_file = argv
print" trying out something spectacluar"
def get_line(file_name, f1, f2, f3, f4, f5,f6,f7,f8,f9,f10,f11,f12,f13):

	lines = []#creating a list to be appended
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

def get_files_in (in_file, f1, f2, f3, f4, f5,f6,f7,f8,f9,f10,f11,f12,f13, out_file):

	filtererd_lines = get_all_lines(in_file, f1, f2, f3, f4, f5,f6,f7,f8,f9,f10,f11,f12,f13)
	joinliens = '\n'.join(filtererd_lines)
	with open(out_file, 'w') as f:
		f.write(joinliens) #joining lines and writing results to a file
	return out_file

Bob = get_files_in(in_file, "Rcv<-PTRNG", "Rcv<-JFACK","Rcv<-DYHM", "Rcv<-RUA", "Rcv<-Alv", "Rcv<-BIDNV", "Rcv<-IHY", "Rcv<-SFY", "Rcv<-SR", "Rcv<-INYP", "Rcv<-CO", "Rcv<-CnclPshp", "Rcv<-PR",out_file) #keywords to be extacred
# makeing a new defination to count received messages	
def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1
	
C = file_len(Bob)
#writing all lines in the file and joining them
def get_files_in (in_file, f1, f2, f3, f4, f5,f6,f7,f8,f9,f10,f11,f12,f13, out_file):

	filtererd_lines = get_all_lines(in_file, f1, f2, f3, f4, f5,f6,f7,f8,f9,f10,f11,f12,f13)
	joinliens = '\n'.join(filtererd_lines)
	with open(out_file, 'w') as f:
		f.write("the total numbers is :{}\n".format(C))
		f.write(joinliens)
	return out_file
#result on screen
print"received messages is %d" %C
time = get_files_in(in_file, "Rcv<-PTRNG", "Rcv<-JFACK","Rcv<-DYHM", "Rcv<-RUA", "Rcv<-Alv", "Rcv<-BIDNV", "Rcv<-IHY", "Rcv<-SFY", "Rcv<-SR", "Rcv<-INYP", "Rcv<-CO", "Rcv<-CnclPshp", "Rcv<-PR",  out_file)
