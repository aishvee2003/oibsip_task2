import matplotlib.pyplot as plt  
from sys import argv
from tkinter import messagebox

newdata = []

def draw():

    try:
        with open('graph.txt') as fh:
            data = fh.read().split('\n')
    except:
        messagebox.showinfo("ERROR", "File Not Found!")
        return

    for x in data:
        separatedata = x.split(',')
        if len(separatedata) > 1:
            newdata.append(separatedata)
        else:
            pass
    

    age = [int(x[0]) for x in newdata]
    bmi = [float(x[1]) for x in newdata]

    
    plt.plot(age, bmi, marker='o', linestyle='-', color='r')  

    plt.xlabel('Age')
    plt.ylabel('BMI')
    plt.title('BMI vs. Age')

    plt.grid(True)
    
    plt.show() 
