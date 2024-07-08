import pyodbc

con_str = 'Driver={{Microsoft Access Driver (*.mdb, *.accdb)}};Dbq={0};'.format(r"C:\Users\ok230195\PycharmProjects\English_communication_Xreading_record\Xreading.accdb")
conn = pyodbc.connect(con_str)
cur = conn.cursor()

def show_access(table_name):
   query = f'SELECT * FROM {table_name}'
   cur.execute(query)
   for row in cur.fetchall():
      print(row)

show_access('2年前期達成状況')