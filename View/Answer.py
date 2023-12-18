from flet import *

from View.RouteChangePath import RouteChangePath

from ModelPade.ModelPade import ModelPade

def Answer(page: Page):
    
    page.views.append(
        View(
            route = "/", 
            controls = [ 
                *context(
                    page
                )
            ]
        )
    )


def context(page: Page):

    return [
        Column(
            controls = [
                Container(
                    content = Text(
                        "Верно",
                        size=21, 
                        color=colors.BLACK
                    ), 
                    alignment=alignment.center,
                    bgcolor=colors.GREEN_300,
                    width=100,
                    padding=5,
                    border_radius = 5, 
                ),
                ElevatedButton(
                    "Loop", 
                    on_click=lambda _: page.go(RouteChangePath.Start)
                )
                
            ],
            height=ModelPade.page.window_height,
            width=ModelPade.page.window_width,
            horizontal_alignment = CrossAxisAlignment.CENTER,
            alignment = MainAxisAlignment.CENTER,
            spacing=20
        ),
    ]