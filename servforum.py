#! /usr/bin/python

# -*- coding: utf8 -*-

HOST='127.0.0.1'
PORT=46000

import socket
import sys
import threading
import time






import logging
formatter = logging.Formatter("%(asctime)s -- %(name)s -- %(levelname)s -- %(message)s")
handler_file = logging.FileHandler("save.log",mode = "a",encoding="utf-8")
handler_file.setFormatter(formatter)
handler_file.setLevel(logging.INFO)
logger = logging.getLogger("servforum")
logger.setLevel(logging.INFO)
logger.addHandler(handler_file)

from base import Base
from unforum import UnForum

class ThreadClient(threading.Thread):

	def __init__(self, c):
		threading.Thread.__init__(self)
		self.connexion=c

	def run(self):
	#dialogue avec le client
		nom=self.getName()
		while 1:
			msgClient=self.connexion.recv(1024).decode("Utf8")
			# if msgClient.upper() == "CREATE TABLE\n":
			# 	query0 = "CREATE TABLE forum(id_forum INTEGER PRIMARY KEY AUTOINCREMENT unique,theme CHAR(50) NOT NULL);"
			# 	query1 = "CREATE TABLE utilisateur(id_utilisateur INTEGER PRIMARY KEY AUTOINCREMENT unique,pseudo CHAR(50) NOT NULL,password CHAR(25) NOT NULL);"
			# 	query2 = "CREATE TABLE message(id_message INTEGER PRIMARY KEY AUTOINCREMENT unique,id_utilisateur INTEGER NOT NULL,id_forum INTEGER NOT NULL,texte CHAR(50) NOT NULL,date_message DATETIME NOT NULL,FOREIGN KEY(id_utilisateur) REFERENCES utilisateur(id_utilisateur)FOREIGN KEY(id_forum) REFERENCES forum(id_forum));"
			# 	query3 = "CREATE TABLE abonnement(id_utilisateur INTEGER NOT NULL,id_forum INTEGER NOT NULL,PRIMARY KEY(id_utilisateur,id_forum),FOREIGN KEY(id_utilisateur) REFERENCES utilisateur(id_utilisateur),FOREIGN KEY(id_forum) REFERENCES forum(id_forum));"	
			# 	database = Base()
			# 	db = database.connection()
			# 	cursor0 = db.cursor()
			# 	cursor0.execute(query0)
			# 	cursor1 = db.cursor()
			# 	cursor1.execute(query1)
			# 	cursor2 = db.cursor()
			# 	cursor2.execute(query2)
			# 	cursor3 = db.cursor()
			# 	cursor3.execute(query3)
			# 	db.commit()
			for cle in conn_client:
				 if cle == nom:
				 	client = conn_client[cle]
			if msgClient.upper() == "INSERT FORUM\n":
				database = Base()
				db = database.connection()
				cursor = db.cursor()
				query = "INSERT INTO forum(theme) VALUES('Deuxieme forum')"
				cursor.execute(query)
				db.commit()
			elif msgClient.upper() == "INSERT USER\n":
				database = Base()
				db = database.connection()
				cursor = db.cursor()
				query = "INSERT INTO utilisateur(pseudo,password) VALUES('admin','admin')"
				cursor.execute(query)
				db.commit()
			elif msgClient.upper() == "ALL FORUMS\n":
				database = Base()
				db = database.connection()
				cursor = db.cursor()
				query = "SELECT * FROM forum"
				cursor.execute(query)
				for i in cursor:
					client.send(i[1].encode("Utf8"))
			elif msgClient.upper() == "ALL USERS\n":
				database = Base()
				db = database.connection()
				cursor = db.cursor()
				query = "SELECT * FROM utilisateur"
				cursor.execute(query)
				for i in cursor:
					print i
			# 1- Creer un nouveau forum
			elif msgClient == "1\n":
				msg = "Entrer le theme de votre forum en respectant la synthaxe suivante (newf>La jardinerie c'est ma passion !)\n"
				print date1
				print date2
				logger.info("tentative creation forum")
				client.send(msg.encode("Utf8"))
			# newf>
			elif msgClient[0:5] == "newf>":
				if len(msgClient)<12:
					logger.warning("probleme creation forum (titre)")
					msg = "Erreur, le theme du forum doit contenir au moins 5 caracteres !\nRessayer :"
				else:
					forum = UnForum()
					forum.insert(msgClient[5:len(msgClient)-1])
					logger.info("creation forum : %s",msgClient[5:len(msgClient)-1])
					msg = "Forum cree !\n\nMenu :\n1- Creer un nouveau forum\n2- Afficher tous les forums\n3- Afficher les forums preferes\n4- Se deconnecter\n\nEntrer 1,2,3 ou 4 :"
				client.send(msg.encode("Utf8"))
			# 2- Afficher tous les forums
			elif msgClient == "2\n":
				database = Base()
				db = database.connection()
				cursor = db.cursor()
				query = "SELECT * FROM forum"
				cursor.execute(query)
				for i in cursor:
					client.send(i[1].encode("Utf8"))
			# 4- Se deconnecter
			elif not msgClient or msgClient == "4\n":
				break

			message="%s> %s" % (nom,msgClient)
			print(message)
			# #faire suivre le message aux autres clients
			# for cle in conn_client:
			# 	if cle == nom:
			# 		conn_client[cle].send(message.encode("Utf8"))
# Fermeture de la connexion
		self.connexion.close()
		del conn_client[nom]
		print("Client %s deconnecte." % nom)

# Initialisation
servSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
	servSocket.bind((HOST,PORT))
except socket.error:
	print("La liaison du socket a l'adresse choisie a echoue.")
	sys.exit()
print("Serveur pret, en attente de requetes...")
servSocket.listen(2)

# Attente des connexions clientes
conn_client={}
while 1:
	connexion, adresse = servSocket.accept()
	th=ThreadClient(connexion)
	th.start()
	it=th.getName()
	conn_client[it]=connexion
	print("Client %s connecte, adresse IP %s, port %s." %\
		(it, adresse[0], adresse[1]))
	msg="\nMenu :\n1- Creer un nouveau forum\n2- Afficher tous les forums\n3- Afficher les forums preferes\n4- Se deconnecter\n\nEntrer 1,2,3 ou 4 :" 
	connexion.send(msg.encode("Utf8"))
