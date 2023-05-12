import kivy
from kivy.app import App
from kivy.core.window import Window
from kivy.config import Config
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.graphics import Rectangle, Color

import ctypes

##############################################################################
# VARIABLES GLOBALES
##############################################################################
tituloPantalla = "INICIO"
usuario = "Luis Sánchez"

##############################################################################
# DEFINIR ANCHURAS Y ALTURAS DE PANTALLA, DISEÑO Y FACTOR DE CONVERSIÓN
##############################################################################
# HALLAR ANCHO Y ALTO DE LA COMPUTADORA
user32 = ctypes.windll.user32
user32.SetProcessDPIAware()
anchoPC, altoPC = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

#DEFINIR ANCHO Y ALTO DE DISEÑO, ADEMÁS FACTORES DE CONVERSIÓN
anchoDiseño, altoDiseño = 1920, 1080
W, H = anchoPC/anchoDiseño, altoPC/altoDiseño

##############################################################################
# PANTALLA DE INICIO
##############################################################################
kivy.require('2.1.0') 

Config.set('graphics', 'resizable', '1')
#Config.set('graphics', 'fullscreen', '1')
#Config.set('graphics', 'window_state', 'maximized')
#Window.fullscreen = 'auto'
Window.size = (anchoPC/2, altoPC/2)
Window.minimum_width, Window.minimum_height = Window.size
Window.maximize()
#Config.write()

##############################################################################
# BACKGROUND
class BackgroundBody(Widget):
    def __init__(self, **kwargs):
        super(BackgroundBody, self).__init__(**kwargs)

        with self.canvas:
            # CREAR FONDO DEL CUERPO
            Color(.871, .871, .871, 1)
            self.rect = Rectangle(pos = self.center, size =(self.width / 2.5, self.height / 2.5))
 
            # Update the canvas as the screen size change
            self.bind(pos = self.update_rect, size = self.update_rect)
 
    # update function which makes the canvas adjustable.
    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

##############################################################################
# HEADER
class Header(Widget):
    def __init__(self, **kwargs):
        super(Header, self).__init__(**kwargs)

        with self.canvas:
            # CREAR FONDO DE LA CABECERA
            Color(44/255, 59/255, 112/255, 1)
            heightHeader = 100*H
            widthWindow = Window.size[0]
            heightWindow = Window.size[1]
            yPos = heightWindow-heightHeader

            self.rect = Rectangle(pos = (0*H,yPos), size =(widthWindow, heightHeader))
 
            # CREAR TÍTULO DE LA CABECERA
            sFontT = 40*H
            xOffsetT = 150*H
            yOffsetT = 0*H
            self.title = Label(text = f"[b]{tituloPantalla}[/b]", font_size = f"{sFontT}sp", color =(1, 1, 1, 1), markup = True)
            self.title.pos = (self.rect.pos[0] + xOffsetT, self.rect.pos[1] + yOffsetT - sFontT/2)

            # CREAR NOMBRE DE USUARIO
            sFontU = 24*H
            xOffsetU = 300*H
            yOffsetU = -10*H
            self.user = Label(text = f"{usuario}", font_size = f"{sFontU}sp", color =(1, 1, 1, 1), markup = True)
            self.user.pos = (self.rect.pos[0] + self.rect.size[0] - xOffsetU, self.rect.pos[1] + yOffsetU - sFontU/2)

            # Update the canvas as the screen size change
            self.bind(pos = self.update_header, size = self.update_header)

    # update function which makes the canvas adjustable.
    def update_header(self, *args):
        # ACTUALIZAR FONDO DE LA CABECERA
        heightHeader = 100*H
        widthWindow = Window.size[0]
        heightWindow = Window.size[1]
        yPos = heightWindow-heightHeader

        self.rect.pos = (0*H,yPos)
        self.rect.size = (widthWindow, heightHeader)

        # ACTUALIZAR TITULO DE LA CABECERA
        sFontT = 40*H
        xOffsetT = 150*H
        yOffsetT = 0*H
        self.title.pos = (self.rect.pos[0] + xOffsetT, self.rect.pos[1] + yOffsetT - sFontT/2)

        # ACTUALIZAR NOMBRE DE USUARIO
        sFontU = 24*H
        xOffsetU = 300*H
        yOffsetU = -10*H
        self.user.pos = (self.rect.pos[0] + self.rect.size[0] - xOffsetU, self.rect.pos[1] + yOffsetU - sFontU/2)

##############################################################################
# VENTANA PRINCIPAL
class MainWindow(Screen):
    def __init__(self, **kwargs):
        super(MainWindow, self).__init__(**kwargs)
        self.add_widget(BackgroundBody())
        self.add_widget(Header())

##############################################################################
# APLICACIÓN PRINCIPAL
class MainApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainWindow(name = "Inicio"))
        return sm
    
MainApp().run()
