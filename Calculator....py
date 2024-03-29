import customtkinter as ctk


currentText = "0"
num = 0
op = ""

def addText(str):
    global currentText

    if float(currentText) ==0 and str !='.' and '.' not in currentText:
        currentText = ""
        currentText = currentText + str
    elif str == '.' and '.' in currentText:
        currentText = currentText
    else :
        currentText = currentText + str
    updateText()

def CE():
    global currentText
    global num
    global op
    currentText = "0"
    num = 0
    op = ""
    updateText()

def C():
    global currentText
    currentText = "0"
    updateText()
def updateText():
    global currentText
    if len(currentText) > 12:
        currentText = currentText[:12]
    clacLabel.configure(text=currentText)

app = ctk.CTk()
app.geometry("350x500")
app.title("Calculator")
app.configure(bg_color="white", fg_color="white")

calcFrame = ctk.CTkFrame(app, width=340, height=70,
                        bg_color="white", fg_color="white")
calcFrame.grid(row=0, column=0, padx=5, pady=5)

clacLabel = ctk.CTkLabel(calcFrame, text="0", width=340, height=50,
                         anchor="e", bg_color="white",
                        font=ctk.CTkFont(size=50))
clacLabel.grid(row=1, column=0, padx=5, pady=5)

btnFrame = ctk.CTkFrame(app, width=340, height=400,
                        bg_color = "white", fg_color = "white")
btnFrame.grid(row=1, column=0, padx=5, pady=5)

btnCE = ctk.CTkButton(btnFrame, width=75, height=65, text="CE",
                      bg_color="white", fg_color="gray", anchor="center",
                      font=ctk.CTkFont(size=30), command=CE)
btnCE.grid(row=0, column=0, padx=2, pady=2)

btnC = ctk.CTkButton(btnFrame, width=75, height=65, text="C",
                      bg_color="white", fg_color="gray", anchor="center",
                      font=ctk.CTkFont(size=30), command=C)
btnC.grid(row=0, column=1, padx=2, pady=2)

btnBack = ctk.CTkButton(btnFrame, width=75, height=65, text="<--",
                      bg_color="white", fg_color="gray", anchor="center",
                      font=ctk.CTkFont(size=30))
btnBack.grid(row=0, column=2, padx=2, pady=2)

btnDivide = ctk.CTkButton(btnFrame, width=75, height=65, text="/",
                      bg_color="white", fg_color="gray", anchor="center",
                      font=ctk.CTkFont(size=30))
btnDivide.grid(row=0, column=3, padx=2, pady=2)



btn7 = ctk.CTkButton(btnFrame, width=75, height=65, text="7", text_color="black",
                      bg_color="white", fg_color="gray75", anchor="center",
                      font=ctk.CTkFont(size=30), command=lambda : addText("7"))
btn7.grid(row=1, column=0, padx=2, pady=2)

btn8 = ctk.CTkButton(btnFrame, width=75, height=65, text="8", text_color="black",
                      bg_color="white", fg_color="gray75", anchor="center",
                      font=ctk.CTkFont(size=30), command=lambda : addText("8"))
btn8.grid(row=1, column=1, padx=2, pady=2)

btn9 = ctk.CTkButton(btnFrame, width=75, height=65, text="9", text_color="black",
                      bg_color="white", fg_color="gray75", anchor="center",
                      font=ctk.CTkFont(size=30), command=lambda : addText("9"))
btn9.grid(row=1, column=2, padx=2, pady=2)

btnMulitply = ctk.CTkButton(btnFrame, width=75, height=65, text="X",
                      bg_color="white", fg_color="gray", anchor="center",
                      font=ctk.CTkFont(size=30))
btnMulitply.grid(row=1, column=3, padx=2, pady=2)

btn4 = ctk.CTkButton(btnFrame, width=75, height=65, text="4", text_color="black",
                      bg_color="white", fg_color="gray75", anchor="center",
                      font=ctk.CTkFont(size=30), command=lambda : addText("4"))
btn4.grid(row=2, column=0, padx=2, pady=2)

btn5 = ctk.CTkButton(btnFrame, width=75, height=65, text="5", text_color="black",
                      bg_color="white", fg_color="gray75", anchor="center",
                      font=ctk.CTkFont(size=30), command=lambda : addText("5"))
btn5.grid(row=2, column=1, padx=2, pady=2)

btn6 = ctk.CTkButton(btnFrame, width=75, height=65, text="6", text_color="black",
                      bg_color="white", fg_color="gray75", anchor="center",
                      font=ctk.CTkFont(size=30), command=lambda : addText("6"))
btn6.grid(row=2, column=2, padx=2, pady=2)

btnSubtract = ctk.CTkButton(btnFrame, width=75, height=65, text="-",
                      bg_color="white", fg_color="gray", anchor="center",
                      font=ctk.CTkFont(size=30))
btnSubtract.grid(row=2, column=3, padx=2, pady=2)

btn1 = ctk.CTkButton(btnFrame, width=75, height=65, text="1", text_color="black",
                      bg_color="white", fg_color="gray75", anchor="center",
                      font=ctk.CTkFont(size=30), command=lambda : addText("1"))
btn1.grid(row=3, column=0, padx=2, pady=2)

btn2 = ctk.CTkButton(btnFrame, width=75, height=65, text="2", text_color="black",
                      bg_color="white", fg_color="gray75", anchor="center",
                      font=ctk.CTkFont(size=30), command=lambda : addText("2"))
btn2.grid(row=3, column=1, padx=2, pady=2)

btn3 = ctk.CTkButton(btnFrame, width=75, height=65, text="3", text_color="black",
                      bg_color="white", fg_color="gray75", anchor="center",
                      font=ctk.CTkFont(size=30), command=lambda : addText("3"))
btn3.grid(row=3, column=2, padx=2, pady=2)

btnAddition = ctk.CTkButton(btnFrame, width=75, height=65, text="+",
                      bg_color="white", fg_color="gray", anchor="center",
                      font=ctk.CTkFont(size=30))
btnAddition.grid(row=3, column=3, padx=2, pady=2)

btnOpposite = ctk.CTkButton(btnFrame, width=75, height=65, text="+/-", text_color="black",
                      bg_color="white", fg_color="gray75", anchor="center",
                      font=ctk.CTkFont(size=30))
btnOpposite.grid(row=4, column=0, padx=2, pady=2)

btn0 = ctk.CTkButton(btnFrame, width=75, height=65, text="0", text_color="black",
                      bg_color="white", fg_color="gray75", anchor="center",
                      font=ctk.CTkFont(size=30), command=lambda : addText("0"))
btn0.grid(row=4, column=1, padx=2, pady=2)

btnDot = ctk.CTkButton(btnFrame, width=75, height=65, text=".", text_color="black",
                      bg_color="white", fg_color="gray75", anchor="center",
                      font=ctk.CTkFont(size=30), command=lambda : addText("."))
btnDot.grid(row=4, column=2, padx=2, pady=2)

btnEqual = ctk.CTkButton(btnFrame, width=75, height=65, text="=",
                      bg_color="white", fg_color="gray", anchor="center",
                      font=ctk.CTkFont(size=30))
btnEqual.grid(row=4, column=3, padx=2, pady=2)


app.mainloop()