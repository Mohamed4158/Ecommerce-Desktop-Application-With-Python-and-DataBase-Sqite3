from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox, ttk
from db import Database


def product():
    from PIL import Image, ImageTk
    laptops = Toplevel()
    laptops.geometry('1250x630+5+5')
    laptops.resizable(False, False)
    laptops.title('Laptops')
    laptops.config(bg='#d9d9d9')
    laptops.iconbitmap('D:\\project\\icons\\laptop.ico')

    # laptopProductsLbl
    laptopProductsLbl = Label(laptops, text='Laptop Products', bg='#00cc00', font='Arial 20')
    laptopProductsLbl.pack(fill=X)

    # cart
    # open img
    cart = Image.open("D:\\project\\images\\cart.png")
    # resize img
    resizedCart = cart.resize((30, 30), Image.ANTIALIAS)
    newCart = ImageTk.PhotoImage(resizedCart)
    cartLbl = Button(laptops, image=newCart, command=cartf)
    cartLbl.place(x=1180, y=2)

    # frame
    fr = Frame(laptops, width='1200', height='560', bg='#f2f2f2')
    fr.pack(pady=20)
    # ---------------------------------------------------------------------
    # ---------------------------------------------------------------------

    # frame Apple
    fr1 = Frame(fr, width='250', height='250', bg='#ffffff')
    fr1.place(x=40, y=20)
    apple = Image.open("D:\\project\\images\\products\\apple.jpg")
    # resize img
    resizedApple = apple.resize((250, 160), Image.ANTIALIAS)
    newApple = ImageTk.PhotoImage(resizedApple)
    appleLbl = Label(fr1, image=newApple)
    appleLbl.place(x=0, y=0)

    # applelbl
    appleLbl = Label(fr1, text='MacBook Air: Apple M2', bg='white', font='arial 12')
    appleLbl.place(x=45, y=185)

    # applebtn
    appleBtn = Button(fr1, text='ADD', bg='white', width='10', font='arial 10')
    appleBtn.place(x=75, y=215)

    # ---------------------------------------------------------------------
    # frame HP
    fr2 = Frame(fr, width='250', height='250', bg='#ffffff')
    fr2.place(x=40, y=290)
    hp1 = Image.open("D:\\project\\images\\products\\hp.jpg")
    # resize img
    resizedHP1 = hp1.resize((250, 160), Image.ANTIALIAS)
    newHP1 = ImageTk.PhotoImage(resizedHP1)
    HP1Lbl = Label(fr2, image=newHP1)
    HP1Lbl.place(x=0, y=0)

    # applelbl
    Hp1Lbl = Label(fr2, text='HP 15 Core i5-1135G', bg='white', font='arial 12')
    Hp1Lbl.place(x=45, y=185)

    # Hp1btn
    Hp1Btn = Button(fr2, text='ADD', bg='white', width='10', font='arial 10')
    Hp1Btn.place(x=75, y=215)

    # --------------------------------------------------------------------
    # -------------------------------------------------------------------
    # frame HP2
    fr3 = Frame(fr, width='250', height='250', bg='#ffffff')
    fr3.place(x=330, y=20)
    hp2 = Image.open("D:\\project\\images\\products\\hp2.jpg")
    # resize img
    resizedHP2 = hp2.resize((250, 160), Image.ANTIALIAS)
    newHP2 = ImageTk.PhotoImage(resizedHP2)
    HP2Lbl = Label(fr3, image=newHP2)
    HP2Lbl.place(x=0, y=0)

    # HP2Lbl
    HpTwoLbl = Label(fr3, text='HP 255 G8 Athlon Gold', bg='white', font='arial 12')
    HpTwoLbl.place(x=45, y=185)

    # Hp2btn
    HpTwoBtn = Button(fr3, text='ADD', bg='white', width='10', font='arial 10')
    HpTwoBtn.place(x=75, y=215)

    # ---------------------------------------------------------------------
    # frame HP3
    fr4 = Frame(fr, width='250', height='250', bg='#ffffff')
    fr4.place(x=330, y=290)
    hp3 = Image.open("D:\\project\\images\\products\\hp3.jpg")
    # resize img
    resizedHP3 = hp3.resize((250, 160), Image.ANTIALIAS)
    newHP3 = ImageTk.PhotoImage(resizedHP3)
    HP3Lbl = Label(fr4, image=newHP3)
    HP3Lbl.place(x=0, y=0)

    # HP3Lbl
    Hp3Lbl = Label(fr4, text='HP Victus 16- Gaming', bg='white', font='arial 12')
    Hp3Lbl.place(x=45, y=185)

    # Hp3btn
    Hp3Btn = Button(fr4, text='ADD', bg='white', width='10', font='arial 10')
    Hp3Btn.place(x=75, y=215)

    # ---------------------------------------------------------------------
    # ---------------------------------------------------------------------

    # frame Dell
    fr5 = Frame(fr, width='250', height='250', bg='#ffffff')
    fr5.place(x=620, y=20)
    dell = Image.open("D:\\project\\images\\products\\dell.jpg")
    # rezise img
    resizedDell = dell.resize((250, 160), Image.ANTIALIAS)
    newDell = ImageTk.PhotoImage(resizedDell)
    dellLbl = Label(fr5, image=newDell)
    dellLbl.place(x=0, y=0)

    # delllbl
    dellLbl = Label(fr5, text='Dell Latitude 5500', bg='white', font='arial 12')
    dellLbl.place(x=45, y=185)

    # dellbtn
    dellBtn = Button(fr5, text='ADD', bg='white', width='10', font='arial 10')
    dellBtn.place(x=75, y=215)

    # ---------------------------------------------------------------------
    # frame lenovo
    fr6 = Frame(fr, width='250', height='250', bg='#ffffff')
    fr6.place(x=620, y=290)
    lenovo = Image.open("D:\\project\\images\\products\\lenovo.jpg")
    # resize img
    resizedLenovo = lenovo.resize((250, 160), Image.ANTIALIAS)
    newLenovo = ImageTk.PhotoImage(resizedLenovo)
    lenovoLbl = Label(fr6, image=newLenovo)
    lenovoLbl.place(x=0, y=0)

    # lenovolbl
    lenovoLbl = Label(fr6, text='Lenovo Legion 5 11th', bg='white', font='arial 12')
    lenovoLbl.place(x=45, y=185)

    # lenovoBtn
    lenovoBtn = Button(fr6, text='ADD', bg='white', width='10', font='arial 10')
    lenovoBtn.place(x=75, y=215)

    # ---------------------------------------------------------------------
    # ---------------------------------------------------------------------

    # frame Dell2
    fr7 = Frame(fr, width='250', height='250', bg='#ffffff')
    fr7.place(x=910, y=20)
    dell2 = Image.open("D:\\project\\images\\products\\dell2.jpg")
    # rezise img
    resizedDell2 = dell2.resize((250, 160), Image.ANTIALIAS)
    newDell2 = ImageTk.PhotoImage(resizedDell2)
    dell2Lbl = Label(fr7, image=newDell2)
    dell2Lbl.place(x=0, y=0)

    # delllbl2
    dell2Lbl = Label(fr7, text='HP Victus 15- Gaming', bg='white', font='arial 12')
    dell2Lbl.place(x=45, y=185)

    # applebtn2
    dell2Btn = Button(fr7, text='ADD', bg='white', width='10', font='arial 10')
    dell2Btn.place(x=75, y=215)

    # ---------------------------------------------------------------------
    # frame Apple2
    fr8 = Frame(fr, width='250', height='250', bg='#ffffff')
    fr8.place(x=910, y=290)
    apple2 = Image.open("D:\\project\\images\\products\\apple2.jpg")
    # rezise img
    resizedApple2 = apple2.resize((250, 160), Image.ANTIALIAS)
    newApple2 = ImageTk.PhotoImage(resizedApple2)
    apple2Lbl = Label(fr8, image=newApple2)
    apple2Lbl.place(x=0, y=0)

    # apple2lbl
    apple2Lbl = Label(fr8, text='MacBook Air: Apple M1', bg='white', font='arial 12')
    apple2Lbl.place(x=45, y=185)

    # apple2btn
    apple2Btn = Button(fr8, text='ADD', bg='white', width='10', font='arial 10')
    apple2Btn.place(x=75, y=215)

    laptops.mainloop()


