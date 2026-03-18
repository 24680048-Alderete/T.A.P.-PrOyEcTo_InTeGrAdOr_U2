import flet as ft

# -----------------------------
# MODELO DE DATOS
# -----------------------------

productos = [
    {"id": 1, "nombre": "N Plush", "descripcion": "Mira este dulce y asesino boi. Adopta este peluche N y él te protegerá para siempre (con fuerza letal).", "precio": 271.00, "ruta_imagen": "n_plush.jpg"},
    {"id": 2, "nombre": "Uzi Plush", "descripcion": "Por una vez, Uzi es tan alta como el resto de sus amigos (pero todavía es bastante pequeña). Recógela hoy y tal vez cambie de opinión sobre todo el asunto de “matar a todos los humanos”.", "precio": 271.00, "ruta_imagen": "uzi_plush.jpg"},
    {"id": 3, "nombre": "V Plush", "descripcion": "Un peluche tan lindo no podría ser siniestro, ¿verdad? Pero eso es lo que el peluche V quiere que pienses...", "precio": 271.00, "ruta_imagen": "v_plush.jpg"},
    {"id": 4, "nombre": "Cyn Plush", "descripcion": "INSERTAR DESCRIPCIÓN DE LINDO PELUCHE", "precio": 271.00, "ruta_imagen": "cyn_plush.jpg"},
    {"id": 5, "nombre": "Cyn T-Rex Plush", "descripcion": "RAWR", "precio": 271.00, "ruta_imagen": "cyn_TRex_plush.jpg"},
]

# -----------------------------
# COMPONENTE REUTILIZABLE
# -----------------------------

class ProductoCard(ft.Container):

    def __init__(self, producto):

        super().__init__()

        self.width = 250
        self.padding = 10
        self.border_radius = 15
        self.bgcolor = ft.Colors.WHITE

        self.shadow = ft.BoxShadow(
            blur_radius=10,
            color=ft.Colors.with_opacity(0.1, "black")
        )

        self.content = ft.Column(
            spacing=8,
            controls=[

                # Imagen
                ft.Image(
                    src=producto["ruta_imagen"],
                    width=230,
                    height=150,
                    fit="fitWidth"
                ),

                # Nombre
                ft.Text(
                    producto["nombre"],
                    size=18,
                    weight="bold"
                ),

                # Descripción
                ft.Text(
                    producto["descripcion"],
                    size=12,
                    color=ft.Colors.GREY_700
                ),

                # Precio
                ft.Text(
                    f"${producto['precio']}",
                    size=16,
                    weight="bold",
                    color=ft.Colors.GREEN
                ),

                # Barra de acciones
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
            ]
        )

# -----------------------------
# INTERFAZ PRINCIPAL
# -----------------------------

def main(page: ft.Page):

    page.title = "Glich Productions"
    page.bgcolor = ft.Colors.BLACK
    page.scroll = "auto"

    header = ft.Text(
        "🛒 Murder Drones",
        size=30,
        weight="black"
    )

    tarjetas = []

    for producto in productos:
        tarjetas.append(ProductoCard(producto))

    catalogo = ft.Row(
        controls=tarjetas,
        wrap=True,
        spacing=20
    )

    page.add(
        header,
        catalogo
    )


ft.app(
    target=main,
    assets_dir="assets"
)