from tkinter import *
import customtkinter
from PIL import Image

app = customtkinter.CTk()
app.title('Pizzeria')
app.geometry('600x400')
customtkinter.set_appearance_mode('Dark')
customtkinter.set_default_color_theme("dark-blue")
app.iconbitmap('pizza.ico')

img = Image.open('pizza-slice.png')
#image = customtkinter.CTkImage(light_image=img)

app.image = PhotoImage(file='img.png')
logo1 = Label(app, image=app.image)
logo1.place(relx=-.2, rely=-.3)

frame_1 = customtkinter.CTkFrame(app, border_width=0, fg_color='#9d9d46', border_color='#fffcfc', width=300, height=600)
frame_1.place(relx=.0, rely=.0)


def click():
    Cost = 0
    pizza = entry_Pizza.get()
    if pizza == "Pepperoni":
        Cost = 6.35
    elif pizza == "Carbonara":
        Cost = 5.20
    elif pizza == "Margaret":
        Cost = 5.69
    elif pizza == "Bolognese":
        Cost = 5.49

    def Chec1():
        Cost1 = 0.2

    def Chec2():
        Cost2 = 0.3

    def Chec3():
        Cost3 = 0.5

    def Chec4():
        Cost4 = 0.55


    def Chec():
        frame_2.destroy()
        buttonplay2.destroy()
        checbox.destroy()
        checbox2.destroy()
        checbox3.destroy()
        checbox4.destroy()
        label_1.destroy()


        def click_Cash():

            def click34():

                en = float(entry_Code2.get())

                if en == Cost:
                    label_10 = customtkinter.CTkLabel(frame_1, text="Thanks for the purchase", font=('Arial', 14))
                    label_10.place(relx=.5, rely=.5, anchor="c")
                elif en > Cost:
                    s = en - Cost
                    label_10 = customtkinter.CTkLabel(frame_1, text=f"Thank you for your purchase! Your change {s}", font=('Arial', 14))
                    label_10.place(relx=.5, rely=.5, anchor="c")
                else:
                    label_10 = customtkinter.CTkLabel(frame_1, text="Insufficient funds", font=('Arial', 14))
                    label_10.place(relx=.5, rely=.5, anchor="c")

            buttonplay5.destroy()
            buttonplay4.destroy()
            label_9.destroy()

            label_8 = customtkinter.CTkLabel(frame_1, text='Payment', font=('Arial', 20))
            label_8.place(relx=.5, rely=.2, anchor="c")
            label_5 = customtkinter.CTkLabel(frame_1, text='Enter Sum', font=('Arial', 14))
            label_5.place(relx=.5, rely=.25, anchor="c")
            entry_Code2 = customtkinter.CTkEntry(frame_1, placeholder_text="sum", font=('Arial', 15))
            entry_Code2.place(relx=.5, rely=0.3, anchor="c")
            label_7 = customtkinter.CTkLabel(frame_1, text=f'Sum: {Cost} $', font=('Arial', 14))
            label_7.place(relx=.5, rely=.35, anchor="c")
            buttonplay3 = customtkinter.CTkButton(frame_1, text='To pay', font=('Arial', 15), text_color='#000000', fg_color='#fffcfc', command=click34)
            buttonplay3.place(relx=.5, rely=.4, anchor="c")


        def click_Card():

            def click28():
                label_11 = customtkinter.CTkLabel(frame_1, text="Thanks for the purchase", font=('Arial', 14))
                label_11.place(relx=.5, rely=.5, anchor="c")

            buttonplay5.destroy()
            buttonplay4.destroy()
            label_9.destroy()

            label_4 = customtkinter.CTkLabel(frame_1, text='Payment', font=('Arial', 20))
            label_4.place(relx=.5, rely=.15, anchor="c")
            label_5 = customtkinter.CTkLabel(frame_1, text='Enter card number', font=('Arial', 14))
            label_5.place(relx=.5, rely=.2, anchor="c")
            entry_Code = customtkinter.CTkEntry(frame_1, placeholder_text="card number", font=('Arial', 15))
            entry_Code.place(relx=.5, rely=0.25, anchor="c")
            label_6 = customtkinter.CTkLabel(frame_1, text='Enter code', font=('Arial', 14))
            label_6.place(relx=.5, rely=.3, anchor="c")
            entry_Code2 = customtkinter.CTkEntry(frame_1, placeholder_text="code", font=('Arial', 15))
            entry_Code2.place(relx=.5, rely=0.35, anchor="c")
            label_7 = customtkinter.CTkLabel(frame_1, text=f'Sum: {Cost} $', font=('Arial', 14))
            label_7.place(relx=.5, rely=.4, anchor="c")
            buttonplay3 = customtkinter.CTkButton(frame_1, text='To pay', font=('Arial', 15), text_color='#000000',fg_color='#fffcfc', command=click28)
            buttonplay3.place(relx=.5, rely=.45, anchor="c")


        label_9 = customtkinter.CTkLabel(frame_1, text='Payment method', font=('Arial', 20))
        label_9.place(relx=.5, rely=.2, anchor="c")

        buttonplay4 = customtkinter.CTkButton(frame_1, text='Cash', font=('Arial', 15), text_color='#000000',fg_color='#fffcfc', command=click_Cash)
        buttonplay4.place(relx=.5, rely=.3, anchor="c")

        buttonplay5 = customtkinter.CTkButton(frame_1, text='Сard', font=('Arial', 15), text_color='#000000',fg_color='#fffcfc', command=click_Card)
        buttonplay5.place(relx=.5, rely=.4, anchor="c")



    entry_Pizza.destroy()
    label.destroy()
    buttonplay.destroy()
    label_3.destroy()
    label_14.destroy()
    frame_10.destroy()
    frame_2 = customtkinter.CTkFrame(frame_1, border_width=2, fg_color='#9d9d46', border_color='#fffcfc', width=100,height=50)
    frame_2.place(relx=.1, rely=.05)
    label_2 = customtkinter.CTkLabel(frame_2, text=(f'Cost: {Cost} $'), font=('Arial', 15))
    label_2.place(relx=.5, rely=.45, anchor="c")
    label_1 = customtkinter.CTkLabel(frame_1, text='Choose supplements', font=('Arial', 17))
    label_1.place(relx=.5, rely=.2, anchor="c")
    checbox = customtkinter.CTkCheckBox(frame_1, text="Onion", fg_color='#dbb187',font=('Arial', 14),  command=Chec1)
    checbox.place(relx=.3, rely=.3, anchor="c")
    checbox2 = customtkinter.CTkCheckBox(frame_1, text="sour cream", fg_color='#dbb187',font=('Arial', 14),  command=Chec2)
    checbox2.place(relx=.3, rely=.4, anchor="c")
    checbox3 = customtkinter.CTkCheckBox(frame_1, text="egg", fg_color='#dbb187',font=('Arial', 14),  command=Chec3)
    checbox3.place(relx=.7, rely=.3, anchor="c")
    checbox4 = customtkinter.CTkCheckBox(frame_1, text="tomatoes", fg_color='#dbb187',font=('Arial', 14),  command=Chec4)
    checbox4.place(relx=.7, rely=.4, anchor="c")
    buttonplay2 = customtkinter.CTkButton(frame_1, text='Next', font=('Arial', 14), text_color='#000000',fg_color='#fffcfc', command=Chec)
    buttonplay2.place(relx=.5, rely=.5, anchor="c")

