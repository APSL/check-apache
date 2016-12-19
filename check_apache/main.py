#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author: eherraiz@apsl.net

"""

"""
import logging
import click
import sys
import dns.resolver
from netaddr import *

NAGIOS_CODES = {
    'OK': 0,
    'WARNING': 1,
    'CRITICAL': 2,
    'UNKNOWN': 3,
    'DEPENDENT': 4
}


@click.command()
#@click.option('--network', '-n', multiple=True)
#@click.option('--domain', '-d')
def check():
  # curl http://127.0.0.1/server-status?auto
  print("curl apache-status?auto") 

  #if KO:
  #    print("Error: La Ip {} del dominio {} NO pertenece a ninguna red {}.".format(ip_domain, domain, network))
  #    sys.exit(NAGIOS_CODES['CRITICAL'])
  #print("Las Ip's del dominio {} pertenecen a los rangos especificados {}".format(domain, network))
  #sys.exit(NAGIOS_CODES['OK'])


if __name__ == '__main__':
    check()



