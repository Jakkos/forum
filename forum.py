#! /usr/bin/python

# -*- coding: utf8 -*-

HOST='127.0.0.1'
PORT=46000

import socket
import sys
import threading
from base import Base
from utilisateur import Utilisateur

class ThreadReception(threading.Thread):
	def __init__(self,conn):
		threading.Thread.__init__(self)
		self.connexion=conn

	def run(self):
		while True:
			msgrecu=self.connexion.recv(1024).decode("Utf8")
			print(msgrecu)
			if not msgrecu or msgrecu.upper()=="FIN\n":
				break
		# th_E._stop()
		print("Client arrete, connexion interrompue.")
		self.connexion.close()

class ThreadEmission(threading.Thread):
	def __init__(self,conn):
		threading.Thread.__init__(self)
		self.connexion=conn

	def run(self):
		while True:
			msge=sys.stdin.readline()
			self.connexion.send(msge.encode("Utf8"))
			# Si le dernier message est 4 donc deconnexion, on arrete le thread
			if msge and msge == "4\n":
				break
# Test des arguments
# 3 arguments : -p pseudo password
if len(sys.argv) != 4:
	print 'Echec, le nombre d arguments est incorrect.\nPour vous connecter, vous devez respecter la synthaxe suivante :\npython forum.py -p votrePseudo votreMotDePasse'
	sys.exit(1)
# Verification du premier argument -p
if sys.argv[1] != '-p':
	print 'Echec, le premier argument <',sys.argv[1],'> n est pas correct.\nPour vous connecter, vous devez respecter la synthaxe suivante :\npython forum.py -p votrePseudo votreMotDePasse'
	sys.exit(1)
# Verification du deuxieme et du troisieme argument (login/password)
utilisateur = Utilisateur()
res = utilisateur.connection_forum(sys.argv[2])
if len(res) == 0:
	print 'Echec, le pseudo renseigne est incorrect.'
	sys.exit(1)
else:
	password = res[0][2]
	if sys.argv[3] != password:
		print 'Echec, le mot de passe est incorrect.'
		sys.exit(1)
# Connexion au socket
connexion=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
try:
	connexion.connect((HOST,PORT))
except socket.error:
	print("Echec de connexion.\nLe serveur n'est peut etre pas demarre !")
	sys.exit()
print("Connecte au serveur.\nBonjour %s"%sys.argv[2])
# Execution des Threads
th_E=ThreadEmission(connexion)
th_R=ThreadReception(connexion)
th_E.start()
th_R.start()