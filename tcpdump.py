import os
import json
import questionary
import time
import re
import ctypes, sys
import webbrowser,getpass
import subprocess
import shutil
from pathlib import Path

path="c:/Users/"+str(getpass.getuser())+"/AppData/Local/temp/pcap"
FileMove="c:/Users/"+str(getpass.getuser())+"/AppData/Local/temp/pcap/PktMon.etl"
Fileout="c:/Users/"+str(getpass.getuser())+"/AppData/Local/temp/pcap/PktMon.pcap"
print(path)
#webbrowser.open(os.path.realpath(path))
try:
    os.mkdir(os.path.realpath(path))
except FileExistsError:
   # webbrowser.open(os.path.realpath(path))
    pass


#webbrowser.open(os.path.realpath(path+'/'+directory))


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

if not is_admin():
    print("\t\t\t\t%%%-----your not admin please run as Admin----%%%%")
    time.sleep(4)
    sys.exit(1)
os.system('pktmon stop')
os.popen('pktmon filter remove')
os.system('cls')
print(style.GREEN + "                        #########interface list#########")
style.WHITE
inter = {'name': [], 'id': [], 'mac': []}
filter = {}
complist = os.popen('pktmon comp list --json')
ifocnfig = os.popen('ipconfig /all | FINDSTR /R "Description* Address.*[0-9][0-9]*\.[0-9][0-9]*\.[0-9][0-9]*\.[0-9][0-9]*"')
inter_list = []
protocol_list = ['TCP','UDP','ICMP']
ipcompile = "^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$"
filter_cmd = []
id_inter = ''

def Counters_Parser(data):
    os.system('cls')
    if len(data) != 0:
        PacketRx = data.split('                ')[1].split()[0]
        BytesRx = data.split('                ')[1].split()[1]
        PacketTx = data.split('                ')[2].split()[0]
        BytesTx = data.split('                ')[2].split()[1]
        filter_status()
        print('to Get the pcap press ctrl+c')
        print(f'PacketRx {PacketRx} PacketTx {PacketTx} BytesRx {BytesRx} BytesTx {BytesTx}')



def host(IP):
    global filter
    if re.search(ipcompile, IP):
        filter['IP'] = IP
    else:
        print('write valid ip')

def port(PORT):
    global filter
    filter['PORT'] = PORT

def PROTOCOL(PROTOCOL):
    global filter
    filter['PROTOCOL'] = PROTOCOL



def run_filter(f):
    os.popen('pktmon filter add Userfilter '+f)


def addfilter():
    os.system('cls')
    global filter,filter_cmd
    filterlist = questionary.checkbox("filter dump [if you select 'ANY' None filters will be apply]",choices=["IP", "PORT", "PROTOCOL", "ANY[will remove all the filter]"]).ask()
    for A in filterlist:
        if "ANY" in filterlist:
            filter.clear()
            os.system('PktMon.exe filter remove')
            break
        else:
            if A == 'IP':
                host(questionary.text("Type Ip").ask())
            elif A == 'PROTOCOL':
                PROTOCOL(questionary.select("choose protocol", choices=protocol_list, ).ask())
            elif A == 'PORT':
                port(questionary.text("Type Port").ask())

    for t in filter.keys():

        if t == 'ID':
            continue
        if t == 'IP':
            filter_cmd.append('-i ' + str(filter[t]))
        if t == 'PROTOCOL':
            filter_cmd.append('-t ' + str(filter[t]))
        if t == 'PORT':
            filter_cmd.append('-p ' + str(filter[t]))


def ipcofig():

    for f in ifocnfig:
        if re.search('Description', f) or re.search('IPv4 Address', f):
            print(str(f).replace('. . . . . . . . . . .', '').replace('           ', ''))

