import os
import sys
import subprocess
from subprocess import check_output
def get_pid(name):
    return check_output(["pidof",name])


def main():
	program = sys.argv[1]
	try:
		old_pid = get_pid(program)
		new_pid = get_pid(program)


		while old_pid == new_pid:
			print old_pid
			print "hello"
			new_pid = get_pid(program)

	except subprocess.CalledProcessError as e:
		print program + " crash or stop"
		
main()

child = subprocess.Popen(['pgrep',' python /opt/mastiff/mas.py /opt/malware/samples/'], stdout=subprocess.PIPE, shell=True)
result = child.communicate()[0]
