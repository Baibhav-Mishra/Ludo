from Home_Screen import *

'''
create database entry;

create table members(Username varchar(30) primary key,
User_age int, EmailID varchar(50), Password varchar(15),
secret_choice int, secret_pass varchar(60));
'''

# Creates splash screen
splash_root = Tk()

# Adjusts splash screen size
splash_root.geometry("200x100")

# Display Text Message - 'Welcome!' on the screen
splash_label = Label(splash_root, text="Welcome!", font=18)
splash_label.pack()

load_label = Label(splash_root, text="Loading...", font=12, pady=10)
load_label.pack()

occ = 1
count, c = 0, 0


def main():  # main welcome window function

    # destroy splash window only once
    global occ
    while occ == 1:
        splash_root.destroy()
        occ = 0

    def in_screen():  # Sign In Window function
        root.destroy()  # closes main window
        root1 = Tk(className=' '*85+'Sign-In Screen')  # creates sign in screen
        root1.iconbitmap('ludo_icon.ico')
        canvas2 = Canvas(root1, width=700, height=400, bg='#00FFBC')  # creates a canvas on the screen on which
        canvas2.grid(columnspan=6, rowspan=15)  # we can add gadgets

        user = Label(root1, text='Enter Username:', font=('SF Pro Display Bold', 20), fg='blue', bg='#00FFBC')
        user.grid(row=4, column=2)

        e1 = Entry(root1, borderwidth=5)  # creates a field for us to enter details
        e1.grid(row=4, column=3)

        passwd = Label(root1, text='Enter Password:', font=('SF Pro Display Bold', 20), fg='blue', bg='#00FFBC')
        passwd.grid(row=8, column=2)

        e2 = Entry(root1, borderwidth=5, show='*')
        e2.grid(row=8, column=3)

        def blankntype_in(a, b):  # function to check if fields are empty
            flag = 0
            dt = [a, b]
            for i in dt:
                if len(i[0]) == 0:
                    messagebox.showerror('Python Error', 'Error: Field {0} Empty'.format(i[1]))
                    flag = 1
                    break
            return flag

        def check():  # checks for all details whether correctly entered or not
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
                            if y2[0] == j[0]:  # checks if entered password matches with database or not
                                root1.destroy()  # closes sign in window
                                home_screen(y1[0])  # opens the main home window after sign in
                                break
                            else:
                                messagebox.showerror('Python Error', 'Error: Password entered does not match')
                                break
                        break
                else:
                    messagebox.showerror('Python Error', 'Error: Username entered does not exist')

        def forgot_screen(z):  # to confirm our identity with security choice
            pass_root = Tk(className=' ' * 60 + 'Forgot Password')
            pass_root.iconbitmap('ludo_icon.ico')
            pass_canvas = Canvas(pass_root, width=550, height=350, bg='#00FFBC')
            pass_canvas.grid(columnspan=7, rowspan=8)

            reset = Label(pass_root, text='Confirm Your Identity', font=('SF Pro Display Bold', 20), fg='blue',
                          bg='#00FFBC')
            reset.grid(row=0, column=1, columnspan=5)

            secure_choice = Label(pass_root, text='Choose any one option:', font=('SF Pro Display Bold', 20), fg='blue',
                                  bg='#00FFBC')
            secure_choice.grid(row=3, column=2)
            OPTIONS = [
                "Favourite Food",
                "Favourite Place",
                "Lucky Number"
            ]

            variable = StringVar(pass_root)
            variable.set('Favourite Food')
            w = OptionMenu(pass_root, variable, *OPTIONS)
            w.grid(row=3, column=3)

            def change_pass(z):  # to change password
                change_root = Tk(className=' ' * 60 + 'Change Password')
                change_root.iconbitmap('ludo_icon.ico')
                change_canvas = Canvas(change_root, width=550, height=350, bg='#00FFBC')
                change_canvas.grid(columnspan=7, rowspan=10)

                initial_passwd = Label(change_root, text='Enter New Password:', font=('SF Pro Display Bold', 20),
                                       fg='blue',
                                       bg='#00FFBC')
                initial_passwd.grid(row=3, column=2)
                e4 = Entry(change_root, borderwidth=5)
                e4.grid(row=3, column=3)

                confirm_passwd = Label(change_root, text='Confirm New Password:', font=('SF Pro Display Bold', 20),
                                       fg='blue',
                                       bg='#00FFBC')
                confirm_passwd.grid(row=5, column=2)
                e5 = Entry(change_root, borderwidth=5)
                e5.grid(row=5, column=3)

                def check_pass(z):  # to update password
                    if e4.get() == e5.get():
                        t = (e5.get(), z)
                        mycursor.execute('update members set Password = %s where Username = %s', t)
                        con.commit()
                        messagebox.showinfo('Congratulations!',
                                            'Your password has been updated! Please close the current '
                                            'window to return to Welcome Screen')
                        # return e4.get()
                    else:
                        messagebox.showerror('Python Error', 'Error: Both Password Do not match')

                pass_checked = Button(change_root, text='Enter', width=9, height=1, bg='grey', borderwidth=1,
                                      font=('SF Pro Display Bold', 15), command=lambda: check_pass(z))
                pass_checked.grid(row=8, column=2, columnspan=2)

                change_root.bind('<Return>', lambda event: check_pass(z))

            def secure_pass(x, z):  # to enter security password
                pass_root.destroy()

                def update_pass(g, x):  # to check security password
                    global c
                    t = (x,)
                    mycursor.execute('select secret_pass from members where secret_choice = %s', t)
                    while True:
                        for i in mycursor:
                            if g == i[0]:
                                secure_root.destroy()
                                change_pass(z)
                                break
                        else:
                            messagebox.showerror('Python Error', 'Error: Incorrect Security Password')
                            c += 1
                            if c == 5:
                                messagebox.showerror('Python Error', 'Error: Maximum number of tries exhausted. '
                                                                     'The application will restart. \nPlease Try again')
                                secure_root.destroy()
                        break

                secure_root = Tk(className=' ' * 65 + 'Security Check')
                secure_root.iconbitmap('ludo_icon.ico')
                change_canvas = Canvas(secure_root, width=550, height=250, bg='#00FFBC')
                change_canvas.grid(columnspan=7, rowspan=5)
                secure_passwd = Label(secure_root, text='Enter Security Password:', font=('SF Pro Display Bold', 20),
                                      fg='blue', bg='#00FFBC')
                secure_passwd.grid(row=2, column=2)
                e = Entry(secure_root, borderwidth=5)
                e.grid(row=2, column=3)
                secure_checked = Button(secure_root, text='Enter', width=9, height=1, bg='grey', borderwidth=1,
                                        font=('SF Pro Display Bold', 15), command=lambda: update_pass(e.get(), x))
                secure_checked.grid(row=4, column=2, columnspan=2)

                secure_root.bind('<Return>', lambda event: update_pass(e.get(), x))

            def check():  # to enter and check security choice
                global count
                y2 = variable.get()
                t = (z,)
                mycursor.execute('select secret_choice from members where Username = %s', t)
                a = mycursor.fetchone()
                d = {'Favourite Food': 1, 'Favourite Place': 2, 'Lucky Number': 3}
                while True:
                    if d[y2] == a[0]:
                        secure_pass(d[y2], z)
                        break
                    else:
                        messagebox.showerror('Python Error', 'Error: Incorrect Option Chosen')
                        count += 1
                        if count == 2:
                            messagebox.showerror('Python Error', 'Error: Maximum number of tries exhausted. '
                                                                 'The application will restart. \nPlease Try again')
                            pass_root.destroy()
                        break

            secure_check = Button(pass_root, text='Enter', width=9, height=1, bg='grey', borderwidth=1,
                                  font=('SF Pro Display Bold', 15), command=check)
            secure_check.grid(row=7, column=2, columnspan=2)

            pass_root.bind('<Return>', lambda event: check())

            mainloop()

        def forgot_clicked():  # function when 'forgot password' is pressed

            u_n = e1.get()  # gets the username from username field
            if u_n == '':
                messagebox.showerror('Python Error', 'Error: Username Field Is Empty')
            else:
                mycursor.execute('select Username from members')
                for i in mycursor:
                    if u_n == i[0]:
                        root1.destroy()
                        forgot_screen(u_n)  # runs forgot_pass function
                        main()  # main runs again after password has changed (even if not)
                        break
                else:
                    messagebox.showerror('Python Error', 'Error: Username Entered Does Not Exist')

        login1 = Button(root1, text='Enter', width=9, height=1, bg='grey', borderwidth=1,
                        font=('SF Pro Display Bold', 15), command=check)
        login1.grid(row=12, column=1, columnspan=2)

        root1.bind('<Return>', lambda event: check())  # using enter key to proceed

        reset_pass = Button(root1, text='forgot password', width=15, bg='#00FFBC', borderwidth=0,
                            font=('SF Pro Display Bold', 10, 'italic'), command=forgot_clicked)
        reset_pass.grid(row=13, column=2, columnspan=2)

        def back_clicked():  # to go back to Welcome Screen
            root1.destroy()
            main()
        back1 = Button(root1, text='Go Back', width=9, height=1, bg='grey', borderwidth=1,
                       font=('SF Pro Display Bold', 15), command=back_clicked)
        back1.grid(row=12, column=3)

    def up_screen():  # Sign up Window function
        root.destroy()

        root1 = Tk(className=' '*100+'Sign Up Screen')  # creates sign-up screen
        root1.iconbitmap('ludo_icon.ico')
        canvas3 = Canvas(root1, width=800, height=600, bg='#00FFBC')  # creates the canvas on screen on which
        canvas3.grid(columnspan=6, rowspan=25)  # we add gadgets

        user = Label(root1, text='Enter Username:', font=('SF Pro Display Bold', 20), fg='blue', bg='#00FFBC')
        user.grid(row=2, column=2)
        e1 = Entry(root1, borderwidth=5)
        e1.grid(row=2, column=3)

        user_age = Label(root1, text='Enter Age:', font=('SF Pro Display Bold', 20), fg='blue', bg='#00FFBC')
        user_age.grid(row=4, column=2)
        e2 = Entry(root1, borderwidth=5)
        e2.grid(row=4, column=3)

        user_mail = Label(root1, text='Enter Email ID:', font=('SF Pro Display Bold', 20), fg='blue', bg='#00FFBC')
        user_mail.grid(row=6, column=2)
        e3 = Entry(root1, borderwidth=5)
        e3.grid(row=6, column=3)

        # warn = Label(root1, text='WARNING!: Password should not be more than 15 characters',
        #              font=('SF Pro Display Bold', 10), fg='blue', bg='#00FFBC')
        # warn.grid(row=8, column=1, columnspan=4)

        initial_passwd = Label(root1, text='Enter Password:', font=('SF Pro Display Bold', 20), fg='blue',
                               bg='#00FFBC')
        initial_passwd.grid(row=8, column=2)
        e4 = Entry(root1, borderwidth=5, show='*')
        e4.grid(row=8, column=3)

        confirm_passwd = Label(root1, text='Confirm Password:', font=('SF Pro Display Bold', 20), fg='blue',
                               bg='#00FFBC')
        confirm_passwd.grid(row=10, column=2)
        e5 = Entry(root1, borderwidth=5, show='*')
        e5.grid(row=10, column=3)

        secure_choice = Label(root1, text='Choose any one option*:', font=('SF Pro Display Bold', 20), fg='blue',
                              bg='#00FFBC')
        secure_choice.grid(row=12, column=2)

        OPTIONS = [
            "Favourite Food",
            "Favourite Place",
            "Lucky Number"
        ]

        variable = StringVar(root1)
        variable.set('Favourite Food')
        w = OptionMenu(root1, variable, *OPTIONS)
        w.grid(row=12, column=3)

        secure_pass = Label(root1, text='Enter Security Password*:', font=('SF Pro Display Bold', 20), fg='blue',
                            bg='#00FFBC')
        secure_pass.grid(row=14, column=2)
        e6 = Entry(root1, borderwidth=5)
        e6.grid(row=14, column=3)

        secure_info = Label(root1, text='* Please note that these fields are necessary for security purposes while '
                                        'resetting password. Choose wisely!', font=('SF Pro Display Bold', 10),
                            fg='blue', bg='#00FFBC')
        secure_info.grid(row=22, column=1, columnspan=4)

        def blankntype(a, b, c, d, e, f):  # function to check for field's emptiness and the value's datatypes
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

        def check():  # function to check for credibility of values entered
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

                if len(y1[0]) > 15:
                    messagebox.showerror('Python Error', 'Error: Username Length exceeds 15 characters limit')
                    f1 = 1

                elif '@' not in y3[0] or '.com' not in y3[0]:
                    messagebox.showerror('Python Error', 'Error: Email ID format is incorrect')
                    f1 = 1

                elif len(y4[0]) > 15:
                    messagebox.showerror('Python Error', 'Error: Password Length exceeds 15 characters limit')
                    f1 = 1

                elif d[y6] == 3:
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
                        font=('SF Pro Display Bold', 15), command=check)
        login2.grid(row=19, column=2)

        root1.bind('<Return>', lambda event: check())

        # when back button is clicked
        def back_clicked():
            root1.destroy()
            main()

        back2 = Button(root1, text='Go Back', width=9, height=1, bg='grey', borderwidth=1,
                       font=('SF Pro Display Bold', 15), command=back_clicked)
        back2.grid(row=19, column=3)

    root = Tk()
    root.title(' '*103+'Welcome Screen')  # creates main welcome screen
    root.iconbitmap('ludo_icon.ico')  # adds ludo icon to the title bar

    canvas1 = Canvas(root, width=800, height=500, bg='#00FFBC')
    canvas1.grid(columnspan=4, rowspan=20)

    game_name = Label(root, text='LUDO', font=('SF Pro Display Bold', 50), fg='blue', bg='#00FFBC')
    game_name.grid(row=1, column=1, columnspan=2)

    greet = Label(root, text='WELCOME!', font=('SF Pro Display Bold', 30), fg='blue', bg='#00FFBC')
    greet.grid(row=3, column=1, columnspan=2)

    signin = Button(root, text='Sign-In', width=9, height=1, bg='grey', borderwidth=1,
                    font=('SF Pro Display Bold', 15), command=in_screen)  # sign in button
    signin.grid(row=6, column=1)

    signup = Button(root, text='Sign Up', width=9, height=1, bg='grey', borderwidth=1,
                    font=('SF Pro Display Bold', 15), command=up_screen)  # sign-up button
    signup.grid(row=6, column=2)

    stop = Button(root, text='Exit The Game', command=root.destroy, bg='red', fg='white')  # button to close the app
    stop.grid(row=19, column=3, columnspan=3)


splash_root.after(2000, main)  # splash screen lasts for 2 sec then opens main welcome screen
mainloop()  # runs tkinter windows infinitely
