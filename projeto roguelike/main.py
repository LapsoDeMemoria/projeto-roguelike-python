
#!usr/bin/env python3

from procgen import generate_dungeon
import tcod
import input_handlers
import entity
from engine import Engine


def main():

    #tamanho da tela
    screen_width=128
    screen_height=96
    map_width=128
    map_height=91

    room_max_size=30
    room_min_size=18
    max_rooms=30
    #definindo a fonte do projeto
    tileset=tcod.tileset.load_tilesheet("dejavu10x10_gs_tc.png", 32,8, tcod.tileset.CHARMAP_TCOD)
    #variável que armazena a classe que lida com os inputs
    event_handler= input_handlers.EventHandler()
    #estabelecendo variáveis para as entidades, suas posições iniciai, caracteres e cores em RGB
    player=entity.Entity(int(screen_width/2), int(screen_height/2),"@",(52,58,121))
    npc= entity.Entity(int(screen_width/2-5),int(screen_height/2),"@",(255,255,0))
    entities={npc,player}

    game_map=generate_dungeon(
        max_rooms=max_rooms,
        room_min_size=room_min_size,
        room_max_size=room_max_size,
        map_width=map_width,
        map_height=map_height,
        player=player

    )

    #cria novo terminal
    engine=Engine(entities=entities,event_handler=event_handler,game_map=game_map,player=player)
    with tcod.context.new_terminal(
        screen_width,
        screen_height,
        tileset=tileset,
        title="Roguelike",
        vsync=True,
    ) as context:
        root_console=tcod.Console(screen_width, screen_height, order="F")
        #gameloop
        while True:
            #printa o player na tela
            engine.render(console=root_console,context=context)
            events=tcod.event.wait()
            engine.handle_events(events)
            


if __name__ == "__main__":
    main()
