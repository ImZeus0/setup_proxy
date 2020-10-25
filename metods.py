import os
import re
import requests

def get_interface(filename):
	check_interfae = os.path.exists(filename)
	if check_interfae:
		f = open(filename,'r')
		for line in f:
			if line.find('state UP') != -1:
				interfase = line.split(':')[1][1::]
				f.close()
				return interfase
	else:
		return 'No file'


def set_inteface_to_conf(interfase):
	f = open('setup_proxy/danted.conf')
	line = f.read()
	f.close()
	line = line.replace('$',interfase)
	f1 = open('/etc/danted.conf', 'w')
	a = f1.write(line)
	f1.close



def check_proxy():
	f = open('setup_proxy/ip.txt','r')
	ip = f.read()
	f.close()
	is_ip = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$",ip) 
	if len(is_ip) == 1:
		return True
	else:
		return False

def info_proxy():
	r = open('setup_proxy/ip.txt','r')
	ip = r.read()
	r.close()
	url = f'http://ipinfo.io/{ip}/json'
	response = requests.get(url)
	text = response.text
	f = open('setup_proxy/info_proxy.json','w')
	f.write(text)
	f.close()


if __name__ == '__main__':
	choose = int(input())
	if choose == 1:
		interfase = get_interface('setup_proxy/interfase.txt')
		set_inteface_to_conf(interfase)
		print('OK')
	elif choose == 2:
		print(check_proxy())
	elif choose == 3:
		info_proxy()
	else:
		print('ERROR')
		
