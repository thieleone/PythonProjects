import sqlite3

conn=sqlite3.connect('employee.db')

c=conn.cursor()

c.execute("DROP TABLE employees")

c.execute("""CREATE TABLE employees (
			first text,
			last text,
			pay integer
			)""")

c.execute("INSERT INTO employees VALUES ('Peter','Programmleiter',100000)")

c.execute("SELECT * FROM employees WHERE last='Programmleiter'")

print(c.fetchall())





conn.commit()

conn.close()





