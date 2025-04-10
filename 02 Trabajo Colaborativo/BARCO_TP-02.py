E. Abril Barco
37857485
2025

Programación I - Unidad II
Tec. Universitaria en Programación 
Universidad Tecnológica Nacional 


Práctico 2: Git y GitHub 

Actividades 
1) Contestar las siguientes preguntas utilizando las guías y documentación proporcionada (Desarrollar las respuestas) : 
• ¿Qué es GitHub? 
GitHub es un plataforma web alojada en la nube para ver, crear, colaborar, almacenar y gestionar repositorios de código y proyectos de desarrollo de software, basada en el sistema de control de versiones Git.

• ¿Cómo crear un repositorio en GitHub?
Primero ingresamos al sitio web https://github.com/ y nos logueamos con nuestras credenciales. 
Luego, clickeamos en el signo + (Create new…) que aparece arriba a la derecha (desktop) y clickeamos en “nuevo repositorio”. Le escribimos un nombre que no hayamos ocupado antes en la plataforma y agregamos una descripcion (una buena practica es utilizar el mismo nombre en el repositorio local que en el de GitHub). Elegimos las preferencias y le damos a Create repository.
Luego es necesario copiar ciertas lineas de codigo que aparecen posteriormente a la creacion del repositorio en la consola de Git para comenzar a sincronizar lo que hacemos localmente con los cambios que se vayan almacenando en la nube. 

 • ¿Cómo crear una rama en Git? ¿Cómo cambiar a una rama en Git?
Para crear una rama en Git se utiliza el comando “git branch <nombre_nueva_rama>”  o bien “git checkout -b <nombre_nueva_rama>” de modo que crea la rama y a la vez te cambia a ella en un solo paso.
Si ejecutamos la primer opcion, luego podemos escribir “git checkout <nombre_nueva_rama>” para cambiar a la nueva rama.

 • ¿Cómo fusionar ramas en Git? 
Podemos fusionar ramas con el comando “git merge”. Para ello es necesario saber que si estamos en la rama “1”, luego escribiremos “git merge <nombre_rama_2>”, de esa forma la rama en la que estabamos quedará fusionada bajo la rama 2.

• ¿Cómo crear un commit en Git?
Podemos crear un commit con el comando “git commit -m <”descripcion”>”
O bien, solo git commit. Se recomienda mas la primera opcion para ir registrando las versiones con una descripcion que nos permita orientarnos cuando tengamos ya varios registros hechos.


 • ¿Cómo enviar un commit a GitHub?
La serie de comandos a ejecutar en la terminal sería la siguiente:
git add . 
git commit -m "descripción" .

 • ¿Qué es un repositorio remoto?
En GitHub, un repositorio remoto es una copia de un proyecto de código alojada en un servidor remoto en la nube (como GitHub) y que puede ser publica o privada. Permite la colaboración y el seguimiento de cambios.
 • ¿Cómo agregar un repositorio remoto a Git? 
Para agregar un repositorio remoto a Git, se usa el comando git remote add <nombre_remoto> <URL_del_repositorio> en nuestra terminal, dentro del directorio de nuestro repositorio local.

• ¿Cómo empujar cambios a un repositorio remoto?
La serie de comandos a ejecutar en la terminal sería la siguiente:
git add . ...
git commit -m "descripción" .
git remote -v . ...
git push origin master (para empujar tus archivos a Github). Utilizamos master, main u otro según como se llame la rama/branch que estamos utilizando. 

 • ¿Cómo tirar de cambios de un repositorio remoto? No se si comprendo la pregunta, pero el comando git pull request sirve para proponer cambios en un repositorio y colaborar con otros desarrolladores, permitiendo que éstos revisen, comenten y aprueben las modificaciones antes de fusionarlas con la rama principal.

Si se refiere a deshacer cambios, git revert sirve para deshacer cambios efectuados en el historial de confirmaciones de un repositorio. Otros comandos para "deshacer" como, por ejemplo, git checkout y git reset, mueven los punteros de referencia de la rama principal a otras secundarias, o bien a una confirmación especificada.

• ¿Qué es un fork de repositorio? 
Un fork de repositorio es la una copia independiente del repositorio original en nuestra propia cuenta, permitiéndonos trabajar con el código sin afectar el proyecto original y luego proponer cambios mediante una solicitud de extracción (pull request).

• ¿Cómo crear un fork de un repositorio? 
en GitHub, vamos a la página del repositorio, buscamos el botón "Fork" en la esquina superior derecha. Navega al repositorio: Ve a la página del repositorio que quieres forkar en GitHub. 
Damos click en el botón "Fork", y luego GitHub te preguntará a qué cuenta o organización quieres forkear el repositorio, es decir, debemos darle un destino. Finalmente, clickeamos "Create fork" o similar. 

• ¿Cómo enviar una solicitud de extracción (pull request) a un repositorio?
Para enviar una solicitud de extracción (pull request) a un repositorio, primero debes forkear el repositorio (crear una copia independiente), realizar los cambios en una nueva rama, enviar los cambios a tu repositorio fork y luego crear la solicitud de extracción desde tu repositorio fork al repositorio original. 


1. Forkear el repositorio:
Ve a la página principal del repositorio en GitHub.
Haz clic en el botón "Fork" en la esquina superior derecha. 

2. Clonar el repositorio fork a tu máquina:
Clona tu repositorio fork a tu máquina local usando git clone.

3. Crear una rama nueva:
Crea una nueva rama para tus cambios.

4. Realizar los cambios y confirmar:
Realiza los cambios necesarios en los archivos.
Añade los cambios a la zona de staging con git add ..
Confirma los cambios con git commit -m "<mensaje de confirmación>". 

