import sys

from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QHBoxLayout, QFormLayout, QApplication, QLineEdit, \
    QPushButton
from PyQt5 import QtGui

class Ventana1(QMainWindow):

    # hacer el metodo de construccion de la ventana
    def __init__(self, parent=None):
        super(Ventana1, self).__init__(parent)

        # poner el titulo
        self.setWindowTitle("Formulario de registro")

        # poner el icono:
        self.setWindowIcon(QtGui.QIcon('imagenes/gato.png'))

        # establecer propiedades de ancho y alto
        self.ancho = 800
        self.alto = 600

        # establecer el tamaño de la ventana
        self.resize(self.ancho, self.alto)

        # hacer que la ventana se vea en el centro:
        self.pantalla = self.frameGeometry()
        self.centro = QDesktopWidget().availableGeometry().center()
        self.pantalla.moveCenter(self.centro)
        self.move(self.pantalla.topLeft())

        # fijar el ancho y el alto de la ventana
        self.setFixedWidth(self.ancho)
        self.setFixedHeight(self.alto)

        # establecer el fondo principal
        self.fondo = QLabel(self)

        # definimos la imagen de fondo
        self.imagenFondo = QPixmap('imagenes/3gatos.jpg')

        # definimos la imagen de fondo
        self.fondo.setPixmap(self.imagenFondo)

        # establecemos el modo para escalar la imagen
        self.fondo.setScaledContents(True)

        # hacemos que se adapte el tamaño de la imagen
        self.resize(self.imagenFondo.width(), self.imagenFondo.height())

        # establecemos la ventana de fondo como la ventana central
        self.setCentralWidget(self.fondo)

        # establecemos la distribucion de los elementos en layout horizontal
        self.horizontal = QHBoxLayout()
        # le ponemos los margenes
        self.horizontal.setContentsMargins(30, 30, 30, 30)

        # --------- LAYOUT IZQUIERDO ---------

        # creamos el layout del lado izquierdo
        self.ladoIzquierdo = QFormLayout()

        # hacemos el letrero
        self.letrero1 = QLabel()

        # le asignamos el texto
        self.letrero1.setText("Informacion del cliente")

        # le asignamos el tipo de letra
        self.letrero1.setFont(QFont("Arial Black",18))

        # le ponemos el color de texto
        self.letrero1.setStyleSheet("color: #f2f2f2;")

        # agregamos el letrero en la primera fila
        self.ladoIzquierdo.addRow(self.letrero1)

        # hacemos el letrero
        self.letrero2 = QLabel()

        # establecemos el ancho del label:
        self.letrero2.setFixedWidth(340)

        # le escribimos el texto
        self.letrero2.setText("Por favor ingresar la informacion del cliente"
                              "\nen el formulario de abajo. Los campos marcados"
                              "\ncon asteriscos son obligatorios.")

        # le asignamos el tipo de letra
        self.letrero2.setFont(QFont("Arial", 10))

        # le ponemos el color de texto y margenes
        self.letrero2.setStyleSheet("color: #f2f2f2; margin-bottom: 30px;"
                                    "margin-top: 20px;"
                                    "padding-bottom 10px;"
                                    "border: 1px solid #f2f2f2;"
                                    "border-left: none;"
                                    "border-right: none;"
                                    "border-top: none;")

        # agregamos el letrero en la fila siguiente
        self.ladoIzquierdo.addRow(self.letrero2)

        # hacemos el campo para ingresar el nombre
        self.nombreCompleto = QLineEdit()
        self.nombreCompleto.setFixedWidth(250)

        # agregamos estos en el formulario
        self.ladoIzquierdo.addRow("Nombre Completo*", self.nombreCompleto)

        # hacemos el campo para ingresar el usuario
        self.usuario = QLineEdit()
        self.usuario.setFixedWidth(250)

        # agregamos estos en el formulario
        self.ladoIzquierdo.addRow("Usuario*", self.usuario)

        # hacemos el campo para ingresar el password
        self.password = QLineEdit()
        self.password.setFixedWidth(250)
        self.password.setEchoMode(QLineEdit.Password)

        # agregamos estos en el formulario
        self.ladoIzquierdo.addRow("Password*", self.password)

        # hacemos el campo para ingresar el password
        self.password2 = QLineEdit()
        self.password2.setFixedWidth(250)
        self.password2.setEchoMode(QLineEdit.Password)

        # agregamos estos en el formulario
        self.ladoIzquierdo.addRow("Password*", self.password2)

        # hacemos el campo para ingresar el documento
        self.documento = QLineEdit()
        self.documento.setFixedWidth(250)

        # agregamos el documento en el formulario
        self.ladoIzquierdo.addRow("Documento*", self.documento)

        # hacemos el campo para ingresar el correo
        self.correo = QLineEdit()
        self.correo.setFixedWidth(250)

        # agregamos el documento en el formulario
        self.ladoIzquierdo.addRow("Correo*", self.correo)

        # hacemos el boton para registrar los datos
        self.botonRegistrar = QPushButton("Registrar")

        # establecemos el ancho del boton
        self.botonRegistrar.setFixedWidth(90)

        # le ponemos los estilos
        self.botonRegistrar.setStyleSheet("background-color: #c14056;"
                                          "color: #ffffff;"
                                          "padding: 10px;"
                                          "margin-top: 40px;")

        self.botonRegistrar.clicked.connect(self.accion_botonRegistrar)

        # hacemos el boton para limpiar los datos
        self.botonLimpiar = QPushButton("Limpiar")

        # establecemos el ancho del boton
        self.botonLimpiar.setFixedWidth(90)

        # le ponemos los estilos
        self.botonLimpiar.setStyleSheet("background-color: #c14056;"
                                          "color: #ffffff;"
                                          "padding: 10px;"
                                          "margin-top: 40px;")

        self.botonLimpiar.clicked.connect(self.accion_botonLimpiar)

        # agregamos lo botones al layout izquierdo
        self.ladoIzquierdo.addRow(self.botonRegistrar, self.botonLimpiar)


        # agregamos el layout ladoIzquierdo al layout horizontal
        self.horizontal.addLayout(self.ladoIzquierdo)

        #---------- FINAL ------------

        # indicamos que el layout principal del fondo es horizontal
        self.fondo.setLayout(self.horizontal)

   # metodo del boton limpiar
    def accion_botonLimpiar(self):
        self.nombreCompleto.setText('')
        self.usuario.setText('')
        self.password.setText('')
        self.password2.setText('')
        self.documento.setText('')
        self.correo.setText('')

   # metodo del boton registrarse
    def accion_botonRegistrar(self):
        pass



if __name__ == '__main__':
    app = QApplication(sys.argv)

    ventana1 = Ventana1()

    ventana1.show()

    sys.exit(app.exec_())