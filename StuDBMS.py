from prettytable import PrettyTable
import mysql.connector
from tkinter import *
import csv
from PIL import ImageTk, Image
from hashlib import md5

mydb = mysql.connector.connect(
    host='localhost', user='root', password='<pass>', database='<database>')
mycursor = mydb.cursor()

mycursor.execute('select username from usernames_1')
opnm = mycursor.fetchall()

# confugurable file paths
icon_img = r".\media\icon.ico"
logo_img = r"D:\Python\Projects\StuDBMS\logo.png"
home_dir_path = "C:\\Users\\<user>\\"

l7 = []
for m in opnm:
    l7.append(m)
usernm = []
for u in l7:
    usernm.append(u[0])

mycursor.execute('select username from usernames_2')
opnm2 = mycursor.fetchall()

l11 = []
for m in opnm2:
    l11.append(m)
usernm2 = []
for u in l11:
    usernm2.append(u[0])

root1 = Tk()
root1.title('LOGIN')
root1.geometry("325x485")
root1.resizable(False, False)
root1.configure(bg='#D3D3D3')
root1.iconbitmap(icon_img)

classdict = {'11 A': '11A', '11 B': '11B'}
examsdict = {'SA 1': 'SA1', 'SA 2': 'SA2'}

def btclosemain_clicked():
    root1.destroy()

btclosemain = Button(root1, text="EXIT", bg="red", command=btclosemain_clicked)
btclosemain.pack(side=TOP, anchor=NE)
img1=Image.open(logo_img)
img1=img1.resize((85,85),Image.Resampling.LANCZOS)
img1_1=ImageTk.PhotoImage(img1)
lblimg1=Label(image=img1_1)
lblimg1.pack()
lbl61 = Label(root1, text='StuDBMS', font=(
    'Bahnschrift', 22, 'bold'), bg='#D3D3D3')
lbl61.pack()
lbl57 = Label(root1, text='LOGIN', bg='#D3D3D3', font=('Bahnschrift', 12,))
lbl57.pack()
lbl1 = Label(
    root1, text="Enter the passcode to access student detabase.", bg='#D3D3D3')
lbl1.pack()
lblspace11 = Label(root1, text='', bg='#D3D3D3')
lblspace11.pack()
lbl50 = Label(root1, text='Choose role:', bg='#D3D3D3')
lbl50.pack()
clicked3 = StringVar()
clicked3.set('Teacher')
drp3 = OptionMenu(root1, clicked3, 'Student', 'Teacher')
drp3.pack()
lblspace51 = Label(root1, text='', bg='#D3D3D3')
lblspace51.pack()


lblusr = Label(root1, text="Username:", bg='#D3D3D3', fg='blue')
lblusr.pack()
ent1 = Entry(root1, width=15, borderwidth=5)
ent1.pack()

lblpsd = Label(root1, text="Password:", bg='#D3D3D3', fg='blue')
lblpsd.pack()
ent2 = Entry(root1, width=15, borderwidth=5,show='*',)
ent2.pack()

lblspace14 = Label(root1, text='', bg='#D3D3D3')
lblspace14.pack()

l1, l2 = [], []


