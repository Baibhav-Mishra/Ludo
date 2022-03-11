from tkinter import Button, Label, Entry, Canvas, mainloop, PhotoImage, Tk, StringVar, OptionMenu
from tkinter import messagebox
import mysql.connector
import cred


con = mysql.connector.connect(host=cred.host, password=cred.password, user=cred.user, database=cred.database)
mycursor = con.cursor(buffered=True)


final_val = []


def try_new(num):  # to enter other players' names
    root1 = Tk(className=' ' * 85 + 'Player Names')
    root1.iconbitmap('ludo_icon.ico')
    canvas2 = Canvas(root1, width=700, height=400, bg='#00FFBC')
    canvas2.grid(columnspan=6, rowspan=15)
    if num == 2:
        user1 = Label(root1, text='Enter player - {0} name:'.format(2), font=('SF Pro Display Bold', 20), fg='blue', bg='#00FFBC')
        user1.grid(row=3, column=2)
        e1 = Entry(root1, borderwidth=5)
        e1.grid(row=3, column=3)

        def blank_type():  # to check for 2nd player's fields
            y1 = e1.get()
            global final_val
            if len(y1) == 0:
                messagebox.showerror('Python Error', 'Error: Username Field is Empty')
            else:
                final_val.append(y1)
                run(num)

        login1 = Button(root1, text='Enter', width=9, height=1, bg='grey', borderwidth=1,
                        font=('SF Pro Display Bold', 15), command=blank_type)
        login1.grid(row=12, column=1, columnspan=2)

        root1.bind('<Return>', lambda event: blank_type())  # using enter key to proceed

    if num == 3:
        user1 = Label(root1, text='Enter player - {0} name:'.format(2), font=('SF Pro Display Bold', 20), fg='blue', bg='#00FFBC')
        user1.grid(row=3, column=2)
        e1 = Entry(root1, borderwidth=5)
        e1.grid(row=3, column=3)

        user2 = Label(root1, text='Enter player - {0} name:'.format(3), font=('SF Pro Display Bold', 20), fg='blue',
                     bg='#00FFBC')
        user2.grid(row=5, column=2)
        e2 = Entry(root1, borderwidth=5)
        e2.grid(row=5, column=3)

        def blank_type():  # to check for other players' fields
            y1 = e1.get()
            y2 = e2.get()
            global final_val
            if len(y1) == 0 or len(y2) == 0:
                messagebox.showerror('Python Error', 'Error: Username Field is Empty')
            else:
                final_val.append(y1)
                final_val.append(y2)
                run(num)

        login1 = Button(root1, text='Enter', width=9, height=1, bg='grey', borderwidth=1,
                        font=('SF Pro Display Bold', 15), command=blank_type)
        login1.grid(row=12, column=1, columnspan=2)

        root1.bind('<Return>', lambda event: blank_type())  # using enter key to proceed

    if num == 4:
        user1 = Label(root1, text='Enter player - {0} name:'.format(2), font=('SF Pro Display Bold', 20), fg='blue', bg='#00FFBC')
        user1.grid(row=3, column=2)
        e1 = Entry(root1, borderwidth=5)
        e1.grid(row=3, column=3)

        user2 = Label(root1, text='Enter player - {0} name:'.format(3), font=('SF Pro Display Bold', 20), fg='blue',
                     bg='#00FFBC')
        user2.grid(row=5, column=2)
        e2 = Entry(root1, borderwidth=5)
        e2.grid(row=5, column=3)

        user3 = Label(root1, text='Enter player - {0} name:'.format(4), font=('SF Pro Display Bold', 20), fg='blue',
                      bg='#00FFBC')
        user3.grid(row=7, column=2)
        e3 = Entry(root1, borderwidth=5)
        e3.grid(row=7, column=3)

        def blank_type():  # to check for other players' fields
            y1 = e1.get()
            y2 = e2.get()
            y3 = e3.get()
            global final_val
            if len(y1) == 0 or len(y2) == 0 or len(y3) == 0:
                messagebox.showerror('Python Error', 'Error: Username Field is Empty')
            else:
                final_val.append(y1)
                final_val.append(y2)
                final_val.append(y3)
                run(num)

        login1 = Button(root1, text='Enter', width=9, height=1, bg='grey', borderwidth=1,
                        font=('SF Pro Display Bold', 15), command=blank_type)
        login1.grid(row=12, column=1, columnspan=2)

        root1.bind('<Return>', lambda event: blank_type())  # using enter key to proceed

    def back_clicked():  # to go back to Welcome Screen
        root1.destroy()
        pass

    back1 = Button(root1, text='Go Back', width=9, height=1, bg='grey', borderwidth=1,
                   font=('SF Pro Display Bold', 15), command=back_clicked)
    back1.grid(row=12, column=3)


