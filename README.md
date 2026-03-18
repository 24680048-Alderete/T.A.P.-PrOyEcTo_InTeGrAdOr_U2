# T.A.P.-PrOyEcTo_InTeGrAdOr_U2
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Git Bash](https://img.shields.io/badge/Git%20Bash-F05032?style=for-the-badge&logo=git&logoColor=white)  ![Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white) ![macOS](https://img.shields.io/badge/mac%20os-000000?style=for-the-badge&logo=apple&logoColor=white) ![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)
## Proyecto Integrador Unidad 2: Tienda de Peluches "Glich Productions"
Este repositorio contiene el proyecto correspondiente a la Unidad 2 de la asignatura de Graficación/Programación. Se desarrolló una tienda en línea de peluches temáticos de la serie Murder Drones utilizando Python y el framework Flet para la creación de la interfaz gráfica.
La aplicación muestra un catálogo de 5 peluches en forma de tarjetas, donde cada producto tiene:
* 🖼️ Imagen del producto.
* 📛 Nombre y descripción temática.
* 💰 Precio.
* 🛒 Botón para agregar al carrito.
* ❤️ Botón de favorito.
Cada peluche se presenta en una tarjeta visual para simular el diseño de una tienda en línea con temática de la serie.

### 📂 Estructura del Repositorio
```text
ProyectoIntegradorU2/
│
├── README.md                 # Este archivo (documentación completa)
├── tienda_peluches.py        # Script principal de la aplicación
├── assets/                   # Carpeta con las imágenes de los productos
│   ├── n_plush.jpg
│   ├── uzi_plush.jpg
│   ├── v_plush.jpg
│   ├── cyn_plush.jpg
│   └── cyn_TRex_plush.jpg
└── captura_app.png           # Captura de pantalla de la aplicación funcionando
```
### 🛠 Requisitos
> [!CAUTION]
> **Python🐍 3.10** o anterioes.
> 
>   Pues checar tu versión de Python usando `py --doctor`.
> 
> **Flet**

### Instalación de dependencias
```bash
pip install flet
```
### 🚀 Instrucciones de uso
1. Clona o descarga este repositorio en tu computadora.
2. Asegúrate de tener las imágenes en la carpeta assets/. Las rutas en el código hacen referencia a los archivos de imagen listados anteriormente.
3. Ejecuta la aplicación:
```bash
python tienda_peluches.py
```
4. Interactúa con la interfaz:
   - Verás el catálogo de peluches organizado en tarjetas con fondo negro.
   - Puedes hacer clic en el ícono de corazón (favoritos) o en el botón "Agregar" (funcionalidad base sin implementación de compra).

📝 Explicación detallada del código
A continuación se desglosa el código paso a paso, con explicaciones de cada sección.

1. Configuración del entorno
python
import flet as ft
Primero se importa Flet, que es el framework que permite crear la interfaz gráfica. Flet funciona creando controles visuales como textos, botones, filas, columnas e imágenes que ayudan a crear nuestro catálogo.

2. Modelo de datos
En esta sección se crea la lista de productos, donde cada producto contiene su información respectiva:

python
productos = [
    {"id": 1, "nombre": "N Plush", "descripcion": "Mira este dulce y asesino boi. Adopta este peluche N y él te protegerá para siempre (con fuerza letal).", "precio": 271.00, "ruta_imagen": "n_plush.jpg"},
    {"id": 2, "nombre": "Uzi Plush", "descripcion": "Por una vez, Uzi es tan alta como el resto de sus amigos (pero todavía es bastante pequeña). Recógela hoy y tal vez cambie de opinión sobre todo el asunto de “matar a todos los humanos”.", "precio": 271.00, "ruta_imagen": "uzi_plush.jpg"},
    {"id": 3, "nombre": "V Plush", "descripcion": "Un peluche tan lindo no podría ser siniestro, ¿verdad? Pero eso es lo que el peluche V quiere que pienses...", "precio": 271.00, "ruta_imagen": "v_plush.jpg"},
    {"id": 4, "nombre": "Cyn Plush", "descripcion": "INSERTAR DESCRIPCIÓN DE LINDO PELUCHE", "precio": 271.00, "ruta_imagen": "cyn_plush.jpg"},
    {"id": 5, "nombre": "Cyn T-Rex Plush", "descripcion": "RAWR", "precio": 271.00, "ruta_imagen": "cyn_TRex_plush.jpg"},
]
Cada producto contiene:

id: identificador único del producto

nombre: nombre del peluche

descripcion: descripción breve del producto (con humor acorde a la serie)

precio: precio del peluche (todos a $271.00)

ruta_imagen: nombre del archivo de imagen que se mostrará en la tarjeta

Nota importante
En nuestra carpeta donde está nuestro main se creará otra carpeta llamada assets que dentro contendrá las imágenes que mostrará nuestro catálogo, con la dirección indicada. Éstas serán mandadas a traer por medio de la ruta_imagen.

3. Creación de un componente reutilizable
Después se crea una clase llamada ProductoCard, la cual representa una tarjeta visual para cada producto:

python
class ProductoCard(ft.Container):
Se usa Container porque permite contener varios controles dentro y aplicar estilos como tamaño, color o bordes.

Dentro del constructor __init__ se recibe el producto que se quiere mostrar:

python
    def __init__(self, producto):
        super().__init__()
Esto permite reutilizar el mismo componente para todos los productos del catálogo.

4. Configuración de la tarjeta
Aquí se definen las propiedades visuales de la tarjeta:

python
        self.width = 250
        self.padding = 10
        self.border_radius = 15
        self.bgcolor = ft.Colors.WHITE
        
        self.shadow = ft.BoxShadow(
            blur_radius=10,
            color=ft.Colors.with_opacity(0.1, "black")
        )
Estas propiedades definen:

width: ancho de la tarjeta (250 píxeles)

padding: espacio interno (10)

border_radius: bordes redondeados (15)

bgcolor: color de fondo (blanco)

shadow: sombra suave para efecto de elevación

5. Organización del contenido
El contenido de la tarjeta se organiza utilizando una Column, que permite acomodar los elementos de arriba hacia abajo:

python
        self.content = ft.Column(
            spacing=8,
            controls=[
                # Aquí se agregan los elementos
            ]
        )
6. Imagen del producto
Para mostrar la imagen se utiliza el control Image:

python
                ft.Image(
                    src=producto["ruta_imagen"],
                    width=230,
                    height=150,
                    fit="fitWidth"
                ),
src: indica la ruta de la imagen (dentro de la carpeta assets)

width y height: dimensiones fijas

fit="fitWidth": ajusta la imagen para que ocupe todo el ancho

7. Nombre del producto
Después se muestra el nombre del peluche:

python
                ft.Text(
                    producto["nombre"],
                    size=18,
                    weight="bold"
                ),
Se utiliza Text para mostrar el nombre del producto con un tamaño mayor y en negrita.

8. Descripción del peluche
Se coloca otro Text para colocar el texto largo de la descripción:

python
                ft.Text(
                    producto["descripcion"],
                    size=12,
                    color=ft.Colors.GREY_700
                )
Este texto es más pequeño (12) y de color gris para no ocupar demasiado protagonismo dentro de la tarjeta.

9. Barra inferior con precio y acciones
En esta parte del código se construye la zona inferior de la tarjeta del producto, donde se muestran el precio del peluche y los botones de acción.

Precio
python
                ft.Text(
                    f"${producto['precio']}",
                    size=16,
                    weight="bold",
                    color=ft.Colors.GREEN
                ),
Se utiliza una f-string para mostrar el precio con el símbolo de dinero y se le da un color verde para que resalte.

Barra de acciones
python
                ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        ft.IconButton(icon=ft.Icons.FAVORITE),
                        ft.ElevatedButton(
                            "Agregar",
                            icon=ft.Icons.SHOPPING_CART
                        )
                    ]
                )
