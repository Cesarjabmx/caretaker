# Caretaker
## Descripción general del proyecto: 

La finalidad de la creación de este proyecto es crear un cuidador virtual que ayude a la monitorización de pacientes hospitalizados haciendo uso de los mecanismos ya existentes para considerar el estado del paciente, pero a su vez se pretende implementar el uso de inteligencia artificial para detectar cambios que pudieran ser sutiles pero muy importantes para la mejora de los pacientes. 

Proyecto de lenguajes de interfaz

Materiales a utilizar: 
- Cámara web
- Bocina de una laptop antigua
- Arduino Mega
- Servomotor
- Cables doupont

Posteriormente se pretende agregar la cámara termica AMG8833

En el archivo FaceT.py se encuentra el código del reconocimiento facial utilizando OpenCV

El archivo Face-Body.py contiene el código para detectar el cuerpo, la cara y calcular las coordenas para que el servomotor pueda moverse.

El archivo Caretaker.ino, contiene la programación necesaria para controlar el servomotor, el sensor dht11 y la bocina que se necesitan para el correcto funcionamiento del proyecto. 

Se pretendía utilizar una cámara termica para monitorear al paciente, pero al no tenerla en este momento, se utilizó el sensor dht11 para obtener esa información.

*Actualización al día 22 de Febrero 2023*


