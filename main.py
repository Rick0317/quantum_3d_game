from ast import In
from logging import root
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.shaders import lit_with_shadows_shader
import webbrowser
from gates import Gate, Gate_Block
from static_objects import Wall, Axis
from inventory import Inventory, ItemBar
from panda3d.core import AudioSound
from math import sqrt, atan

app = Ursina()
t = 0
Sky()

random.seed(0)
Entity.default_shader = lit_with_shadows_shader

# General
ground = Entity(model='plane', collider='box', scale=64, texture='grass', texture_scale=(4,4))
editor_camera = EditorCamera(enabled=False, ignore_paused=True)
player = FirstPersonController(z=-10, color=color.orange, origin_y=-.5, speed=14)
player.collider = BoxCollider(player, Vec3(0,1,0), Vec3(1,2,1))
player.cursor.visible=True
window.fps_counter.enabled=True

# Each axis
x_axis = Axis(position=(5, 5, 10), rotation=(0,0,0))
y_axis = Axis(position=(0, 10, 10), rotation=(0,0,270))
z_axis = Axis(position=(0, 5, 5), rotation=(0,90,0))

#Walls
wall_1 = Wall(position=(0,0,32), scale=(64, 10, 1))
wall_2 = Wall(position=(0, 0, -32), scale=(64, 10, 1))
wall_3 = Wall(position=(32, 0, 0), scale=(1, 10, 63))
wall_4 = Wall(position=(-32, 0, 0), scale=(1, 10, 63))

# BlochSphere
bloch_sphere = Entity(model="sphere", collider="box", position = (0, 5, 10), scale=10, color=color.rgba(255,255,255,64))
bs_explanation = Text(text="BlochSphere", position=(0, 13, 10), scale=50, parent=scene)
quantum_state = Entity(model="arrow", scale=5, color=color.red, rotation_z = 270, position=(0, 7.5, 10))

video = 'assets/Qiskit_video_example.mp4'
video_player = Entity(model='quad', parent=camera.ui, scale=(0.9, 0.6), texture=video, position=(0.2,0.2), enabled=False)
video_sound=loader.loadSfx("assets/Qiskit_sound_example.mp3")

def input(key):
    if key == "1":
        video_player.enabled = True
        video_player.texture.synchronizeTo(video_sound)
        video_sound.play()
    if key=="n":
        video_player.enabled=False
        video_sound.stop()

# Share the app on twitter
def twitter_share():
    webbrowser.open('https://twitter.com/share?ref_src=twsrc%5Etfw')

# gate transformations
def h_transform():
    relative_x = quantum_state.x - 0
    relative_y = quantum_state.y - 5
    relative_z = quantum_state.z - 10

    pointer_x = relative_x * 2/5
    pointer_y = relative_y * 2/5
    pointer_z = relative_z * 2/5

    divisor = sqrt((sqrt(pointer_y+1) - pointer_z)**2 + pointer_x**2)
    if divisor != 0:
        pointer_x2 = (- sqrt(2)) * pointer_x * (sqrt(pointer_y + 1) + pointer_z )/ divisor
        pointer_y2 = divisor**2 / 2 - 1
        pointer_z2 = (-1/sqrt(2)) * (pointer_y+1-pointer_x**2-pointer_z**2 + 2*pointer_z * sqrt(pointer_y+1)) / divisor 
    else:
        pointer_x2 = (-1/sqrt(2))*(sqrt(pointer_y+1)+pointer_z)
        pointer_y2 = - 1
        pointer_z2 = (-1/sqrt(2)) * pointer_x
        
    quantum_state.x = pointer_x2*5/2  
    quantum_state.y = pointer_y2*5/2 + 5
    quantum_state.z = pointer_z2*5/2 + 10
    if pointer_y - pointer_y2 != 0:
        quantum_state.rotation_x = atan((pointer_z - pointer_z2)/ (pointer_y - pointer_y2))
    if pointer_z - pointer_z2 != 0:
        quantum_state.rotation_y = atan((pointer_x - pointer_x2)/ (pointer_z - pointer_z2))
    if pointer_x - pointer_x2 != 0:
        quantum_state.rotation_z = atan((pointer_y - pointer_y2)/ (pointer_x - pointer_x2))


def x_transform():
    relative_x = quantum_state.x - 0
    relative_y = quantum_state.y - 5
    relative_z = quantum_state.z - 10

    pointer_x = relative_x * 2/5
    pointer_y = relative_y * 2/5
    pointer_z = relative_z * 2/5

    pointer_x2 = pointer_x
    pointer_y2 = -pointer_y
    pointer_z2 = -pointer_z

    quantum_state.x = pointer_x2 * 5/2
    quantum_state.y = pointer_y2 * 5/2 + 5
    quantum_state.z = pointer_z2 * 5/2 + 10


def z_transform():
    relative_x = quantum_state.x - 0
    relative_y = quantum_state.y - 5
    relative_z = quantum_state.z - 10

    pointer_x = relative_x * 2/5
    pointer_y = relative_y * 2/5
    pointer_z = relative_z * 2/5

    pointer_x2 = -pointer_x
    pointer_y2 = -pointer_y
    pointer_z2 = pointer_z

    quantum_state.x = pointer_x2 * 5/2
    quantum_state.y = pointer_y2 * 5/2 + 5
    quantum_state.z = pointer_z2 * 5/2 + 10
    

def s_transform():
    pass

def t_transform():
    pass

def set_back():
    quantum_state.rotation_z = 270
    quantum_state.position=(0, 7.5, 10)


# several gates
h_gate=Gate(position=(0,1,3), icon="assets/h_gate.png")
h_gate2=Gate(position=(0,1,2), icon="assets/h_gate.png", rotation=(0,0,0))
h_gate_block = Gate_Block(position=(0, 0.5, 2.5))

x_gate=Gate(position=(1,1,3), icon="assets/x_gate.png")
x_gate2=Gate(position=(1,1,2), icon="assets/x_gate.png", rotation=(0,0,0))
x_gate_block = Gate_Block(position=(1, 0.5, 2.5))

z_gate=Gate(position=(2,1,3), icon="assets/z_gate.png")
z_gate2=Gate(position=(2,1,2), icon="assets/z_gate.png", rotation=(0,0,0))
z_gate_block = Gate_Block(position=(2, 0.5, 2.5))

s_gate=Gate(position=(3,1,3), icon="assets/s_gate.jpeg")
s_gate2=Gate(position=(3,1,2), icon="assets/s_gate.jpeg", rotation=(0,0,0))
s_gate_block = Gate_Block(position=(3, 0.5, 2.5))

t_gate=Gate(position=(4,1,3), icon="assets/t_gate.png")
t_gate2=Gate(position=(4,1,2), icon="assets/t_gate.png", rotation=(0,0,0))
t_gate_block = Gate_Block(position=(4, 0.5, 2.5))

twitter = Gate(position=(-5, 1, -0.5), icon="assets/twitter.png", rotation=(0,0,0))
twitter_block = Gate_Block(position=(-5, 0.5, 0))

h_gate.on_click = h_transform
h_gate2.on_click = h_transform
twitter.on_click = twitter_share

x_gate.on_click = x_transform
x_gate2.on_click = x_transform

z_gate.on_click = z_transform
z_gate2.on_click = z_transform


item_bar = ItemBar()

app.run()