5. Enviar los cambios a tu repositorio fork:
Envía los cambios a tu repositorio fork con git push origin <nombre de la rama>. 

6. Crear la solicitud de extracción:
Ve a la página principal de tu repositorio fork en GitHub.
Haz clic en el botón "Compare & pull request" (o similar).
Selecciona la rama de tu repositorio fork que contiene los cambios y la rama de destino en el repositorio original.
Escribe un título y una descripción para tu solicitud de extracción.
Haz clic en "Create pull request". 

7. si usamos GitHub CLI, podemos crear la solicitud de extracción directamente desde la línea de comandos con comandos como <gh pr create>

• ¿Qué es una etiqueta en Git?
En Git, una etiqueta (tag) es una referencia que apunta a un punto específico en el historial de commits, típicamente utilizado para marcar versiones importantes o lanzamientos de software. Permiten identificar fácilmente versiones de software, puntos de referencia importantes o cualquier otro momento significativo en el desarrollo de un proyecto. 

• ¿Cómo crear una etiqueta en Git?
Para crear una etiqueta en Git, se usa el comando git tag <nombre_de_la_etiqueta>

• ¿Cómo enviar una etiqueta a GitHub?
El comando git tag -a <tagname> sirve para crear una nueva etiqueta.

• ¿Qué es un historial de Git?
El historial de Git es un gráfico de commits que muestran el estado del repositorio en distintos puntos del tiempo.  

• ¿Cómo ver el historial de Git?
Utilizando el comando git log, se puede visualizar la lista de confirmaciones en orden cronológico inverso. El comando git log tambien permite variar el formato de la salida usando opciones como --oneline para ver cada confirmación en una sola línea.

• ¿Cómo buscar en el historial de Git?
Búsqueda básica: Utiliza git log para ver el historial completo de commits. Esto mostrará todas las confirmaciones en orden cronológico inverso.

Búsqueda por autor: Usa la opción --author con git log para filtrar los commits de un autor específico. Por ejemplo: git log --author="Nombre del Autor".

Búsqueda por mensaje de commit: Usa la opción --grep para buscar palabras clave específicas en los mensajes de los commits. Por ejemplo: git log --grep="corrección de error".

Búsqueda por fecha: Usa las opciones --since y --until para filtrar commits dentro de un rango de fechas específico. Por ejemplo: git log --since="hace 2 semanas".

Búsqueda por cambios en archivos: Usa la opción -S seguida de una cadena para encontrar commits que añadieron o eliminaron las ocurrencias de esa cadena en el código. Por ejemplo: git log -S"nombreFuncion".

• ¿Cómo borrar el historial de Git?
Se puede eliminar el directorio .git:
>> Localizar el repositorio en tu sistema de archivos.
Borrar el directorio oculto .git. Esto eliminará todo el historial y la configuración de Git. Usa el siguiente comando si estás en el directorio raíz del repositorio:
rm -rf .git
Esto transformará el repositorio en un directorio normal, sin control de versiones.

Se puede reiniciar el historial desde cero:
>>Borrar el directorio .git como se mencionó anteriormente.
Vuelve a inicializar el repositorio usando:
git init
Añade y confirma todos los archivos al nuevo repositorio para crear un nuevo historial:
git add .git commit -m "Inicio de un nuevo historial"

Por último, se puede también forzar un push del nuevo historial (si el repositorio está conectado a un remoto):
Ten en cuenta que esta acción sobrescribirá el historial remoto, y debería hacerse solo si estás seguro de los cambios.
Usa:
git push origin --force

• ¿Qué es un repositorio privado en GitHub?
es un tipo de repositorio que permite al propietario controlar quién puede ver y acceder al contenido y al historial del proyecto. Es útil para equipos que necesitan trabajar en proyectos colaborativos manteniendo la privacidad y el control sobre quién puede ver y colaborar en su código.

• ¿Cómo crear un repositorio privado en GitHub? 
• ¿Cómo invitar a alguien a un repositorio privado en GitHub?
Iniciamos sesión en GitHub, vamos a la esquina superior derecha y hacemos clic en el icono “+”  para crear un nuevo repositorio, y luego de completar el nombre y descripción, marcamos la opción "Private" para asegurarnos que solo las personas que nosotros (el propietario) invitemos puedan ver y colaborar en el repositorio.

Vamos al repositorio privado, accedemos a la configuración del repositorio ("Settings" que se encuentra en la parte superior del repositorio) y damos click luego en  "Manage access" (Administrar acceso).
Luego hacemos clic en el botón verde “Invite a collaborator” e introducimos el nombre de usuario de GitHub o la dirección de correo electrónico de la persona que deseas invitar. Posteriormente, clic en el botón "Add" o "Send invitation". La persona recibirá una notificación en GitHub y/o un correo electrónico con la invitación. Debe aceptar la invitación para poder acceder al repositorio.

• ¿Qué es un repositorio público en GitHub?
• ¿Cómo crear un repositorio público en GitHub?
• ¿Cómo compartir un repositorio público en GitHub?
Seguimos los mismos pasos que en en el punto anterior, pero cuando estamos creando un repositorio, en vez de cliquear en “Privado” cliqueamos en “Público”. Y cuando queramos compartirlo, podemos sencillamente ingresar al repositorio público y desde ahí, compartir la URL desde la barra de direcciones de nuestro navegador. 
GitHub también permite compartir contenido directamente desde la plataforma utilizando botones de compartir para redes sociales si se configuran o simplemente compartiendo enlaces en plataformas de colaboración.
Finalmente, se puede añadir un README divulgativo para incluir información detallada sobre el proyecto, cómo contribuir o cómo clonar el repositorio, lo que puede facilitar que otros usuarios interactúen con él.

https://github.com/mumi-b/CONFLICT-EXCERCISE 

