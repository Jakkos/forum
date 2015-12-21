#! /usr/bin/python

# -*- coding: utf8 -*-

import sqlite3

class Base:
	
	def __init__(self):
		self.db = ""

	def connection(self):
		db = sqlite3.connect("db/database.sq3")
		return db