Aquí se utiliza un Row porque los elementos se quieren organizar horizontalmente.

La propiedad alignment=ft.MainAxisAlignment.SPACE_BETWEEN significa que los elementos se colocarán uno a cada extremo de la fila:

IconButton: botón de corazón (favoritos) a la izquierda

ElevatedButton: botón "Agregar" con icono de carrito a la derecha

10. Interfaz principal
Después se crea la función principal main, donde se configura la página:

python
def main(page: ft.Page):
Dentro se configuran algunas propiedades de la ventana:

python
    page.title = "Glich Productions"
    page.bgcolor = ft.Colors.BLACK
    page.scroll = "auto"
Estas propiedades indican:

title: título de la ventana

bgcolor: color de fondo (negro)

scroll: permite desplazarse si el contenido es mayor que la pantalla

11. Encabezado de la página
Se agrega un título para la tienda:

python
    header = ft.Text(
        "🛒 Murder Drones",
        size=30,
        weight="black"
    )
Este texto muestra el nombre de la tienda con referencia a la serie, tamaño grande (30) y peso "black" (muy negrita), además de un emoji de carrito.

12. Creación del catálogo
Después se generan las tarjetas automáticamente usando un ciclo:

python
    tarjetas = []
    for producto in productos:
        tarjetas.append(ProductoCard(producto))
Aquí se recorre la lista de productos, tomando los valores que se dieron al inicio en el array y se crea una tarjeta para cada uno.

13. Organización del catálogo
Las tarjetas se colocan dentro de una Row:

python
    catalogo = ft.Row(
        controls=tarjetas,
        wrap=True,
        spacing=20
    )
Esto permite que:

Las tarjetas se acomoden horizontalmente

Se ajusten automáticamente cuando no haya espacio (wrap)

Se mantenga una separación entre ellas (spacing de 20)

14. Mostrar la interfaz
Finalmente se agregan los elementos a la página:

python
    page.add(
        header,
        catalogo
    )
Esto hace que se muestre el título y el catálogo de productos.

15. Ejecución de la aplicación
Para iniciar la aplicación se utiliza:

python
ft.app(
    target=main,
    assets_dir="assets"
)
Donde:

target=main: indica la función principal de la aplicación

assets_dir="assets": especifica la carpeta donde se encuentran las imágenes de los productos

📸 Visualización del resultado
https://captura_app.png

La aplicación muestra un catálogo de peluches con tarjetas blancas organizadas sobre un fondo negro. Al redimensionar la ventana, las tarjetas se reordenan automáticamente gracias a la propiedad wrap=True.

(Reemplaza captura_app.png con tu propia captura de pantalla)
