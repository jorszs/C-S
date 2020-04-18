from tkinter.ttk import *
from tkinter import *
from pymongo import MongoClient
from functools import partial


class Napster:
    aplication = "mundo"
    servers = "servidores"

    def __init__(self, window, comand, texto, path):
        wind = window
        wind.title("Napster Application")

        '''background = PhotoImage(file = 'unnamed.gif')
        Background = Label(wind, image = background)
        Background.place(x = -2, y = -2)'''

        # Crear un Frame: donde me permite adentro crear elementos

        frame = LabelFrame(wind, text="BUSCAR", font=15)
        frame.grid(row=1, column=0, pady=15, padx=5)

        # Name input

        Label(frame, text="Opcion", font=12).grid(row=1, column=0)
        self.filtro = Combobox(frame,  width=10)
        self.filtro['values'] = ("titulo", "album", "artista")
        self.filtro.grid(row=1, column=1, padx=5, pady=5)
        self.filtro.current(0)
        self.opcion = Entry(frame, width=40)
        self.opcion.focus()
        self.opcion.grid(row=1, column=2, padx=5)

        # Button search
        # Column span:Centrado
        # Sticky: Todo el ancho de mi ventana

        btn_buscar = Button(frame, text=texto, width=10, command=partial(comand, self, path)).grid(
            row=1, columnspan=3, column=3, padx=5)

        # Table
        self.tree = Treeview(height=10, columns=("1", "2", "3"))
        self.tree.grid(row=4, column=0, columnspan=5)
        self.tree.heading('#0', text="Titulo", anchor=CENTER)
        self.tree.heading("1", text="Artista", anchor=CENTER)
        self.tree.heading("2", text="Album", anchor=CENTER)
        self.tree.heading("3", text="Opcion", anchor=CENTER)
        #self.tree.bind("<ButtonRelease-1>", self.download)
        self.run_query()

    def download(self, a):
        print("click")

    def run_query(self, parameters=()):

        try:
            puerto = 27017
            mongoClient = MongoClient("localhost", puerto)
            db = mongoClient.napster

            collection = db.canciones
            canciones = collection.find({})
            for cursor in canciones:
                print("x")
                # cursor["titulo"]
        except:
            print("no se conecto a base de datos")

    def search(self, opcion, filtro):
        puerto = 27017
        mongoClient = MongoClient("localhost", puerto)
        db = mongoClient.napster

        search = opcion.get()

        if len(search) == 0:
            print("Buscar")
        else:
            filter = filtro.get()
            if (filter == 'Canciones'):
                print("aaa")

    def getTable(self):
        return self.tree

    def setApplication(self, application):
        self.application = application
        # print(self.aplication)

    def setServers(self, servers):
        self.servers = servers
# if __name__ == '__main__':


'''
def interfaz():
    window = Tk()
    application = Napster(window)
    window.mainloop()'''
