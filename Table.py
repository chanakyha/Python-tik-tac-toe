#give the window name and header and the dat nested list to show table
from tkinter import *

def tk_table(root,list=[[]],header=[], colour="white"):
    from tkinter import ttk
    tree_frame = Frame(root,bg=colour)
    tree_frame.pack()
    tree_scroll = Scrollbar(tree_frame)
    tree_scroll.pack(side=RIGHT, fill=Y)

    my_table = ttk.Treeview(tree_frame,yscrollcommand=tree_scroll.set)
    tree_scroll.config(command=my_table.yview)
    my_table["columns"]=tuple(header)

    my_table.column("#0", width=0,stretch=NO)
    for i in range(len(header)):
        print(list,i,sep="\n")
        dmy_lst = []
        for j in range (len(list[i])):
            dmy_lst.append(len(str(list[i][j])))
            max_ = max(dmy_lst)
        if max_ < len(header[i]):
            max_ = len(header[i])
        my_table.column(str(header[i]), anchor=W, width=max_*9)
    my_table.heading("#0", text="", anchor=W)
    for i in range(len(header)):
        my_table.heading(str(header[i]), text=str(header[i]), anchor=W)

    for record in range(len(list)):
        my_table.insert(parent='', index=END, iid=record, text="", values=list[record])

    return my_table