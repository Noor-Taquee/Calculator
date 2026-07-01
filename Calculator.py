from tkinter import Tk,Frame,Label,Button
from math import radians,sin,cos,tan

window = Tk()

#region variables
frameList = []
componentType_1 = []
componentType_2 = []
registered = False
expression = ""
display_expression_text = ""
themeColor = "light blue"
current_theme = "dark"
bgColorType_1 = "black"
bgColorType_2 = "black"
fgColorType_1 = "white"
fgColorType_2 = themeColor
#endregion variables


#region functions
def registerComponents():
    global frameList,componentType_1,componentType_2
    frameList = [screen_frame,top_panel,option_panel,theme_panel,expression_panel,more_panel,button_panel]
    componentType_1 = [display_name,display_expression,bn_0,bn_1,bn_2,bn_3,bn_4,bn_5,bn_6,bn_7,bn_8,bn_9,]
    componentType_2 = [bn_option,bn_theme,bn_color,bn_lght,bn_dark,bn_mor,bn_les,bn_sin,bn_cos,bn_tan,bn_fac,bn_clear,bn_power,bn_delet,bn_resul,bn_add,bn_sub,bn_mul,bn_div,bn_brack,bn_decim]

def trigo(expression):
    if "sin" in expression:
        return round(sin(radians(int(expression[4:]))),ndigits = 3)
    elif "cos" in expression:
        return round(cos(radians(int(expression[4:]))),ndigits = 3)
    else:
        return round(tan(radians(int(expression[4:]))),ndigits = 3)

def factorial(n):
    return 1 if n <= 1 else n*factorial(n-1)

def refreshPage():
    for component in componentType_1:
        component.config(fg = fgColorType_1,bg = bgColorType_1)
    for component in componentType_2:
        component.config(fg = fgColorType_2,bg = bgColorType_2)
    for frame in frameList:
        frame.config(bg = bgColorType_1)
        display_name.config(fg = themeColor)

def changeColor(color):
    global themeColor,fgColorType_2,bgColorType_2
    themeColor = color
    if current_theme == "dark":
        fgColorType_2 = color
    else:
        bgColorType_2 = color
    f_cancel()


#BUTTON FUNCTIONS==========================
def f_1(event = None):
    global expression, display_expression_text
    expression += "*1" if expression and expression[-1] == ")" else "1"
    display_expression_text += "1"
    display_expression.config(text = display_expression_text,fg = fgColorType_1,bg = bgColorType_1)

def f_2(event = None):
    global expression, display_expression_text
    expression += "*2" if expression and expression[-1] == ")" else "2"
    display_expression_text += "2"
    display_expression.config(text = display_expression_text,fg = fgColorType_1,bg = bgColorType_1)

def f_3(event = None):
    global expression, display_expression_text
    expression += "*3" if expression and expression[-1] == ")" else "3"
    display_expression_text += "3"
    display_expression.config(text = display_expression_text,fg = fgColorType_1,bg = bgColorType_1)

def f_4(event = None):
    global expression, display_expression_text
    expression += "*4" if expression and expression[-1] == ")" else "4"
    display_expression_text += "4"
    display_expression.config(text = display_expression_text,fg = fgColorType_1,bg = bgColorType_1)

def f_5(event = None):
    global expression, display_expression_text
    expression += "*5" if expression and expression[-1] == ")" else "5"
    display_expression_text += "5"
    display_expression.config(text = display_expression_text,fg = fgColorType_1,bg = bgColorType_1)

def f_6(event = None):
    global expression, display_expression_text
    expression += "*6" if expression and expression[-1] == ")" else "6"
    display_expression_text += "6"
    display_expression.config(text = display_expression_text,fg = fgColorType_1,bg = bgColorType_1)

def f_7(event = None):
    global expression, display_expression_text
    expression += "*7" if expression and expression[-1] == ")" else "7"
    display_expression_text += "7"
    display_expression.config(text = display_expression_text,fg = fgColorType_1,bg = bgColorType_1)

