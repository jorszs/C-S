from tkinter import ttk
from tkinter import *
from pymongo import MongoClient



class Napster:

    def __init__(self, window):

        wind = window
        wind.title("Napster Application")

        background = PhotoImage(file = 'unnamed.gif')
        Background = Label(wind, image = background)
        Background.place(x = -2, y = -2)

    
        #Crear un Frame: donde me permite adentro crear elementos 

        frame = LabelFrame(wind, text = "Busqueda", font =  15)
        frame.grid(row = 1, column = 0, pady = 15, padx = 5)

        #Name input

        Label(frame, text = "Opcion", font =  12).grid(row = 1, column = 0)
        com = ttk.Combobox(frame, values =["Canciones", "Album", "Artista"],  width=10 ).grid(row = 1, column = 1, padx = 5, pady = 5)
        opcion = Entry(frame, width=40)
        opcion.focus()
        opcion.grid(row = 1, column = 2, padx = 5)

        #Button search
        #Column span:Centrado
        #Sticky: Todo el ancho de mi ventana 
        ttk.Button(frame, text = "BUSCAR", width=10).grid(row = 1, columnspan = 3,column = 3, padx = 5)
        

        
        

        #Table
        tree = ttk.Treeview(height = 10, columns = ("1", "2", "3"))
        tree.grid(row = 4, column = 0, columnspan = 5)
        tree.heading('#0', text = "Titulo",anchor = CENTER)
        tree.heading("1", text = "Artista", anchor = CENTER)
        tree.heading("2", text = "Album", anchor = CENTER)
        tree.heading("3", text = "Opcion", anchor = CENTER)

        self.run_query()


    def run_query(self, parameters = ()):
        puerto = 27017
        mongoClient = MongoClient("localhost", puerto)
        db = mongoClient.napster

        collection = db.Canciones
        print(collection)

    def search(self, opcion, com):
        puerto = 27017
        mongoClient = MongoClient("localhost", puerto)
        db = mongoClient.napster

        search = opcion.get()

        if len(search) == 0:
            print("Buscar")
        else:
            filter = com.get()
            if (filter == 'Canciones'):
                print("aaa")

        




if __name__ == '__main__':
    window =Tk()
    application = Napster(window)
    window.mainloop()