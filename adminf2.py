#!/usr/bin/env python
# -*- coding: utf-8 -*-
#####################################################
import os                                           #
import urllib2                                      #
import random                                       #
import sys                                          #
import time                                         #
import datetime                                     #
from termcolor import colored, cprint               #
import requests                                     #
from bs4 import BeautifulSoup                       #
                                                    #
#COLOR                                              #
G = "\033[0;32m"                                    #
GI = "\033[0;32;3m"                                 #
B = "\033[0;36;1m"                                  #
BI = "\033[0;36;3m"                                 #
R = "\033[0;31m"                                    #
RI = "\033[31;3m"                                   #
Y = "\033[33;1m"                                    #
YI = "\033[33;1;3m"                                 #
W = "\033[37;1m"                                    #
WI = "\033[37;1;3m"                                 #
N = "\033[0m"                                       #
NI = "\033[0;3m"                                    #
#####################################################

os.system('clear')
banner="""
       d888       88             d8b           
      d8888       88             Y8P        888888888     ╳
     d8P888       88                        888          ╱█╲
    d8P 888  .d88888 000b.d000b. 888 8888b. 888888      ╱▓▓▓╲
   d88  888 d8b   88 888"888"888 888 88 "8b 888        ╱▒▒▒▒▒╲      
 d888888888 Y8b   88 888 '8' 888 888 88  88 888     ╔════════════╗   
d88P   8888  "Y88888 888  :  888 888 88  88 888     ╠═By System╳═╣             
═════════════════════════════════════════════════════════════════╝                                                              
"""
Finish="""
╔═════════════════════════════════════════╗
╠════════════════> DONE! <════════════════╣
╚═════════════════════════════════════════╝
"""
Int=000
while os.path.exists('/home/sysx/Public/tmp/Result_{0}.txt'.format(Int)): 
    Int+=1
f=open('/home/sysx/Public/tmp/Result_{0}.txt'.format(Int),'a')
f.close()
print(BI+''+str(banner)+N)
try:
    print (YI+'Enter link/Ip addr without'+RI+' [http:// or https://]\n'+N)
    # target= raw_input(N+'Link/Ip addr: '+G)
    target='bit.ly'
    print(GI+''+str(target)+N)
except (IndexError,ValueError):
    print (YI+'Enter link/Ip addr without'+RI+' [http:// or https://]'+N)
    # target=raw_input(W+'Link/Ip addr: '+N)
    target='bit.ly'
    print(GI+''+str(target)+N)
except KeyboardInterrupt:
    print ('\n'+YI+'CLEAN UP...'+N)
    time.sleep(1)
    print ('\n'+BI+'Bye :)'+N)
    time.sleep(2)
    os.system('clear')
    sys.exit()
    print ("\n")
