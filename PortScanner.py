#!/usr/bin/python

#Socket lib used for devloping netwok tools
from socket import *
# optparse lib used for command line option features
from optparse import  OptionParser
#Threading  lib used for running multiple threads in python
from threading import *






# Defining ConnScan Function
def connScan(tgtHost,tgtPort):
	try:
		sock=socket(AF_INET,SOCK_STREAM)
		sock.connect((tgtHost,tgtPort))
		print ' [+] %d/tcp is Open' %tgtPort
	except: 
		print '[-] %d/tcp is Closed' %tgtPort
	finally:
		sock.close()

#defing PortScan method
def portscan(tgtHost,tgtPorts):
#here we are tying to get  ip from domain , if suppose user enters domain name instead of  host ip address
# gethostbyname   is funtion which is used for get target ip from domain name
	try:
            tgtIP =gethostbyname(tgtHost)
        except:
		print('Unknown Host %s' %tgtHost)

	try:
		tgtName = gethustbyaddr(tgtIP)
		print'[*] Scan Results For: '+tgtName[0]

	except:
		print'[+] Scan Result For: '+tgtIP

#here we are defing timeout for a 1 sec
	setdefaulttimeout(1)
#  creating for loop function  to get "tgtPort" one by one from "tgtPorts"
	for tgtPort in tgtPorts:
# Creating thread to run muliple process at a time
		t = Thread(target=connScan,args=(tgtHost,int(tgtPort)) )

		t.start()













#Defining Main Function
def main():
    parser = OptionParser("Usage of Program:"+ "-H <Target Host> -P <Target Port>")
    parser.add_option("-H",dest="tgthost",help="Target Host")
    parser.add_option("-P",dest="tgtport",help="Target Ports , Use(,)comma to seprate")

 
    (options,args)=parser.parse_args()
##Assigning values to the Variable
    tgtHost=options.tgthost
    tgtPorts=str(options.tgtport).split(',')
#Checking host and port to return usage if  values are null
    if  (tgtHost==None) |(tgtPorts[0] == None):
	    print parser.usage
            exit(0)
#Portscan funtion calling 
    portscan(tgtHost,tgtPorts)

if __name__ == '__main__':
         main()


