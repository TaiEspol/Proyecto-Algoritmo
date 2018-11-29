from tkinter import * 
import tkinter as tk
from tkinter import filedialog as fd
import time
import random
from prettytable import PrettyTable
import matplotlib
import matplotlib.pyplot as pyplot


class Aplicacion():
	def __init__(self):
		#Ventana principal
		self.raiz = Tk()
		self.raiz.title("Analisis de Algoritmo")
		self.raiz.minsize(550, 300)
		self.raiz.resizable(0,0)

		#barra de menu
		self.barraMenu = Menu(self.raiz)
		self.raiz.config(menu=self.barraMenu,width=300,height=200)
		self.inicio = Menu(self.barraMenu,tearoff=0)
		#self.inicio.add_command(label="Nuevo",command=lambda: self.show_frame("PageInicio"))
		self.inicio.add_command(label="Salir",command=self.raiz.destroy)
		#self.herramienta = Menu(self.barraMenu,tearoff=0)
		self.barraMenu.add_cascade(label="Inicio",menu=self.inicio)
		#self.barraMenu.add_cascade(label="Herramienta",menu=self.herramienta)
		#contenedor de los frames para cambiar de pantalla
		contenedor = tk.Frame(self.raiz)
		contenedor.pack(side="top", fill="both", expand=True)

		self.frames = {}
		for F in (PageInicio, PageTwo):
			nombre_pagina = F.__name__
			frame = F(parent=contenedor, controller=self)
			self.frames[nombre_pagina] = frame

            # poner todas las páginas en la misma ubicación; 
            # el que está en la parte superior del orden de apilamiento 
            # será el que está visible.
			frame.grid(row=0, column=0, sticky="nsew")
		self.show_frame("PageInicio")
		self.raiz.mainloop()

	def show_frame(self, page_name):
		'''Show a frame for the given page name'''
		frame = self.frames[page_name]
		frame.tkraise()

	def get_page(self, page_class):
		'''obtener las variables de un frame'''
		return self.frames[page_class]

