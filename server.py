import Pyro4
import random

@Pyro4.expose



class Aleatorio(object):
  
  def etiqueta(self):
   global contador
   cont = contador
   contador = contador + 1

   return "%03d" % cont


Pyro4.config.HOST = '127.0.0.1'

contador = 001 

daemon = Pyro4.Daemon()
uri = daemon.register(Aleatorio)

print("Ready.object uri =", uri)
daemon.requestLoop()
		
