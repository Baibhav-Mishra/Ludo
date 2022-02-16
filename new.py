# import mysql.connector
import os
from timeit import default_timer as timer
from datetime import timedelta

# con = mysql.connector.connect(host="localhost",password="root1234",user="root",database="Ludo")
# cursor = con.cursor()
# os.system('python Signin_Signup.py')
# cursor.execute("select * from info2")
# results = cursor.fetchone()
# print(results)
#
# if results[0] == 'True':
#     os.system('python main.py')
start = timer()
os.system('python main.py')
end = timer()
f = open('endnote.txt', 'w')
elapsed_time = timedelta(seconds=end-start)
f.write(f'Thanks for playing \nElapsed time: {elapsed_time}')
f.close()
os.system('open -a TextEdit endnote.txt')
