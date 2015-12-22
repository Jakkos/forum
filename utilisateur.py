#! /usr/bin/python

# -*- coding: utf8 -*-

from base import Base

class Utilisateur:

	nb_utilisateurs = 0

	def __init__(self):
		self.pseudo = ""
		self.password = ""

	def connection_forum(self,username):
		base = Base()
		db = base.connection()
		cursor = db.cursor()
		query = 'SELECT * FROM utilisateur WHERE pseudo=\'%s\''%username
		cursor.execute(query)
		res = []
		for i in cursor:
			res.append(i)
		db.close()
		return res

	def disconnection_forum(username):
		res = "Merci de votre visite " + username + " ! A bientot !"
		return res

	def insert(self, username,passw):
		base = Base()
		db = base.connection()
		cursor = db.cursor()
		params = (username, passw)
		requete = "INSERT INTO utilisateur(pseudo,password) VALUES(?,?)"
		lines = cursor.execute(requete, params)
		db.commit()
		data = cursor.fetchall()
		db.close()
		return data

	def test():
		base = Base()
		db = base.connection()
		cursor = db.cursor()
		query = "SELECT * FROM utilisateur WHERE pseudo = " + username
		lines = cursor.execute(query)
		while True:
			row = cursor.fetchone()
			if row == None:
				break
		db.close()