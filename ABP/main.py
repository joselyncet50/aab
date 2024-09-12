import flet as ft


def main(page: ft.Page):
    page.tittle="suma de 2 numeros"
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER
    page.bg_color("red")
    
    lbl1=ft.Text("Primer numero",
                style=ft.TextStyle(size=40,weight="bold"))
    lmg1=ft.image(src="travis.jpg",width=200,height=200)
    
    btnsuma=ft.ElevatedButton("Suma",
                            color="green",
                            width=100,
                            height=50)
    
    btnlimpiar=ft.ElevatedButton("limpiar",
                                color="azul",
                                width="100",
                                height=50)
    
    page.add(
        ft.column(
            [
                lbl1,
                img1,
                ft.Row([btnsuma,btnlimpiar],
                    alignment=ft.MainAxisAlignment.CENTER
                    ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20
        )
    )
    


ft.app(main)
