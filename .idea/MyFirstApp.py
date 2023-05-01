import customtkinter as ctk

def enter_clicked():
    print("Enter clicked")
    userName = entry.get()
    addString = address.get()
    print(userName)
    print(addString)

app = ctk.CTk()
app.title("My first app")
app.geometry("500x300")


label = ctk.CTkLabel(app, text= " Name:    ")
label.grid(row=0, column=0)

labelAddress = ctk.CTkLabel(app, text="Adress:   ")
labelAddress.grid(row=1, column=0, padx=5, pady=5)

address = ctk.CTkEntry(app, placeholder_text="Enter you adress:   ",
                       font=ctk.CTkFont(size=15))
address.grid(row=1, column=1, padx=5, pady=5)

labelAge = ctk.CTkLabel(app, text= " Age:    ")
labelAge.grid(row=2, column=0)

age= ctk.CTkEntry(app, placeholder_text="Enter you age:   ",
                       font=ctk.CTkFont(size=15))
age.grid(row=2, column=1, padx=5, pady=5)

btn=ctk.CTkButton(app, text="Enter", command = enter_clicked)
btn.grid(row=3, column=1, padx=5, pady=5)

entry = ctk.CTkEntry(app, placeholder_text="Enter your name: ")
entry.grid(row=0, column=1)

app.mainloop()