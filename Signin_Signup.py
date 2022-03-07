from home_forgot import *

'''
create database entry;

create table members(Username varchar(30) primary key,
User_age int, EmailID varchar(50), Password varchar(15),
secret_choice int, secret_pass varchar(60));
'''

# Create object
splash_root = Tk()

# Adjust size
splash_root.geometry("200x100")

# Set Label
splash_label = Label(splash_root, text="Welcome!", font=18)
splash_label.pack()

load_label = Label(splash_root, text="Loading...", font=12, pady=10)
load_label.pack()

occ = 1
y = ''


def main():  # main window function
    # destroy splash window only once

    global occ
    while occ == 1:
        splash_root.destroy()
        occ = 0

    def in_screen():  # Sign In Window function
        root.destroy()
        root1 = Tk(className=' '*85+'Sign-In Screen')
        canvas2 = Canvas(root1, width=700, height=400, bg='#00FFBC')
        canvas2.grid(columnspan=6, rowspan=15)

        user = Label(root1, text='Enter Username:', font=('Fira Code SemiBold', 20), fg='blue', bg='#00FFBC')
        user.grid(row=4, column=2)
        e1 = Entry(root1, borderwidth=5)
        e1.grid(row=4, column=3)
        # y1 = e1.get()
        passwd = Label(root1, text='Enter Password:', font=('Fira Code SemiBold', 20), fg='blue', bg='#00FFBC')
        passwd.grid(row=8, column=2)
        e2 = Entry(root1, borderwidth=5, show='*')
        e2.grid(row=8, column=3)

        def blankntype_in(a, b):
            flag = 0
            dt = [a, b]
            for i in dt:
                if len(i[0]) == 0:
                    messagebox.showerror('Python Error', 'Error: Field {0} Empty'.format(i[1]))
                    flag = 1
                    break
            return flag

        def check():
            y1 = (e1.get(), 'Enter Username: ')
            y2 = (e2.get(), 'Enter Password: ')
            verify = blankntype_in(y1, y2)
            if verify == 0:
                mycursor.execute('select Username from members')
                for i in mycursor:
                    if y1[0] == i[0]:
                        t = (y1[0],)
                        mycursor.execute('select Password from members where Username = %s', t)
                        for j in mycursor:
                            if y2[0] == j[0]:
                                print('Worked')
                                root1.destroy()
                                home_screen(y1[0])  # open the main window here
                                break
                            else:
                                messagebox.showerror('Python Error', 'Error: Password entered does not match')
                                break
                        break
                else:
                    messagebox.showerror('Python Error', 'Error: Username entered does not exist')

        def forgot_clicked():  # when forgot password is pressed
            global y
            y = e1.get()
            if y == '':
                messagebox.showerror('Python Error', 'Error: Username Field Is Empty')
            else:
                mycursor.execute('select Username from members')
                for i in mycursor:
                    if y == i[0]:
                        root1.destroy()
                        forgot_screen(y)  # from home_forgot0.py
                        main()
                        break
                else:
                    messagebox.showerror('Python Error', 'Error: Username Entered Does Not Exist')

        login1 = Button(root1, text='Enter', width=9, height=1, bg='grey', borderwidth=1,
                        font=('Fira Code SemiBold', 15), command=check)
        login1.grid(row=12, column=1, columnspan=2)

        root1.bind('<Return>', lambda event: check())  # using enter key to proceed

        reset_pass = Button(root1, text='forgot password', width=15, bg='#00FFBC', borderwidth=0,
                            font=('Fira Code SemiBold', 10, 'italic'), command=forgot_clicked)
        reset_pass.grid(row=13, column=2, columnspan=2)

        def back_clicked():  # to go back to Welcome Screen
            root1.destroy()
            main()
        back1 = Button(root1, text='Go Back', width=9, height=1, bg='grey', borderwidth=1,
                       font=('Fira Code SemiBold', 15), command=back_clicked)
        back1.grid(row=12, column=3)

    def up_screen():  # Sign up Window function
        root.destroy()

        root1 = Tk(className=' '*100+'Sign Up Screen')
        canvas3 = Canvas(root1, width=800, height=600, bg='#00FFBC')
        canvas3.grid(columnspan=6, rowspan=25)

        user = Label(root1, text='Enter Username:', font=('Fira Code SemiBold', 20), fg='blue', bg='#00FFBC')
        user.grid(row=2, column=2)
        e1 = Entry(root1, borderwidth=5)
        e1.grid(row=2, column=3)

        user_age = Label(root1, text='Enter Age:', font=('Fira Code SemiBold', 20), fg='blue', bg='#00FFBC')
        user_age.grid(row=4, column=2)
        e2 = Entry(root1, borderwidth=5)
        e2.grid(row=4, column=3)

        user_mail = Label(root1, text='Enter Email ID:', font=('Fira Code SemiBold', 20), fg='blue', bg='#00FFBC')
        user_mail.grid(row=6, column=2)
        e3 = Entry(root1, borderwidth=5)
        e3.grid(row=6, column=3)

        warn = Label(root1, text='WARNING!: Password should not be more than 15 characters',
                     font=('Arial', 10), fg='blue', bg='#00FFBC')
        warn.grid(row=8, column=1, columnspan=4)

        initial_passwd = Label(root1, text='Enter Password:', font=('Fira Code SemiBold', 20), fg='blue', bg='#00FFBC')
        initial_passwd.grid(row=9, column=2)
        e4 = Entry(root1, borderwidth=5)
        e4.grid(row=9, column=3)

        confirm_passwd = Label(root1, text='Confirm Password:', font=('Fira Code SemiBold', 20), fg='blue',
                               bg='#00FFBC')
        confirm_passwd.grid(row=11, column=2)
        e5 = Entry(root1, borderwidth=5)
        e5.grid(row=11, column=3)

        secure_info = Label(root1, text='Please note that the fields below are necessary for security purposes while '
                            'resetting password. Choose wisely!', font=('Arial', 10), fg='blue', bg='#00FFBC')
        secure_info.grid(row=13, column=1, columnspan=4)

        secure_choice = Label(root1, text='Choose any one option:', font=('Fira Code SemiBold', 20), fg='blue',
                              bg='#00FFBC')
        secure_choice.grid(row=14, column=2)

        OPTIONS = [
            "Favourite Food",
            "Favourite Place",
            "Lucky Number"
        ]

        variable = StringVar(root1)
        variable.set('Favourite Food')
        w = OptionMenu(root1, variable, *OPTIONS)
        w.grid(row=14, column=3)

        secure_pass = Label(root1, text='Enter Security Password:', font=('Fira Code SemiBold', 20), fg='blue',
                            bg='#00FFBC')
        secure_pass.grid(row=16, column=2)
        e6 = Entry(root1, borderwidth=5)
        e6.grid(row=16, column=3)

        def blankntype(a, b, c, d, e, f):
            flag = 0
            dt = [a, b, c, d, e, f]
            for i in dt:
                if len(i[0]) == 0:
                    messagebox.showerror('Python Error', 'Error: Field {0} Empty'.format(i[1]))
                    flag = 1
                    break
            if not b[0].isdigit() and flag == 0:
                messagebox.showerror('Python Error', 'Error: Datatype not matched with the given '
                                     'field {0}.'.format(b[1]))
                flag = 1
            return flag

        def check():
            y1 = (e1.get(), 'Enter Username')
            y2 = (e2.get(), 'Enter Age')
            y3 = (e3.get(), 'Enter Email ID')
            y4 = (e4.get(), 'Enter Password')
            y5 = (e5.get(), 'Confirm Password')
            y6 = variable.get()
            y7 = (e6.get(), 'Security Password')

            x = blankntype(y1, y2, y3, y4, y5, y7)
            if x == 0 and y4[0] == y5[0]:
                d = {'Favourite Food': 1, 'Favourite Place': 2, 'Lucky Number': 3}
                f1 = 0
                if d[y6] == 3:
                    if not y7[0].isdigit():
                        messagebox.showerror('Python Error', "Error: Datatype not matched with the given field "
                                             "'Security Password' based on the field 'Choose any one option'.")
                        f1 = 1
                else:
                    if not y7[0].isalpha():
                        messagebox.showerror('Python Error', "Error: Datatype not matched with the given field "
                                             "'Security Password' based on the field 'Choose any one option'.")
                        f1 = 1

                mycursor.execute('select Username from members')
                for i in mycursor:
                    if y1[0] == i[0] and f1 == 0:
                        messagebox.showerror('Python Error', 'Error: Username has already been taken')
                        break
                else:
                    if f1 == 0:
                        val = (y1[0], int(y2[0]), y3[0], y5[0], d[y6], y7[0])
                        mycursor.execute('insert into members values(%s,%s,%s,%s,%s,%s)', val)
                        con.commit()
                        messagebox.showinfo('Data Inserted', 'Congratulations! Your details have been added '
                                                             'to our database')
                        root1.destroy()
                        home_screen(y1[0])
            if y4[0] != y5[0] and x == 0:
                messagebox.showerror('Python Error', 'Error: Password Do not match')

        login2 = Button(root1, text='Enter', width=9, height=1, bg='grey', borderwidth=1,
                        font=('Fira Code SemiBold', 15), command=check)
        login2.grid(row=20, column=2)

        root1.bind('<Return>', lambda event: check())

        # when back button is clicked
        def back_clicked():
            root1.destroy()
            main()

        back2 = Button(root1, text='Go Back', width=9, height=1, bg='grey', borderwidth=1,
                       font=('Fira Code SemiBold', 15), command=back_clicked)
        back2.grid(row=20, column=3)

    root = Tk()
    root.title(' '*103+'Welcome Screen')
    root.iconbitmap('ludo_icon.ico')

    canvas1 = Canvas(root, width=800, height=500, bg='#00FFBC')
    canvas1.grid(columnspan=4, rowspan=20)

    name = Label(root, text='LUDO', font=('Arial', 50), fg='blue', bg='#00FFBC')
    name.grid(row=1, column=1, columnspan=2)

    greet = Label(root, text='WELCOME!', font=('Arial', 30), fg='blue', bg='#00FFBC')
    greet.grid(row=3, column=1, columnspan=2)

    signin = Button(root, text='Sign-In', width=9, height=1, bg='grey', borderwidth=1,
                    font=('Fira Code SemiBold', 15), command=in_screen)
    signin.grid(row=6, column=1)

    signup = Button(root, text='Sign Up', width=9, height=1, bg='grey', borderwidth=1,
                    font=('Fira Code SemiBold', 15), command=up_screen)
    signup.grid(row=6, column=2)

    stop = Button(root, text='Exit The Game', command=root.destroy, bg='red', fg='white')
    stop.grid(row=19, column=3, columnspan=3)


splash_root.after(2000, main)
mainloop()
