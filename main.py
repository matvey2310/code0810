import flet as ft
import random
import string

def main(page: ft.Page):
    page.title = "Кликер на Flet"
    page.bgcolor = "#87CEEB"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Текстовое поле, куда будет выводиться готовый пароль
    password_field = ft.TextField(
        label="Ваш пароль",
        value="",
        read_only=True,
        width=400,
        text_align=ft.TextAlign.CENTER,
    )

    # Компонент для выбора длины пароля (от 6 до 32 символов)
    length_slider = ft.Slider(
        min=6,
        max=32,
        divisions=26,
        value=12,
        label="Длина: {value}",
        width=400,
    )

    # Функция генерации пароля
    def generate_password(e):
        length = int(length_slider.value)
        # Набор символов: буквы (верхний/нижний регистр), цифры и спецсимволы
        characters = string.ascii_letters + string.digits + "!@#$%^&*()_+-="

        # Гарантируем, что в пароле будет хотя бы одна буква, цифра и спецсимвол
        password = [
            random.choice(string.ascii_lowercase),
            random.choice(string.ascii_uppercase),
            random.choice(string.digits),
            random.choice("!@#$%^&*()_+-=")
        ]

        # Добираем оставшуюся длину случайными символами
        password += [random.choice(characters) for _ in range(length - 4)]

        # Перемешиваем, чтобы гарантированные символы не стояли всегда в начале
        random.shuffle(password)

        # Выводим в поле
        password_field.value = "".join(password)
        page.update()

    # Кнопка генерации
    click_button = ft.ElevatedButton(
        width=400,
        height=50,
        content=ft.Row(
            [ft.Text("Сгенерировать пароль", size=16, weight=ft.FontWeight.BOLD)],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        on_click=generate_password,  # Привязываем функцию к клику
    )

    # Добавляем все элементы на страницу
    page.add(
        ft.Text("Генератор безопасных паролей", size=20, weight=ft.FontWeight.BOLD, color="#87CEEB"),
        ft.Container(height=10),
        length_slider,
        password_field,
        ft.Container(height=10),
        click_button  #
    )
    page.update()  #


if __name__ == "__main__":
    ft.run(main)
