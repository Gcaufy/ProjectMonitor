import os

def chkGrep (name):
	rst = os.popen('ps aux | grep ' + name + ' | grep -v grep').read()
	return len(rst) > 0

def chkTomcat ():
	return chkGrep('tomcat')

def chkNginx ():
	return chkGrep('nginx')

def chkSmb ():
	return chkGrep('smb')

def chkMySQL ():
	return chkGrep('mysql')

def getServices ():
	data = {
		'Tomcat': {
			'viewLog': True,
			'run': chkTomcat()
		},
		'Nginx': {
			'run': chkNginx()
		},
		'Samba': {
			'run': chkSmb()
		},
		'MySQL': {
			'run': chkMySQL()
		}
	}
	return data

if __name__ == "__main__":
	chkTomcat()