def bt1_clicked():

    mycursor.execute(
        "select pass from usernames_1 where username = '"+ent1.get()+"'")
    oppd = mycursor.fetchall()
    l9 = []
    for m in oppd:
        l9.append(m)
    pswd = []
    for u in l9:
        pswd.append(u[0])

    mycursor.execute(
        "select pass from usernames_2 where username = '"+ent1.get()+"'")
    oppd2 = mycursor.fetchall()

    l10 = []
    for m in oppd2:
        l10.append(m)
    pswd2 = []
    for u in l10:
        pswd2.append(u[0])

    pswd_inp = ent2.get().encode('utf-8')
    pswd_inp_hash = (md5(pswd_inp).hexdigest())

    if pswd_inp_hash in pswd and ent1.get() in usernm and clicked3.get() == 'Teacher':

        def grade(x):
            if x in range(21):
                grd = "E2"
            elif x in range(21, 33):
                grd = "E2"
            elif x in range(33, 41):
                grd = "D"
            elif x in range(41, 51):
                grd = "C2"
            elif x in range(51, 61):
                grd = "C1"
            elif x in range(61, 71):
                grd = "B2"
            elif x in range(71, 81):
                grd = "B1"
            elif x in range(81, 91):
                grd = "A2"
            elif x in range(91, 101):
                grd = "A1"
            return (grd)

        ent1.configure(bg='#00BFFF')
        ent2.configure(bg='#00BFFF')
        entry1 = ent1.get()
        bt1.configure(state=DISABLED)
        root = Toplevel()
        root.geometry('300x475')
        root.title('HOME')
        root.iconbitmap(icon_img)
        root.configure(bg="#D3D3D3")

        def btclosemain02_clicked():
            root.destroy()
        btclosemain02 = Button(root, text='EXIT', bg='red',
                               command=btclosemain02_clicked)
        btclosemain02.pack(side=TOP, anchor=NE)
        lbl3 = Label(root, text='Access granted!', fg="#00BFFF", bg='#D3D3D3')
        lbl3.pack()
        l1.append(1)
        lbl4 = Label(root, text='', bg='#D3D3D3')
        lbl4.pack()
        lblnmdisp = Label(root, text='Welcome '+entry1,
                          bg='#D3D3D3', font=('Calibri', 12))
        lblnmdisp.pack()
        lblhome = Label(root, text="HOME", font=(
            'Calibri', 16, 'bold'), bg='#D3D3D3')
        lblhome.pack()
        lblspace10 = Label(root, text='', bg='#D3D3D3')
        lblspace10.pack()
        lbltitle5 = Label(root, text="Select class:", bg='#D3D3D3')
        lbltitle5.pack()
        clicked2 = StringVar()
        clicked2.set('11 A')
        drp2 = OptionMenu(root, clicked2, "11 A", "11 B")
        drp2.pack()
        lblspace57 = Label(root, text='', bg='#D3D3D3')
        lblspace57.pack()
        lbl56 = Label(root, text='Select test:', bg='#D3D3D3')
        lbl56.pack()
        clicked6 = StringVar()
        clicked6.set('SA 1')
        drp6 = OptionMenu(root, clicked6, 'SA 1', 'SA 2')
        drp6.pack()
        lblspace51 = Label(root, text='', bg='#D3D3D3')
        lblspace51.pack()
        lbl5 = Label(root, text='Select your choice:', bg='#D3D3D3')
        lbl5.pack()
        clicked1 = StringVar()
        clicked1.set("View student info.")
        drp1 = OptionMenu(root, clicked1, "View student info.", "Add student info.",
                          "Delete student info.", "Alter student info.", "Scan Excel.", "Write Excel.")
        drp1.pack()
        lblspace46 = Label(root, text='', bg='#D3D3D3')
        lblspace46.pack()
        lblspace59 = Label(root, text='', bg='#D3D3D3')
        lblspace59.pack()

        def bt2_clicked():
            tab = classdict[clicked2.get()]+'_'+examsdict[clicked6.get()]

            if clicked1.get() == "Add student info.":
                l2 = []
                mycursor.execute("select rollno from "+tab+"")
                rno = mycursor.fetchall()
                l4 = []
                for m in rno:
                    l4.append(m)
                l5 = []
                for u in l4:
                    l5.append(u[0])

                win2 = Toplevel()
                win2.title('ADD')
                win2.geometry('400x650')
                win2.iconbitmap(icon_img)

                def btclosewin2_clicked():
                    win2.destroy()
                btclosewin2 = Button(
                    win2, text='EXIT', bg='red', command=btclosewin2_clicked)
                btclosewin2.pack(side=TOP, anchor=NE)

                lbltitle5 = Label(
                    win2, text="Enter the student details below", font=('Bahnschrift', 12))
                lbltitle5.pack()
                lblspace15 = Label(win2, text='')
                lblspace15.pack()
                lbl6 = Label(win2, text="Enter student RollNo")
                lbl6.pack()

                def bt3_clicked():
                    bt3.configure(state=DISABLED)
                    inp1 = ent2.get()
                    if inp1.isdigit() == False or int(inp1) in l5 or len(inp1) > 2:
                        lblspace49 = Label(win2, text='')
                        lblspace49.pack()
                        lbl7 = Label(
                            win2, text='Enter a valid and unique RollNo!', fg="red")
                        lbl7.pack()
                        lblspace50 = Label(win2, text='')
                        lblspace50.pack()

                    else:
                        a = inp1
                        lbl8 = Label(win2, text="Enter student Name")
                        lbl8.pack()

                        def bt4_clicked():
                            bt4.configure(state=DISABLED)
                            inp2 = ent3.get()
                            if inp2.isalpha() == False or len(inp2) > 20:
                                lblspace54 = Label(win2, text='')
                                lblspace54.pack()
                                lbl9 = Label(
                                    win2, text='Enter a valid Name!', fg='red')
                                lbl9.pack()
                                lblspace55 = Label(win2, text='')
                                lblspace55.pack()

                            else:
                                count = 0
                                b = inp2
                                b = b.lower()
                                l6 = []
                                strx = ''
                                for y in b:
                                    if y == b[0] and count == 0:
                                        l6.append(y.capitalize())
                                        count = 1
                                    else:
                                        l6.append(y)
                                for x in l6:
                                    strx = strx+x
                                b = strx

                                def bt5_clicked():
                                    bt5.configure(state=DISABLED)
                                    inp3, inp4, inp5, inp6, inp7 = ent4.get(
                                    ), ent5.get(), ent6.get(), ent7.get(), ent8.get()
                                    if (inp3.isdigit() == False or inp4.isdigit() == False or inp5.isdigit() == False or inp6.isdigit() == False or inp7.isdigit() == False):
                                        lblspace51 = Label(win2, text='')
                                        lblspace51.pack()
                                        lbl15 = Label(
                                            win2, text="Enter valid scores!", fg="red")
                                        lbl15.pack()
                                        lblspace24 = Label(win2, text='')
                                        lblspace24.pack()

                                    if (inp3.isdigit() == True and inp4.isdigit() == True and inp5.isdigit() == True and inp6.isdigit() == True and inp7.isdigit() == True) and (int(inp3) > 100 or int(inp4) > 100 or int(inp5) > 100 or int(inp6) > 100 or int(inp7) > 100):
                                        lblspace60 = Label(win2, text='')
                                        lblspace60.pack()
                                        lbl16 = Label(
                                            win2, text="Maximum obtainable score is 100!", fg='red')
                                        lbl16.pack()
                                        lblspace24 = Label(win2, text='')
                                        lblspace24.pack()
                                    if (inp3.isdigit() == True and inp4.isdigit() == True and inp5.isdigit() == True and inp6.isdigit() == True and inp7.isdigit() == True) and (int(inp3) <= 100 and int(inp4) <= 100 and int(inp5) <= 100 and int(inp6) <= 100 and int(inp7) <= 100):
                                        bt5.configure(state=DISABLED)
                                        c, d, e, f, g = inp3, inp4, inp5, inp6, inp7
                                        mycursor.execute(
                                            "insert into "+tab+"(RollNo,Name,Physics,Chemistry,Maths,Computer,English) values('"+a+"','"+b+"','"+c+"','"+d+"','"+e+"','"+f+"','"+g+"')")
                                        mydb.commit()
                                        lblspace20 = Label(win2, text='')
                                        lblspace20.pack()
                                        lbl17 = Label(
                                            win2, text="Data added successfully!")
                                        lbl17.pack()
                                        lblspace21 = Label(win2, text='')
                                        lblspace21.pack()
                                lblspace10 = Label(win2, text='')
                                lblspace10.pack()
                                lbl10 = Label(win2, text="Physics score:")
                                lbl10.pack()
                                ent4 = Entry(win2, width=5, borderwidth=5)
                                ent4.pack()
                                lbl11 = Label(win2, text="Chemistry score:")
                                lbl11.pack()
                                ent5 = Entry(win2, width=5, borderwidth=5)
                                ent5.pack()
                                lbl12 = Label(win2, text="Maths score:")
                                lbl12.pack()
                                ent6 = Entry(win2, width=5, borderwidth=5)
                                ent6.pack()
                                lbl13 = Label(
                                    win2, text="Compter Science score:")
                                lbl13.pack()
                                ent7 = Entry(win2, width=5, borderwidth=5)
                                ent7.pack()
                                lbl14 = Label(win2, text="English score:")
                                lbl14.pack()
                                ent8 = Entry(win2, width=5, borderwidth=5)
                                ent8.pack()
                                lblspace11 = Label(win2, text='')
                                lblspace11.pack()
                                bt5 = Button(win2, text='Enter',
                                             command=bt5_clicked)
                                bt5.pack()

                        ent3 = Entry(win2, width=15, borderwidth=5)
                        ent3.pack()
                        bt4 = Button(win2, text="Enter", command=bt4_clicked)
                        bt4.pack()
                ent2 = Entry(win2, width=5, borderwidth=5)
                ent2.pack()
                bt3 = Button(win2, text='Enter', command=bt3_clicked)
                bt3.pack()

            if clicked1.get() == 'View student info.':

                win3 = Toplevel()
                win3.geometry('425x450')
                win3.title('VIEW')
                win3.iconbitmap(icon_img)

                def btclosewin3_clicked():
                    win3.destroy()
                btclosewin3 = Button(
                    win3, text='EXIT', bg='red', command=btclosewin3_clicked)
                btclosewin3.pack(side=TOP, anchor=NE)

                lbl18 = Label(
                    win3, text="Enter the RollNo of the student whose data is to be accessed")
                lbl18.pack()

                def bt6_clicked():
                    bt6.configure(state=DISABLED)

                    chk = ent9.get()

                    if chk.isdigit()==False:
                        lblspace30 = Label(win3, text='')
                        lblspace30.pack()
                        lbl19 = Label(
                            win3, text="Enter a valid RollNo!", fg="red")
                        lbl19.pack()
                        lblspace31 = Label(win3, text='')
                        lblspace31.pack()

                    else:
                        mycursor.execute("select * from "+tab +
                                        " where RollNo = "+chk+"")
                        op1 = mycursor.fetchall()

                        mycursor.execute("select rollno from "+tab+"")
                        rno = mycursor.fetchall()
                        l4 = []
                        for m in rno:
                            l4.append(m)
                        l5 = []
                        for u in l4:
                            l5.append(str(u[0]))
                        if chk not in l5:
                            lblspace30 = Label(win3, text='')
                            lblspace30.pack()
                            lbl19 = Label(
                                win3, text="Data does not exist!", fg="red")
                            lbl19.pack()
                            lblspace31 = Label(win3, text='')
                            lblspace31.pack()
                        else:
                            mycursor.execute(
                                "select max(physics+chemistry+maths+computer+english) from "+tab+"")
                            op2 = mycursor.fetchone()

                            mycursor.execute(
                                "select min(physics+chemistry+maths+computer+english) from "+tab+"")
                            op3 = mycursor.fetchone()

                            mycursor.execute("select * from " +
                                            tab+" where RollNo = "+chk+"")
                            op1 = mycursor.fetchall()

                            l1 = []
                            for i in op1:
                                l1.append(i)

                            a1, b1, c1, d1, e1, f1, g1 = l1[0]
                            c1, d1, e1, f1, g1 = int(c1), int(
                                d1), int(e1), int(f1), int(g1)

                            tot = c1+d1+e1+f1+g1

                            lblspace8 = Label(win3, text='')
                            lblspace8.pack()

                            lblrln = Label(win3, text="RollNo: "+str(a1) +
                                        "    Name: "+b1, font='TkHeadingFont')
                            lblrln.pack()

                            lblspace50 = Label(win3, text='')
                            lblspace50.pack()

                            tbl = PrettyTable()
                            tbl.field_names = [
                                'Physics', 'Chemistry', 'Maths', 'ComputerSc', 'English']
                            tbl.add_row(
                                [str(c1), str(d1), str(e1), str(f1), str(g1)])
                            tbl.add_row(
                                [grade(c1), grade(d1), grade(e1), grade(f1), grade(g1)])

                            lblprt = Label(win3, text=tbl, font='TkHeadingFont')
                            lblprt.pack()
                            lblspace9 = Label(win3, text='')
                            lblspace9.pack()

                            mycursor.execute(
                                "select rollno,(physics+chemistry+maths+computer+english) from "+tab+"")
                            op1 = mycursor.fetchall()
                            d1 = {}
                            for i in op1:
                                d1[i[0]] = i[1]

                            sort_op1 = sorted(d1.items(), key=lambda t: t[1])
                            sort_op1.reverse()

                            d2 = {}
                            for i in sort_op1:
                                d2[i[0]] = i[1]
                            countxy = 0
                            for i in d2:
                                if str(i) == str(chk):
                                    countxy += 1
                                    break
                                else:
                                    countxy += 1

                            classtot = 0
                            for i in d1:
                                classtot += d1[i]

                            lbl26 = Label(win3, text="Average score: " +
                                        str(tot/5), font='TkHeadingFont')
                            lbl26.pack()
                            lbl27 = Label(win3, text="Total score: "+str(tot))
                            lbl27.pack()
                            lbl28 = Label(
                                win3, text="Average total: "+str(round(classtot/len(d1), 2)), font='TkHeadingFont')
                            lbl28.pack()
                            lbl29 = Label(win3, text="Class rank: " +
                                        str(countxy), font='TkHeadingFont')
                            lbl29.pack()
                            lbl30 = Label(win3, text="Highest total: " +
                                        str(op2[0]), font='TkHeadingFont')
                            lbl30.pack()
                            lbl31 = Label(win3, text="Lowest total: " +
                                        str(op3[0]), font='TkHeadingFont')
                            lbl31.pack()
                            lblspace7 = Label(win3, text='')
                            lblspace7.pack()

                ent9 = Entry(win3, width=5, borderwidth=5)
                ent9.pack()
                bt6 = Button(win3, text="Enter", command=bt6_clicked)
                bt6.pack()

            if clicked1.get() == "Delete student info.":
                win4 = Toplevel()
                win4.geometry('425x550')
                win4.title("DELETE")
                win4.iconbitmap(icon_img)

                def btclosewin4_clicked():
                    win4.destroy()
                btclosewin4 = Button(
                    win4, text='EXIT', bg='red', command=btclosewin4_clicked)
                btclosewin4.pack(side=TOP, anchor=NE)

                lbl32 = Label(
                    win4, text="Enter the RollNo of the student whose data is to be erased")
                lbl32.pack()

                def bt7_clicked():
                    bt7.configure(state=DISABLED)

                    del1 = ent9.get()

                    mycursor.execute("select rollno from "+tab+"")
                    rno = mycursor.fetchall()
                    l4 = []
                    for m in rno:
                        l4.append(m)
                    l5 = []
                    for u in l4:
                        l5.append(str(u[0]))
                    if del1 not in l5:
                        lblspace33 = Label(win4, text='')
                        lblspace33.pack()

                        lbl33 = Label(
                            win4, text="Data does not exist!", fg="red")
                        lbl33.pack()
                        lblspace34 = Label(win4, text='')
                        lblspace34.pack()

                    else:
                        mycursor.execute("select * from " +
                                         tab+" where RollNo="+del1+"")
                        op1 = mycursor.fetchall()

                        l1 = []
                        for i in op1:
                            l1.append(i)

                        a1, b1, c1, d1, e1, f1, g1 = l1[0]
                        c1, d1, e1, f1, g1 = int(c1), int(
                            d1), int(e1), int(f1), int(g1)

                        lblrln = Label(win4, text="RollNo: "+str(a1) +
                                       "    Name: "+b1, font='TkHeadingFont')
                        lblrln.pack()
                        lblspace50 = Label(win4, text='')
                        lblspace50.pack()

                        tbl = PrettyTable()
                        tbl.field_names = [
                            'Physics', 'Chemistry', 'Maths', 'ComputerSc', 'English']
                        tbl.add_row(
                            [str(c1), str(d1), str(e1), str(f1), str(g1)])
                        tbl.add_row(
                            [grade(c1), grade(d1), grade(e1), grade(f1), grade(g1)])

                        lblprt = Label(win4, text=tbl, font='TkHeadingFont')
                        lblprt.pack()
                        lblspace9 = Label(win4, text='')
                        lblspace9.pack()

                        bt7.configure(state=DISABLED)
                        mycursor.execute("select name from " +
                                         tab+" where rollno='"+del1+"'")
                        op5 = mycursor.fetchall()
                        l2 = []
                        for j in op5:
                            l2.append(j)
                        stup = l2[0]
                        sname = stup[0]
                        lblspace18 = Label(win4, text='')
                        lblspace18.pack()
                        lbl34 = Label(win4, text="Warning! All of "+sname +
                                      "'s data will be permanently erased. Still proceed?", fg="red")
                        lbl34.pack()
                        var2 = IntVar()
                        var2.set(0)
                        chk2 = Checkbutton(
                            win4, text='I understand and wish to proceed.', variable=var2)
                        chk2.pack()
                        lblspace56 = Label(win4, text='')
                        lblspace56.pack()

                        def btyes_clicked():
                            if var2.get() == 1:
                                btyes.configure(state=DISABLED)
                                mycursor.execute(
                                    "Delete from "+tab+" where rollno='"+del1+"'")
                                mydb.commit()
                                lblspace27 = Label(win4, text='')
                                lblspace27.pack()
                                lbl35 = Label(
                                    win4, text="Data erased successfully!",)
                                lbl35.pack()
                                lblspace26 = Label(win4, text='')
                                lblspace26.pack()
                        btyes = Button(win4, text="PROCEED",
                                       fg="red", command=btyes_clicked)
                        btyes.pack()

                ent9 = Entry(win4, width=5, borderwidth=5)
                ent9.pack()
                bt7 = Button(win4, text="Enter", command=bt7_clicked)
                bt7.pack()

            if clicked1.get() == 'Alter student info.':
                l2 = []
                mycursor.execute("select rollno from "+tab+"")
                rno = mycursor.fetchall()
                l4 = []
                for m in rno:
                    l4.append(m)
                l5 = []
                for u in l4:
                    l5.append(u[0])

                win5 = Toplevel()
                win5.geometry('425x770')
                win5.title('ALTER')
                win5.iconbitmap(icon_img)

                def btclosewin5_clicked():
                    win5.destroy()
                btclosewin5 = Button(
                    win5, text='EXIT', bg='red', command=btclosewin5_clicked)
                btclosewin5.pack(side=TOP, anchor=NE)

                lbl6 = Label(
                    win5, text="Enter the RollNo of the student whose data is to be altered")
                lbl6.pack()

                def bt3_clicked():
                    bt3.configure(state=DISABLED)
                    inp1 = ent2.get()
                    if inp1.isdigit() == False or int(inp1) not in l5:
                        lblspace35 = Label(win5, text='')
                        lblspace35.pack()
                        lbl7 = Label(
                            win5, text='Data does not exist!', fg="red")
                        lbl7.pack()
                        lblspace36 = Label(win5, text='')
                        lblspace36.pack()

                    else:
                        bt3.configure(state=DISABLED)
                        mycursor.execute("select * from " +
                                         tab+" where RollNo="+inp1+"")
                        op1 = mycursor.fetchall()

                        l1 = []
                        for i in op1:
                            l1.append(i)

                        a1, b1, c1, d1, e1, f1, g1 = l1[0]
                        c1, d1, e1, f1, g1 = int(c1), int(
                            d1), int(e1), int(f1), int(g1)

                        lblrln = Label(win5, text="RollNo: "+str(a1) +
                                       "    Name: "+b1, font='TkHeadingFont')
                        lblrln.pack()
                        lblspace50 = Label(win5, text='')
                        lblspace50.pack()

                        tbl = PrettyTable()
                        tbl.field_names = [
                            'Physics', 'Chemistry', 'Maths', 'ComputerSc', 'English']
                        tbl.add_row(
                            [str(c1), str(d1), str(e1), str(f1), str(g1)])
                        tbl.add_row(
                            [grade(c1), grade(d1), grade(e1), grade(f1), grade(g1)])

                        lblprt = Label(win5, text=tbl, font='TkHeadingFont')
                        lblprt.pack()
                        lblspace9 = Label(win5, text='')
                        lblspace9.pack()

                        a = inp1
                        lblspace5 = Label(win5, text='')
                        lblspace5.pack()
                        lbltitle1 = Label(
                            win5, text='Enter the updated details below', font="bold")
                        lbltitle1.pack()
                        lblspace6 = Label(win5, text='')
                        lblspace6.pack()
                        lbl8 = Label(win5, text="Enter student Name")
                        lbl8.pack()

                        def bt4_clicked():
                            bt4.configure(state=DISABLED)
                            inp2 = ent3.get()
                            if inp2.isalpha() == False or len(inp2) > 20:
                                lblspace42 = Label(win5, text='')
                                lblspace42.pack()
                                lbl9 = Label(
                                    win5, text='Enter a valid Name!', fg='red')
                                lbl9.pack()
                                lblspace43 = Label(win5, text='')
                                lblspace43.pack()

                            else:
                                count1 = 0

                                n2 = inp2
                                n2 = n2.lower()
                                l6 = []
                                strx = ''
                                for y in n2:
                                    if y == n2[0] and count1 == 0:
                                        l6.append(y.capitalize())
                                        count1 = 1
                                    else:
                                        l6.append(y)
                                for x in l6:
                                    strx = strx+x
                                n2 = strx

                                def bt5_clicked():
                                    bt5.configure(state=DISABLED)

                                    inp3, inp4, inp5, inp6, inp7 = ent4.get(
                                    ), ent5.get(), ent6.get(), ent7.get(), ent8.get()
                                    if (inp3.isdigit() == False or inp4.isdigit() == False or inp5.isdigit() == False or inp6.isdigit() == False or inp7.isdigit() == False):
                                        lblspace37 = Label(win5, text='')
                                        lblspace37.pack()
                                        lbl15 = Label(
                                            win5, text="Enter valid scores!", fg="red")
                                        lbl15.pack()
                                        lblspace38 = Label(win5, text='')
                                        lblspace38.pack()
                                        allow = 1

                                    if (inp3.isdigit() == True and inp4.isdigit() == True and inp5.isdigit() == True and inp6.isdigit() == True and inp7.isdigit() == True) and (int(inp3) > 100 or int(inp4) > 100 or int(inp5) > 100 or int(inp6) > 100 or int(inp7) > 100):
                                        lblspace40 = Label(win5, text='')
                                        lblspace40.pack()
                                        lbl16 = Label(
                                            win5, text="Maximum obtainable score is 100!", fg='red')
                                        lbl16.pack()
                                        lblspace41 = Label(win5, text='')
                                        lblspace41.pack()
                                        allow = 1
                                    if (inp3.isdigit() == True and inp4.isdigit() == True and inp5.isdigit() == True and inp6.isdigit() == True and inp7.isdigit() == True) and (int(inp3) <= 100 and int(inp4) <= 100 and int(inp5) <= 100 and int(inp6) <= 100 and int(inp7) <= 100):
                                        allow = 0
                                        bt5.configure(state=DISABLED)
                                        lblspace17 = Label(win5, text='')
                                        lblspace17.pack()
                                        lbl35 = Label(
                                            win5, text="Warning! "+b1+"'s data will be altered. Still proceed?")
                                        lbl35.pack()
                                        var1 = IntVar()
                                        var1.set(0)
                                        chk1 = Checkbutton(
                                            win5, text='I understand and wish to proceed.', variable=var1)
                                        chk1.pack()

                                        def altyes():
                                            if var1.get() == 1:
                                                btaltyes.configure(
                                                    state=DISABLED)
                                                n3, n4, n5, n6, n7 = inp3, inp4, inp5, inp6, inp7
                                                mycursor.execute("update "+tab+" set name='"+n2+"',physics='"+n3+"',chemistry='" +
                                                                 n4+"',maths='"+n5+"',computer='"+n6+"',english='"+n7+"' where rollno='"+a+"'")
                                                mydb.commit()
                                                lblspace28 = Label(
                                                    win5, text='')
                                                lblspace28.pack()
                                                lbl17 = Label(
                                                    win5, text="Data altered successfully!")
                                                lbl17.pack()
                                                lblspace29 = Label(
                                                    win5, text='')
                                                lblspace29.pack()
                                        lblspace4 = Label(win5, text='')
                                        lblspace4.pack()
                                        btaltyes = Button(
                                            win5, text='PROCEED', command=altyes, fg="red", width=10)
                                        btaltyes.pack()
                                lblspace17 = Label(win5, text='')
                                lblspace17.pack()
                                lbltitle6 = Label(
                                    win5, text="Enter subject-wise scores:")
                                lbltitle6.pack()

                                ent4 = Entry(win5, width=12, borderwidth=5)
                                ent4.pack()
                                ent4.insert(0, "Physics")
                                ent5 = Entry(win5, width=12, borderwidth=5)
                                ent5.pack()
                                ent5.insert(0, "Chemistry")
                                ent6 = Entry(win5, width=12, borderwidth=5)
                                ent6.pack()
                                ent6.insert(0, "Maths")
                                ent7 = Entry(win5, width=12, borderwidth=5)
                                ent7.pack()
                                ent7.insert(0, "ComputerSc")
                                ent8 = Entry(win5, width=12, borderwidth=5)
                                ent8.pack()
                                ent8.insert(0, "English")

                                bt5 = Button(win5, text='Enter',
                                             command=bt5_clicked)
                                bt5.pack()
                        ent3 = Entry(win5, width=15, borderwidth=5)
                        ent3.pack()
                        bt4 = Button(win5, text="Enter", command=bt4_clicked)
                        bt4.pack()
                ent2 = Entry(win5, width=5, borderwidth=5)
                ent2.pack()
                bt3 = Button(win5, text='Enter', command=bt3_clicked)
                bt3.pack()

            if clicked1.get() == 'Scan Excel.':
                win6 = Toplevel()
                win6.geometry('370x770')
                win6.title('TRANSFER')
                win6.iconbitmap(icon_img)

                def btclosewin6_clicked():
                    win6.destroy()
                btclosewin6 = Button(
                    win6, text='EXIT', bg='red', command=btclosewin6_clicked)
                btclosewin6.pack(side=TOP, anchor=NE)

                lbl6_1 = Label(win6, text='Choose file location:')
                lbl6_1.pack()
                clicked4 = StringVar()
                clicked4.set('Desktop')
                drp4 = OptionMenu(win6, clicked4, 'Desktop',
                                  'Documents', 'Downloads')
                drp4.pack()
                lblspace6_1 = Label(win6, text='')
                lblspace6_1.pack()
                lbl6_2 = Label(win6, text='Enter file name:')
                lbl6_2.pack()
                ent6_1 = Entry(win6, borderwidth=5)
                ent6_1.pack()
                lblspace6_2 = Label(win6, text='')
                lblspace6_2.pack()
                lbl62 = Label(win6, text='Choose file type:')
                lbl62.pack()
                clicked5 = StringVar()
                clicked5.set('.csv')
                drp5 = OptionMenu(win6, clicked5, '.xlsx', '.csv')
                drp5.pack()
                lblspace6_9 = Label(win6, text='')
                lblspace6_9.pack()

                def bt6_1_clicked():
                    if var3.get() == 1:
                        bt6_1.configure(state=DISABLED)
                        if ent6_1.get() == '':
                            lbl6_2 = Label(
                                win6, text='Enter a file name!', fg='red')
                            lbl6_2.pack()
                            lblspace6_3 = Label(win6, text='')
                            lblspace6_3.pack()
                        else:

                            l2 = []
                            count5 = 0
                            count2 = 0
                            count3 = 0
                            count4 = 0

                            loc = home_dir_path+clicked4.get()+'\\'+ent6_1.get()+clicked5.get()

                            try:
                                with open(loc, 'r') as f1:
                                    reader = csv.reader(f1)
                                    next(reader)
                                    for line in reader:
                                        if line[0].isdigit() == False:
                                            count3 += 1
                                            count2 += 1
                                            continue
                                        mycursor.execute(
                                            "select rollno from "+tab+"")
                                        rno = mycursor.fetchall()
                                        l4 = []
                                        for m in rno:
                                            l4.append(m)
                                        l5 = []
                                        for u in l4:
                                            l5.append(u[0])

                                        if int(line[0]) in l5:
                                            count5 += 1
                                            count3 += 1
                                            continue
                                        inp1 = int(line[0])
                                        if inp1 > 100:
                                            count2 += 1
                                            count3 += 1
                                            continue
                                        inp2_1 = line[1]
                                        if inp2_1.isalpha() == False:
                                            count2 += 1
                                            count3 += 1
                                            continue
                                        count = 0
                                        b = inp2_1
                                        b = b.lower()
                                        l6 = []
                                        strx = ''
                                        for y in b:
                                            if y == b[0] and count == 0:
                                                l6.append(y.capitalize())
                                                count = 1
                                            else:
                                                l6.append(y)
                                        for x in l6:
                                            strx = strx+x
                                        inp2 = strx
                                        inp3 = int(line[2])
                                        if inp3 not in range(0, 101):
                                            count2 += 1
                                            count3 += 1
                                            continue
                                        inp4 = int(line[3])
                                        if inp4 not in range(0, 101):
                                            count2 += 1
                                            count3 += 1
                                            continue
                                        inp5 = int(line[4])
                                        if inp5 not in range(0, 101):
                                            count2 += 1
                                            count3 += 1
                                            continue
                                        inp6 = int(line[5])
                                        if inp6 not in range(0, 101):
                                            count2 += 1
                                            count3 += 1
                                            continue
                                        inp7 = int(line[6])
                                        if inp7 not in range(0, 101):
                                            count2 += 1
                                            count3 += 1
                                            continue
                                        mycursor.execute(
                                            f"insert into {tab} values({inp1},'{inp2}',{inp3},{inp4},{inp5},{inp6},{inp7})")
                                        mydb.commit()
                                        count4 += 1
                                        count3 += 1
                                    lbl6_4 = Label(
                                        win6, text='Data transfered successfully!', font=('TkHeadingFont', 10))
                                    lbl6_4.pack()
                                    lbl6_10 = Label(
                                        win6, text='Rows scanned: '+str(count3+1))
                                    lbl6_10.pack()
                                    lbl6_11 = Label(
                                        win6, text='Redundant data (skipped): '+str(count5))
                                    lbl6_11.pack()
                                    lbl6_12 = Label(
                                        win6, text='Rows skipped: '+str(count2+1))
                                    lbl6_12.pack()
                                    lblspace6_5 = Label(win6, text='')
                                    lblspace6_5.pack()
                            except:
                                lbl6_5 = Label(
                                    win6, text='Error occured while reading data!', fg='red')
                                lbl6_5.pack()
                                lbl6_6 = Label(
                                    win6, text='(Check file name and file structure.)')
                                lbl6_6.pack()
                                lblspace6_6 = Label(win6, text='')
                                lblspace6_6.pack()
                                lbl6_13 = Label(win6, text=str(
                                    count4)+' rows transfered so far.')
                                lbl6_13.pack()
                                lblspace6_8 = Label(win6, text='')
                                lblspace6_8.pack()

                lbl6_9 = Label(win6, text='CAUTION', fg='red',
                               font=('Bahnschrift', 12))
                lbl6_9.pack()
                lbl6_7 = Label(win6, text='Make sure you choose the correct file with all', fg='red', font=(
                    'Bahnschrift', 10))
                lbl6_7.pack()
                lbl6_8 = Label(win6, text='fields in correct order before proceeding!', fg='red', font=(
                    'Bahnschrift', 10))
                lbl6_8.pack()
                var3 = IntVar()
                var3.set(0)
                chk3 = Checkbutton(
                    win6, text='I understand and wish to proceed.', variable=var3)
                chk3.pack()
                lblspace6_7 = Label(win6, text='')
                lblspace6_7.pack()
                bt6_1 = Button(win6, text='PROCEED', command=bt6_1_clicked)
                bt6_1.pack()
                lblspace6_4 = Label(win6, text='')
                lblspace6_4.pack()

            if clicked1.get() == 'Write Excel.':
                win7 = Toplevel()
                win7.geometry('370x400')
                win7.title('TRANSFER')
                win7.iconbitmap(icon_img)

                def btclosewin7_clicked():
                    win7.destroy()
                btclosewin7 = Button(
                    win7, text='EXIT', bg='red', command=btclosewin7_clicked)
                btclosewin7.pack(side=TOP, anchor=NE)

                lbl7_1 = Label(win7, text='Choose file location:')
                lbl7_1.pack()
                clicked4 = StringVar()
                clicked4.set('Desktop')
                drp4 = OptionMenu(win7, clicked4, 'Desktop',
                                  'Documents', 'Downloads')
                drp4.pack()
                lblspace7_1 = Label(win7, text='')
                lblspace7_1.pack()
                lbl7_2 = Label(win7, text='Enter file name:')
                lbl7_2.pack()
                ent7_1 = Entry(win7, borderwidth=5)
                ent7_1.pack()
                lblspace7_2 = Label(win7, text='')
                lblspace7_2.pack()
                lbl7_3 = Label(win7, text='Choose file type:')
                lbl7_3.pack()
                clicked5 = StringVar()
                clicked5.set('.csv')
                drp5 = OptionMenu(win7, clicked5, '.csv')
                drp5.pack()
                lblspace7_9 = Label(win7, text='')
                lblspace7_9.pack()

                def bt7_1_clicked():
                    bt7_1.configure(state=DISABLED)
                    mycursor.execute(f'select * from {tab}')
                    data = mycursor.fetchall()
                    list_data = []
                    for i in data:
                        list_data.append(list(i))
                    csv_loc = home_dir_path+'{}\\{}{}'.format(
                        clicked4.get(), ent7_1.get(), clicked5.get())
                    with open(csv_loc, 'w', newline='') as f:
                        writer = csv.writer(f)
                        try:
                            writer.writerow(
                                ['RollNo', 'Name', 'Physics', 'Chemistry', 'Maths', 'ComputerSc', 'English'])
                            writer.writerows(list_data)
                            lbl7_5 = Label(
                                win7, text='Data written into file.')
                            lbl7_5.pack()
                        except:
                            lbl7_4 = Label(
                                win7, text='Error occured while writing file!', fg='red')
                            lbl7_4.pack()

                bt7_1 = Button(win7, text='PROCEED', command=bt7_1_clicked)
                bt7_1.pack()
                lblspace7_10 = Label(win7, text='')
                lblspace7_10.pack()

        bt2 = Button(root, text="Enter", command=bt2_clicked, width=15)
        bt2.pack()
        lblspace = Label(root, text='', bg='#D3D3D3')
        lblspace.pack()

    elif pswd_inp_hash in pswd2 and ent1.get() in usernm2 and clicked3.get() == 'Student':

        def grade(x):
                if x in range(21):
                    grd = "E2"
                elif x in range(21, 33):
                    grd = "E2"
                elif x in range(33, 41):
                    grd = "D"
                elif x in range(41, 51):
                    grd = "C2"
                elif x in range(51, 61):
                    grd = "C1"
                elif x in range(61, 71):
                    grd = "B2"
                elif x in range(71, 81):
                    grd = "B1"
                elif x in range(81, 91):
                    grd = "A2"
                elif x in range(91, 101):
                    grd = "A1"
                return (grd)

        ent1.configure(bg='#00BFFF')
        ent2.configure(bg='#00BFFF')
        entry1 = ent1.get()
        bt1.configure(state=DISABLED)
        root = Toplevel()
        root.geometry('300x395')
        root.title('HOME')
        root.iconbitmap(icon_img)
        root.configure(bg="#D3D3D3")

        def btclosemain02_clicked():
            root.destroy()
        btclosemain02 = Button(root, text='EXIT', bg='red',
                               command=btclosemain02_clicked)
        btclosemain02.pack(side=TOP, anchor=NE)
        lbl3 = Label(root, text='Access granted!', fg="#00BFFF", bg='#D3D3D3')
        lbl3.pack()
        l1.append(1)
        lbl4 = Label(root, text='', bg='#D3D3D3')
        lbl4.pack()
        lblnmdisp = Label(root, text='Welcome '+entry1,
                          font=('Calibri', 12), bg='#D3D3D3')
        lblnmdisp.pack()
        lblhome = Label(root, text="HOME", font=(
            'Calibri', 16, 'bold'), bg='#D3D3D3')
        lblhome.pack()
        lblspace10 = Label(root, text='', bg='#D3D3D3')
        lblspace10.pack()
        lbltitle5 = Label(root, text="Select class:", bg='#D3D3D3')
        lbltitle5.pack()
        clicked2 = StringVar()
        clicked2.set('11 A')
        drp2 = OptionMenu(root, clicked2, "11 A", "11 B")
        drp2.pack()
        lblspace52 = Label(root, text='', bg='#D3D3D3')
        lblspace52.pack()
        lbl58 = Label(root, text='Select exam:', bg='#D3D3D3')
        lbl58.pack()
        clicked7 = StringVar()
        clicked7.set('SA 1')
        drp7 = OptionMenu(root, clicked7, 'SA 1', 'SA 2')
        drp7.pack()
        lblspace51 = Label(root, text='', bg='#D3D3D3')
        lblspace51.pack()
        lblspace60 = Label(root, text='', bg='#D3D3D3')
        lblspace60.pack()

        def bt3_clicked():
            tab = classdict[clicked2.get()]+'_'+examsdict[clicked7.get()]
            win3 = Toplevel()
            win3.geometry('325x450')
            win3.title('VIEW')
            win3.iconbitmap(icon_img)
            lbl18 = Label(
                win3, text="Enter the RollNo of the student whose data is to be accessed")

            def btclosewin3_clicked():
                win3.destroy()
            btclosewin3 = Button(win3, text='EXIT', bg='red',
                                 command=btclosewin3_clicked)
            btclosewin3.pack(side=TOP, anchor=NE)
            lbl18.pack()

            def bt6_clicked():
                bt6.configure(state=DISABLED)

                chk = ent9.get()
                mycursor.execute("select rollno from "+tab+"")
                rno = mycursor.fetchall()
                l4 = []
                for m in rno:
                    l4.append(m)
                l5 = []
                for u in l4:
                    l5.append(str(u[0]))
                if chk not in l5:
                    lblspace30 = Label(win3, text='')
                    lblspace30.pack()
                    lbl19 = Label(win3, text="Data does not exist!", fg="red")
                    lbl19.pack()
                    lblspace31 = Label(win3, text='')
                    lblspace31.pack()

                else:
                    mycursor.execute(
                        "select max(physics+chemistry+maths+computer+english) from "+tab+"")
                    op2 = mycursor.fetchone()

                    mycursor.execute(
                        "select min(physics+chemistry+maths+computer+english) from "+tab+"")
                    op3 = mycursor.fetchone()

                    mycursor.execute("select * from "+tab +
                                     " where RollNo="+chk+"")
                    op1 = mycursor.fetchall()

                    l1 = []
                    for i in op1:
                        l1.append(i)

                    a1, b1, c1, d1, e1, f1, g1 = l1[0]
                    c1, d1, e1, f1, g1 = int(c1), int(
                        d1), int(e1), int(f1), int(g1)

                    tot = c1+d1+e1+f1+g1

                    lblspace8 = Label(win3, text='')
                    lblspace8.pack()

                    lblrln = Label(win3, text="RollNo: "+str(a1) +
                                   "    Name: "+b1, font='TkHeadingFont')
                    lblrln.pack()

                    lblspace50 = Label(win3, text='')
                    lblspace50.pack()

                    tbl = PrettyTable()
                    tbl.field_names = ['Physics', 'Chemistry',
                                       'Maths', 'ComputerSc', 'English']
                    tbl.add_row([str(c1), str(d1), str(e1), str(f1), str(g1)])
                    tbl.add_row(
                        [grade(c1), grade(d1), grade(e1), grade(f1), grade(g1)])

                    lblprt = Label(win3, text=tbl, font='TkHeadingFont')
                    lblprt.pack()
                    lblspace9 = Label(win3, text='')
                    lblspace9.pack()

                    mycursor.execute(
                        "select rollno,(physics+chemistry+maths+computer+english) from "+tab+"")
                    op1 = mycursor.fetchall()
                    d1 = {}
                    for i in op1:
                        d1[i[0]] = i[1]

                    sort_op1 = sorted(d1.items(), key=lambda t: t[1])
                    sort_op1.reverse()

                    d2 = {}
                    for i in sort_op1:
                        d2[i[0]] = i[1]
                    countxy = 0
                    for i in d2:
                        if str(i) == str(chk):
                            countxy += 1
                            break
                        else:
                            countxy += 1

                    classtot = 0
                    for i in d1:
                        classtot += d1[i]

                    lbl26 = Label(win3, text="Average score: " +
                                  str(tot/5), font='TkHeadingFont')
                    lbl26.pack()
                    lbl27 = Label(win3, text="Total score: "+str(tot))
                    lbl27.pack()
                    lbl28 = Label(win3, text="Average total: " +
                                  str(round(classtot/len(d1), 2)), font='TkHeadingFont')
                    lbl28.pack()
                    lbl29 = Label(win3, text="Class rank: " +
                                  str(countxy), font='TkHeadingFont')
                    lbl29.pack()
                    lbl30 = Label(win3, text="Highest total: " +
                                  str(op2[0]), font='TkHeadingFont')
                    lbl30.pack()
                    lbl31 = Label(win3, text="Lowest total: " +
                                  str(op3[0]), font='TkHeadingFont')
                    lbl31.pack()
                    lblspace7 = Label(win3, text='')
                    lblspace7.pack()

            ent9 = Entry(win3, width=5, borderwidth=5)
            ent9.pack()
            bt6 = Button(win3, text="Enter", command=bt6_clicked)
            bt6.pack()

        bt3 = Button(root, text='Enter', command=bt3_clicked, width=15)
        bt3.pack()
        lblspace52 = Label(root, text='', bg='#D3D3D3')
        lblspace52.pack()

    else:
        ent1.configure(bg='#F25278')
        ent2.configure(bg='#F25278')
        bt1.configure(state=DISABLED)
        lbl3 = Label(root1, text='Access denied!', fg="red", bg='#D3D3D3')
        lbl3.pack()
        lblspace54 = Label(root1, text='', bg='#D3D3D3')
        lblspace54.pack()


bt1 = Button(root1, width=15, text="Enter", command=bt1_clicked)
bt1.pack()
lblspace53 = Label(root1, text='', bg='#D3D3D3')
lblspace53.pack()

root1.mainloop()