#! /usr/bin/python

# -*- coding: utf8 -*-

from base import Base

class UnForum:

	def __init__(self):
		self.theme = ''

	def insert(self,theme_forum):
		base = Base()
		db = base.connection()
		cursor = db.cursor()
		query = 'INSERT INTO forum(theme) VALUES(\'%s\')'%theme_forum
		cursor.execute(query)
		db.commit()
		cursor.close()
		db.close()
		return cursor

	def getAllForums():
		base = Base()
		db = base.connection()
		cursor = db.cursor()
		query = "SELECT * from forum"
		cursor.execute(query)
		res = []
		j = 0
		for i in cursor:
			res[j] = i
			j += 1
		cursor.close()
		db.close()
		return res