def cartf():
    db = Database("Products.db")

    cartr = Toplevel()
    cartr.geometry('1200x600+25+20')
    cartr.resizable(False, False)
    cartr.title('Cart')
    cartr.config(bg='#d9d9d9')
    cartr.iconbitmap('D:\\project\\icons\\cart.ico')

    nameV = StringVar()
    priceV = StringVar()

    def getData(event):
        selected_row = tv.focus()
        data = tv.item(selected_row)
        global row
        row = data["values"]
        nameV.set(row[1])
        priceV.set(row[2])

    def displayAll():
        tv.delete(*tv.get_children())
        for row in db.fetch():
            tv.insert("", END, values=row)

    def delete():
        db.remove(row[0])
        Clear()
        displayAll()

    def Clear():
        nameV.set("")
        priceV.set("")

    def addProduct():
        if nameccombo.get() == "" or priceEntry.get() == "":
            messagebox.showerror("Error", "Please Fill all the Entry")
            return
        db.insert(nameccombo.get(), priceEntry.get())
        messagebox.showinfo("Success", "Add new Product")
        Clear()
        displayAll()

    def update():
        if nameccombo.get() == "" or priceEntry.get() == "":
            messagebox.showerror("Error", "Please Fill all the Entry")
            return
        db.update(row[0],
                  nameccombo.get(),
                  priceEntry.get())
        messagebox.showinfo("Success", "Products Updated")
        Clear()
        displayAll()

    # frameC
    frc = Frame(cartr, width='800', height='530', bg='#f2f2f2')
    frc.place(x=40, y=35)

    # # CartLbl
    # cartLbl = Label(frc, text='Cart', bg='#00cc00', fg='white', font='Arial 20', width=48)
    # cartLbl.place(x=15, y=20)
    # # open img
    # cart = Image.open("D:\\project\\images\\cart.png")
    # # resize img
    # resizedCart = cart.resize((30, 30), Image.ANTIALIAS)
    # newCart = ImageTk.PhotoImage(resizedCart)
    # cartLbl = Label(frc, image=newCart)
    # cartLbl.place(x=440, y=22)

    # ===========Table Frame===========
    style = ttk.Style()
    style.configure("mystyle.Treeview", font='Arial 10', rowheight=50)
    style.configure("mystyle.Treeview.Heading", font='Arial 15', rowheight=50)

    tv = ttk.Treeview(frc, columns=(1, 2, 3), style='mystyle.Treeview')
    tv.heading('1', text='ID')
    tv.column('1', width='80')
    tv.heading('2', text='Name')
    tv.column('2', width='400')
    tv.heading('3', text='Price')
    tv.column('3', width='200')
    tv['show'] = 'headings'
    tv.bind("<ButtonRelease-1>", getData)
    tv.pack()

    # frameR
    frr = Frame(cartr, width='290', height='530', bg='#f2f2f2')
    frr.place(x=870, y=35)

    # namecLbl
    namecLbl = Label(frr, text='Name', font='Arial 13', )
    namecLbl.place(x=10, y=14)
    nameccombo = ttk.Combobox(frr, width=26, state='readonly', textvariable=nameV)
    nameccombo['values'] = ("MacBook Air: Apple M2",
                            "HP 15 Core i5-1135G",
                            "HP 255 G8 Athlon Gold",
                            "HP Victus 16- Gaming",
                            "Dell Latitude 5500",
                            "Lenovo Legion 5 11th",
                            "HP Victus 15- Gaming",
                            "MacBook Air: Apple M1")
    nameccombo.place(x=80, y=14)

    # priceLbl
    priceLbl = Label(frr, text='Price', font='Arial 13')
    priceLbl.place(x=10, y=50)
    priceEntry = Entry(frr, width=29, textvariable=priceV)
    priceEntry.place(x=80, y=50)

    # addbtn
    btnAdd = Button(frr, text='ADD', width=14, bg='#339966', font='Arial 10', fg='white', command=addProduct)
    btnAdd.place(x=13, y=100)
    # deletebtn
    deletebtn = Button(frr, text='Delete', width=14, bg='#cc3300', font='Arial 10', fg='white', command=delete)
    deletebtn.place(x=150, y=100)
    # updatebtn
    updatebtn = Button(frr, text='Update', width=14, bg='#0099cc', font='Arial 10', fg='white', command=update)
    updatebtn.place(x=13, y=140)
    # clearbtn
    clearbtn = Button(frr, text='Clear', width=14, bg='#ff9900', font='Arial 10', fg='white', command=Clear)
    clearbtn.place(x=150, y=140)

    # CartLbl
    resetLbl = Label(frr, text='Reaset', bg='#00cc00', font='Arial 20', width=16)
    resetLbl.place(x=13, y=200)

    displayAll()

    cartr.mainloop()


