import sys

from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QHBoxLayout, QFormLayout, QApplication, QLineEdit, \
    QPushButton, QDialog, QDialogButtonBox, QVBoxLayout
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import Qt
from cliente import cliente

class Ventana1(QMainWindow):

    # hacer el metodo de construccion de la ventana
    def __init__(self, parent=None):
        super(Ventana1, self).__init__(parent)

        # poner el titulo
        self.setWindowTitle("Formulario de registro")

        # poner el icono:
        self.setWindowIcon(QtGui.QIcon('imagenes/gato.png'))

        # establecer propiedades de ancho y alto
        self.ancho = 900
        self.alto = 610

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

        # --------------layout derecho------------

        # creamos el layout del lado izquierdo
        self.ladoDerecho = QFormLayout()

        # se asigna la margen solo a la izquierda de 100px
        self.ladoDerecho.setContentsMargins(100, 0, 0, 0)

        # hacemos el letrero
        self.letrero3 = QLabel()

        # le escribimos el texto
        self.letrero3.setText("Recuperar contraseña")

        # le asignamos el tipo de letra
        self.letrero3.setFont(QFont("Arial Black", 18))

        # le ponemos el color de texto y margenes
        self.letrero3.setStyleSheet("color: #f2f2f2;")

        # le ponemos el color de texto
        self.letrero3.setStyleSheet("color: #f2f2f2;")

        # agregamos el letrero en la primera fila
        self.ladoDerecho.addRow(self.letrero3)

        # hacemos el letrero
        self.letrero4 = QLabel()

        # establecemos el ancho del label
        self.letrero4.setFixedWidth(400)

        # le escribimos el texto
        self.letrero4.setText("Por favor ingrese la informacion para recuperar"
                              "\nla contraseña. Los campos marcados"
                              "\ncon asterisco son obligatorios")

        # le asignamos el tipo de letra
        self.letrero4.setFont(QFont("Arial", 10))

        # le ponemos el color de texto y margenes
        self.letrero4.setStyleSheet("color: #f2f2f2; margin-bottom: 30px;"
                                    "margin-top: 20px;"
                                    "padding-bottom 10px;"
                                    "border: 1px solid #f2f2f2;"
                                    "border-left: none;"
                                    "border-right: none;"
                                    "border-top: none;")

        # agregamos el letrero en la fila siguiente
        self.ladoDerecho.addRow(self.letrero4)

        # --- 1

        # hacemos el letrero de la pregunta 1
        self.labelPregunta1 = QLabel("Pregunta de verificacion 1*")

        # agregamos el letrero a la fila siguiente
        self.ladoDerecho.addRow(self.labelPregunta1)

        # hacemos el campo para ingresar la pregunta 1
        self.pregunta1 = QLineEdit()
        self.pregunta1.setFixedWidth(320)

        # agregamos el campo en el formulario
        self.ladoDerecho.addRow(self.pregunta1)

        # hacemos el letrero de la respuesta 1
        self.labelRespuesta1 = QLabel("Respuesta de verificacion 1*")

        # agregamos el letrero en la fila siguiente
        self.ladoDerecho.addRow(self.labelRespuesta1)

        # hacemos el campo para ingresar la respuesta 1
        self.respuesta1 = QLineEdit()
        self.respuesta1.setFixedWidth(320)

        # agregamos el campo en el formulario
        self.ladoDerecho.addRow(self.respuesta1)

        # --- 2

        # hacemos el letrero de la pregunta 2
        self.labelPregunta2 = QLabel("Pregunta de verificacion 2*")

        # agregamos el letrero a la fila siguiente
        self.ladoDerecho.addRow(self.labelPregunta2)

        # hacemos el campo para ingresar la pregunta
        self.pregunta2 = QLineEdit()
        self.pregunta2.setFixedWidth(320)

        # agregamos el campo en el formulario
        self.ladoDerecho.addRow(self.pregunta2)

        # hacemos el letrero de la respuesta 2
        self.labelRespuesta2 = QLabel("Respuesta de verificacion 2*")

        # agregamos el letrero en la fila siguiente
        self.ladoDerecho.addRow(self.labelRespuesta2)

        # hacemos el campo para ingresar la respuesta 2
        self.respuesta2 = QLineEdit()
        self.respuesta2.setFixedWidth(320)

        # agregamos el campo en el formulario
        self.ladoDerecho.addRow(self.respuesta2)

        # --- 3

        # hacemos el letrero de la pregunta 3
        self.labelPregunta3 = QLabel("Pregunta de verificacion 3*")

        # agregamos el letrero a la fila siguiente
        self.ladoDerecho.addRow(self.labelPregunta3)

        # hacemos el campo para ingresar la pregunta 3
        self.pregunta3 = QLineEdit()
        self.pregunta3.setFixedWidth(320)

        # agregamos el campo en el formulario
        self.ladoDerecho.addRow(self.pregunta3)

        # hacemos el letrero de la respuesta 3
        self.labelRespuesta3 = QLabel("Respuesta de verificacion 3*")

        # agregamos el letrero en la fila siguiente
        self.ladoDerecho.addRow(self.labelRespuesta3)

        # hacemos el campo para ingresar la respuesta 3
        self.respuesta3 = QLineEdit()
        self.respuesta3.setFixedWidth(320)

        # agregamos el campo en el formulario
        self.ladoDerecho.addRow(self.respuesta3)

        # hacemos el boton para buscar las preguntas
        self.botonBuscar = QPushButton("Buscar")

        # establecemos el ancho del boton
        self.botonBuscar.setFixedWidth(90)

        # le ponemos los estilos
        self.botonBuscar.setStyleSheet("background-color: #c14056;"
                                        "color: #ffffff;"
                                        "padding: 10px;"
                                        "margin-top: 40px;")
        # hacemos que el botonBuscar tenga su metodo
        self.botonBuscar.clicked.connect(self.accion_botonBuscar)



        # hacemos el boton para recuperar la contraseña
        self.botonRecuperar = QPushButton("Recuperar")

        # establecemos el ancho del boton
        self.botonRecuperar.setFixedWidth(90)

        # le ponemos los estilos
        self.botonRecuperar.setStyleSheet("background-color: #c14056;"
                                          "color: #ffffff;"
                                          "padding: 10px;"
                                          "margin-top: 40px;")

        # agregamos botones al layout ladoDerecho
        self.ladoDerecho.addRow(self.botonBuscar, self.botonRecuperar)
        # ---

        # agregamos el layout ladoDerecho al layout horizontal
        self.horizontal.addLayout(self.ladoDerecho)



        #---------- FINAL ------------

        # indicamos que el layout principal del fondo es horizontal
        self.fondo.setLayout(self.horizontal)

        # creamos una ventana de dialogo
        self.ventanaDialogo = QDialog(None, QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowTitleHint)

        # definimos el tamaño de la ventana
        self.ventanaDialogo.resize(300, 150)

        # creamos el boton para aceptar
        self.botonAceptar = QDialogButtonBox.Ok
        self.opciones = QDialogButtonBox(self.botonAceptar)
        self.opciones.accepted.connect(self.ventanaDialogo.accept)

        # establecemos el titulo de la ventana
        self.ventanaDialogo.setWindowTitle("Formulario de registro")

        # configuramos la ventana para que sea modal
        self.ventanaDialogo.setWindowModality(Qt.ApplicationModal)

        # creamos un layout vertical
        self.vertical = QVBoxLayout()

        # creamos un label para los mensajes
        self.mensaje = QLabel("")

        # le ponemos estilos al label mensaje
        self.mensaje.setStyleSheet("background-color: #c14056; color: #ffffff; padding: 10px;")

        # agregamos el label de mensajes
        self.vertical.addWidget(self.mensaje)

        # agregamos las opciones de los botones
        self.vertical.addWidget(self.opciones)

        # establecemos el layout para la ventana
        self.ventanaDialogo.setLayout(self.vertical)

        # variable para controlar que se han ingresado los datos correctos
        self.datosCorrectos = True

   # metodo del boton limpiar
    def accion_botonLimpiar(self):
        self.nombreCompleto.setText('')
        self.usuario.setText('')
        self.password.setText('')
        self.password2.setText('')
        self.documento.setText('')
        self.correo.setText('')
        self.pregunta1.setText('')
        self.respuesta1.setText('')
        self.pregunta2.setText('')
        self.respuesta2.setText('')
        self.pregunta3.setText('')
        self.respuesta3.setText('')

   # metodo del boton registrarse
    def accion_botonRegistrar(self):

       # validamos que los passwords sean iguales
        if(
            self.password.text() != self.password2.text()
        ):
            self.datosCorrectos = False

            # escribimos el texto explicativo
            self.mensaje.setText("Los passwords no son iguales")

            # hacemos que la ventana de dialogo se vea
            self.ventanaDialogo.exec_()

        # validamos que se ingresen todos los campos
        if (
                self.nombreCompleto.text() == ''
                or self.usuario.text() == ''
                or self.password.text() == ''
                or self.password2.text() == ''
                or self.documento.text() == ''
                or self.correo.text() == ''
                or self.pregunta1.text() == ''
                or self.respuesta1.text() == ''
                or self.pregunta2.text() == ''
                or self.respuesta2.text() == ''
                or self.pregunta3.text() == ''
                or self.respuesta3.text() == ''
        ):
           self.datosCorrectos = False

           # escribimos el texto explicativo
           self.mensaje.setText("Debe ingresar todos los campos")

           # hacemos que la ventana de dialogo se vea
           self.ventanaDialogo.exec_()

        # si los datos estan correctos
        if self.datosCorrectos:

            # abrimos el archivo en modo agregar escribiendo datos en binario
            self.file = open('datos/cliente.txt', 'ab')

            self.file.write(bytes(
                self.nombreCompleto.text() + ";"
                + self.usuario.text() + ";"
                + self.password.text() + ";"
                + self.password2.text() + ";"
                + self.documento.text() + ";"
                + self.correo.text() + ";"
                + self.pregunta1.text() + ";"
                + self.respuesta1.text() + ";"
                + self.pregunta2.text() + ";"
                + self.respuesta2.text() + ";"
                + self.pregunta3.text() + ";"
                + self.respuesta3.text() + "\n"
                , encoding='UTF-8'))
            self.file.close()

            # abrimos en modo lectura em formato bytes
            self.file = open('datos/cliente.txt', 'rb')

            # recorrer el archivo linea por linea
            while self.file:
                linea = self.file.readline().decode('UTF-8')
                print(linea)
                if linea == '':
                    break
            self.file.close()

    # metodo del botonBuscar
    def accion_botonBuscar(self):
       # establecemos el titulo de la ventana
       self.ventanaDialogo.setWindowTitle("Buscar preguntas de validación")

       # validar que se haya ingresado el documento
       if(
                self.documento.text() == ''
       ):
            self.datosCorrectos = False

            # escribimos el texto explicativo
            self.mensaje.setText("Si va a buscar las preguntas"
                                 "para recuperar la contraseña"
                                 "\nDebe primero, ingresar el documento")

            # hacemos que la ventana de dialogo se vea
            self.ventanaDialogo.exec_()

       # validar si el documento es numerico
       if(
              not self.documento.text().isnumeric()
       ):
           self.datosCorrectos = False

           # escribimos el texto explicativo
           self.mensaje.setText("El documento debe ser numerico"
                                 "\nNo ingrese letras"
                                 "ni caracterés especiales")

           # hacemos que la vemtana de dialogo se vea
           self.ventanaDialogo.exec_()

           # limpiamos el campo del documento:
           self.documento.setText('')

       # si los datos estan correctos
       if (
                self.datosCorrectos
       ):
           # abrimos el archivo en modo lectura
           self.file = open('datos/cliente.txt', 'rb')

           # lista vacia para guardar los ususarios
           usuarios = []

           while self.file:
               linea = self.file.readline().decode('UTF-8')

               # obtenemos del string una lista con 11 datos separados por ;
               lista = linea.split(";")

               # se para si ya no hay mas registros en el archivo
               if linea == '':
                    break

               # creamos un objeto tipo cliente llamado u
               u = cliente(
                    lista[0],
                    lista[1],
                    lista[2],
                    lista[3],
                    lista[4],
                    lista[5],
                    lista[6],
                    lista[7],
                    lista[8],
                    lista[9],
                    lista[10],
                )

               # metemos el objeto en la lista de usuarios
               usuarios.append(u)

           # cerramos el archivo
           self.file.close()

           # variable para controlar si existe el documento
           existeDocumento = False

           # buscamos en la lista usuario por usuario si existe la cedula
           for u in usuarios:
               # comnpramos el documento ingresado
               # si corresponde con el documento es el usuario correcto
               if u.documento == self.documento.text():
                   # mostramos la pregunta del formulario
                   self.pregunta1.setText(u.pregunta1)
                   self.pregunta2.setText(u.pregunta2)
                   self.pregunta3.setText(u.pregunta3)
                   # indicamos que encontramos el documento
                   existeDocumento = True
                   # paramos el for
                   break
           # si no existe un usuario con este documento
           if (
                   not existeDocumento
           ):
               # escribimos el texto explicativo:
               self.mensaje.setText("No esxiste un usuario con este documento:\n"
                                    + self.documento.text())

               # hacemos que la ventana de dialogo se vea
               self.ventanaDialogo.exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    ventana1 = Ventana1()

    ventana1.show()

    sys.exit(app.exec_())