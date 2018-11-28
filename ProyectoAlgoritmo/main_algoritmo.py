from tkinter import *
from tkinter import filedialog as fd

class Aplicacion():
	def __init__(self):
		#Ventana principal
		self.raiz = Tk()
		self.raiz.title("Analisis de Algoritmo")
		self.raiz.minsize(550, 250)
		#barra de menu
		self.barraMenu = Menu(self.raiz)
		self.raiz.config(menu=self.barraMenu,width=300,height=200)
		self.inicio = Menu(self.barraMenu,tearoff=0)
		self.inicio.add_command(label="Nuevo")
		self.inicio.add_command(label="Salir",command=self.raiz.destroy)
		self.herramienta = Menu(self.barraMenu,tearoff=0)
		self.barraMenu.add_cascade(label="Inicio",menu=self.inicio)
		self.barraMenu.add_cascade(label="Herramienta",menu=self.herramienta)

		self.frame1()
		self.mensajeError = Label(self.raiz)
		self.mensajeError.pack(side=BOTTOM)
		self.raiz.mainloop()
#--------------------------frame--------------------------------------
	def frame1(self):
		self.url = StringVar(value='')
		self.insertV = BooleanVar()
		self.mergeV = BooleanVar()
		self.quickV = BooleanVar()
		self.stoogeV = BooleanVar()
		self.numdata = IntVar(value=0)

		self.frame1 = Frame(self.raiz,width=300,height=200)
		self.frame1.pack(fill="x")

		#parte de archivos
		Label(self.frame1,text="Archivo:",font=("Comic Sans MS",12)).grid(row=0,column=0,sticky="e")
		texto = Entry(self.frame1,textvariable=self.url,state='disabled')
		texto.grid(row=0,column=1,padx=10)
		Label(self.frame1,text="*",font=("Comic Sans MS",10),fg="red").grid(row=0,column=1,sticky="e")
		botonAbrirArchivo = Button(self.frame1,text="Abrir",command=self.abrirArchivo)
		botonAbrirArchivo.grid(row=0,column=2,padx=10)

		#parte de numero de elementos
		Label(self.frame1,text="Numero de elementos:",font=("Comic Sans MS",12)).grid(row=1,column=0,sticky="e")
		numDatos = Entry(self.frame1,textvariable=self.numdata)
		numDatos.grid(row=1,column=1,padx=10)
		#parte de selector de opciones
		Label(self.frame1,text="Seleccione el tipo de algoritmo a comparar:",font=("Comic Sans MS",12)).grid(row=2,column=0,sticky="e",padx=10)
		Label(self.frame1,text="*",font=("Comic Sans MS",10),fg="red").grid(row=2,column=0,sticky="e")
		insert = Checkbutton(self.frame1, text='Insert-Sort',variable=self.insertV).grid(row=4,column=1,padx=10)
		merge = Checkbutton(self.frame1, text='Merge-Sort',variable=self.mergeV).grid(row=5,column=1,padx=10)
		quick = Checkbutton(self.frame1, text='Quick-Sort',variable=self.quickV).grid(row=6,column=1,padx=10)
		stooge = Checkbutton(self.frame1, text='Stooge-Sort',variable=self.stoogeV).grid(row=7,column=1,padx=10)


		botones = Button(self.frame1,text="Continuar",width=70,bg='green',fg='white',command=self.verificar,relief="groove")
		botones.grid(row=8,column=0,columnspan=3)

#--------------------------Funciones--------------------------------------
	#Funcion abrir ventana de selector de archivos
	def abrirArchivo(self):
		archivo = fd.askopenfilename(initialdir = "/",title = "Abrir",filetypes = (("txt files","*.txt"),("todos los archivos","*.*")))
		self.url.set(archivo) 
	#Funcion para verificar si los campos estan vacios o no
	def verificar(self):
		if (self.url.get() != '' ):
			if (self.insertV.get() == True or self.mergeV.get() == True or self.quickV.get() == True or self.stoogeV.get() == True):
				self.mensajeError.config(text="")
			else:
				self.mensajeError.config(text="Al menos selecciones uno de los algoritmos")
		else:
			self.mensajeError.config(text="*Debe llenar los campos obligatorio",fg="red")

#-----------------------Funcion main para ejecutar la aplicacion---------------------
def main():
	mi_app = Aplicacion()
	return 0

if __name__ == '__main__':
	main()