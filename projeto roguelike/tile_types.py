from typing import Tuple
import numpy as np

# Tile graphics structured type compatible with Console.tiles_rgb.

graphic_dt=np.dtype(
    [

    ("ch", np.int32), #unicode codepoint
    ("fg", "3B"), #3 unsigned bytersm for RGB colors
    ("bg", "3B"),
    ]
)

#Tile struct used for statically defined tile data
tile_dt=np.dtype(
    [

    ("walkable",np.bool),#true if this tile can be walked over.
    ("trasnparent", np.bool),#true if this tile does'nt block FOV
    ("dark", graphic_dt),# graphics for when tile is not in FOV
    ("light", graphic_dt), #graficos pra quando o tile está no fov
    
    ]
)

def new_tile(
   
    walkable:int,
    transparent:int,
    dark:Tuple[int, Tuple[int,int,int], Tuple[int,int,int]],
    light:Tuple[int, Tuple[int, int, int], Tuple[int, int, int]],
)-> np.ndarray:
#helper function for defining individual tile types
    return np.array((walkable, transparent, dark, light), dtype=tile_dt)


    #"Neblina" representa os tiles não vistos e inexplorados
SHROUD= np.array((ord(" "), (255,255,255),(0,0,0)), dtype=graphic_dt)
floor=new_tile(
    walkable=True,
    transparent=True,
    dark=(ord(" "),(255,255,255),(83,188,121)),
    light=(ord(" "), (255,255,255),(200,180,50)),

)
wall=new_tile(
    walkable=False,
    transparent=True,
    dark=(ord(" "),(255,255,255),(90,96,110)),
    light=(ord(" "), (255,255,255), (130,110,50)),
    )
