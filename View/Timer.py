from typing import Any, List, Optional, Tuple, Union
from flet import *
from flet_core.alignment import Alignment
from flet_core.blur import Blur
from flet_core.border import Border
from flet_core.control import Control, OptionalNumber
from flet_core.gradients import Gradient
from flet_core.ref import Ref
from flet_core.shadow import BoxShadow
from flet_core.theme import Theme
from flet_core.types import AnimationValue, BlendMode, BorderRadiusValue, BoxShape, ClipBehavior, ImageFit, ImageRepeat, MarginValue, OffsetValue, PaddingValue, ResponsiveNumber, RotateValue, ScaleValue, ThemeMode
from ModelPade.ModelPade import ModelPade

from View.RouteChangePath import RouteChangePath

from threading import Thread, Event
from time import monotonic

from Settings.Timer import timer_time



timer_text: Text

button_next: ElevatedButton




class Blok_loud(Container):
    item_loud: Container = []
    next_item_loud_full: int = 1


    def __init__(self, content: Control | None = None, ref: Ref | None = None, key: str | None = None, width: OptionalNumber = None, height: OptionalNumber = None, left: OptionalNumber = None, top: OptionalNumber = None, right: OptionalNumber = None, bottom: OptionalNumber = None, expand: bool | int | None = None, col: ResponsiveNumber | None = None, opacity: OptionalNumber = None, rotate: RotateValue = None, scale: ScaleValue = None, offset: OffsetValue = None, aspect_ratio: OptionalNumber = None, animate_opacity: AnimationValue = None, animate_size: AnimationValue = None, animate_position: AnimationValue = None, animate_rotation: AnimationValue = None, animate_scale: AnimationValue = None, animate_offset: AnimationValue = None, on_animation_end=None, tooltip: str | None = None, visible: bool | None = None, disabled: bool | None = None, data: Any = None, padding: PaddingValue = None, margin: MarginValue = None, alignment: Alignment | None = None, bgcolor: str | None = None, gradient: Gradient | None = None, blend_mode: BlendMode = BlendMode.NONE, border: Border | None = None, border_radius: BorderRadiusValue = None, image_src: str | None = None, image_src_base64: str | None = None, image_repeat: ImageRepeat | None = None, image_fit: ImageFit | None = None, image_opacity: OptionalNumber = None, shape: BoxShape | None = None, clip_behavior: ClipBehavior | None = None, ink: bool | None = None, animate: AnimationValue = None, blur: float | int | Tuple[float | int, float | int] | Blur | None = None, shadow: BoxShadow | List[BoxShadow] | None = None, url: str | None = None, url_target: str | None = None, theme: Theme | None = None, theme_mode: ThemeMode | None = None, on_click=None, on_long_press=None, on_hover=None):
        super().__init__(content, ref, key, width, height, left, top, right, bottom, expand, col, opacity, rotate, scale, offset, aspect_ratio, animate_opacity, animate_size, animate_position, animate_rotation, animate_scale, animate_offset, on_animation_end, tooltip, visible, disabled, data, padding, margin, alignment, bgcolor, gradient, blend_mode, border, border_radius, image_src, image_src_base64, image_repeat, image_fit, image_opacity, shape, clip_behavior, ink, animate, blur, shadow, url, url_target, theme, theme_mode, on_click, on_long_press, on_hover)

        self.width = 400
        self.height = 15

        self.bgcolor = colors.AMBER
        self.border_radius = 10

        self.animate_size = animation.Animation(500, AnimationCurve.BOUNCE_IN)

        self.context()


    def context(self):
        self.width_item = self.width / timer_time
        
        self.item_loud = Container(
            width = 1,
            height = self.height,
        ) 

        color = colors.RED_600

        self.item_loud.border= Border(
            BorderSide(1, color),
            BorderSide(1, color),
            BorderSide(1, color),
            BorderSide(1, color),
        )
        self.item_loud.bgcolor = color

        self.content = Row(
            [self.item_loud]
        )

    def next(self):
        self.item_loud.width = self.width_item * self.next_item_loud_full
        
        self.next_item_loud_full += 1 

class Heart_Animated(Column):
    def __init__(self, size: OptionalNumber = None, paiding: OptionalNumber = 10):
        super().__init__(width=size, height=size)
        
        self.horizontal_alignment = CrossAxisAlignment.CENTER
        self.alignment = MainAxisAlignment.CENTER


        self.favorite_rounded = Icon(
            name = icons.FAVORITE_ROUNDED,
            size = size - paiding * 2,
            color=colors.DEEP_PURPLE_100
        )
            
        self.favorite_outline_rounded = Icon(
            name = icons.FAVORITE_OUTLINE_ROUNDED,
            size = size - paiding * 2,
            color=colors.PURPLE_100
        )
        
        self.favorite_animated_switcher = AnimatedSwitcher(
            self.favorite_rounded,
            transition = AnimatedSwitcherTransition.SCALE,
            duration = 600,
            reverse_duration = 100,
            switch_in_curve = AnimationCurve.BOUNCE_OUT,
            switch_out_curve = AnimationCurve.BOUNCE_IN,
        )

        self.controls = [self.favorite_animated_switcher]


    def Heartbeat(self):
        if (self.favorite_animated_switcher.content == self.favorite_rounded):
            self.favorite_animated_switcher.content = self.favorite_outline_rounded
        else:
            self.favorite_animated_switcher.content = self.favorite_rounded
        self.update()






blok_loud: Blok_loud

heart_animated: Heart_Animated

def func():
    _time: int = 0

    timer_text.value = f"{_time}"

    time_start = monotonic()

    time_heart = monotonic()

    while True:
        
        if (monotonic() - time_heart >= 0.6):
            time_heart = monotonic()
            heart_animated.Heartbeat()
        

        if (monotonic() - time_start >= 1):
            _time += 1
            timer_text.value = f"{_time}"
            time_start = monotonic()

            blok_loud.next()

            if (_time == timer_time):
                button_next.disabled = False
                ModelPade.page.update()
                return
            

            


            ModelPade.page.update()

th1: Thread

def Timer(page: Page):
    global th1
    th1 = Thread(target=func)
    
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
    global timer_text
    timer_text = Text("Таймер")

    global button_next
    button_next = ElevatedButton(
            "Go to", 
            on_click = lambda _: page.go(RouteChangePath.Riddle),
            disabled = True

        )


    global th1
    th1.start()
    
    global blok_loud
    blok_loud = Blok_loud()

    global heart_animated
    heart_animated = Heart_Animated(200, 5)


    return [
        Column(
            height=ModelPade.page.window_height,
            width=ModelPade.page.window_width,
            controls = [
                Container(
                    Column(
                        horizontal_alignment = CrossAxisAlignment.CENTER,
                        alignment = MainAxisAlignment.CENTER,
                        controls = [
                            heart_animated,
                            blok_loud,
                            button_next
                        ]
                    ),
                ),
            ],
            horizontal_alignment = CrossAxisAlignment.CENTER,
            alignment = MainAxisAlignment.CENTER
        )
    ]