# to add other player names and start the game
def run(number):
    global name
    if number == 2:
        mycursor.execute('''insert into info2 values({0},"{1}","{2}","{3}","{4}")'''.format(number, name, "Player3", final_val[0], "Player4"))
        con.commit()
        mycursor.execute(f'insert into info values("True")')
        con.commit()
        exit()
    elif number == 3:
        mycursor.execute('''insert into info2 values({0},"{1}","{2}","{3}","{4}")'''.format(number, name, final_val[0], final_val[1], "Player4"))
        con.commit()
        mycursor.execute(f'insert into info values("True")')
        con.commit()
        exit()
    elif number == 4:
        mycursor.execute('''insert into info2 values({0},"{1}","{2}","{3}","{4}")'''.format(number, name, final_val[0], final_val[1], final_val[2]))
        con.commit()
        mycursor.execute(f'insert into info values("True")')
        con.commit()
        exit()


name = ''


def home_screen(x):  # Creates main home window
    global name
    name = x
    # pass_root.destroy()
    home_root = Tk(className=' ' * 105 + 'Home Screen')  # creates home screen
    home_root.iconbitmap('ludo_icon.ico')
    home_canvas = Canvas(home_root, width=800, height=550, bg='#00FFBC')
    home_canvas.grid(columnspan=8, rowspan=45)

    greet1 = Label(home_root, text='Home Screen', font=('SF Pro Display Bold', 30), fg='blue', bg='#00FFBC')
    greet1.grid(row=2, column=2, columnspan=4)

    greet2 = Label(home_root, text='Hello {}!'.format(x), font=('SF Pro Display Bold', 22), fg='blue', bg='#00FFBC')
    greet2.grid(row=3, column=2, columnspan=4)

    bg = PhotoImage(file='Assets/Boards/board300px.png')
    ludo = Label(home_root, image=bg)
    ludo.grid(row=5, column=2, columnspan=4)

    p2 = Button(home_root, text='2 Player', width=9, height=1, bg='grey', borderwidth=1,
                font=('SF Pro Display Bold', 15), command=lambda: try_new(2))
    p2.grid(row=27, column=1, columnspan=2)

    p3 = Button(home_root, text='3 Player', width=9, height=1, bg='grey', borderwidth=1,
                font=('SF Pro Display Bold', 15), command=lambda: try_new(3))
    p3.grid(row=27, column=3, columnspan=2)

    p4 = Button(home_root, text='4 Player', width=9, height=1, bg='grey', borderwidth=1,
                font=('SF Pro Display Bold', 15), command=lambda: try_new(4))
    p4.grid(row=27, column=5, columnspan=2)

    def setting_screen():  # creates setting window
        set_root = Tk(className=' ' * 39 + 'Settings Screen')
        set_root.iconbitmap('ludo_icon.ico')
        # set_root.geometry('400x300+{}+{}'.format(int(set_root.winfo_screenwidth() / 2 - set_root.winfo_reqwidth() / 2),
        #                   int(set_root.winfo_screenheight() / 2 - set_root.winfo_reqheight() / 2)))
        set_canvas = Canvas(set_root, width=400, height=300, bg='#00FFBC')
        set_canvas.grid(columnspan=5, rowspan=4)

        head = Label(set_root, text='Settings', font=('SF Pro    Display Bold', 20), fg='blue', bg='#00FFBC')
        head.grid(row=0, column=2)

        def signing_out():  # to sign out and close game
            ques = messagebox.askyesno('Warning', 'Do you really want to sign out?')
            if ques:
                messagebox.showinfo('Signing Out', 'Thank you for playing the game!')
                set_root.destroy()
                home_root.destroy()

        out = Button(set_root, text='Sign Out', width=14, height=1, bg='grey', borderwidth=1,
                     font=('SF Pro Display Bold', 15), command=signing_out)
        out.grid(row=2, column=2)

        def del_acc():  # to delete account and close game
            ques = messagebox.askyesno('Warning', 'Do you really want to delete your account?')
            if ques:
                tup = (x,)
                mycursor.execute('delete from members where Username = %s', tup)
                messagebox.showinfo('Account Deleted', 'Your account has been deleted. The application will close now.')
                con.commit()
                set_root.destroy()
                home_root.destroy()

        delete_acc = Button(set_root, text='Delete Account', width=14, height=1, bg='grey', borderwidth=1,
                            font=('SF Pro Display Bold', 15), command=del_acc)
        delete_acc.grid(row=1, column=2)

    sett = PhotoImage(file='Assets/Icon/settings_64.png')

    setting = Button(home_root, image=sett, bg='#00FFBC', borderwidth=0, command=setting_screen)
    setting.grid(row=2, column=7, columnspan=2)

    close = PhotoImage(file='Assets/Icon/close_48.png')

    stop = Button(home_root, image=close, command=home_root.destroy, bg='#00FFBC', borderwidth=0)
    stop.grid(row=27, column=7, columnspan=2)

    mainloop()


