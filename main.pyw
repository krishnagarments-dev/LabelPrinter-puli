from tkinter import FLAT, SUNKEN, RAISED, Button, Entry, Label,font,Listbox,END
from tkinter.messagebox import showinfo,showwarning
import tkinter
from core import check_stock,find_data,find_data_wrate,load_from_code
from printqr import print_qr_for_me


root = tkinter.Tk()
root.title("Victor")
root.iconbitmap('v.ico')
root.geometry("240x500+25+30")
font_head = ('MS Sans Serif', 15)
font_sub = ('MS Sans Serif', 10)

item_code = []
item_rate = []
item_name = []
def find_product(evt):
    global item_code, item_rate, item_name
    if itemname.get() not in [" ",None,' ',"",'']:
        if itemrate.get() not in [""," ",'',' ',None]:
            print_btn.config(relief=RAISED)
            code,item,rate_product = find_data_wrate(item_name=itemname.get(),item_rate=itemrate.get())
            lb.delete(0,'end')
            item_code = code
            item_name = item
            item_rate = rate_product
            lst = item
            i = 1

            for l in lst:
                lb.insert(i,l)
                i+=1
        else:
            print_btn.config(relief=RAISED)
            code,item,rate_product = find_data(item_name=itemname.get())
            lb.delete(0,'end')
            item_code = code
            item_name = item
            item_rate = rate_product
            lst = item
            i = 1

            for l in lst:
                lb.insert(i,l)
                i+=1



def load_code(evt):
    global item_code, item_rate
    try:
        print_btn.config(relief=RAISED)
        itemcode.delete(0,END)
        itemstock.delete(0,END)
        itemname.delete(0,END)
        landing.delete(0,END)
        itemrate.delete(0,END)
        sel = evt.widget.curselection()
        selected = sel[0]
        itemcode.insert(0,item_code[selected])
        curstk,selling_rate,purchase_rate,item_name,ngst = load_from_code(item_code=f'{item_code[selected]}')
        itemstock.insert(0,curstk)
        itemname.insert(0,item_name)
        landing.insert(0,purchase_rate)
        itemrate.insert(0,selling_rate)


    except:
        pass

def clear_all(evt):
    print_btn.config(relief=RAISED)
    lb.delete(0,'end')
    itemname.delete(0,END)
    itemcode.delete(0,END)
    itemrate.delete(0,END)
    landing.delete(0,END)
    itemstock.delete(0,END)
    printqty.delete(0,END)

def print_statement(evt):
    try:
        print_qr_for_me(item_code=itemcode.get(),item_name=itemname.get(),item_rate=int(float(itemrate.get())),print_nos=printqty.get())
        print_btn.config(relief=RAISED)
    except:
        pass
        print_btn.config(relief=RAISED)

head = Label(root,text="Product Manager",font=font_head)
head.grid(row=0,columnspan=3,pady=20,padx=5)
itemname_lbl = Label(root,text="Item Name",font=font_sub)
itemname_lbl.grid(row=1,column=0,padx=5)
itemname = Entry(root,font=font_sub)
itemname.grid(row=1,column=1)

itemrate_lbl = Label(root,text="Rate",font=font_sub)
itemrate_lbl.grid(row=2,column=0)
itemrate = Entry(root,font=font_sub)
itemrate.grid(row=2,column=1)

itemcode_lbl = Label(root,text="Item Code",font=font_sub)
itemcode_lbl.grid(row=3,column=0)
itemcode = Entry(root,font=font_sub)
itemcode.grid(row=3,column=1)

itemstock_lbl = Label(root,text="Stock",font=font_sub)
itemstock_lbl.grid(row=4,column=0)
itemstock = Entry(root,font=font_sub)
itemstock.grid(row=4,column=1)

landing_lbl = Label(root,text="Landing",font=font_sub)
landing_lbl.grid(row=5,column=0)
landing = Entry(root,font=font_sub)
landing.grid(row=5,column=1)

# buttons
check_btn = Button(root,text="Check",font=font_sub)
check_btn.grid(row=6,column=0,pady=3)

check_btn.bind('<Return>',find_product)
check_btn.bind('<Button-1>',find_product)

clear_btn = Button(root,text="Clear",font=font_sub)
clear_btn.grid(row=6,column=1,pady=3)
clear_btn.bind('<Return>',clear_all)
clear_btn.bind('<Button-1>',clear_all)

# Print Option
print_qty = Label(root,text="Print Quantity",font=font_sub)
print_qty.grid(row=7,column=0)
printqty = Entry(root,font=font_sub)
printqty.grid(row=7,column=1)

# Print Button

print_btn = Button(root,text="Retail Print",font=font_sub,relief=RAISED)
print_btn.grid(row=8,columnspan=3,pady=8)
print_btn.bind('<Button-1>',print_statement)

lst = ["A","B","C","D","E","F","G"]
# List Box
lb = Listbox(root)
lb.bind("<<ListboxSelect>>",load_code)
length = len(lst)
print(length)

# i = 1

# for l in lst:
#     lb.insert(i,l)
#     i+=1

lb.grid(row=9,columnspan=3,pady=7)

root.mainloop()