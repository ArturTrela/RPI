import flet as ft
import random

measure = random.randint(0, 100)
print(measure)
def main(page: ft.Page):
    page.title = "Raspberry Data Collecting"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.bgcolor=ft.colors.INDIGO_50
    page.padding=30


    t = ft.Tabs(
        selected_index=0,
        animation_duration=500,
        divider_color="red",
        indicator_tab_size= True,
        label_color="orange",
        unselected_label_color="black",

        tabs=[
            ft.Tab(
                text="PANEL GŁÓWNY",
                icon=ft.icons.HOME,
                content=ft.TextField(
                    value="Marcinku !\n\nLepiej zbieraj już na słonia ",
                    min_lines=3,
                    max_lines=3,
                    multiline=True,
                    border_width=0,
                    color="black",
                    text_size=20,
                    text_align="center",

                ),

            ),
            ft.Tab(
                text="KONFIGURUJ DANE ",
                icon=ft.icons.NOTE,
                    content=ft.TextField(
                        value=(measure),
                        height=50,
                        width=30,
                        border_color="pink",
                        color="black",
                ),

            ),
            ft.Tab(
                text="PODGLĄD DANYCH",
                icon=ft.icons.STORAGE,
                content=ft.Column(
                     [
                            ft.Text(
                               value="Change the column height to see how child items wrap onto multiple columns:",
                                color="black",
                                text_align="center",
                            ),
                        ],

                ),
            ),
            ft.Tab(
                text="DANE HISTORYCZNE",
                icon=ft.icons.HISTORY,
                content=ft.Container(
                    content=ft.Text("This is Tab 1"), alignment=ft.alignment.center
                ),
            ),
            ft.Tab(
                text="WYSZUKAJ",
                icon=ft.icons.SEARCH,
                content=ft.Text("This is Tab 2"),
            ),
            ft.Tab(
                text="KONTAKT",
                icon=ft.icons.MAIL,
                content=ft.Text("This is Tab 2"),
            ),
            ft.Tab(
                text="PANEL ADMINISTARTORA",
                icon=ft.icons.SETTINGS,
                content=ft.Text("This is Tab 3"),
            ),
        ],

    )

    page.add(t)

ft.app(target=main, view=ft.AppView.WEB_BROWSER )

