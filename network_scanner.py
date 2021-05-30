#!/usr/bin/env python

from scapy.all import *


def scan(ip):
    arp_request = scapy.all.ARP(pdst=ip)
    print(arp_request.summary())

    #Comando que lista os campos que podemos mudar, nesse caso da classe ARP
    # scapy.all.ls(scapy.all.ARP())


scan("192.168.15.10")
