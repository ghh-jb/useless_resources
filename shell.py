import os
def cd(path):
	try:
		os.chdir(path)
	except:
		print("[-] Could not chdir")
while (True):
	c_path = os.getcwd()
	cmd = input(f"pyTerm:{c_path}# ")
	if (cmd == ""): continue
	if (cmd.split()[0] == "cd"):
		cd(cmd.split()[1])
		continue
	os.system(f"TERM=xterm-256color http_proxy= https_proxy= {cmd}")