def f_8(event = None):
    global expression, display_expression_text
    expression += "*8" if expression and expression[-1] == ")" else "8"
    display_expression_text += "8"
    display_expression.config(text = display_expression_text,fg = fgColorType_1,bg = bgColorType_1)

def f_9(event = None):
    global expression, display_expression_text
    expression += "*9" if expression and expression[-1] == ")" else "9"
    display_expression_text += "9"
    display_expression.config(text = display_expression_text,fg = fgColorType_1,bg = bgColorType_1)

def f_0(event = None):
    global expression, display_expression_text
    expression += "*0" if expression and expression[-1] == ")" else "0"
    display_expression_text += "0"
    display_expression.config(text = display_expression_text,fg = fgColorType_1,bg = bgColorType_1)
        
def f_decimal(event = None):
    global expression, display_expression_text
    if "tan" in expression or "cos" in expression or "sin" in expression:
        pass
    else:
        if not expression:
            expression += "0."
            display_expression_text += "0."
        if expression[-1] == ".":
            pass
        elif not expression[-1].isdigit():
            expression += "0."
            display_expression_text += "0."
        else:
            expression += "."
            display_expression_text += "."
    display_expression.config(text = display_expression_text,fg = fgColorType_1,bg = bgColorType_1)    

def f_add(event = None):
    global expression, display_expression_text
    if "tan" in expression or "cos" in expression or "sin" in expression:
        pass
    elif not expression:
        pass
    else:
        if expression[len(expression)-2:len(expression)] in "**":
            expression = expression[:len(expression)-2] + "+"
        if expression[-1] in "/*-+":
            expression = expression[:len(expression)-1] + "+"
        else:
            expression += "+"
        if display_expression_text[len(display_expression_text)-1] in "÷×-+^":
            display_expression_text = display_expression_text[:len(display_expression_text)-1] + "+"
        else:
            display_expression_text += "+"
    display_expression.config(text = display_expression_text,fg = fgColorType_1,bg = bgColorType_1)  

def f_sub(event = None):
    global expression, display_expression_text
    if ("tan" in expression or "cos" in expression or "sin" in expression) and "-" in expression:
        pass
    elif not expression:
        pass
    else:
        if expression[-1] in "-+":
            expression = expression[:len(expression)-1] + "-"
        else:
            expression += "-"
        if display_expression_text[len(display_expression_text)-1] in "-+":
            display_expression_text = display_expression_text[:len(expression)-1] + "-"
        else:
            display_expression_text += "-"
    display_expression.config(text = display_expression_text,fg = fgColorType_1,bg = bgColorType_1)

def f_mul(event = None):
    global expression, display_expression_text
    if "tan" in expression or "cos" in expression or "sin" in expression:
        pass
    elif not expression:
        pass
    else:
        if expression[len(expression)-2:len(expression)] in "**":
            expression = expression[:len(expression)-2] + "*"
        if expression[-1] in "/*-+":
            expression = expression[:len(expression)-1] + "*"
        else:
            expression += "*"
        if display_expression_text[len(display_expression_text)-1] in "÷×-+^":
            display_expression_text = display_expression_text[:len(display_expression_text)-1] + "×"
        else:
            display_expression_text += "×"
    display_expression.config(text = display_expression_text,fg = fgColorType_1,bg = bgColorType_1)

def f_div(event = None):
    global expression, display_expression_text
    if "tan" in expression or "cos" in expression or "sin" in expression:
        pass
    elif not expression:
        pass
    else:
        if expression[len(expression)-3:len(expression)] in "/**":
            expression = expression[:len(expression)-3]+"/"
        elif expression[len(expression)-2:len(expression)] in "**":
            expression = expression[:len(expression)-2] + "/"
        if expression[-1] in "/*-+":
            expression = expression[:len(expression)-1] + "/"
        else:
            expression += "/"
        if display_expression_text[len(display_expression_text)-1] in "÷×^-+":
            display_expression_text = display_expression_text[:len(display_expression_text)-1] + "÷"
        else:
            display_expression_text += "÷"
    display_expression.config(text = display_expression_text,fg = fgColorType_1,bg = bgColorType_1)