def Start():
    try:
        Request_File=raw_input(N+'File Location: '+N)
        File= open(Request_File, 'r')
        kontent= File.read()
        x =kontent.split('\n')
        print('\n')
    except (IOError, IndexError):
        print (YI+'NO SUCH FILE OR DIRECTORY!'+N)
        time.sleep(1)
        Request_File=raw_input(N+'File Location: '+N)
        File= open(Request_File, 'r')
        kontent= File.read()
        x =kontent.split('\n')
        print('\n')
    except KeyboardInterrupt:
        print ('\n'+YI+'CLEAN UP...'+N)
        time.sleep(1)
        print ('\n'+BI+'Bye :)'+N)
        time.sleep(2)
        os.system('clear')
        sys.exit()
        print ("\n")
    try:
        SaveFile=raw_input(W+'Do u want to save?'+W+'['+GI+'Y'+W+'/'+NI+'n'+W+']: '+N)
        print('\n')
        StartTime = datetime.datetime.now()
        for i in x:
            url = target+"/"+i
            StatusCode = requests.get('https://'+str(url)).status_code
            Page = requests.get('https://' +str(url))
            Soup = BeautifulSoup(Page.text, 'html.parser')

            def StatusCodeOk():
                print (G+'[+] '+G+'GRANTED  ' +W+ '| ' +G+''+str(StatusCode)+W+' | '+G+'' +url+''+N)
                try:
                    Cheking_For_Text = Soup.find('div', class_='freebirdFormviewerViewResponseMessage').text
                    print(G+' ╚> '+Y+'(?) ' +W+'>> ' +NI+''+str(Cheking_For_Text)+N)
                except AttributeError:
                    Cheking_NoText = Soup.find('div', class_='freebirdFormviewerViewResponseMessage')
                    print(G+' ╚> '+Y+'(?) ' +W+'>> ' +NI+''+str(Cheking_NoText)+N)
            def Failure():
                print (W+'['+R+'-'+W+']'+R+' DENIED   '+W+'| ' +R+''+str(StatusCode)+W+' | ' +R+''+url+''+N)
            try:
                if StatusCode == 200:
                    StatusCodeOk()
                    try:
                        Cheking_For_Text = Soup.find('div', class_= 'freebirdFormviewerViewHeaderTitle exportFormTitle freebirdCustomFont').text
                        print(G+' ╚> '+G+'(✔)'+W+' >> '+NI+''+str(Cheking_For_Text)+'\033[0m'+N)
                        f=open('/home/sysx/Public/tmp/Result_{0}.txt'.format(Int),'a')
                        f.write('http://'+str(url) +' >> '+str(Cheking_For_Text)+'\n')
                        f.close()
                    except AttributeError:
                        Cheking_NoText = Soup.find('div', class_= 'freebirdFormviewerViewHeaderTitle exportFormTitle freebirdCustomFont')
                        print(G+' ╚> '+G+'(✔)'+W+' >> '+NI+''+str(Cheking_NoText)+'\033[0m'+N)
                elif StatusCode == 200:
                    StatusCodeOk()
                    try:
                        Cheking_For_Text = Soup.find('div', class_='freebirdFormviewerViewHeaderTitleRow').text
                        print(G+' ╚> '+NI+''+str(Cheking_NoText)+N)
                    except AttributeError:
                        Cheking_NoText = Soup.find('div', class_='freebirdFormviewerViewHeaderTitleRow')#.text
                        print(G+' ╚> '+NI+''+str(Cheking_NoText)+N)
                else:
                    Failure()
            except KeyboardInterrupt as e:
                print ('\n'+BI+'Bye :)'+N)
            
    except KeyboardInterrupt as e:
        print ('\n'+BI+'Bye :)'+N)
        print ("\n")
    except EOFError:
        print (YI+'ERROR!'+N)
    except requests.exceptions.ConnectionError:
        print ("\n")
        print (YI+'Connections maybe not safe!'+N)
        pass
    except IOError:
        print (YI+'NO SUCH FILE OR DIRECTORY!'+N)
        time.sleep(2) 
    finally:
        cprint(Finish, 'green', attrs=['blink'])
        print ("\n")
        try:
            print(W+'Final results:\n'+N)
            f=open('/home/sysx/Public/tmp/Result_{0}.txt'.format(Int),'r')
            print(f.read())
            if SaveFile in ('y','Y'):
                print(W+'Was saved in '+NI+'/home/sysx/Public/tmp/Result_{0}.txt\n'.format(Int)+N)
                pass
            elif SaveFile in ('n','N'):
                if os.path.exists("/home/sysx/Public/tmp/Result_{0}.txt".format(Int)):
                  os.remove("/home/sysx/Public/tmp/Result_{0}.txt".format(Int))
                else:
                  print("The file does not exist")
            else:
                pass
        except (IOError):
            print (YI+'NO SUCH FILE OR DIRECTORY!, or maybe not created'+N)
        except KeyboardInterrupt:
            print ('\n'+BI+'Bye :)'+N)
            print ("\n")
        Ending = datetime.datetime.now()
        EndOfTime = Ending - StartTime
        print(NI+'\n\t\t\t\tTotal Time: '+BI+'{0}''\n'+N).format(EndOfTime)
        try:
            Asking=raw_input(W+'Do u want to scan again?'+W+'['+GI+'Y'+W+'/'+NI+'n\033[0m'+W+']'': '+N)
            if Asking in ('y', 'Y'):
                Start()
            elif Asking in ('n', 'N'):
                print ('\n'+BI+'Bye :)'+N)
                sys.exit()
                print ("\n")
            else:
                Start()
        except KeyboardInterrupt as e:
            print ('\n'+BI+'Bye :)'+N)
            print ("\n")
if __name__ == '__main__':
    Start()