from tkinter import *
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import wmi
import webbrowser

#******************************** Datos Equipo ***************************
c = wmi.WMI()
my_system = c.Win32_ComputerSystem()[0]
my_system1 = c.Win32_Bios()[0]

marca = my_system.Manufacturer
modelo = my_system.SystemFamily
serieb = my_system1.SerialNumber.strip()

#******************************** Interfaz ********************************
#Variable de interfaz
archivo = Tk()

#Varibles de obtencion de Texto
correo = StringVar()
contraseña = StringVar()
asunto = StringVar()
documentacion = StringVar()
env = StringVar()


#Funcion
def abrirUrl():
    url = webbrowser.open("https://www.linkedin.com/in/eusa/", new=2, autoraise=True)
def enviarDatos():
    # ******************************** Envio de Correo ********************************
    # Establecer conexion con el servidor de correos SMTP
    conexion = smtplib.SMTP(host='smtp.office365.com', port=587)
    conexion.ehlo()

    # Encriptacion TLS(solamente si el puerto es el 587)
    conexion.starttls()
    try:
        #Variable
        correo_var = correo.get()
        # iniciar sesion
        conexion.login(correo_var, password=contraseña.get())

        # Definimos Variable
        msg = MIMEMultipart()
        #Enviar correo
        msg['From'] = correo_var
        msg['To'] = 'correo@correo.com'
        msg['Subject'] = f'Reporte - {asunto.get()}'

        # Cuerpo del correo
        msg.attach(MIMEText(f"Datos del Equipo:\nUsuario: {correo_var[:correo_var.find('@')]} \nMarca: {marca} \nModelo: {modelo} \nSerie: {serieb} \n\n{documentacion.get()}"))

        #Envio de datos del correo
        conexion.sendmail(msg['From'], msg['To'], msg.as_string())
        #Mensaje
        env.set(f"correo enviado a {msg['To']}")
        # Desconectar el SMTP
        conexion.quit()
    except smtplib.SMTPException as e:
        env.set(e)

#Configuracion de variable de Interfaz
archivo.title('Grupo Axo')
archivo.geometry('600x350')
archivo.config(bg='white')

#Ingreso de Imagenes
img = PhotoImage(file='icono2.png')
Label(archivo, image= img,bg='white').pack()
img2 = PhotoImage(file='clavera2.png')
Label(archivo,image = img2,bg='white').place(x=320, y=320)
img3 = PhotoImage(file='soporte121.png')
Label(archivo,image = img3,bg='white').place(x=400, y=125)

#Ingreso de Texto
Label(archivo, text='Ingresa tu correo:',bg='white',font='Curier 13').place(x=40,y=125)
Label(archivo,text='Ingresa tu contraseña:', bg='white', font='Curier 13').place(x=40,y=155)
Label(archivo,text='Asunto:', bg='white', font='Curier 13').place(x=40,y=185)
Label(archivo,text='Descripcion breve:', font='Curier 13', bg='white').place(x= 40,y=215)
contacto = Label(archivo,text='By EusaHack',font='Curier 8', bg='white').place(x=250,y=320)
mensaje = Label(archivo, textvariable=env, bg='white').place(x = 10, y=290 )



#Ingreso de Cajas de Texto
txt1 = Entry(archivo,bd=3, textvariable=correo, bg ='gainsboro').place(x=185, y=125)
txt2 = Entry(archivo,bd=3, textvariable=contraseña, show ='*',bg ='gainsboro').place(x=220, y=155)
txt3 = Entry(archivo,bd=3, textvariable=asunto,bg ='gainsboro').place(x=110, y=185)
txt4 = Entry(archivo,bd=3, textvariable=documentacion,bg ='gainsboro').place(x=195, y=215)

#Ingreso de Botones
enviar = Button(archivo,text='Enviar', command= lambda: enviarDatos()).place(x = 260, y = 260)
info = Button(archivo,text= '®', bg='white', command = lambda : abrirUrl()).place(x= 335, y =320) 

archivo.mainloop()
