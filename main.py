import flet as ft

def main(page: ft.Page):
    page.title = "Кликер на Flet"
    page.bgcolor = "#87CEEB"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    click_button = ft.ElevatedButton(
        width=400,
        height=50,
        content = ft.Row(
            [
                ft.Text("Сгенерировать пароль"),
             ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),

    )
    page.add(click_button)
    page.update()

if __name__ == "__main__":
    ft.run(main)