# count, c = 0, 0
#
#
# def forgot_screen(z):  # to confirm our identity with security choice
#     pass_root = Tk(className=' ' * 60 + 'Forgot Password')
#     pass_root.iconbitmap('ludo_icon.ico')
#     pass_canvas = Canvas(pass_root, width=550, height=350, bg='#00FFBC')
#     pass_canvas.grid(columnspan=7, rowspan=8)
#
#     reset = Label(pass_root, text='Confirm Your Identity', font=('SF Pro Display Bold', 20), fg='blue', bg='#00FFBC')
#     reset.grid(row=0, column=1, columnspan=5)
#
#     secure_choice = Label(pass_root, text='Choose any one option:', font=('SF Pro Display Bold', 20), fg='blue',
#                           bg='#00FFBC')
#     secure_choice.grid(row=3, column=2)
#     OPTIONS = [
#         "Favourite Food",
#         "Favourite Place",
#         "Lucky Number"
#     ]
#
#     variable = StringVar(pass_root)
#     variable.set('Favourite Food')
#     w = OptionMenu(pass_root, variable, *OPTIONS)
#     w.grid(row=3, column=3)
#
#     def change_pass(z):  # to change password
#         change_root = Tk(className=' ' * 60 + 'Change Password')
#         change_root.iconbitmap('ludo_icon.ico')
#         change_canvas = Canvas(change_root, width=550, height=350, bg='#00FFBC')
#         change_canvas.grid(columnspan=7, rowspan=10)
#
#         initial_passwd = Label(change_root, text='Enter New Password:', font=('SF Pro Display Bold', 20), fg='blue',
#                                bg='#00FFBC')
#         initial_passwd.grid(row=3, column=2)
#         e4 = Entry(change_root, borderwidth=5)
#         e4.grid(row=3, column=3)
#
#         confirm_passwd = Label(change_root, text='Confirm New Password:', font=('SF Pro Display Bold', 20), fg='blue',
#                                bg='#00FFBC')
#         confirm_passwd.grid(row=5, column=2)
#         e5 = Entry(change_root, borderwidth=5)
#         e5.grid(row=5, column=3)
#
#         def check_pass(z):  # to update password
#             if e4.get() == e5.get():
#                 t = (e5.get(), z)
#                 mycursor.execute('update members set Password = %s where Username = %s', t)
#                 con.commit()
#                 messagebox.showinfo('Congratulations!', 'Your password has been updated! Please close the current '
#                                                         'window to return to Welcome Screen')
#                 # return e4.get()
#             else:
#                 messagebox.showerror('Python Error', 'Error: Both Password Do not match')
#
#         pass_checked = Button(change_root, text='Enter', width=9, height=1, bg='grey', borderwidth=1,
#                               font=('SF Pro Display Bold', 15), command=lambda: check_pass(z))
#         pass_checked.grid(row=8, column=2, columnspan=2)
#
#         change_root.bind('<Return>', lambda event: check_pass(z))
#
#     def secure_pass(x, z):  # to enter security password
#         pass_root.destroy()
#
#         def update_pass(g, x):  # to check security password
#             global c
#             t = (x,)
#             mycursor.execute('select secret_pass from members where secret_choice = %s', t)
#             while True:
#                 for i in mycursor:
#                     if g == i[0]:
#                         secure_root.destroy()
#                         change_pass(z)
#                         break
#                 else:
#                     messagebox.showerror('Python Error', 'Error: Incorrect Security Password')
#                     c += 1
#                     if c == 5:
#                         messagebox.showerror('Python Error', 'Error: Maximum number of tries exhausted. '
#                                                              'The application will restart. \nPlease Try again')
#                         secure_root.destroy()
#                 break
#
#         secure_root = Tk(className=' ' * 65 + 'Security Check')
#         secure_root.iconbitmap('ludo_icon.ico')
#         change_canvas = Canvas(secure_root, width=550, height=250, bg='#00FFBC')
#         change_canvas.grid(columnspan=7, rowspan=5)
#         secure_passwd = Label(secure_root, text='Enter Security Password:', font=('SF Pro Display Bold', 20),
#                               fg='blue', bg='#00FFBC')
#         secure_passwd.grid(row=2, column=2)
#         e = Entry(secure_root, borderwidth=5)
#         e.grid(row=2, column=3)
#         secure_checked = Button(secure_root, text='Enter', width=9, height=1, bg='grey', borderwidth=1,
#                                 font=('SF Pro Display Bold', 15), command=lambda: update_pass(e.get(), x))
#         secure_checked.grid(row=4, column=2, columnspan=2)
#
#         secure_root.bind('<Return>', lambda event: update_pass(e.get(), x))
#
#     def check():  # to enter and check security choice
#         global count
#         y2 = variable.get()
#         t = (z,)
#         mycursor.execute('select secret_choice from members where Username = %s', t)
#         a = mycursor.fetchone()
#         d = {'Favourite Food': 1, 'Favourite Place': 2, 'Lucky Number': 3}
#         while True:
#             if d[y2] == a[0]:
#                 secure_pass(d[y2], z)
#                 break
#             else:
#                 messagebox.showerror('Python Error', 'Error: Incorrect Option Chosen')
#                 count += 1
#                 if count == 2:
#                     messagebox.showerror('Python Error', 'Error: Maximum number of tries exhausted. '
#                                                          'The application will restart. \nPlease Try again')
#                     pass_root.destroy()
#                 break
#
#     secure_check = Button(pass_root, text='Enter', width=9, height=1, bg='grey', borderwidth=1,
#                           font=('SF Pro Display Bold', 15), command=check)
#     secure_check.grid(row=7, column=2, columnspan=2)
#
#     pass_root.bind('<Return>', lambda event: check())
#
#     mainloop()
