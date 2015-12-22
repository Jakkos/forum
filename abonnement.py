#! /usr/bin/python

# -*- coding: utf8 -*-

from base import Base
import datetime

ts = time.time()


dateMoinsUneHeure = datetime.date.today() - datetime.timedelta(hours=1)
dateMoinsUneHeureTimestamp = dateMoinsUneHeure.strftime("%s")



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


"""  Ici c'est la fonction qui va récuperer la liste des forums ou l'utilisateur possède des messages non lus
	Sachant qu'un forum dont le message non lu est un forum qui se trouve dans abonnement et dont la date dans last_visite est inférieur à la date actuelle.
	utiliser la variable ts définie plus haut pour récupérer le temps actuel qui sera à comparer avec la date de l'utilisateur.

	def getAllForumAboNonLus(idu):
		base=Base()
		db=base.connection()
		cursor=db.cursor()
		query="SELECT id_forum from abonnement WHERE id_utilisateur="+idu+" AND last_visite<getdate"
		lines = cursor.execute(query)
		res=[]
		i=0
		while True:
			row=cursor.fetchone()
			if row=None:
				break
			res[i] = row

		db.close()
		return res
		"""