def f_clear(event = None):
    global expression, display_expression_text
    expression = display_expression_text = ""
    display_expression.config(text = display_expression_text,fg = fgColorType_1,bg = bgColorType_1)

def f_factorial(event = None):
    global expression, display_expression_text
    if "tan" in expression or "cos" in expression or "sin" in expression:
        pass
    elif not expression:
        pass
    else:
        try:
            expression = int(eval(expression))
            expression = str(factorial(expression))
        except:
            expression = "ERROR"
        if expression == "ERROR":
            display_expression.config(text = expression,fg = "red")
            expression = display_expression_text = ""
        else:
            display_expression_text = expression
    display_expression.config(text = display_expression_text,fg = fgColorType_1,bg = bgColorType_1)    

def f_delete(event = None):
    global expression, display_expression_text
    if "tan" in expression or "cos" in expression or "sin" in expression:
        if len(expression) == 4:
            expression = ""
        else:
            expression = expression[:-1]
    if not expression:
        pass
    elif expression[len(expression)-2:len(expression)] in "**":
        expression = expression[:-2]
        display_expression_text = expression[:-1]
    else:
        expression = expression[:-1]
        display_expression_text = display_expression_text[:-1]
    display_expression.config(text = display_expression_text,fg = fgColorType_1,bg = bgColorType_1)

def f_power(event = None):
    global expression, display_expression_text
    if "tan" in expression or "cos" in expression or "sin" in expression:
        pass
    elif not expression:
        pass
    else:
        if expression[len(expression)-3:len(expression)] in "***":
            expression = expression[:len(expression)-3] + "**"
        if expression[len(expression)-2:len(expression)] in "**":
            expression = expression[:len(expression)-2] + "**"
        elif expression[-1] in "/*-+":
            expression = expression[:len(expression)-1] + "**"
        else:
            expression += "**"
        if display_expression_text[len(display_expression_text)-1] in "÷×^-+":
            display_expression_text = display_expression_text[:len(expression)-1] + "^"
        else:
            display_expression_text += "^"
    display_expression.config(text = display_expression_text,fg = fgColorType_1,bg = bgColorType_1)  

def f_bracket(event = None):
    ob,cb = 0,0
    global expression, display_expression_text
    if "tan" in expression or "cos" in expression or "sin" in expression:
        pass
    else:
        for i in expression:
            if i == "(":
                ob += 1
            elif i == ")":
                cb += 1
        if ob > cb:
            if expression[-1].isdigit() or expression[-1] == ")":
                expression += ")"
                display_expression_text += ")"
            else:
                expression += "("
                display_expression_text += "("
        else:
            expression += "("
            display_expression_text += "("
        if expression[len(expression)-2] == ")" and expression[-1] == "(":
            expression = expression[:len(expression)-2] + ")*("
        if expression[len(expression)-2].isdigit() and expression[-1] == "(":
            expression = expression[:len(expression)-1] + "*("
    display_expression.config(text = display_expression_text,fg = fgColorType_1,bg = bgColorType_1)
        
def f_sin():
    global expression, display_expression_text
    if not expression:
        expression = display_expression_text = "sin "
    display_expression.config(text = display_expression_text,fg = fgColorType_1,bg = bgColorType_1)
    
def f_cos():
    global expression, display_expression_text
    if not expression:
        expression = display_expression_text = "cos "
    display_expression.config(text = display_expression_text,fg = fgColorType_1,bg = bgColorType_1)

def f_tan():
    global expression, display_expression_text
    if not expression:
        expression = display_expression_text = "tan "
    display_expression.config(text = display_expression_text,fg = fgColorType_1,bg = bgColorType_1)
        
