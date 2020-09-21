import os
import subprocess
import shutil

db_dir_cij = 'D:/Data/Database/test'
db_dir_cij_sys = 'D:/Data/Database/test_sys'
db_dir = ['D:/Data/Database/test','D:/Data/Database/test_sys']
mariadb_dir = 'c:/xampp/mysql/bin/'
mariadb_program = 'mysqld.exe'

def checkDir():
	dir1 = os.path.isdir(db_dir_cij)
	dir2 = os.path.isdir(db_dir_cij_sys)
	if dir1 == True:
		print('directory cij ada')
		# shutil.rmtree(db_dir_cij)
		# print('directory '+db_dir_cij+' dihapus!!')
	else:
		print('directory '+db_dir_cij+' tidak ada!')
	if dir2 == True:
		print('directory cij_sys ada')
		# shutil.rmtree(db_dir_cij_sys)
		# print('directory '+db_dir_cij+' dihapus!!')
	else:
		print('directory '+db_dir_cij_sys+' tidak ada!')


def stopProgram(program_dir,program):

	call = 'TASKLIST','/FI','imagename eq %s' % program

	output = subprocess.check_output(call).decode()

	last_line = output.strip().split('\r\n')[-1]

	process_exists = last_line.lower().startswith(program.lower())

	if os.path.isfile(program_dir+program):
		print('file mysql ada!')
		if process_exists == True:
			os.system('taskkill /f /IM '+program)
		else:
			print('mariadb is not running :)')
	else:
		print('file mysql tidak ada')

def startProgram(program_dir,program):

	call = 'TASKLIST','/FI','imagename eq %s' % program

	output = subprocess.check_output(call).decode()

	last_line = output.strip().split('\r\n')[-1]

	process_exists = last_line.lower().startswith(program.lower())

	if os.path.isfile(program_dir+program):
		print('file mysql ada!')
		if process_exists == False:
			os.system('start '+program_dir+program)
		else:
			print('mariadb is running :)')
	else:
		print('file mysql tidak ada')	

stopProgram(mariadb_dir,mariadb_program)	
checkDir()

startProgram(mariadb_dir,mariadb_program)
