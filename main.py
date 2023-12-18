import flet
from flet import *
from ModelPade.ModelPade import ModelPade

from View.RouteChange import RouteChange
import os

def on_resize(_):
    print(ModelPade.page.height)
    print(ModelPade.page.width)
    ModelPade.page.update()	

def main(page: Page):

    ModelPade.page = page
        
    page.title = "routing app"

    page.on_route_change = RouteChange.route_change	
    page.on_view_pop = RouteChange.view_pop


    page.window_min_width = 700

    page.window_title_bar_hidden = True

    page.on_resize = on_resize
    
    page.go(page.route)

    
if __name__ == "__main__":
    flet.app(target=main)