root = Tk()
root.geometry('550x500+350+50')
root.resizable(False, False)
root.title('LOG IN')
root.config(bg='#d9d9d9')
root.iconbitmap('D:\\project\\icons\\log.ico')
# frame
fr0 = Frame(root, width='300', height='400', bg='#f2f2f2')
fr0.pack(pady=90)

# login
login = Label(fr0, text='Log in', font='Arial 20')
login.place(x=20, y=10)

# username Entry
username = Label(fr0, text='Username', font='Arial 10')
username.place(x=17, y=70)
usernameEntry = Entry(fr0, width=43)
usernameEntry.place(x=20, y=90)

# password Entry
password = Label(fr0, text='Password', font='Arial 10')
password.place(x=17, y=125)
passwordEntry = Entry(fr0, width=43)
passwordEntry.place(x=20, y=145)


def login(username, password):
    if username.strip() == "mo" and password.strip() == "1234567":
        messagebox.showinfo('Login Success', 'Welcome IN Home App')
        product()

    else:
        messagebox.showinfo('Login Fiald', 'username or password wrong..')


def checkDataLogin():
    usernameText = usernameEntry.get()
    passwordText = passwordEntry.get()
    if usernameText == "":
        messagebox.showinfo('Invild UserName', 'enter correct username')
    elif passwordText == "":
        messagebox.showinfo('Invild Password', 'enter correct password')
    elif len(passwordText) < 6:
        messagebox.showinfo('Invild Password', 'enter password > 6 digit')
    else:
        login(usernameText, passwordText)


# login Button
loginButton = Button(fr0, text='Log in', font='Arial 15', width='23', height='1', bg='#d9d9d9', command=checkDataLogin)

loginButton.place(x=19, y=190)
# sign up Label
signUpLbl = Label(fr0, text='Dont have an account?', font='Arial 8')
signUpLbl.place(x=88, y=263)
# sign up Button
signUpButton = Button(fr0, text='Sign Up', font='Arial 11', width='20', bg='#d9d9d9', command=product)

signUpButton.place(x=50, y=280)

root.mainloop()
