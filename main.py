import flet as ft
import random
import string


def main(page: ft.Page):
    page.title = "Кликер на Flet"
    page.bgcolor = "#87CEEB"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Переменная для подсчета количества генераций паролей
    click_count = 0

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

    # Функция закрытия модального окна
    def close_dialog(e):
        subscription_dialog.open = False
        page.update()

    # Создаем всплывающее диалоговое окно (модальное)
    subscription_dialog = ft.AlertDialog(
        modal=True,
        title=ft.Text("Лимит исчерпан", text_align=ft.TextAlign.CENTER),
        content=ft.Text("Вы использовали все 5 бесплатных генераций.\nЧтобы продолжить, нужно оформить подписку!"),
        actions=[
            ft.TextButton("Оформить подписку", on_click=close_dialog),
            ft.TextButton("Закрыть", on_click=close_dialog),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )

    # Функция генерации пароля
    def generate_password(e):
        nonlocal click_count  # Используем внешнюю переменную счетчика

        # Проверяем, если количество использований достигло или превысило 5
        if click_count >= 5:
            page.dialog = subscription_dialog  # Привязываем окно к странице
            subscription_dialog.open = True  # Открываем окно
            page.update()  # Обновляем страницу для показа окна
            return  # Прерываем выполнение функции, пароль не генерируется

        length = int(length_slider.value)
        characters = string.ascii_letters + string.digits + "!@#$%^&*()_+-="

        password = [
            random.choice(string.ascii_lowercase),
            random.choice(string.ascii_uppercase),
            random.choice(string.digits),
            random.choice("!@#$%^&*()_+-=")
        ]

        password += [random.choice(characters) for _ in range(length - 4)]
        random.shuffle(password)

        password_field.value = "".join(password)

        # Увеличиваем счетчик после успешной генерации
        click_count += 1
        page.update()

    # Кнопка генерации
    click_button = ft.ElevatedButton(
        width=400,
        height=50,
        content=ft.Row(
            [ft.Text("Сгенерировать пароль", size=16, weight=ft.FontWeight.BOLD)],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        on_click=generate_password,
    )

    # Добавляем все элементы на страницу
    page.add(
        ft.Text("Генератор безопасных паролей", size=20, weight=ft.FontWeight.BOLD, color="#E0FFFF"),
        ft.Container(height=10),
        length_slider,
        password_field,
        ft.Container(height=10),
        click_button
    )
    page.update()


if __name__ == "__main__":
    ft.run(main)
