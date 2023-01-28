# DataMailer
## Este fue un proyecto realizado para una empresa la cual queria automatizar el envio de los datos de la pc para darle soporte o realizar el reporte con los daos enviados
### Se utilizo el lenguaje python, se subio el archivo .py pero si se puede convertir a .exe para que lo puedan llevar en una memoria y utilizar sin instalar nada
#### Nota : este software solo sirve para windows y correos outlook

1. Se importan las librerias 

[![1.png](https://i.postimg.cc/HL175Dvp/1.png)](https://postimg.cc/mPVDfqGq)

2.  Se crean las varaibles para otner los datos especificos

[![2.png](https://i.postimg.cc/prKdPpxz/2.png)](https://postimg.cc/645K068p)

3.  Se crea la interfaz y unas variables String que utilizaremos en las funciones

[![3.png](https://i.postimg.cc/QxXBjJ9M/3.png)](https://postimg.cc/mh5ZwMSx)

4. Se crean las funciones:
- abrirUrl : esa funcion sirve para que al momento de presionar el boton te envie directamente a mi linkedin
- enviarDatos : esta funcion realiza varias cosas como
- 1 : primero establece la conexion con el servidro SMTP , si quieren utilizar gmail o otro correo deben de cambiar estos valores para que funcione
- 2 : encriptamos el TLS(Transport Layer Security) solamente para los puertos 587 
- 3 : se realiza un try y except por si hay algun error de usuario o contraseña o culaquier otro error 
- 4 : si todo es correcto obtiene los datos de la variable verifica la conexion 
- 5 : se crea una variable para obtener las partes del correo como from , to , subject y el cuerpo del correo donde se ingresan los datos que se obtuvieron de las variables
- 6 : envia los datos 
- 7 : se desconecta del SMTP

[![4.png](https://i.postimg.cc/ZYphRktb/4.png)](https://postimg.cc/mhLnX5gJ)

5. Se configura la interfaz, ingresando titulo , medida y color del bg 

[![5.png](https://i.postimg.cc/yNgbb971/5.png)](https://postimg.cc/3yh1ykyV)

6. Se ingresan las imagenes ubicandolas en la interfaz 

[![6.png](https://i.postimg.cc/WzX83bsY/6.png)](https://postimg.cc/300mfh42)

7. Se ingresan las etiquetas de texto 

[![7.png](https://i.postimg.cc/02jdnvkx/7.png)](https://postimg.cc/YhcW2JLy)

8. Se ingresan las cajas de texto

[![8.png](https://i.postimg.cc/Y94LgrNy/8.png)](https://postimg.cc/TL6PvX4r)

9. Se ingresan los botones 

[![9.png](https://i.postimg.cc/Wz8V1rFR/9.png)](https://postimg.cc/y3DtfDyn)

10. Presentacion del poryecto 

[![10.png](https://i.postimg.cc/gJcNPZWL/10.png)](https://postimg.cc/Y4V16jjt)

11. Se ingresan datos para la prueba, demora unos segundos y arroja el mensaje de enviado 

[![11.png](https://i.postimg.cc/ry1pWK03/11.png)](https://postimg.cc/Rq09xCTL)

12. Se valida que llegaron los datos

[![12.png](https://i.postimg.cc/v8kpQzZd/12.png)](https://postimg.cc/QVg6mc76)

13. Esta es la pantalla cuando envia un error si es de usuario o contraseña 

[![13.png](https://i.postimg.cc/fL2QjQs3/13.png)](https://postimg.cc/4790sMmZ)
