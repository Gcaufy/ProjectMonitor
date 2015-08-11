import os

PROJECTS = {
	'sino-hkgta-fe': '/data/sino-hkgta-fe/',
	'web-portal': '/data/web-portal/',
	'sino-hkgta-be': '/data/sino-hkgta-be/',
}

def getBranch (project):
	os.chdir(PROJECTS[project])
	rst = os.popen('git rev-parse --abbrev-ref HEAD 2> /dev/null').read()
	return rst

def getLastCommit (project):
	os.chdir(PROJECTS[project])
	rst = os.popen("git log --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit -1").read()
	return rst

def getLastDeploy (project):
	rst = os.popen('cat /var/log/deploy/' + project + '.version').read()
	return rst

def getProjects ():
	data = {}
	for (k, v) in PROJECTS.items():
		data[k] = {
			'branch': getBranch(k),
			'lastDeploy': getLastDeploy(k),
			'lastCommit': getLastCommit(k)
		}
	return data

if __name__ == "__main__":
	print getProjects()

