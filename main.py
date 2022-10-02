from tkinter import *
from tkinter import messagebox
import passwordGenerator
import pyperclip
import json
BLUE="#abdbe3"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    newpass=passwordGenerator.genPass()
    pass_entry.delete(0, END)
    pass_entry.insert(index=0,string=newpass)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    websit=str(web_entry.get())
    emailuser=str(Emailuser_entry.get())
    password=str(pass_entry.get())

    if len(websit)==0 or len(emailuser)==0 or len(password)==0:
        messagebox.showerror(title="Empty fields", message="please fill all the fields")
    else:
        is_it_ok=messagebox.askokcancel(title="Details",message=f"Entered details:\n"
                                                                f"Website:{websit}\n"
                                                                f"Email/Username:{emailuser}\n"
                                                                f"Password:{password}\n\ncontinue?")
        if is_it_ok==True:
            datadict = {websit: {"Email/UserName": emailuser, "Password": password}}

            try:
                with open("data.json" ,"r") as datafile:
                    data=json.load(datafile)
            except FileNotFoundError:
                with open("data.json","w") as datafile:
                    json.dump(datadict,datafile,indent=4)
            else:
                with open("data.json", "w") as datafile:
                  data.update(datadict)
                  json.dump(data,datafile,indent=4)

            finally:
                messagebox.showinfo(title="Success!",message="Details saved. Password copied to clipboard ")
                pyperclip.copy(password)
                web_entry.delete(0,END)
                pass_entry.delete(0,END)
# ---------------------------- SEARCH ------------------------------- #
def search():
    try:
        with open("data.json", "r") as datafile:
            data = json.load(datafile)
    except FileNotFoundError:
        messagebox.showinfo(title="No Record !", message="No Record found")

    else:
        if web_entry.get() in data:
            websitename=web_entry.get()
            websiteuser = data[web_entry.get()]["Email/UserName"]
            websitepass = data[web_entry.get()]["Password"]
            print(websiteuser,websiteuser,websitepass)
            pyperclip.copy(websitepass)
            messagebox.showinfo(title="No Record !", message=f"Website: {websitename}\n"
                                                                    f"Email/Username: {websiteuser}\n"
                                                                    f"Password: {websitepass}\n"
                                                             f"\npassword copied to clipboard!")
        elif len(web_entry.get())==0 :
            messagebox.showinfo(title="Empty field", message="please fill required fields")
        else:
            messagebox.showinfo(title="Empty field", message="please fill required fields")
    finally:

        web_entry.delete(0,END)
        pass_entry.delete(0,END)


# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.config(pady=20,padx=20,bg=BLUE,highlightthickness=0)
#window.minsize(120,100)
window.title("Password Manager")

mycanvas=Canvas( width=140, height=160,bg=BLUE,highlightthickness=0)
lock_img=PhotoImage(file="logo.png")
mycanvas.create_image(70,85,image=lock_img,)
mycanvas.grid(column=1,row=0)

website_lable=Label(text="Website:",font=("arial",10,"normal"),bg=BLUE,highlightthickness=0)
website_lable.grid(column=0,row=1)
web_entry=Entry(width=23)
web_entry.grid(column=1,row=1)
web_entry.focus()
web_search=Button(text="Search",width=14,command=search)
web_search.grid(column=2,row=1)

Emailuser_lable=Label(text="Email/User Name:",font=("arial",10,"normal"),bg=BLUE,highlightthickness=0)
Emailuser_lable.grid(column=0,row=2)
Emailuser_entry=Entry(width=41)
Emailuser_entry.grid(column=1,row=2,columnspan=2)
Emailuser_entry.insert(0,"kedar@gmail.com")

pass_lable=Label(text="Password:",font=("arial",10,"normal"),bg=BLUE,highlightthickness=0)
pass_lable.grid(column=0,row=3)
pass_entry=Entry(width=23)
pass_entry.grid(column=1,row=3)
gen_but=Button(text="Generate Password",command=generate)
gen_but.grid(column=2,row=3)

add_but=Button(width=35,text="Add",command=save)
add_but.grid(column=1,row=4,columnspan=2)

window.mainloop()