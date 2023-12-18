from flet import *
from ModelPade.ModelPade import ModelPade

from View.RouteChangePath import RouteChangePath

from threading import Thread, Event
from time import time
import pygame


cut_sound: pygame.mixer.Sound = None
time_start: float


def func(sound_path):
    global cut_sound
    global time_start

    if (cut_sound is not None):
        cut_sound.stop()
        cut_sound = None

    pygame.mixer.init()
    sound = pygame.mixer.Sound(file=sound_path)
    raw_array = sound.get_raw()

    raw_array = raw_array[len(raw_array) // 2: len(raw_array)]
    cut_sound = pygame.mixer.Sound(buffer=raw_array)
    cut_sound.play()

    time_start = time()
    
    while True: 
        
        if (cut_sound is None):
            return

        if (time() - time_start >= 10 ): 
            cut_sound.stop()
            cut_sound = None
            return
        
        




def Riddle(page: Page):    
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
        
    
                Row(
                    [
                        image_card(page, "MP3/Крысолов/Крысолов.jpg", 
                                   "ТMP3/Крысолов/Крысолов.mp3", 
                                   "Крысолов",),

                        image_card(page, "MP3/Перед Казнью/Перед Казнью.jpg", 
                                   "MP3/Перед Казнью/Перед Казнью.mp3", 
                                   "Перед Казнью",),

                        image_card(page, "MP3/Tom's Diner/Tom's Diner.jpg", 
                                   "MP3/Tom's Diner/Tom's Diner.mp3", 
                                   "Tom's Diner",)
                    ],
                    spacing=100,
                    alignment=MainAxisAlignment.CENTER,
                    height=ModelPade.page.window_height,
                    width=ModelPade.page.window_width,
                )
    ]


def image_card(page: Page, cover_path, music_path, music_name):

    def start_play():
        th1 = Thread(target=func, args=([music_path]))
        th1.start()
            
    button_play = IconButton(
        icon=icons.PLAY_CIRCLE_FILLED_ROUNDED,
        icon_color=colors.YELLOW_ACCENT_700,
        left = 300 // 2 - 50 // 2 - 5,
        top = 300 // 2 - 50 // 2 - 5,
        icon_size=50,
        visible=False,
        on_click = lambda _: start_play()

    )
    
    holder = Container(
        width = 300,
        height = 300,
        bgcolor= colors.with_opacity(.4, colors.BLACK12),
        visible=False

    )
    


    def hover_image():
        button_play.visible = not button_play.visible
        holder.visible = not holder.visible
        print(button_play.visible, holder.visible)
        ModelPade.page.update()


    
    
    return Card(


            content = Container(
                content = Column(
                    controls = [
                        Container(
                            Stack(
                                controls = [
                                    Image(
                                        src = cover_path,
                                        width = 300,
                                        height = 300,
                                        fit = ImageFit.FILL,
                                    ),
                                    holder,
                                    button_play
                                ]
                            ),
                            on_hover = lambda _: hover_image()

                        ),
                        
                        Text(
                            value = music_name if not len(music_name) >= 30 else music_name[:26] + "...",
                            text_align = TextAlign.CENTER,
                        ),
                        FilledButton(
                            text="Выбрать",
                            on_click = lambda _: page.go(RouteChangePath.Answer),
                        )
                    ],
                    horizontal_alignment = CrossAxisAlignment.CENTER,
                    wrap=True,
                ),
                padding=10,
                
            )
        )

