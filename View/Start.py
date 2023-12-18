from flet import *

from ModelPade.ModelPade import ModelPade

from View.RouteChangePath import RouteChangePath


def Start(page: Page):
    
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

def start_rider(_):
    ...

def context(page: Page):

    return [
        Column(
            controls = [
                Container(
                    content = TextButton(
                        "Запись",
                        on_click = lambda _: page.go(
                            RouteChangePath.Timer
                        ),
                    ), 
                    alignment=alignment.center,
                )
                
            ],
            height=ModelPade.page.window_height,
            width=ModelPade.page.window_width,
            horizontal_alignment = CrossAxisAlignment.CENTER,
            alignment = MainAxisAlignment.CENTER
        ),
    ]