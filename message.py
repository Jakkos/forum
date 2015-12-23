#! /usr/bin/python

# -*- coding: utf8 -*-

import time
from base import Base

class Message:

	nb_messages = 0

	def __init__(self,idu,idf,txt):
		Message.nb_messages += 1
		self.id_message = nb_messages
		self.id_utilisateur = idu
		self.id_forum = idf
		self.texte = txt
		self.date_message = time.strftime('%d/%m/%y %H:%M',time.localtime())

	def insert(idu,idf,txt):
		base = Base()
		db = base.connection()
		cursor = db.cursor()
		query = "INSERT INTO message(id_utilisateur,id_forum,texte,date_message) VALUES("+idu+","+idf+","+txt+","+time.strftime('%d/%m/%y %H:%M',time.localtime())+")"
		cursor.execute(query)
		db.commit()
		cursor.close()
		db.close()
		return cursor

	def getAllMessagesByForum(idf):
		base = Base()
		db = base.connection()
		cursor = db.cursor()
		query = "SELECT * from message WHERE id_forum ="+idf
		cursor.execute(query)
		res = []
		j = 0
		for i in cursor:
			res[j] = i
			j += 1
		cursor.close()
		db.close()
		return res