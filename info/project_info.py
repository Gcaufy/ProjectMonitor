import os

PROJECTS = {
	'sino-hkgta-fe': { 
		'path': '/data/sino-hkgta-fe/',
		'url': 'http://www.sino.dev'
	},
	'web-portal': { 
		'path': '/data/web-portal/',
		'url': 'http://member.sino.dev'
	},
	'sino-hkgta-be': { 
		'path': '/data/sino-hkgta-be/sino-hkgta-be/',
		'url': 'http://www.sino.dev:8080/sino-hkgta/'
	}
}

currentPath = os.getcwd()

def getBranch (path):
	os.chdir(path)
	rst = os.popen('git rev-parse --abbrev-ref HEAD 2> /dev/null').read()[0:-1]
	os.chdir(currentPath)
	return rst

def getLastCommit (path):
	os.chdir(path)
	rst = os.popen("git log --pretty=format:'%h -%d %s (%cr) <%an>' --abbrev-commit -1").read()
	os.chdir(currentPath)
	return rst

def getLastDeploy (project):
	rst = os.popen('cat /var/log/deploy/' + project + '.version').read()
	return rst

def getProjects ():
	data = {}
	for (k, v) in PROJECTS.items():
		data[k] = {
			'url': v['url'],
			'branch': getBranch(v['path']),
			'lastDeploy': getLastDeploy(k),
			'lastCommit': getLastCommit(v['path'])
		}
	return data

if __name__ == "__main__":
	print getProjects()

