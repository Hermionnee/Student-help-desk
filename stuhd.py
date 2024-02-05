import tkinter as tk
from tkinter import font  as tkfont
from PIL import ImageTk
from tkinter import ttk

from tkinter import*
from tkinter import messagebox
import webbrowser


class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")


        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, mainmenu, importantcontact,lecturelinks,lablocator):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame


            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):

        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.controller.geometry("1600x800")
        self.configure(bg="#912CEE")
        self.bg = ImageTk.PhotoImage(file="student 3.jpg")
        self.bgimage = Label(self, image=self.bg)
        self.bgimage.pack(padx=0,pady=20)

        startpage_label=Label(self,text="WELCOME VIITIANS",font="Impact 35 bold",fg="black",bg="#912CEE")
        startpage_label.pack(side="top",fill="x", pady=10)

        framelogin = Frame(self, bg="#912CEE")
        framelogin.place(x=950, y=150, height=400, width=400)

        titlelogin = Label(framelogin, text="STUDENT LOGIN", font="Impact 35 bold", fg="black", bg="#912CEE")
        titlelogin.place(x=50, y=30)
        userlogin = Label(framelogin, text="User ID", font="Goudy 15 bold", fg="black", bg="#912CEE")
        userlogin.place(x=30, y=120)

        self.text_user = Entry(framelogin, font="times 15", bg="white")
        self.text_user.place(x=30, y=150)
        self.text_password = Entry(framelogin, font="times 15", bg="white",show="•")
        self.text_password.place(x=30, y=230)
        self.text_password.bind("<FocusIn>")

        forg_btn = Button(framelogin, text="Forgot password", font="times 15", fg="black",
                          bg="#912CEE", bd=0,command=self.forgot_function)
        forg_btn.place(x=30, y=280)
        login_btn = Button(framelogin, text="Login",command=self.login_function, font="times 15", fg="black",
                           bg="white", )
        login_btn.place(
            x=200, y=280, width=100, height=40)

        passlogin = Label(framelogin, text="Password", font="Goudy 15 bold", fg="black", bg="#912CEE")
        passlogin.place(
            x=30, y=200)

    def login_function(self):
        if self.text_user.get() == '' or self.text_password.get() == '':
                messagebox.showerror(title="error", message="all field required")
        elif self.text_user.get()==self.text_password.get() and self.text_user.get().isnumeric() and self.text_password.get().isnumeric():
            self.controller.show_frame("mainmenu")

        else :
            messagebox.showerror(message="invalid credentials")

    def forgot_function(self):
            messagebox.showinfo(message="Hint :PRN number", parent=self)


class mainmenu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        mainmenu_label=Label(self,text="STUDENT HELP DESK",font="Impact 40 bold",fg="black",bg="#912CEE")
        mainmenu_label.pack(side="top",fill="x", pady=20)



        mainmenu_label1=Label(self,text="Mainmenu",font="Impact 25 bold")
        mainmenu_label1.pack(padx=40,pady=25,)

        but_login=Button(self,text="Back to login",font="arial 12 bold",command=lambda :controller.show_frame("StartPage"),
                         bg="#912CEE")
        but_login.place(x=50,y=620)

        mainmenu_frame=Frame(self,bg="#912CEE")
        mainmenu_frame.place(x=120, y=200, height=400, width=1150)

        mainmenu_label2=Label(mainmenu_frame,text="SELECT YOUR COMMAND",font="Impact 20",bg="#912CEE")
        mainmenu_label2.pack(side="top")

        but_ic=Button(mainmenu_frame,text="IMPORTANT CONTACTS",font="arial 12 bold",width=20,height=1,command=lambda :controller.show_frame("importantcontact"))
        but_ic.place(x=100,y=100)

        def openlink():
            webbrowser.open("https://drive.google.com/drive/folders/1iP1clom4ynUjp7Ip0Fx6NOgQoJ84HAJw?usp=sharing")

        studybutton = Button(mainmenu_frame, text="STUDY MATERIAL",font="arial 12 bold",width=20,height=1, command=openlink)
        studybutton.place(x=100,y=200)

        lecturelink_button=Button(mainmenu_frame,text="LECTURE LINKS",font="arial 12 bold",width=20,height=1,command=lambda
            :controller.show_frame("lecturelinks"))
        lecturelink_button.place(x=700,y=100)

        def tt():
            webbrowser.open("https://drive.google.com/file/d/110zNg5J4vcMb_3unvqIDvSeBS4C6_xHl/view?usp=sharing")

        linkbutton_tt = Button(mainmenu_frame, text="TIME TABLE",font="arial 12 bold",width=20,height=1, command=tt)
        linkbutton_tt.place(x=700,y=200)

        lablocatorbt=Button(mainmenu_frame,text="LAB LOCATOR",font="arial 12 bold",width=20,height=1,command=lambda:
                            controller.show_frame("lablocator"))
        lablocatorbt.place(x=700,y=300)


