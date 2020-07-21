# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 10:28:53 2019

@author: Nithin Sai
"""


from functools import partial
from tkinter import StringVar
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

#%matplotlib qt

LARGE_FONT= ("Verdana", 12)
keys=[]
values=[]

class GraphPlot(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        
        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.wm_title(self, "Graph Plot")
        
        
        self.geometry("800x600")
        self.resizable(0,0)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo, PageThree,PageFour,PageFive,PageSix,PageSeven):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

        
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Graph Plot", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        
        
        button = ttk.Button(self, text="Linear",
                            command=lambda: controller.show_frame(PageOne))
        button.pack()

        button2 = ttk.Button(self, text="Quadratic",
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack()

        button3 = ttk.Button(self, text="Cubic",
                            command=lambda: controller.show_frame(PageThree))
        button3.pack()
        
        button4 = ttk.Button(self, text="3-D Plane",
                            command=lambda: controller.show_frame(PageFour))
        button4.pack()
        
        button5 = ttk.Button(self, text="Pie Chart",
                            command=lambda: controller.show_frame(PageFive))
        button5.pack()
        
        button6 = ttk.Button(self, text="Line Graph",
                            command=lambda: controller.show_frame(PageSix))
        button6.pack()
        
        button7 = ttk.Button(self, text="Bar Graph",
                            command=lambda: controller.show_frame(PageSeven))
        button7.pack()

class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Linear", font=LARGE_FONT)
        txtv=StringVar()
        txtv2=StringVar()
        txtv3=StringVar()
        txtv4=StringVar()
        txtv5=StringVar()
        label.pack(pady=10,padx=10)
        lin="The genral form of linear equation is \n Ax+By+C=Y. To get the graph of \n the equation, enter values of A,B,C\n and enter limits of x"
        msg=tk.Label(self,text=lin,height=5,width=40).pack()
        lb1=tk.Label(self,text="A:").pack()
        en1=tk.Entry(self,textvariable=txtv).pack()
        
        lb2=tk.Label(self,text="B:").pack()
        en2=tk.Entry(self,textvariable=txtv2).pack()
        
        lb3=tk.Label(self,text="C:").pack()
        en3=tk.Entry(self,textvariable=txtv3).pack()
        
        lb4=tk.Label(self,text="x-Lower limit:").pack()
        en4=tk.Entry(self,textvariable=txtv4).pack()
        
        lb5=tk.Label(self,text="x-Upper limit:").pack()
        en5=tk.Entry(self,textvariable=txtv5).pack()
        
        btn2=ttk.Button(self,text="plot",command=lambda: self.plot(txtv.get(),txtv2.get(),txtv3.get(),txtv4.get(),txtv5.get())).place(x=355,y=450)
        
        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.place(x=355,y=500)
        
        
    
    def plot(self,a,b,c,d,e):
        a=int(a)
        b=int(b)
        c=int(c)
        d=int(d)
        e=int(e)
        import matplotlib.pyplot as plt
        if b==0:
            f=10
            y=list(range(d,e+1))
            x=[]
            for i in range(d,e+1):
                x.append(-c/a)
        else:
            def linear(i):
                return (-c-a*i)/b
            x=list(range(d,e+1))
            y=[]
            for i in x:
                t=linear(i)
                y.append(t)
            f=max(linear(d),linear(e))*1.5
        plt.figure(figsize=(7,7))
        plt.plot(x, y)
        plt.xlim((d,e))
        plt.ylim(-f,f)
        plt.plot([d,e],[0,0], linewidth=1.2, color='red' )
        plt.plot([0,0],[-f,f], linewidth=1.2, color='red' )
        plt.title('Linear plot')
        plt.show()

        



class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Quadratic", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        
        txtv=StringVar()
        txtv2=StringVar()
        txtv3=StringVar()
        txtv4=StringVar()
        txtv5=StringVar()
        label.pack(pady=10,padx=10)
        lin="The genral form of quadratic equation is \n Ax^2+Bx+C=Y. To get the graph of \n the equation, enter values of A,B,C\n and enter limits of x"
        msg=tk.Label(self,text=lin,height=5,width=40).pack()
        lb1=tk.Label(self,text="A:").pack()
        en1=tk.Entry(self,textvariable=txtv).pack()
        
        lb2=tk.Label(self,text="B:").pack()
        en2=tk.Entry(self,textvariable=txtv2).pack()
        
        lb3=tk.Label(self,text="C:").pack()
        en3=tk.Entry(self,textvariable=txtv3).pack()
        
        lb4=tk.Label(self,text="x-Lower limit:").pack()
        en4=tk.Entry(self,textvariable=txtv4).pack()
        
        lb5=tk.Label(self,text="x-Upper limit:").pack()
        en5=tk.Entry(self,textvariable=txtv5).pack()
        
        btn3=ttk.Button(self,text="plot",command=lambda: self.plot(txtv.get(),txtv2.get(),txtv3.get(),txtv4.get(),txtv5.get())).place(x=355,y=450)
        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.place(x=355,y=500)
        
    
    def plot(self,a,b,c,d,e):
        a=int(a)
        b=int(b)
        c=int(c)
        d=int(d)
        e=int(e)
        p=[]
        q=[]
        def quad(x):
            return a*x**2+b*x+c
        for x in range(d,e,1):
            y=quad(x)
            p.append(x)
            q.append(y)
        plt.figure(figsize=(7,7))
        plt.plot(p, q)
        plt.xlim(d,e)
        f=max(quad(d),quad(e))*1.5
        plt.ylim(-f,f)
        plt.plot([d,e],[0,0], linewidth=1.2, color='red' )
        plt.plot([0,0],[-f,f], linewidth=1.2, color='red' )
        plt.title('Quadrant plot')
        plt.show()




class PageThree(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Cubic", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        
        
        txtv=StringVar()
        txtv2=StringVar()
        txtv3=StringVar()
        txtv4=StringVar()
        txtv5=StringVar()
        txtv6=StringVar()
        label.pack(pady=10,padx=10)
        lin="The genral form of cubic equation is \n Ax^3+Bx^2+CX+D=Y. To get the graph of \n the equation, enter values of A,B,C,D\n and enter limits of x"
        
        msg=tk.Label(self,text=lin,height=5,width=40).pack()
        
        
        lb1=tk.Label(self,text="A:").pack()
        en1=tk.Entry(self,textvariable=txtv).pack()
        
        lb2=tk.Label(self,text="B:").pack()
        en2=tk.Entry(self,textvariable=txtv2).pack()
        
        lb3=tk.Label(self,text="C:").pack()
        en3=tk.Entry(self,textvariable=txtv3).pack()
        
        lb4=tk.Label(self,text="D:").pack()
        en4=tk.Entry(self,textvariable=txtv4).pack()
        
        lb5=tk.Label(self,text="x-Lower limit:").pack()
        en5=tk.Entry(self,textvariable=txtv5).pack()
        
        lb5=tk.Label(self,text="x-Upper limit:").pack()
        en5=tk.Entry(self,textvariable=txtv6).pack()
        
        
        btn4=ttk.Button(self,text="plot",command=lambda: self.plot(txtv.get(),txtv2.get(),txtv3.get(),txtv4.get(),txtv5.get(),txtv6.get())).place(x=355,y=450)
        button1 = ttk.Button(self, text="Back to Home",command=lambda: controller.show_frame(StartPage)).place(x=355,y=500)
        
        


    def plot(self,a,b,c,d,e,f):
        a=int(a)
        b=int(b)
        c=int(c)
        d=int(d)
        e=int(e)
        f=int(f)
        p=[]
        q=[]
        def cubic(x):
            return a*x**3+b*x**2+c*x+d
        x=np.linspace(e,f,1000)
        for i in x:
            y=cubic(i)
            p.append(i)
            q.append(y)
        plt.figure(figsize=(7,7))
        plt.plot(p, q)
        plt.xlim(e,f)
        g=max(q)*1.00003
        plt.ylim(-g,g)
        plt.plot([e,f],[0,0], linewidth=1.1, color='red' )
        plt.plot([0,0],[-g,g], linewidth=1.1, color='red' )
        plt.title('Cubic plot')
        plt.show()


class PageFour(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="3D-Plane", font=LARGE_FONT)
        txtv=StringVar()
        txtv2=StringVar()
        txtv3=StringVar()
        txtv4=StringVar()
        txtv5=StringVar()
        txtv6=StringVar()
        txtv7=StringVar()
        txtv8=StringVar()
        label.pack(pady=10,padx=10)
        lin="The genral form of 3d-Plane equation is \n Ax+By+Cz+D=Y. To get the graph of \n the equation, enter values of A,B,C,D\n and enter limits of x and y"
        msg=tk.Label(self,text=lin,height=5,width=40).pack()
        lb1=tk.Label(self,text="A:").pack()
        en1=tk.Entry(self,textvariable=txtv).pack()
        
        lb2=tk.Label(self,text="B:").pack()
        en2=tk.Entry(self,textvariable=txtv2).pack()
        
        lb3=tk.Label(self,text="C:").pack()
        en3=tk.Entry(self,textvariable=txtv3).pack()
        
        lb4=tk.Label(self,text="D:").pack()
        en4=tk.Entry(self,textvariable=txtv4).pack()
        
        lb5=tk.Label(self,text="x-Lower limit:").pack()
        en5=tk.Entry(self,textvariable=txtv5).pack()
        
        lb6=tk.Label(self,text="x-Upper limit:").pack()
        en6=tk.Entry(self,textvariable=txtv6).pack()
        
        lb7=tk.Label(self,text="y-Lower limit:").pack()
        en7=tk.Entry(self,textvariable=txtv7).pack()
        
        lb8=tk.Label(self,text="y-Upper limit:").pack()
        en8=tk.Entry(self,textvariable=txtv8).pack()
        
        btn5=ttk.Button(self,text="plot",command=lambda: self.plot(txtv.get(),txtv2.get(),txtv3.get(),txtv4.get(),txtv5.get(),txtv6.get(),txtv7.get(),txtv8.get())).place(x=355,y=450)
        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.place(x=355,y=500)
        
        
    
    def plot(self,a,b,c,d,e,f,g,h):
        a=int(a)
        b=int(b)
        c=int(c)
        d=int(d)
        e=int(e)
        f=int(f)
        g=int(g)
        h=int(h)
        if c==0:
            if b==0:
                f=10
                y=list(range(e,f+1))
                x=[]
                for i in range(e,f+1):
                    x.append(-d/a)
            else:
                def linear(i):
                    return (-c-a*i)/b
                x=list(range(e,f+1))
                y=[]
                for i in x:
                    t=linear(i)
                    y.append(t)
                #f=max(linear(d),linear(e))*1.5
            plt.figure()
            plt.plot(x, y)
            plt.xlim((e,f))
            plt.ylim(g,h)
            plt.plot([e,f],[0,0], linewidth=1.2, color='red' )
            plt.plot([0,0],[g,h], linewidth=1.2, color='red' )
            plt.title('Linear plot')
            plt.show()
        else:
            x = np.linspace(e,f,2)
            y = np.linspace(g,h,2)
            X,Y = np.meshgrid(x,y)
            Z = (d - a*X - b*Y) / c
            fig = plt.figure(figsize=(7,7))
            fig.suptitle('Plane Graph')
            ax = fig.gca(projection='3d')
            surf = ax.plot_surface(X, Y, Z)
            fig.show()




class PageFive(tk.Frame):
    
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Pie Chart", font=LARGE_FONT)
        txtv=StringVar()
        txtv2=StringVar()
        
        
        label.pack(pady=10,padx=10)
        lin="To create a pie chart you have to input labels and its values\n according to the number of labels and their values pie chart is formed"
        msg=tk.Label(self,text=lin,height=5,width=55).pack()
        
        lb1=tk.Label(self,text="Label:").pack()
        en1=tk.Entry(self,textvariable=txtv).pack()
        
        lb2=tk.Label(self,text="Value:").pack()
        en2=tk.Entry(self,textvariable=txtv2).pack()
        
        
        btn=ttk.Button(self,text="Add",command=lambda:add(txtv.get(),txtv2.get()))
        btn.pack()
        
       
        
        btn2=ttk.Button(self,text="Plot",command=lambda: self.plot()).place(x=355,y=450)
        
        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.place(x=355,y=500)
        def add(k,v):
            keys.append(str(k))
            values.append(int(v))
            

        
        
    def plot(self):
        
        labels = keys[:]
        sizes = values[:]
        keys.clear()
        values.clear()
        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, labels=labels, autopct='%1.1f%%',shadow=True, startangle=90)
        ax1.axis('equal') 
        plt.show()
        

        
       
        
class PageSix(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Line Graph", font=LARGE_FONT)
        txtv=StringVar()
        txtv2=StringVar()
        
        label.pack(pady=10,padx=10)
        lin="To create a Line graph you have to input X and Y values\n according to the given X and Y values line Graph is formed"

        msg=tk.Label(self,text=lin,height=5,width=55).pack()
        
        lb1=tk.Label(self,text="X:").pack()
        en1=tk.Entry(self,textvariable=txtv).pack()
        
        lb2=tk.Label(self,text="Y:").pack()
        en2=tk.Entry(self,textvariable=txtv2).pack()
        
        
        
        btn=ttk.Button(self,text="Add",command=lambda:add(txtv.get(),txtv2.get())).pack()
        
        btn2=ttk.Button(self,text="Plot",command=lambda: self.plot()).place(x=355,y=450)
        
        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.place(x=355,y=500)
        
        def add(k,v):
            
            keys.append(str(k))
            values.append(int(v))
            
    
    
    def plot(self):
        labels = keys[:]
        sizes = values[:]
        keys.clear()
        values.clear()
        y_pos = np.arange(len(labels))
        fig = plt.figure()
        ax = fig.add_subplot(111)
        for i,j in zip(y_pos,sizes):
            ax.annotate(str(j),xy=(i,j),size=13)
        plt.plot( y_pos, sizes, marker='o', markerfacecolor='blue', markersize=4, color='skyblue', linewidth=2)
        plt.xticks(y_pos, labels)
        plt.show()
        




    

class PageSeven(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Bar Graph", font=LARGE_FONT)
        txtv=StringVar()
        txtv2=StringVar()
        
        label.pack(pady=10,padx=10)
        lin="To create a Bar graph you have to input labels and its values\n according to the number of labels and their values Bar graph is formed"

        msg=tk.Label(self,text=lin,height=5,width=55).pack()
        
        lb1=tk.Label(self,text="Label:").pack()
        en1=tk.Entry(self,textvariable=txtv).pack()
        
        lb2=tk.Label(self,text="Value:").pack()
        en2=tk.Entry(self,textvariable=txtv2).pack()
        
        
        
        btn=ttk.Button(self,text="Add",command=lambda:add(txtv.get(),txtv2.get())).pack()
        
        btn2=ttk.Button(self,text="Plot",command=lambda: self.plot()).place(x=355,y=450)
        
        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.place(x=355,y=500)
        
        def add(k,v):
            keys.append(str(k))
            values.append(int(v))
            
    
    
    def plot(self):
        labels = keys[:]
        sizes = values[:]
        keys.clear()
        values.clear()
        y_pos = np.arange(len(labels))
        fig = plt.figure()
        ax = fig.add_subplot(111)
        for a,b in zip(y_pos, sizes):
                plt.text(a, b+0.1, str(b))
        plt.bar(y_pos, sizes, color=(0.6, 0.4, 0.6, 0.6))
        plt.xticks(y_pos, labels)
        plt.show()
        

        
        

app = GraphPlot()
app.mainloop()