class PageInicio(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller
	#variales de los campos
		self.url = StringVar(value='')
		self.insertV = BooleanVar(value=True)
		self.mergeV = BooleanVar(value=True)
		self.quickV = BooleanVar(value=True)
		self.numdata = IntVar(value=0)
		self.mensajeError = StringVar(value='')
		self.arreglo = []
		self.generarDato = BooleanVar(value=False)
		self.numeros = IntVar(value=0)
		self.direccionArchivoGuardado = StringVar(value='')

		#parte de archivos
		Label(self,text="Archivo:",font=("Comic Sans MS",12)).grid(row=0,column=0,sticky="e")
		texto = Entry(self,textvariable=self.url,state='disabled')
		texto.grid(row=0,column=1,padx=10)
		Label(self,text="*",font=("Comic Sans MS",10),fg="red").grid(row=0,column=1,sticky="e")
		self.botonAbrirArchivo = Button(self,text="Abrir",command=self.abrirArchivo,state='active')
		self.botonAbrirArchivo.grid(row=0,column=2,padx=10)

		#parte de generar datos aleatorios
		Label(self,text="Numeros generados aleatoriamente:",font=("Comic Sans MS",12)).grid(row=1,column=0,sticky="e")
		generarDatos = Checkbutton(self, text='Si',variable=self.generarDato,command=self.eventoDatos).grid(row=1,column=1,padx=10,sticky="w")
		self.numero = Entry(self,textvariable=self.numeros,state='disabled',width=5)
		self.numero.grid(row=1,column=1,padx=10,sticky="e")
		self.botonGuardar = Button(self,text="Guardar",command=self.guardar,state='disabled')
		self.botonGuardar.grid(row=1,column=2,padx=10)

		#parte de numero de elementos
		Label(self,text="Numero de elementos a ordenarse:",font=("Comic Sans MS",12)).grid(row=2,column=0,sticky="e")
		numDatos = Entry(self,textvariable=self.numdata)
		numDatos.grid(row=2,column=1,padx=10)

		#parte de selector de opciones
		Label(self,text="Seleccione el tipo de algoritmo a comparar:",font=("Comic Sans MS",12)).grid(row=3,column=0,sticky="e",padx=10)
		Label(self,text="*",font=("Comic Sans MS",10),fg="red").grid(row=3,column=0,sticky="e")
		insert = Checkbutton(self, text='Insert-Sort',variable=self.insertV).grid(row=4,column=1,padx=10)
		merge = Checkbutton(self, text='Merge-Sort',variable=self.mergeV).grid(row=5,column=1,padx=10)
		quick = Checkbutton(self, text='Quick-Sort',variable=self.quickV).grid(row=6,column=1,padx=10)

		#boton de mostrar
		botones = Button(self,text="Mostrar",width=70,bg='green',fg='white',relief="groove",command=self.verificar)
		botones.grid(row=8,column=0,columnspan=3)

		botones = Button(self,text="Limpiar",width=70,bg='red',fg='white',relief="groove",command=self.limpiar)
		botones.grid(row=9,column=0,columnspan=3)

		Label(self,textvariable=self.mensajeError,font=("Comic Sans MS",12),fg="red").grid(row=10,column=0,columnspan=3)
	
#----------------------------merge sort----------------------------
	def mergeSort(self,alist):
		if len(alist)>1:
			mid = len(alist)//2
			lefthalf = alist[:mid]
			righthalf = alist[mid:]

			self.mergeSort(lefthalf)
			self.mergeSort(righthalf)

			i=0
			j=0
			k=0
			while i < len(lefthalf) and j < len(righthalf):
				if lefthalf[i] < righthalf[j]:
					alist[k]=lefthalf[i]
					i=i+1
				else:
					alist[k]=righthalf[j]
					j=j+1
				k=k+1

			while i < len(lefthalf):
				alist[k]=lefthalf[i]
				i=i+1
				k=k+1

			while j < len(righthalf):
				alist[k]=righthalf[j]
				j=j+1
				k=k+1
#-----------------------------insert sort--------------------
	def insertionSort(self,alist):
		for index in range(1,len(alist)):

			currentvalue = alist[index]
			position = index
			while position>0 and alist[position-1]>currentvalue:
				alist[position]=alist[position-1]
				position = position-1
			alist[position]=currentvalue
#-----------------quick sort -----------------------------------
	def quickSort(self,alist):
	  self.quickSortHelper(alist,0,len(alist)-1)

	def quickSortHelper(self,alist,first,last):
	   if first<last:

	       splitpoint = self.partition(alist,first,last)

	       self.quickSortHelper(alist,first,splitpoint-1)
	       self.quickSortHelper(alist,splitpoint+1,last)


	def partition(self,alist,first,last):
	   pivotvalue = alist[first]

	   leftmark = first+1
	   rightmark = last

	   done = False
	   while not done:

	       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
	           leftmark = leftmark + 1

	       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
	           rightmark = rightmark -1

	       if rightmark < leftmark:
	           done = True
	       else:
	           temp = alist[leftmark]
	           alist[leftmark] = alist[rightmark]
	           alist[rightmark] = temp

	   temp = alist[first]
	   alist[first] = alist[rightmark]
	   alist[rightmark] = temp


	   return rightmark

#--------------------------Funciones--------------------------------------
	#Funcion abrir ventana de selector de archivos
	def abrirArchivo(self):
		archivo = fd.askopenfilename(initialdir = "/",title = "Abrir",filetypes = (("txt files","*.txt"),("todos los archivos","*.*")))
		self.url.set(archivo) 

	#Funcion para verificar si los campos estan vacios o no
	def verificar(self):
		
		if (self.url.get() != ''):
			if (self.insertV.get() == True or self.mergeV.get() == True or self.quickV.get() == True or self.stoogeV.get() == True):
					self.mensajeError.set("")
					self.abrirArchivo2()
					if len(self.arreglo) != 0:
						if self.numdata.get() == 0:
							self.numdata.set(len(self.arreglo))
						self.dibujarCoordenads(self.numdata.get(),self.arreglo)
						
					else:
						self.mensajeError.set("NO EXISTE ELEMENTO EN EL ARREGLO")
			else:
				self.mensajeError.set("Al menos selecciones uno de los algoritmos")
		else:
			if self.generarDato.get() != False:
				if self.numero.get() != 0 and self.direccionArchivoGuardado.get() != '' and self.numero.get().isdigit() == True:
					if (self.insertV.get() == True or self.mergeV.get() == True or self.quickV.get() == True or self.stoogeV.get() == True):
							self.mensajeError.set("")
							self.generarArreglos()
							if len(self.arreglo) != 0:
								if self.numdata.get() == 0:
									self.numdata.set(len(self.arreglo))
								self.dibujarCoordenads(self.numdata.get(),self.arreglo)
							else:
								self.mensajeError.set("NO EXISTE ELEMENTO EN EL ARREGLO")
					else:
						self.mensajeError.set("Al menos selecciones uno de los algoritmos")
				else:
					self.mensajeError.set("Casillero debe ser un numero > 0 y debe crear un archivo")
				
			else:
				self.mensajeError.set("*Debe llenar los campos obligatorio")
	#borra todos los datos ingresados
	def limpiar(self):
		self.url.set("")
		self.insertV.set(True)
		self.mergeV.set(True)
		self.quickV.set(True)
		self.numdata.set(0)
		self.mensajeError.set('')
		self.arreglo = []
		self.generarDato.set(False)
		self.direccionArchivoGuardado.set('')
		self.botonAbrirArchivo['state'] = 'active'
		self.botonGuardar['state'] = 'disabled'
		self.numero['state'] = 'disabled'
		self.numeros.set(0)
#abrir el archivo y convertir el contenido en un arreglo
	def abrirArchivo2(self):
		array = []
		array2 = []
		archivo = open(self.url.get(), "r")
		array = archivo.readlines()
		if len(array) == 0:
			archivo.close()
			self.mensajeError.set("El archivo de texto esta vacio")
		else:
			for x in array:
				if x != '\n':
				    array2.append(int(x.replace("\n",""))) 
			archivo.close()
			self.arreglo = array2

	#guarda la direccion del donde se va a guardar el arreglo generado
	def guardar(self):
		nombrearch=fd.asksaveasfilename(initialdir = "/",title = "Guardar como",filetypes = (("txt files","*.txt"),("todos los archivos","*.*")))
		if nombrearch!='':
			self.direccionArchivoGuardado.set( nombrearch + '.txt')

#genera los numeros aleatorios
	def generarArreglos(self):
		n = self.numeros.get()
		lista = [0] * n
		archivo = open(self.direccionArchivoGuardado.get(), "w")
		for i in range(n):
			lista[i] = random.randint(0, 400)
			archivo.write(str(lista[i]) + '\n')
		archivo.close()
		self.arreglo = lista

	#cambia los estados del numero aleatorio y archivos
	def eventoDatos(self):
		if self.generarDato.get() == True:
			self.botonAbrirArchivo['state'] = 'disabled'
			self.botonGuardar['state'] = 'active'
			self.numero['state'] = 'normal'
		else:
			self.botonAbrirArchivo['state'] = 'active'
			self.botonGuardar['state'] = 'disabled'
			self.numero['state'] = 'disabled'

	#guardar los resultados de la tabla en un archivo txt en el directorio donde se encuentra el codigo fuente 
	def crearArchivoYguardar(self,variableEntrada):
		with open('resultado.txt', 'w') as archivo:
			archivo.write(str(variableEntrada))
		archivo.close()
		self.mensajeError.set("SE GUARDO LOS RESULTADOS EN UN ARCHIVO .TXT,SE ENCUENTRA JUNTO AL CODIGO FUENTE DEL PROYECTO ")
	#funcion para graficar las coordenadas y tablas
	def dibujarCoordenads(self,numdata, selfarreglo):
		selfnumdata = numdata
		inslist = []
		insrep = []
		mergerep = []  # arreglo de datos usando merge
		quickrep = []  # arreglo de datos usando quick
		nlist = []
		alist = selfarreglo
		self.limpiar()#limpiar la salida
		t = 0 #insertion
		v = 0 #merger
		u = 0 #quick

		# ordena y recorre los algoritmos
		for index in range(5, selfnumdata,5):  # se define el rango de 200 numeros de 5 en 5
			nlist.append(index)
			# suavizando los arreglos
			time1 = 0
			time2 = 0
			time3 = 0
			
			for j in range(0, 2):
				alist1 = list(alist)
				alist2 = list(alist)
				alist3 = list(alist)

				if self.insertV.get() == True:
					start_time = time.time()
					self.insertionSort(alist1)
					ti = time.time() - start_time
					time1 += ti
					t = 1

				if self.mergeV.get() == True:
					start_time = time.time()
					self.mergeSort(alist2)
					tm = time.time() - start_time
					time2 += tm
					v = 1

				if self.quickV.get() == True:
					start_time = time.time()
					self.quickSort(alist3)
					tq = time.time() - start_time
					time3 += tq
					u = 1

			insrep.append(time1 / 3)
			mergerep.append(time2 / 3)
			quickrep.append(time3 / 3)
#---------------Graficar y mostrar en pantalla-----
		pyplot.xticks([10 * index for index in range(1, selfnumdata)])

		pyplot.xlabel('$N$')
		pyplot.ylabel('$Time$')
		#Graficar en una tabla y coordenadas 
		if (t==1 and v==0 and u==0):
			ta = PrettyTable(['N', 'Insertion Sort Time'])  # se define el nombre de las columnas de la tabla
			for index in range(0, len(insrep)):
				ta.add_row([nlist[index], insrep[index]])
			self.crearArchivoYguardar(ta)
			pyplot.line = pyplot.plot(nlist, insrep, label='Insertion Sort')
			pyplot.legend(loc='upper left')
			pyplot.show()
		else:
			if (v==1 and t==0 and u==0):
				ta = PrettyTable(['N','Merge Sort Time'])  # se define el nombre de las columnas de la tabla
				for index in range(0, len(insrep)):
					ta.add_row([nlist[index], mergerep[index]])
				self.crearArchivoYguardar(ta)
				pyplot.line = pyplot.plot(nlist, mergerep, label='Merge Sort')
				pyplot.legend(loc='upper left')
				pyplot.show()
			else:
				if (u==1 and t==0 and v==0):
					ta = PrettyTable(['N','Quick Sort Time'])  # se define el nombre de las columnas de la tabla
					for index in range(0, len(insrep)):
						ta.add_row([nlist[index], quickrep[index]])
					self.crearArchivoYguardar(ta)
					pyplot.line = pyplot.plot(nlist, quickrep, label='Quick Sort')
					pyplot.legend(loc='upper left')
					pyplot.show()

		if t==1 and v==1 and u==1:
			ta = PrettyTable(['N', 'Insertion Sort Time', 'Merge Sort Time','Quick Sort Time'])  # se define el nombre de las columnas de la tabla
			for index in range(0, len(insrep)):
				ta.add_row([nlist[index], insrep[index], mergerep[index], quickrep[index]])
			self.crearArchivoYguardar(ta)
			pyplot.line = pyplot.plot(nlist, insrep, label='Insertion Sort')
			pyplot.line = pyplot.plot(nlist, mergerep, label='Merge Sort')
			pyplot.line = pyplot.plot(nlist, quickrep, label='Quick Sort')
			pyplot.legend(loc='upper left')
			pyplot.show()
		else:
			if t==1 and v==1 and u==0:
				ta = PrettyTable(['N', 'Insertion Sort Time', 'Merge Sort Time'])  # se define el nombre de las columnas de la tabla
				for index in range(0, len(insrep)):
					ta.add_row([nlist[index], insrep[index], mergerep[index]])
				self.crearArchivoYguardar(ta)
				pyplot.line = pyplot.plot(nlist, mergerep, label='Merge Sort')
				pyplot.line = pyplot.plot(nlist, insrep, label='Insertion Sort')
				pyplot.legend(loc='upper left')
				pyplot.show()
			else:
				if t==1 and u==1 and v==0:
					ta = PrettyTable(['N', 'Insertion Sort Time','Quick Sort Time'])  # se define el nombre de las columnas de la tabla
					for index in range(0, len(insrep)):
						ta.add_row([nlist[index], insrep[index], quickrep[index]])
					self.crearArchivoYguardar(t)
					pyplot.line = pyplot.plot(nlist, insrep, label='Insertion Sort')
					pyplot.line = pyplot.plot(nlist, quickrep, label='Quick Sort')
					pyplot.legend(loc='upper left')
					pyplot.show()
				else:
					if u==1 and v==1 and t==0:
						ta = PrettyTable(['N','Merge Sort Time','Quick Sort Time'])  # se define el nombre de las columnas de la tabla
						for index in range(0, len(insrep)):
							ta.add_row([nlist[index],mergerep[index], quickrep[index]])
						self.crearArchivoYguardar(ta)
						pyplot.line = pyplot.plot(nlist, mergerep, label='Merge Sort')
						pyplot.line = pyplot.plot(nlist, quickrep, label='Quick Sort')
						pyplot.legend(loc='upper left')
						pyplot.show()

#segundo frame
class PageTwo(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller
		self.contenido_pageInicio = self.controller.get_page('PageInicio')


	
#-----------------------Funcion main para ejecutar la aplicacion---------------------
def main():
	mi_app = Aplicacion()
	return 0

if __name__ == '__main__':
	main()