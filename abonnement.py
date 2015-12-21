#! /usr/bin/python

# -*- coding: utf8 -*-

from base import Base

class Abonnement:

	def __init__(self,idu,idf):
		self.id_utilisateur = idu
		self.id_forum = idf

	def insert(idu,idf):
		base = Base()
		db = base.connection()
		cursor = db.cursor()
		query = "INSERT INTO abonnement VALUES("+idu+","+idf+")"
		lines = cursor.execute(query)
		db.commit()
		data = cursor.fetchall()
		db.close()
		return data

	def delete(idu,idf):
		base = Base()
		db = base.connection()
		cursor = db.cursor()
		query = "DELETE FROM abonnement WHERE id_utilisateur="+idu+" AND id_forum="+idf
		lines = cursor.execute(query)
		db.commit()
		data = cursor.fetchall()
		db.close()
		return data

	def getAllAbonnementsByUser(idu):
		base = Base()
		db = base.connection()
		cursor = db.cursor()
		query = "SELECT * from abonnement WHERE id_utilisateur =" + idu
		lines = cursor.execute(query)
		res = []
		i = 0
		while True:
			row = cursor.fetchone()
			if row == None:
				break
			res[i] = row
			
		db.close()
		return res