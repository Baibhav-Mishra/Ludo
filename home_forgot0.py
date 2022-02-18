from tkinter import Button, Label, Entry, Canvas, mainloop, PhotoImage, Tk, StringVar, OptionMenu
from tkinter import messagebox
import mysql.connector
import cred


con = mysql.connector.connect(host=cred.host, password=cred.password, user=cred.user, database=cred.database)
mycursor = con.cursor(buffered=True)



def try_new():
    final_val = ""
    root1 = Tk(className=' ' * 85 + 'Player Names')
    canvas2 = Canvas(root1, width=700, height=400, bg='#00FFBC')
    canvas2.grid(columnspan=6, rowspan=15)
    while True:
        user = Label(root1, text='Enter player-{} name:'.format(1), font=('Fira Code SemiBold', 20), fg='blue', bg='#00FFBC')
        user.grid(row=4, column=2)
        e1 = Entry(root1, borderwidth=5)
        e1.grid(row=4, column=3)

        def blank_type(a):
            global final_val
            if len(a) == 0:
                messagebox.showerror('Python Error', 'Error: Field {0} Empty'.format(a))
            else:
                return final_val
        y1 = (e1.get(), 'Enter Username: ')
        login1 = Button(root1, text='Enter', width=9, height=1, bg='grey', borderwidth=1,
                        font=('Fira Code SemiBold', 15), command=lambda : blank_type(y1))
        login1.grid(row=12, column=1, columnspan=2)

        root1.bind('<Return>', lambda event: blank_type(y1))  # using enter key to proceed

        def back_clicked():  # to go back to Welcome Screen
            root1.destroy()
            # main()
            pass
        back1 = Button(root1, text='Go Back', width=9, height=1, bg='grey', borderwidth=1,
                       font=('Fira Code SemiBold', 15), command=back_clicked)
        back1.grid(row=12, column=3)













def run(number):
    # a=try_new()
    mycursor.execute(f'insert into info2 values({number},"B","A","L","A")')
    con.commit()
    mycursor.execute(f'insert into info values("True")')
    con.commit()
    exit()

def home_screen(x):
    # pass_root.destroy()
    home_root = Tk(className=' ' * 80 + 'Home Screen')
    home_root.iconbitmap('ludoicon.ico')
    home_canvas = Canvas(home_root, width=650, height=500, bg='#00FFBC')
    home_canvas.grid(columnspan=8, rowspan=45)

    def multi_options(x):
        if x == 'Y':
            opt_root = Tk(className=' ')
            opt_root.iconbitmap('ludoicon.ico')
            opt_root.geometry('+{}+{}'.format(int(opt_root.winfo_screenwidth()/2-opt_root.winfo_reqwidth()/2),
                                              int(opt_root.winfo_screenheight()/2-opt_root.winfo_reqheight()/2)))
            opt_canvas = Canvas(opt_root, width=200, height=200, bg='#00FFBC')
            opt_canvas.grid(columnspan=1, rowspan=6)

            opts = Label(opt_root, text='Multiplayer Options:', font=('Fira Code SemiBold', 10), fg='blue', bg='#00FFBC')
            opts.grid(row=1, column=0)

            p2 = Button(opt_root, text='2 Player', width=13, height=1, bg='grey', borderwidth=1,
                        font=('Fira Code SemiBold', 15), command=lambda: run(2))
            p2.grid(row=2, column=0)

            p3 = Button(opt_root, text='3 Player', width=13, height=1, bg='grey', borderwidth=1,
                        font=('Fira Code SemiBold', 15),command=lambda: run(3))
            p3.grid(row=3, column=0)

            p4 = Button(opt_root, text='4 Player', width=13, height=1, bg='grey', borderwidth=1,
                        font=('Fira Code SemiBold', 15),command=lambda: run(4))
            p4.grid(row=4, column=0)


    greet1 = Label(home_root, text='Home Screen', font=('Fira Code SemiBold', 30), fg='blue', bg='#00FFBC')
    greet1.grid(row=2, column=2, columnspan=4)

    greet2 = Label(home_root, text='Hello {}!'.format(x), font=('Fira Code', 28), fg='blue', bg='#00FFBC')
    greet2.grid(row=3, column=2, columnspan=4)

    bg = PhotoImage(file='ludo.png')
    ludo = Label(home_root, image=bg)
    ludo.grid(row=5, column=2, columnspan=4)

    single = Button(home_root, text='Single Player', width=13, height=1, bg='grey', borderwidth=1,
                    font=('Fira Code SemiBold', 15))
    single.grid(row=27, column=3)

    multi = Button(home_root, text='Multiplayer', width=13, height=1, bg='grey', borderwidth=1,
                   font=('Fira Code SemiBold', 15), command=lambda: multi_options('Y'))
    multi.grid(row=27, column=4)

    def setting_screen():
        set_root = Tk(className=' ' * 39 + 'Settings Screen')
        set_root.iconbitmap('ludoicon.ico')
        set_root.geometry('400x300+{}+{}'.format(int(set_root.winfo_screenwidth() / 2 - set_root.winfo_reqwidth() / 2),
                          int(set_root.winfo_screenheight() / 2 - set_root.winfo_reqheight() / 2)))
        set_canvas = Canvas(set_root, width=400, height=300, bg='#00FFBC')
        set_canvas.grid(columnspan=5, rowspan=4)

        head = Label(set_root, text='Settings', font=('Fira Code SemiBold', 20), fg='blue', bg='#00FFBC')
        head.grid(row=0, column=2)

        def signing_out():
            ques = messagebox.askyesno('Warning', 'Do you really want to sign out?')
            if ques:
                messagebox.showinfo('Signing Out', 'Thank you for playing the game!')
                set_root.destroy()
                home_root.destroy()

        out = Button(set_root, text='Sign Out', width=14, height=1, bg='grey', borderwidth=1,
                     font=('Fira Code SemiBold', 15), command=signing_out)
        out.grid(row=2, column=2)

        def del_acc():
            ques = messagebox.askyesno('Warning', 'Do you really want to delete your account?')
            if ques:
                tup = (x,)
                mycursor.execute('delete from members where Username = %s', tup)
                messagebox.showinfo('Account Deleted', 'Your account has been deleted. The application will close now.')
                con.commit()
                set_root.destroy()
                home_root.destroy()

        delete_acc = Button(set_root, text='Delete Account', width=14, height=1, bg='grey', borderwidth=1,
                            font=('Fira Code SemiBold', 15), command=del_acc)
        delete_acc.grid(row=1, column=2)

    sett = PhotoImage(file='settings_64.png')

    setting = Button(home_root, image=sett, bg='#00FFBC', borderwidth=0, command=setting_screen)
    setting.grid(row=2, column=6, columnspan=2)

    close = PhotoImage(file='close_48.png')

    stop = Button(home_root, image=close, command=home_root.destroy, bg='#00FFBC', borderwidth=0)
    stop.grid(row=27, column=6, columnspan=2)

    mainloop()