def f_result(event = None):
    global expression, display_expression_text
    if "tan" in expression or "cos" in expression or "sin" in expression:
        if len(expression) > 4:
            expression = display_expression_text = str(trigo(expression))
    elif expression:
        if expression[-1] not in "*/+-":
            try:
                expression = str(eval(expression))
            except:
                expression += "f"
    if "f" in expression:
        expression = display_expression_text = expression[:len(expression)-1]
        display_expression.config(text = display_expression_text + "\n Format Error",fg = "red")
    else:
        if expression[len(expression)-2:len(expression)] == ".0":
            expression = expression[:len(expression)-2]
        display_expression_text = expression
    display_expression.config(text = display_expression_text,fg = fgColorType_1,bg = bgColorType_1)

def f_less(event = None):
    bn_sin.grid_forget()
    bn_cos.grid_forget()
    bn_tan.grid_forget()
    bn_fac.grid_forget()
    bn_les.grid_forget()
    bn_mor.grid(column = 0,row = 0,rowspan = 2,sticky = "nsew")

def f_more(event = None):
    bn_sin.grid(column = 0,row = 0,columnspan = 2,sticky = "nsew")
    bn_cos.grid(column = 2,row = 0,columnspan = 2,sticky = "nsew")
    bn_tan.grid(column = 4,row = 0,columnspan = 2,sticky = "nsew")
    bn_fac.grid(column = 0,row = 1,columnspan = 2,sticky = "nsew")
    bn_les.grid(column = 6,row = 0,rowspan = 2,sticky = "nsew")

def f_option(event = None):
    global registered
    bn_option.config(text = "X",font = ("times new roman",5),fg = fgColorType_1,bg = bgColorType_2,command = f_cancel)
    option_panel.grid(column = 3,row = 0,rowspan = 2,sticky = "nsew")
    if not registered:
        registerComponents()
        registered = True

def f_cancel(event = None):
    option_panel.grid_forget()
    theme_panel.grid_forget()
    color_panel.grid_forget()
    bn_option.config(text = "...",font = ("times new roman",4,"bold"),fg = fgColorType_1,bg = bgColorType_1,command = f_option)
    refreshPage()
    
def f_theme(event = None):
    theme_panel.grid(column = 2,row = 0,rowspan = 2,sticky = "nsew")
    theme_panel.lift()

def f_color(event = None):
    color_panel.grid(column = 2,row = 0,sticky = "nsew")
    color_panel.lift()

def f_dark(event = None):
    global current_theme,fgColorType_1,fgColorType_2,bgColorType_1,bgColorType_2
    current_theme = "dark"
    fgColorType_1 = "white"
    fgColorType_2 = themeColor
    bgColorType_1 = "black"
    bgColorType_2 = "black"
    f_cancel()

def f_light(event = None):
    global current_theme,fgColorType_1,fgColorType_2,bgColorType_1,bgColorType_2
    current_theme = "light"
    fgColorType_1 = "black"
    fgColorType_2 = "black"
    bgColorType_1 = "white"
    bgColorType_2 = themeColor
    f_cancel()
#endregion functions

#region UI
#FRAMES====================================
screen_frame = Frame(window,bg = bgColorType_1)
screen_frame.columnconfigure(0,weight = 1)
screen_frame.rowconfigure(0,weight = 1)
screen_frame.rowconfigure(1,weight = 3)
screen_frame.rowconfigure(2,weight = 3)
screen_frame.rowconfigure(3,weight = 10)


top_panel = Frame(screen_frame,bg = bgColorType_1)
top_panel.columnconfigure(0,weight = 1)
top_panel.columnconfigure(1,weight = 1)
top_panel.columnconfigure(2,weight = 1)
top_panel.columnconfigure(3,weight = 1)
top_panel.rowconfigure(0,weight = 1)
top_panel.rowconfigure(1,weight = 1)

