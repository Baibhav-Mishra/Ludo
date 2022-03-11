import mysql.connector
import os
from timeit import default_timer as timer
from datetime import timedelta, date
import cred
import platform
con = mysql.connector.connect(host=cred.host, password=cred.password, user=cred.user, database=cred.database)
cursor = con.cursor()
cursor.execute('Delete from info2')
con.commit()
cursor.execute('Delete from info')
con.commit()
os.system('python Welcome_Screen.py')
cursor.execute("select * from info")
results = cursor.fetchone()

if results is not None:
    if results[0] == 'True':
        start = timer()
        os.system('python main_game.py')
        end = timer()

    f = open('endnote.txt', 'a')
    elapsed_time = timedelta(seconds=end-start)
    f.write(f'Thanks for playing\nElapsed time: {elapsed_time}\nDate: {date.today()} \n \n')
    f.close()

    if platform.system() == 'Darwin':
        os.system("open -a TextEdit endnote.txt")
    elif platform.system() == 'Windows':
        os.system("endnote.txt")
else:
    print("You didn't start the game! ")