from tkinter import *
class window(object):
    def input_information(self):
        login_data = {}
        def cancel():
            root.quit()

        def confirm():
            login_data['number'] = lab1.get()
            login_data['password'] = lab2.get()
            root.quit()

        root = Tk()
        root.title("模拟登陆")
        frame = Frame(root)
        frame.pack(padx=30, pady=16, ipadx=4)
        _number = StringVar()
        lab1 = Entry(frame,textvariable = _number)
        lab1.grid(row=3, column=1, sticky='ew', columnspan=2)
        _password = StringVar()
        lab2 = Entry(frame,textvariable = _password)
        lab2.grid(row=7, column=1, sticky='ew', columnspan=2)
        button1 = Button(frame, text = "确认",default='active',command = confirm)
        button1.grid(row=11, column=2)
        button2 = Button(frame,text = "取消",command = cancel)
        button2.grid(row=11, column=1, sticky=W)



        root.update_idletasks()
        x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
        y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
        root.geometry("+%d+%d" % (x, y))
        root.mainloop()

        return login_data