option_panel = Frame(top_panel,bg = bgColorType_1)
option_panel.columnconfigure(0,weight = 1)
option_panel.rowconfigure(0,weight = 1)
option_panel.rowconfigure(1,weight = 1)

theme_panel = Frame(top_panel,bg = bgColorType_1)
theme_panel.columnconfigure(0,weight = 1)
theme_panel.rowconfigure(0,weight = 1)
theme_panel.rowconfigure(1,weight = 1)

color_panel = Frame(top_panel,bg = bgColorType_1)
color_panel.rowconfigure(0,weight = 1)
color_panel.columnconfigure(0,weight = 1)
color_panel.columnconfigure(1,weight = 1)
color_panel.columnconfigure(2,weight = 1)
color_panel.columnconfigure(3,weight = 1)

expression_panel = Frame(screen_frame,bg = bgColorType_1)
expression_panel.columnconfigure(0,weight = 1)
expression_panel.rowconfigure(0,weight = 1)

more_panel = Frame(screen_frame,bg = bgColorType_1)
more_panel.rowconfigure(0,weight = 1)
more_panel.rowconfigure(1,weight = 1)
more_panel.columnconfigure(0,weight = 1)
more_panel.columnconfigure(1,weight = 1)
more_panel.columnconfigure(2,weight = 1)
more_panel.columnconfigure(3,weight = 1)
more_panel.columnconfigure(4,weight = 1)
more_panel.columnconfigure(5,weight = 1)
more_panel.columnconfigure(6,weight = 1)

button_panel = Frame(screen_frame,bg = bgColorType_1)
button_panel.columnconfigure(0,weight = 1)
button_panel.columnconfigure(1,weight = 1)
button_panel.columnconfigure(2,weight = 1)
button_panel.columnconfigure(3,weight = 1)
button_panel.rowconfigure(0,weight = 1)
button_panel.rowconfigure(1,weight = 1)
button_panel.rowconfigure(2,weight = 1)
button_panel.rowconfigure(3,weight = 1)


#MESSAGES==================================
display_name = Label(top_panel,text = "CALCULATOR",font = ("times new roman",15),fg = themeColor,bg = bgColorType_1)
display_expression = Label(expression_panel,text = display_expression_text, font = ("Arial",15),fg = fgColorType_1,bg = bgColorType_1,height = 3)



#BUTTONS===================================
bn_option = Button(top_panel,text = "...",font = ("times new roman",5,"bold"),width = 4,height = 2,fg = fgColorType_1,bg = bgColorType_2,command = f_option)

bn_theme = Button(option_panel,text = "Theme",font = ("times new roman",10),fg = fgColorType_2,bg = bgColorType_2,command = f_theme)
bn_color = Button(option_panel,text = "Color",font = ("times new roman",10),fg = fgColorType_2,bg = bgColorType_2,command = f_color)

bn_lght = Button(theme_panel,text = "Light",font = ("times new roman",10),fg = fgColorType_2,bg = bgColorType_2,command = f_light)
bn_dark = Button(theme_panel,text = "Dark",font = ("times new roman",10),fg = fgColorType_2,bg = bgColorType_2,command = f_dark)

bn_green = Button(color_panel,text = "",font = ("times new roman",10),fg = "green",bg = "green",command = lambda: changeColor("green"))
bn_lightBlue = Button(color_panel,text = "",font = ("times new roman",10),fg = "light blue",bg = "light blue",command = lambda: changeColor("light blue"))
bn_orange = Button(color_panel,text = "",font = ("times new roman",10),fg = "orange",bg = "orange",command = lambda: changeColor("orange"))
bn_hotpink = Button(color_panel,text = "",font = ("times new roman",10),fg = "hotpink",bg = "hotpink",command = lambda: changeColor("hotpink"))

