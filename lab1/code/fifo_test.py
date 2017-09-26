# Lab 1 09/13/2017
# Yi Chen yc2329
# Mingda Yang my432

import subprocess

while True:
	input_cmd = raw_input("Please enter your command: ") # let user enter their commend and stored in input_cmd
	cmd = 'echo "' + input_cmd + '" > my_fifo'           # Form the correct typo for fifo commend, pass user input as an arbitrary component 
	print subprocess.check_output(cmd,shell=True)        # Run the comment with subprocess, first check whether comment is exist  and correct, then if yes return, else raise error flag
	if input_cmd == 'quit':                              # quit the program when met 'quit'
		break
