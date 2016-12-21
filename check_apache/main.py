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
@click.option('--threshold', '-t')
def busy_workers(threshold):

  if not threshold:
    threshold = 10
  try:
    r = requests.get("http://127.0.0.1/server-status?auto")
  except:
    print('No se puede leer informacion de status de apache')
    sys.exit(NAGIOS_CODES['WARNING'])
  for l in r.iter_lines():
    attr, value = l.split(": ")
    if attr == 'BusyWorkers':
      if int(value) > int(threshold):
        print('Error: Num. de workers busy por encima del umbral: {} > {}|busy_workers={}'.format(value, threshold, value))
        sys.exit(NAGIOS_CODES['CRITICAL'])
      else:
        print('Num. de workers busy por debajo del umbral: {} < {}|busy_workers={}'.format(value, threshold, value))
        sys.exit(NAGIOS_CODES['OK'])

@click.command()
#@click.option('--network', '-n', multiple=True)
@click.option('--threshold', '-t')
def graceful_workers(threshold):

  if not threshold:
    threshold = 10
  try:
    r = requests.get("http://127.0.0.1/server-status?auto")
  except: 
    print('No se puede leer informacion de status de apache')
    sys.exit(NAGIOS_CODES['WARNING'])
  for l in r.iter_lines():
    attr, value = l.split(": ")
    if attr == 'Scoreboard':
      graceful = value.count('G')
      if graceful > threshold:
        print('Error: Num. de workers graceful por encima del umbral: {} > {}|graceful_workers={}'.format(graceful, threshold, graceful))
        sys.exit(NAGIOS_CODES['CRITICAL'])
      else:
        print('Num. de workers graceful por debajo del umbral: {} < {}|graceful_workers={}'.format(graceful, threshold, graceful))
        sys.exit(NAGIOS_CODES['OK'])

if __name__ == '__main__':
    busy_workers()
    graceful_workers()



