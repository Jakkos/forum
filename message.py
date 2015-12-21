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
		lines = cursor.execute(query)
		db.commit()
		data = cursor.fetchall()
		db.close()
		return data

	def getAllMessagesByForum(idf):
		base = Base()
		db = base.connection()
		cursor = db.cursor()
		query = "SELECT * from message WHERE id_forum =" + idf
		lines = cursor.execute(query)
		res = []
		i = 0
		while True:
			i =+ 1
			row = cursor.fetchone()
			if row == None:
				break
			res[i] = row
			
		db.close()
		return res