def interlist():
   global inter,complist,id_inter
   j = json.load(complist)
   for t in range(0, len(j)):
       if j[t]['Components'][0]['Properties'][1]['Value'] == 'Ethernet':
           inter['name'].append(j[t]['Components'][0]['Name'])
           inter['id'].append(j[t]['Components'][0]['Id'])
           inter['mac'].append(j[t]['Components'][0]['Properties'][0]['Value'])
   for n in range(0, len(inter['name'])):
       fullname = str(inter['name'][n]) + '_' + str(inter['mac'][n])
       inter_list.append(fullname)

   interface = questionary.select("choose interface", choices=inter_list, ).ask()
   #filter['ID']= inter['id'][inter['name'].index(str(interface).split('_')[0])]
   id_inter = inter['id'][inter['name'].index(str(interface).split('_')[0])]
   #print(id_inter)
   #print(inter)
   time.sleep(2)
   #os.system('cls')

def filter_status():
    filterlist = os.popen('pktmon filter list')
    for f in filterlist.readlines():
        print(f)

ipcofig()
interlist()

def runlive():
    global id_inter
    process = subprocess.Popen('pktmon start  --capture --comp {} --pkt-size 0 -m  real-time'.format(id_inter), stdout=subprocess.PIPE,
                               stderr=subprocess.STDOUT, encoding='utf-8')
    filter_status()
    while True:
        try:
            for line in process.stdout:
                if re.search(':', line):
                    print(line.replace('Collected Data:', '').replace('Capture Type:', '').replace(
                        'Monitored Components:', '').replace('Packet Filters:', ''))
        except KeyboardInterrupt:
            print('stop')
            os.system('cls')
            break

def PcapSave():
    global id_inter
    if Path(os.path.realpath(FileMove)).is_file():
        os.remove(os.path.realpath(FileMove))
        # shutil.move(r'C:\Windows\system32\PktMon.etl', os.path.realpath(FileMove))
    else:
        pass
    if Path(os.path.realpath(Fileout)).is_file():
        os.remove(os.path.realpath(Fileout))
    else:
        pass
        # shutil.move(r'C:\Windows\system32\PktMon.etl', os.path.realpath(FileMove))
    #print('pktmon start  --capture --comp {} --pkt-size 0 -f {}'.format(id_inter,FileMove))
    os.system('pktmon start  --capture --comp {} --pkt-size 0 --file-size 2048 -m circular -f {}'.format(id_inter,os.path.realpath(FileMove)))
    os.system('cls')
    print('the windows will fill when the data start transmit ')
    while True:
        try:
            cmd = ['pktmon', 'counters']
            with subprocess.Popen(cmd, stdout=subprocess.PIPE, bufsize=1, universal_newlines=True,
                                  encoding='utf-8') as p:
                for b in p.stdout:
                    # filter_status()
                    if b is not None:
                        if re.search('Tx', b):
                            Counters_Parser(b)
                        else:
                            continue
            time.sleep(5)
        except KeyboardInterrupt:
            print('Dont Close windows')
            time.sleep(5)
            os.system('cls')
            os.system('pktmon stop')
            os.system('cls')
            print('Dont Close windows')
            os.system('PktMon.exe etl2pcap {} -o {} '.format(os.path.realpath(FileMove),os.path.realpath(Fileout)))
            if Path(os.path.realpath(FileMove)).is_file():
                os.remove(os.path.realpath(FileMove))
            time.sleep(4)
            webbrowser.open(os.path.realpath(path))
            break


def Menu(answer):
    os.system('cls')
    #print(answer)
    if answer == 'Live traffic':
        runlive()
    else:
        PcapSave()


os.system('pktmon stop')
addfilter()
run_filter(' '.join(filter_cmd))
time.sleep(1)
filter.clear()
filter_cmd.clear()
print(os.system('pktmon filter list'))
while questionary.confirm("ADD more filter ?").ask():
    addfilter()
    os.system('cls')
run_filter(' '.join(filter_cmd))
print(os.system('pktmon filter list'))
filter.clear()
filter_cmd.clear()
Menu(questionary.select("What do you want to do?",choices=["Live traffic", "save the pcap to file"], ).ask())
os.system('cls')
#run_filter(filter)