count, c = 0, 0


def forgot_screen(z):
    # pass_root.destroy()
    pass_root = Tk(className=' ' * 60 + 'Forgot Password')
    pass_root.iconbitmap('ludoicon.ico')
    pass_canvas = Canvas(pass_root, width=550, height=350, bg='#00FFBC')
    pass_canvas.grid(columnspan=7, rowspan=8)

    reset = Label(pass_root, text='Confirm Your Identity', font=('Fira Code SemiBold', 20), fg='blue', bg='#00FFBC')
    reset.grid(row=0, column=1, columnspan=5)
    '''
    user = Label(pass_root, text='Enter Username:', font=('Fira Code SemiBold', 20), fg='blue', bg='#00FFBC')
    user.grid(row=3, column=2)
    e1 = Entry(pass_root, borderwidth=5)
    e1.grid(row=3, column=3)
    '''
    secure_choice = Label(pass_root, text='Choose any one option:', font=('Fira Code SemiBold', 20), fg='blue',
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
        change_root.iconbitmap('ludoicon.ico')
        change_canvas = Canvas(change_root, width=550, height=350, bg='#00FFBC')
        change_canvas.grid(columnspan=7, rowspan=10)

        initial_passwd = Label(change_root, text='Enter New Password:', font=('Fira Code SemiBold', 20), fg='blue',
                               bg='#00FFBC')
        initial_passwd.grid(row=3, column=2)
        e4 = Entry(change_root, borderwidth=5)
        e4.grid(row=3, column=3)

        confirm_passwd = Label(change_root, text='Confirm New Password:', font=('Fira Code SemiBold', 20), fg='blue',
                               bg='#00FFBC')
        confirm_passwd.grid(row=5, column=2)
        e5 = Entry(change_root, borderwidth=5)
        e5.grid(row=5, column=3)

        def check_pass(z):
            if e4.get() == e5.get():
                t = (e5.get(), z)
                mycursor.execute('update members set Password = %s where Username = %s', t)
                con.commit()
                messagebox.showinfo('Congratulations!', 'Your password has been updated! Please close the current '
                                                        'window to return to Welcome Screen')
                # return e4.get()
            else:
                messagebox.showerror('Python Error', 'Error: Both Password Do not match')

        pass_checked = Button(change_root, text='Enter', width=9, height=1, bg='grey', borderwidth=1,
                              font=('Fira Code SemiBold', 15), command=lambda: check_pass(z))
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
        secure_root.iconbitmap('ludoicon.ico')
        change_canvas = Canvas(secure_root, width=550, height=250, bg='#00FFBC')
        change_canvas.grid(columnspan=7, rowspan=5)
        secure_passwd = Label(secure_root, text='Enter Security Password:', font=('Fira Code SemiBold', 20),
                              fg='blue', bg='#00FFBC')
        secure_passwd.grid(row=2, column=2)
        e = Entry(secure_root, borderwidth=5)
        e.grid(row=2, column=3)
        secure_checked = Button(secure_root, text='Enter', width=9, height=1, bg='grey', borderwidth=1,
                                font=('Fira Code SemiBold', 15), command=lambda: update_pass(e.get(), x))
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
                          font=('Fira Code SemiBold', 15), command=check)
    secure_check.grid(row=7, column=2, columnspan=2)

    pass_root.bind('<Return>', lambda event: check())

    mainloop()
