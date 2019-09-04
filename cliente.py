#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Pyro4



uri = input("URI Object ").strip()
sim = True
while (sim == True):
  pergunta = input("Deseja uma nova etiqueta sim/nao").strip()	

  numero_aleatorio = Pyro4.Proxy(uri)
  print(numero_aleatorio.etiqueta())
  if(pergunta == 'sim'):
   sim = True
  else:
   sim = False



