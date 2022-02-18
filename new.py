import mysql.connector
import os
from timeit import default_timer as timer
from datetime import timedelta

con = mysql.connector.connect(host="localhost",password="root1234",user="root",database="entry")
cursor = con.cursor()
cursor.execute('Delete from info2')
con.commit()
cursor.execute('Delete from info')
con.commit()
os.system('python Signin_Signup.py')
cursor.execute("select * from info")
results = cursor.fetchone()
if results is not None:
    if results[0] == 'True':
        start = timer()
        os.system('python main.py')
        end = timer()
    f = open('endnote.txt', 'w')
    elapsed_time = timedelta(seconds=end-start)
    f.write(f'Thanks for playing \nElapsed time: {elapsed_time}')
    f.close()
    os.system("endnote.txt")
else:
    print("You didn't start the game!!! ")