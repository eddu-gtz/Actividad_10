from PySide2.QtWidgets import QMainWindow
#Decorador que se llama cuando se ejecute la aplicacion
from PySide2.QtCore import Slot
#clase Vista
from ui_mainwindow import Ui_MainWindow
#Clases Administradora y Particula
from administradora import Administradora
from particula import Particula

#Controlador de vista
class MainWindow(QMainWindow):
    def __init__(self):
        #inicializar el objeto QMainWindow
        super(MainWindow, self).__init__()
        #Creacion del objeto Administrador de particulas
        self.administrador = Administradora()

        #Objeto de la clase Ui_MainWindow
        self.ui = Ui_MainWindow()
        #Se incrustan las configuraciones de la clase
        self.ui.setupUi(self)
        #Configurar el evento click del boton
        self.ui.agregar_final_pushButton.clicked.connect(self.click_agregar_final)
        self.ui.agregar_inicio_pushButton.clicked.connect(self.click_agregar_inicio)
        self.ui.mostrar_pushButton.clicked.connect(self.click_mostrar)

    @Slot()
    def click_mostrar(self):
        #Limpia el PlainText y despues inserta los datos
        self.ui.salida.clear()
        self.ui.salida.insertPlainText(str(self.administrador))
    
    @Slot()
    def click_agregar_final(self):
        #Variables para obtener la informacion
        id = self.ui.id_spinBox.value()
        origen_x = self.ui.origen_x_spinBox.value()
        origen_y = self.ui.origen_y_spinBox.value()
        destino_x = self.ui.destino_x_spinBox.value()
        destino_y = self.ui.destino_y_spinBox.value()
        velocidad = self.ui.velocidad_spinBox.value()
        red = self.ui.red_spinBox.value()
        green = self.ui.green_spinBox.value()
        blue = self.ui.blue_spinBox.value()
        
        particula = Particula(id, origen_x, origen_y, destino_x, destino_y, velocidad, red, green, blue)

        self.administrador.agregar_final(particula)

        

    @Slot()
    def click_agregar_inicio(self):
        #Variables para obtener la informacion
        id = self.ui.id_spinBox.value()
        origen_x = self.ui.origen_x_spinBox.value()
        origen_y = self.ui.origen_y_spinBox.value()
        destino_x = self.ui.destino_x_spinBox.value()
        destino_y = self.ui.destino_y_spinBox.value()
        velocidad = self.ui.velocidad_spinBox.value()
        red = self.ui.red_spinBox.value()
        green = self.ui.green_spinBox.value()
        blue = self.ui.blue_spinBox.value()
        
        particula = Particula(id, origen_x, origen_y, destino_x, destino_y, velocidad, red, green, blue)

        self.administrador.agregar_inicio(particula)

        
        