frame_10 = customtkinter.CTkFrame(app, border_width=1, fg_color='#9d9d46', border_color='#fffcfc', width=200,height=200)
frame_10.place(relx=.55, rely=.1)

label_14 = customtkinter.CTkLabel(frame_10, text='Menu:\n\n Pepperoni - 6.35 \n\n Carbonara - 5.20 \n\n  Margaret - 5.69 \n\n Bolognes - 5.49',  font=('Arial', 16))
label_14.place(relx=.5, rely=.47, anchor="c")


label_3 = customtkinter.CTkLabel(frame_1, text='Welcome!', font=('Arial', 24))
label_3.place(relx=.5, rely=.14, anchor="c")

label = customtkinter.CTkLabel(frame_1, text='Choose a pizza', font=('Arial', 15))
label.place(relx=.5, rely=.2, anchor="c")

entry_Pizza = customtkinter.CTkEntry(frame_1, placeholder_text="Pizza", font=('Arial', 15))
entry_Pizza.place(relx=.5, rely=.3, anchor="c")

buttonplay = customtkinter.CTkButton(frame_1, text='Next', font=('Arial', 15), text_color='#000000',fg_color='#fffcfc', command=click)
buttonplay.place(relx=.5, rely=.4, anchor="c")

app.mainloop()