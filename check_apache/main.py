#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author: eherraiz@apsl.net

"""

"""
import logging
import click
import sys
import requests


NAGIOS_CODES = {
    'OK': 0,
    'WARNING': 1,
    'CRITICAL': 2,
    'UNKNOWN': 3,
    'DEPENDENT': 4
}


@click.command()
#@click.option('--network', '-n', multiple=True)
@click.option('--busy_workers', '-b')
def check(busy_workers):
  # curl http://127.0.0.1/server-status?auto
  r = requests.get("http://127.0.0.1/server-status?auto")
  for l in r.iter_lines():
    attr, value = l.split(": ")
    if attr == 'BusyWorkers':
      print('Busy: {}'.format(value))
      if value > busy_workers:
        print('Error: Num. de workers_busy: {} - Por encima del umbral: {}'.format(value, busy_workers))
        sys.exit(NAGIOS_CODES['CRITICAL'])

  #if KO:
  #    print("Error: La Ip {} del dominio {} NO pertenece a ninguna red {}.".format(ip_domain, domain, network))
  #    sys.exit(NAGIOS_CODES['CRITICAL'])
  #print("Las Ip's del dominio {} pertenecen a los rangos especificados {}".format(domain, network))
  #sys.exit(NAGIOS_CODES['OK'])


if __name__ == '__main__':
    check()