bn_mor = Button(more_panel, text = ">",font = ("Arial",13),fg = fgColorType_2,bg = bgColorType_2,command = f_more)
bn_les = Button(more_panel, text = "<", font = ("Arial",13),fg = fgColorType_2,bg = bgColorType_2,command = f_less)
bn_sin = Button(more_panel, text = "  sin  ", font = ("Arial",13),fg = fgColorType_2,bg = bgColorType_2,command = f_sin)
bn_cos = Button(more_panel, text = "  cos  ", font = ("Arial",13),fg = fgColorType_2,bg = bgColorType_2,command = f_cos)
bn_tan = Button(more_panel, text = "  tan  ", font = ("Arial",13),fg = fgColorType_2,bg = bgColorType_2,command = f_tan)
bn_fac = Button(more_panel, text = "!", font = ("Arial",13),fg = fgColorType_2,bg = bgColorType_2,command = f_factorial)
        
bn_1 = Button(button_panel, text = "1",font = ("Arial",13),fg = fgColorType_1,bg = bgColorType_1,width = 5,height = 2,command = f_1)
bn_2 = Button(button_panel, text = "2",font = ("Arial",13),fg = fgColorType_1,bg = bgColorType_1,width = 5,height = 2,command = f_2)
bn_3 = Button(button_panel, text = "3",font = ("Arial",13),fg = fgColorType_1,bg = bgColorType_1,width = 5,height = 2,command = f_3)
bn_4 = Button(button_panel, text = "4",font = ("Arial",13),fg = fgColorType_1,bg = bgColorType_1,width = 5,height = 2,command = f_4)
bn_5 = Button(button_panel, text = "5",font = ("Arial",13),fg = fgColorType_1,bg = bgColorType_1,width = 5,height = 2,command = f_5)
bn_6 = Button(button_panel, text = "6",font = ("Arial",13),fg = fgColorType_1,bg = bgColorType_1,width = 5,height = 2,command = f_6)
bn_7 = Button(button_panel, text = "7",font = ("Arial",13),fg = fgColorType_1,bg = bgColorType_1,width = 5,height = 2,command = f_7)
bn_8 = Button(button_panel, text = "8",font = ("Arial",13),fg = fgColorType_1,bg = bgColorType_1,width = 5,height = 2,command = f_8)
bn_9 = Button(button_panel, text = "9",font = ("Arial",13),fg = fgColorType_1,bg = bgColorType_1,width = 5,height = 2,command = f_9)
bn_0 = Button(button_panel, text = "0",font = ("Arial",13),fg = fgColorType_1,bg = bgColorType_1,width = 5,height = 2,command = f_0)
bn_add = Button(button_panel, text = "+", font = ("Arial",15),fg = fgColorType_2,bg = bgColorType_2,width = 5,height = 2,command = f_add)
bn_sub = Button(button_panel, text = "-", font = ("Arial",15),fg = fgColorType_2,bg = bgColorType_2,width = 5,height = 2,command = f_sub)
bn_mul = Button(button_panel, text = "x", font = ("Arial",15),fg = fgColorType_2,bg = bgColorType_2,width = 5,height = 2,command = f_mul)
bn_div = Button(button_panel, text = "÷", font = ("Arial",15),fg = fgColorType_2,bg = bgColorType_2,width = 5,height = 2,command = f_div)
bn_clear = Button(button_panel, text = "AC", font = ("Arial",10),fg = fgColorType_2,bg = bgColorType_2,height = 2,command = f_clear)
bn_power = Button(button_panel, text = "^", font = ("Arial",15),fg = fgColorType_2,bg = bgColorType_2,height = 2,command = f_power)
bn_brack = Button(button_panel, text = "()", font = ("Arial",13),fg = fgColorType_2,bg = bgColorType_2,height = 2,command = f_bracket)
bn_decim = Button(button_panel, text = ".",font = ("Arial",15),fg = fgColorType_2,bg = bgColorType_2,height = 2,command = f_decimal)
bn_delet = Button(button_panel, text = "<",font = ("Arial",15),fg = fgColorType_2,bg = bgColorType_2,height = 2,command = f_delete)
bn_resul = Button(button_panel, text = "=",font = ("Arial",15),fg = fgColorType_2,bg = bgColorType_2,height = 2,command = f_result)



