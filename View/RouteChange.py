from flet import *
from ModelPade.ModelPade import ModelPade

from View.Start import Start
from View.Timer import Timer
from View.Riddle import Riddle
from View.Answer import Answer

from View.RouteChangePath import RouteChangePath



class RouteChange:

    @staticmethod
    def route_change(route):
        ModelPade.page.views.clear()
        
        match ModelPade.page.route:
            case RouteChangePath.Start: Start(ModelPade.page)
            case RouteChangePath.Timer: Timer(ModelPade.page)
            case RouteChangePath.Riddle: Riddle(ModelPade.page)
            case RouteChangePath.Answer: Answer(ModelPade.page)

    @staticmethod
    def view_pop(view):
        RouteChange.page.views.pop()
        myview = RouteChange.page.views[-1]
        RouteChange.page.go(myview.route)
