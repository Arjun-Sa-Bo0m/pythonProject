import customtkinter as ctk

def enter_clicked():
    userName = entry.get()
    addString = address.get()
    print(userName)
    print(addString)

app = ctk.CTk()
app.geometry("750x500")
app.title("Number Guesser")

labelGuessed = ctk.CTkLabel(app, text="Guess a number from 1-10:   ")
labelGuessed.grid(row=0, column=0, padx=5, pady=5)

Geussed = ctk.CTkEntry(app, placeholder_text="Your number :   ",
                       font=ctk.CTkFont(size=13))
Geussed.grid(row=0, column=1, padx=5, pady=5)

btn = ctk.CTkButton(app, text="Enter", command = enter_clicked)
btn.grid(row=1, column=1, padx=5, pady=5)

app.mainloop()