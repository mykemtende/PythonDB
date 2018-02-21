#import json
import sqlite3

class People:
	global cur, conn
	conn = sqlite3.connect('db.sqlite')
	cur = conn.cursor()
	cur.execute('''CREATE TABLE IF NOT EXISTS People (idno INTEGER PRIMARY KEY, name TEXT , age INTEGER)''')
	


	def InsertDB(self):
		print('Enter your details below to save in sqliteDB')
		m= raw_input('ID Number: ')
		n = raw_input('Enter name: ')
		a = raw_input('Enter age:  ')
		cur.execute('''INSERT INTO People (idno, name, age) VALUES (?,? , ?)''', (m, n,a))
		conn.commit()


	def ShowDB(self):# data retrieval
		cur.execute('SELECT * FROM People')
		count = 0
		
		print('Database Details')
		for row in cur:
			if count < 5: print(row)
			count = count + 1
			print(count, 'rows.')
			#cur.close()

p= People()
p.InsertDB()
p.ShowDB()
