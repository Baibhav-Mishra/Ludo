import mysql.connector
import os
from timeit import default_timer as timer
from datetime import timedelta
import cred
import platform
con = mysql.connector.connect(host=cred.host, password=cred.password, user=cred.user, database=cred.database)
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

    if platform.system() == 'Darwin':
        os.system("open -a TextEdit endnote.txt")
    elif platform.system() == 'Windows':
        os.system("endnote.txt")
else:
    print("You didn't start the game! ")