#! /usr/bin/python

# -*- coding: utf8 -*-

from base import Base
import datetime

ts = time.time()


dateMoinsUneHeure = datetime.date.today() - datetime.timedelta(hours=1)
dateMoinsUneHeureTimestamp = dateMoinsUneHeure.strftime("%s")



class Abonnement:

	def __init__(self,idu,idf,lv):
		self.id_utilisateur = idu
		self.id_forum = idf
		self.last_visite = lv

	def insert(idu,idf,lv):
		base = Base()
		db = base.connection()
		cursor = db.cursor()
		query = "INSERT INTO abonnement VALUES("+idu+","+idf+","+lv+")"
		cursor.execute(query)
		db.commit()
		cursor.close()
		db.close()
		return cursor

	def getAllAbonements():
		base = Base()
		db = base.connection()
		cursor = db.cursor()
		query = "SELECT * from abonnement"
		cursor.execute(query)
		res = []
		j = 0
		for i in cursor:
			res[j] = i
			j += 1
		cursor.close()
		db.close()
		return res

	def delete(idu,idf):
		base = Base()
		db = base.connection()
		cursor = db.cursor()
		query = "DELETE FROM abonnement WHERE id_utilisateur="+idu+" AND id_forum="+idf
		cursor.execute(query)
		db.commit()
		cursor.close()
		db.close()
		return cursor

	def getAllAbonnementsByUser(idu):
		base = Base()
		db = base.connection()
		cursor = db.cursor()
		query = "SELECT * from abonnement WHERE id_utilisateur ="+idu
		cursor.execute(query)
		res = []
		j = 0
		for i in cursor:
			res[j] = i
			j += 1
		cursor.close()
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
		cursor.execute(query)
		res = []
		j = 0
		for i in cursor:
			res[j] = i
			j += 1
		cursor.close()
		db.close()
		return res
		"""