#KEY BINDINGS==============================
window.bind("1",f_1)
window.bind("2",f_2)
window.bind("3",f_3)
window.bind("4",f_4)
window.bind("5",f_5)
window.bind("6",f_6)
window.bind("7",f_7)
window.bind("8",f_8)
window.bind("9",f_9)
window.bind("0",f_0)
window.bind(".",f_decimal)
window.bind("+",f_add)
window.bind("-",f_sub)
window.bind("*",f_mul)
window.bind("/",f_div)
window.bind("!",f_factorial)
window.bind("^",f_power)
window.bind("(",f_bracket)
window.bind(")",f_bracket)
window.bind("<Delete>",f_clear)
window.bind("<BackSpace>",f_delete)
window.bind("<Return>",f_result)




#================PLACEMENT=================
#PLACING MESSAGES
display_name.grid(column = 0,row = 0,columnspan = 2,rowspan = 2,sticky = "e")
display_expression.grid(column = 0,row = 0,sticky = "e")



#PLACING BUTTONS
bn_option.grid(column = 4,row = 0,rowspan = 2,sticky = "nsew")

bn_theme.grid(column = 0,row = 0,sticky = "nsew")
bn_color.grid(column = 0,row = 1,sticky = "nsew")

bn_lght.grid(column = 0,row = 0,sticky = "nsew")
bn_dark.grid(column = 0,row = 1,sticky = "nsew")

bn_green.grid(column = 0,row = 0,sticky = "nsew")
bn_lightBlue.grid(column = 1,row = 0,sticky = "nsew")
bn_orange.grid(column = 2,row = 0,sticky = "nsew")
bn_hotpink.grid(column = 3,row = 0,sticky = "nsew")

bn_mor.grid(column = 0,row = 0,rowspan = 2,sticky = "nsew")

bn_1.grid(column = 0,row = 1,sticky = "nsew")
bn_2.grid(column = 1,row = 1,sticky = "nsew")
bn_3.grid(column = 2,row = 1,sticky = "nsew")
bn_4.grid(column = 0,row = 2,sticky = "nsew")
bn_5.grid(column = 1,row = 2,sticky = "nsew")
bn_6.grid(column = 2,row = 2,sticky = "nsew")
bn_7.grid(column = 0,row = 3,sticky = "nsew")
bn_8.grid(column = 1,row = 3,sticky = "nsew")
bn_9.grid(column = 2,row = 3,sticky = "nsew")
bn_0.grid(column = 1,row = 4,sticky = "nsew")
bn_add.grid(column = 3,row = 1,sticky = "nsew")
bn_sub.grid(column = 3,row = 2,sticky = "nsew")
bn_mul.grid(column = 3,row = 3,sticky = "nsew")
bn_div.grid(column = 2,row = 0,sticky = "nsew")
bn_clear.grid(column = 0,row = 0,sticky = "nsew")
bn_power.grid(column = 1,row = 0,sticky = "nsew")
bn_brack.grid(column = 2,row = 4,sticky = "nsew")
bn_decim.grid(column = 0,row = 4,sticky = "nsew")
bn_delet.grid(column = 3,row = 0,sticky = "nsew")
bn_resul.grid(column = 3,row = 4,sticky = "nsew")



#PLACING FRAMES
screen_frame.pack(fill = "both",expand = True)

top_panel.grid(column = 0,row = 0,sticky = "nsew")
expression_panel.grid(column = 0,row = 1,sticky = "nsew")
more_panel.grid(column = 0,row = 2,sticky = "nsew")
button_panel.grid(column = 0,row = 3,sticky = "nsew")

#endregion UI


window.mainloop()