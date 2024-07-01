import tkinter
from tkinter.filedialog import asksaveasfilename
from tkinter import messagebox  
from graph import draw  
from webbrowser import open_new_tab 

COLOR = '#444c69'  
file_path = '' 
BMI = 0

def aboutus():
	open_new_tab('https://github.com/Debang5hu/OIBSIP/blob/main/BMI-Calculator/README.md')


def data_visualisation():
	draw()


def save():
	if file_path=='':
		files=[('Text Files', '*.txt')]
		file_name=asksaveasfilename(defaultextension = files)
	else:
		file_name=file_path

	if file_name is not None:
		data = f'\n{agefield.get()},{BMI}\n'   
		
		with open(file_name, 'a+') as fh:
			fh.write(data)


def clear():
	agefield.delete(0,tkinter.END)
	heightfield.delete(0,tkinter.END)   
	weightfield.delete(0,tkinter.END)

	
def calculate() -> float:
	global BMI
	try:
		height = float(heightfield.get())
		weight = float(weightfield.get())

		if height == 0:
			messagebox.showinfo("ERROR", "ERROR! Division by 0")
			result.config(text='ERROR! Division by 0')
			return

		BMI = round((weight / (height ** 2)),2)  

		
		if BMI <= 18.5:
			result.config(text=f'{BMI} - Under Weight')
		elif BMI >= 18.5 and BMI <= 24.9:
			result.config(text=f'{BMI} - Healthy Weight') 
		elif BMI >= 25.0 and BMI <= 29.9:
			result.config(text=f'{BMI} - Over Weight') 
		elif BMI >= 30.0:
			result.config(text=f'{BMI} - Obesity ') 
		else:
			result.config(text='Check the value correctly')

	except ValueError:
		messagebox.showinfo("ERROR", "Enter Correct Value!")
		result.config(text='Enter Correct Value!')


if __name__ == '__main__':

	
	screen = tkinter.Tk()
	screen.title("BMI Calculator")
	screen.geometry("550x400")
	screen.resizable(0,0)  
	screen.configure(background=COLOR)


	tkinter.Label(screen,text='Age: ',background=COLOR,font=('monospace', 15)).place(x=50,y=50)
	agefield = tkinter.Entry(screen)
	agefield.place(x=200,y=50)


	tkinter.Label(screen,text='Height [m]: ',background=COLOR,font=('monospace', 15)).place(x=50,y=100)
	heightfield = tkinter.Entry(screen)
	heightfield.place(x=200,y=100)


	tkinter.Label(screen,text='Weight [kg]: ',background=COLOR,font=('monospace', 15)).place(x=50,y=150)
	weightfield = tkinter.Entry(screen)
	weightfield.place(x=200,y=150)

	tkinter.Label(screen,text='BMI: ',background=COLOR,font=('monospace', 15)).place(x=50,y=200)

	result = tkinter.Label(screen,text='0',background=COLOR,font=('monospace', 15))
	result.place(x=200,y=200)


	calculatebutton = tkinter.Button(screen,text='Calculate',activeforeground='red',activebackground='black',bd=3,font='monospace',command=calculate).place(x=200,y=250) # calculate

	clearbutton = tkinter.Button(screen,text='Clear',activeforeground='red',activebackground='black',bd=3,font='monospace',command=clear).place(x=100,y=250) # clear

	menubar = tkinter.Menu(screen,background='#28282B',foreground='white')

	savemenu = tkinter.Menu(menubar, tearoff=False,background='#28282B',fg='white')  
	menubar.add_command(label='Save',command=save)

	graph = tkinter.Menu(menubar, tearoff=False,background='#28282B',fg='white') 
	menubar.add_command(label='Graph',command=data_visualisation)

	about = tkinter.Menu(menubar, tearoff=False,background='#28282B',fg='white')
	menubar.add_command(label='About',command=aboutus)

	exit = tkinter.Menu(menubar, tearoff=False,background='#28282B',fg='white') 
	menubar.add_command(label='Exit',command=screen.destroy)

	screen.config(menu=menubar)

	screen.mainloop()
