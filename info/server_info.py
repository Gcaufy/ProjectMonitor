import os

def chkTomcat ():
	rst = os.popen('ps aux | grep tomcat | grep -v grep').read()
	return len(rst) > 0

def chkNginx ():
	rst = os.popen('ps aux | grep nginx | grep -v grep').read()
	return len(rst) > 0

def chkSmb ():
	rst = os.popen('ps aux | grep smb | grep -v grep').read()
	return len(rst) > 0

def getServices ():
	data = {
		'tomcat': {
			'run': chkTomcat()
		},
		'nginx': {
			'run': chkNginx()
		},
		'samba': {
			'run': chkSmb()
		}
	}
	return data

if __name__ == "__main__":
	chkTomcat()