class importantcontact(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        my_tree = ttk.Treeview(self,cursor="exchange")

        my_tree['columns'] = ("Name of Member", "Post", "Year", "Department", " GR No.", " Contact No.", "E-Mail ID")
        my_tree.column("#0", width=50)
        my_tree.column("Name of Member", width=150, anchor=W, )
        my_tree.column("Post", anchor=W, width=150)
        my_tree.column("Year", anchor=W, width=150)
        my_tree.column("Department", anchor=W, width=150)
        my_tree.column(" GR No.", anchor=CENTER, width=150)
        my_tree.column(" Contact No.", anchor=W, width=150)
        my_tree.column("E-Mail ID", anchor=W, width=150)

        my_tree.heading("#0", text="Sr.No.", anchor=W)
        my_tree.heading("Name of Member", text="Name of Member", anchor=W)
        my_tree.heading("Post", text="Post", anchor=W)
        my_tree.heading("Year", text="Year", anchor=W)
        my_tree.heading("Department", text="Department", anchor=W)
        my_tree.heading(" GR No.", text="GR No.", anchor=W)
        my_tree.heading(" Contact No.", text="Contact No.", anchor=W)
        my_tree.heading("E-Mail ID", text="E-Mail ID", anchor=W)

        my_tree.insert(parent='', index='end', iid='0', text="1.", values=(
        " Dr. V. S. Deshpande", "Director", "Faculty Members", "E & TC", "NA", "NA", "director@viit.ac.in"))
        my_tree.insert(parent='', index='end', iid='1', text="2.", values=(
        "Dr. J. V. Bagade", "Dean Students Affair", "Faculty Members", "IT", "NA", "NA", "deanstudent@viit.ac.in"))
        my_tree.insert(parent='', index='end', iid='2', text="3.", values=(
        "Mrs. A. P. Navghane", "Associate Dean Students Affair", "Faculty Members", "E & TC", "NA", "NA",
        "associate-deanstudent@viit.ac.in"))
        my_tree.insert(parent='', index='end', iid='3', text="4.", values=(
        "Mr. Mahendra Gadge", "Representative", "Faculty Members", "Mechanical", "NA", "9923204960",
        " mahendra.gadge@viit.ac.in"))
        my_tree.insert(parent='', index='end', iid='4', text="5.", values=(
        "Mr. Saurav Chavan", "Sports President", "B.Tech", "E & TC", "21810942", "9284591256 ",
        "saurav.21810942@viit.ac.in"))
        my_tree.insert(parent='', index='end', iid='5', text="6.", values=(
        "Mr. Jainil Jain ", "Vishwaracer Club President", "B.Tech", "Mechanical", "21810890", "9028843751 ",
        "jainil.21810890@viit.ac.in"))
        my_tree.insert(parent='', index='end', iid='6', text="7.", values=(
        "Ms. Harsha Gupta", "Cultural President", "B.tech", "E & TC", "21810512", "8982814410",
        "harsha.21810512@viit.ac.in"))
        my_tree.insert(parent='', index='end', iid='7', text="8.", values=(
        "Sourabh Pawar", "NSS President", "T.Y.B.Tech", "Computer", "21911190", " 9658886555",
        "sourabh.21911190@viit.ac.in"))
        my_tree.insert(parent='', index='end', iid='8', text="9.", values=(
        "Hritik Chalse", "TedX VIIT President", "B.Tech", "Mechanical", "21810052", "8796618899 ",
        "hritik.21810052@viit.ac.in"))
        my_tree.insert(parent='', index='end', iid='9', text="10.", values=(
        "Suraj Surkutla", "Rotract President", "Third Year", "E & TC", "21910606", "8888606148 ",
        "suraj.21910606@viit.ac.in"))
        my_tree.insert(parent='', index='end', iid='10', text="11.", values=(
        " Dhruv Kolhatkar", "Magazine President", "Third Year", "IT", "21910005", "NA", "dhruv.21910005@viit.ac.in"))
        my_tree.insert(parent='', index='end', iid='11', text="12.", values=(
        "Parikshit Mali", "CEC President", "Third Year", "E & TC", "21910387", "9049550954",
        "parikshit.21910387@viit.ac.in"))

        my_tree.pack(pady=100)

        but_login = Button(self, text="Back to login", font="arial 12 bold",
                           command=lambda: controller.show_frame("StartPage"),
                           bg="#912CEE")
        but_login.place(x=40, y=600)

        but_ic = Button(self, text="Back mainmenu", font="arial 12 bold",
                        command=lambda: controller.show_frame("mainmenu"),bg="#912CEE")
        but_ic.place(x=1150, y=600)

class lecturelinks(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        lecturelink_label = Label(self, text="STUDENT HELP DESK", font="Impact 40 bold", fg="black", bg="#912CEE")
        lecturelink_label.pack(side="top", fill="x", pady=20)

        lecturelink_label1=Label(self,text="LECTURE LINKS",font="Impact 20 bold",fg="black")
        lecturelink_label1.pack(padx=400,pady=20)

        #theory
        lecture_frame1=Frame(self,bg="#912CEE")
        lecture_frame1.place(x=50, y=200, height=400, width=200)
        lecturef1l1=Label(lecture_frame1,text="THEORY",font="Impact 20 ",bg="#912CEE")
        lecturef1l1.pack(side="top")

        def openlink1():
            webbrowser.open("https://meet.google.com/trj-oaai-pkp")

        linkbutton = Button(lecture_frame1, text="PYTHON",font="arial 12",width=20,height=1,command=openlink1)

        def openlink2():
            webbrowser.open("https://us02web.zoom.us/j/89370931455?pwd=MDFUd2M5cFNhNERCbDlBN2FhQStkdz09")

        linkbutton1 = Button(lecture_frame1, text="SMART SENSORS",font="arial 12",width=20,height=1, command=openlink2)

        def openlink3():
            webbrowser.open("https://us02web.zoom.us/j/85060360024?pwd=Nkd0ekNLZkU2a0toY2")

        linkbutton2 = Button(lecture_frame1, text="BXE",font="arial 12",width=20,height=1, command=openlink3)

        def openlink4():
            webbrowser.open("https://zoom.us/j/96756985146?pwd=SVR1Sm1ianJBRU5DZlFFbFJBYW54UT09")

        linkbutton3 = Button(lecture_frame1, text="EM",font="arial 12",width=20,height=1, command=openlink4)

        def openlink5():
            webbrowser.open("https://us02web.zoom.us/j/83498664969?pwd=dTJxNDd4Z1dvK2tnSjhpU1RHQUV0QT09")

        linkbutton4 = Button(lecture_frame1, text="PDPE",font="arial 12",width=20,height=1, command=openlink5)

        def openlink6():
            webbrowser.open("https://us02web.zoom.us/j/85217902263?pwd=R1dZeGh6bWVDRVN2d3gwQW5W")

        linkbutton5 = Button(lecture_frame1, text="CHEMISTRY",font="arial 12",width=20,height=1, command=openlink6)

        linkbutton.place()
        linkbutton.place(x=5,y=50)
        linkbutton1.place(x=5,y=100)
        linkbutton2.place(x=5,y=150)
        linkbutton3.place(x=5,y=200)
        linkbutton4.place(x=5,y=250)
        linkbutton5.place(x=5,y=300)

        #L1
        lecture_frame2 = Frame(self, bg="#912CEE")
        lecture_frame2.place(x=350, y=200, height=400, width=200)
        lecturef2l2 = Label(lecture_frame2, text="L1 TUTORIAL", font="Impact 20 ", bg="#912CEE")
        lecturef2l2.pack(side="top")

        def openlink7():
            webbrowser.open("https://meet.google.com/vmk-mnjn-eyx")

        linkbutton6 = Button(lecture_frame2, text="PE ",font="arial 12",width=20,height=1, command=openlink7)

        def openlink8():
            webbrowser.open("https://us02web.zoom.us/j/83498664969?pwd=dTJxNDd4Z1dvK2tnSjhpU1RHQUV0QT09")

        linkbutton7 = Button(lecture_frame2, text="PDP",font="arial 12",width=20,height=1, command=openlink8)

        def openlink9():
            webbrowser.open("https://zoom.us/j/4071256083?pwd=Zkw3SHJadzRpdEVFbmJlSXN6YXRudz09")

        linkbutton8 = Button(lecture_frame2, text="BXE",font="arial 12",width=20,height=1, command=openlink9)

        def openlink10():
            webbrowser.open("https://us02web.zoom.us/j/86583555210?pwd=bkg1RjBGZGVaeWdmMWlKRFlqUnh5dz09")

        linkbutton9 = Button(lecture_frame2, text="QA" ,font="arial 12",width=20,height=1, command=openlink10)

        def openlink11():
            webbrowser.open("https://zoom.us/j/91643626038?pwd=UkI4RlZwYUQyd20zejRGOWp1RGVVdz09")

        linkbutton10 = Button(lecture_frame2, text="EM",font="arial 12",width=20,height=1, command=openlink11)

        def openlink12():
            webbrowser.open("https://us02web.zoom.us/j/87411741067?pwd=bUhJd2dHSTFjL05oOGZCZXhGdUpHdz09")

        linkbutton11 = Button(lecture_frame2, text="SS",font="arial 12",width=20,height=1, command=openlink12)

        linkbutton7.place(x=5, y=50)
        linkbutton8.place(x=5, y=100)
        linkbutton9.place(x=5, y=150)
        linkbutton10.place(x=5, y=200)
        linkbutton11.place(x=5, y=250)

        #l2

        lecture_frame3 = Frame(self, bg="#912CEE")
        lecture_frame3.place(x=750, y=200, height=400, width=200)
        lecturef3l3 = Label(lecture_frame3, text="L2 TUTORIAL", font="Impact 20 ", bg="#912CEE")
        lecturef3l3.pack(side="top")

        def openlink13():
            webbrowser.open("https://meet.google.com/vmk-mnjn-eyx")

        linkbutton12 = Button(lecture_frame3, text="PE" ,font="arial 12",width=20,height=1, command=openlink13)

        def openlink14():
            webbrowser.open("https://meet.google.com/qxz-zvtp-imf")

        linkbutton13 = Button(lecture_frame3, text="PDP",font="arial 12",width=20,height=1, command=openlink14)

        def openlink15():
            webbrowser.open("https://zoom.us/j/97932338863?pwd=VmRrdkZlRVZ6V1JQZzI5RjZwYUs1UT09")

        linkbutton14 = Button(lecture_frame3, text="BXE",font="arial 12",width=20,height=1, command=openlink15)

        def openlink16():
            webbrowser.open("https://zoom.us/j/93364073352")

        linkbutton15 = Button(lecture_frame3, text="QA" ,font="arial 12",width=20,height=1, command=openlink16)

        def openlink17():
            webbrowser.open("https://zoom.us/j/91643626038?pwd=UkI4RlZwYUQyd20zejRGOWp1RGVVdz09")

        linkbutton16 = Button(lecture_frame3, text="EM" ,font="arial 12",width=20,height=1, command=openlink17)

        def openlink18():
            webbrowser.open("https://us02web.zoom.us/j/87411741067?pwd=bUhJd2dHSTFjL05oOGZCZXhGdUpHdz09")

        linkbutton17 = Button(lecture_frame3, text="SS",font="arial 12",width=20,height=1, command=openlink18)

        linkbutton12.place(x=5, y=50)
        linkbutton13.place(x=5, y=100)
        linkbutton14.place(x=5, y=150)
        linkbutton15.place(x=5, y=200)
        linkbutton16.place(x=5, y=250)
        linkbutton17.place(x=5,y=300)
        #l3

        lecture_frame4 = Frame(self, bg="#912CEE")
        lecture_frame4.place(x=1100, y=200, height=400, width=200)
        lecturef4l4 = Label(lecture_frame4, text="L3 TUTORIAL", font="Impact 20 ", bg="#912CEE")
        lecturef4l4.pack(side="top")

        def openlink19():
            webbrowser.open("https://meet.google.com/avf-pxfi-brw")

        linkbutton18 = Button(lecture_frame4, text="PE",font="arial 12",width=20,height=1, command=openlink19)

        def openlink20():
            webbrowser.open("https://meet.google.com/giv-mjfu-zpf")

        linkbutton19 = Button(lecture_frame4, text="PDP",font="arial 12",width=20,height=1, command=openlink20)

        def openlink21():
            webbrowser.open("https://meet.google.com/cxd-pnmj-wmf")

        linkbutton20 = Button(lecture_frame4, text="BXE",font="arial 12",width=20,height=1, command=openlink21)

        def openlink22():
            webbrowser.open("https://zoom.us/j/93364073352")

        linkbutton21 = Button(lecture_frame4, text="QA",font="arial 12",width=20,height=1, command=openlink22)

        def openlink23():
            webbrowser.open("https://zoom.us/j/91643626038?pwd=UkI4RlZwYUQyd20zejRGOWp1RGVVdz09")

        linkbutton22 = Button(lecture_frame4, text="EM",font="arial 12",width=20,height=1, command=openlink23)

        def openlink24():
            webbrowser.open("https://meet.google.com/cje-coau-oun")

        linkbutton23 = Button(lecture_frame4, text="SS",font="arial 12",width=20,height=1, command=openlink24)

        linkbutton18.place(x=5, y=50)
        linkbutton19.place(x=5, y=100)
        linkbutton20.place(x=5, y=150)
        linkbutton21.place(x=5, y=200)
        linkbutton22.place(x=5, y=250)
        linkbutton23.place(x=5, y=300)





        but_ic = Button(self, text="Back mainmenu", font="arial 12 bold",
                        command=lambda: controller.show_frame("mainmenu"), bg="#912CEE")
        but_ic.place(x=1150, y=650)

        but_login = Button(self, text="Back to login", font="arial 12 bold",
                           command=lambda: controller.show_frame("StartPage"),
                           bg="#912CEE")
        but_login.place(x=50, y=650)









class lablocator(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        lecturelink_label = Label(self, text="STUDENT HELP DESK", font="Impact 40 bold", fg="black", bg="#912CEE")
        lecturelink_label.pack(side="top", fill="x", pady=20)

        def popup():
            if userentry.get() == ("Chemistry"):
                messagebox.showinfo("Chemistry Lab", "Lab no. is E314")
            elif userentry.get() == ("Bxe"):
                messagebox.showinfo("Bxe Lab", "Lab No. is C107")
            elif userentry.get() == ("Physics"):
                messagebox.showinfo("Physics Lab", "Lab No. is E128")
            elif userentry.get() == ("Python"):
                messagebox.showinfo("Computer Lab", "Lab No. is E111")
            elif userentry.get() == ("Ss"):
                messagebox.showinfo("Smart Sensor Lab", "Lab No. is E215")
            elif userentry.get() == ("Em"):
                messagebox.showinfo("Mechanics Lab", "Lab No. is E214")
            else:
                messagebox.showerror("No room record")



        lab_frame=Frame(self,bg="#912CEE")
        lab_frame.place(x=450,y=200,height=400, width=500)

        ll_label=Label(lab_frame,text="Lab Locator",font="Impact 20 bold", fg="black", bg="#912CEE")
        ll_label.pack(side="top")

        userentry = StringVar()
        uservalue = Label(lab_frame,text="LAB NAME",font="Goudy 15 bold", fg="black",bg="#912CEE")
        uservalue.place(x=100,y=200)


        userentry = Entry(lab_frame, textvariable=uservalue)
        userentry.place(x=250,y=200,)


        submit_bt=Button(lab_frame,text="Submit", command=popup,width=20,height=1)
        submit_bt.place(x=100,y=300)

        but_ic = Button(self, text="Back mainmenu", font="arial 12 bold",
                        command=lambda: controller.show_frame("mainmenu"), bg="#912CEE")
        but_ic.place(x=1150, y=650)

        but_login = Button(self, text="Back to login", font="arial 12 bold",
                           command=lambda: controller.show_frame("StartPage"),
                           bg="#912CEE")
        but_login.place(x=50, y=650)


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
