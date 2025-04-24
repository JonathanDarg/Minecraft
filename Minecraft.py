from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

# Player setup
player = FirstPersonController()

# Sky
Sky()

# Block types with PNG textures
BLOCK_TYPES = {
    'grass': {'color': color.white, 'texture': 'grass.png'},
    'stone': {'color': color.white, 'texture': 'stone.png'},
    'brick': {'color': color.white, 'texture': 'brick.png'}
}
current_block_type = 'grass'  # Default block type

# Create initial platform
boxes = []
for i in range(20):
    for j in range(20):
        box = Button(
            color=BLOCK_TYPES['grass']['color'],
            model='cube',
            position=(j, 0, i),
            texture=BLOCK_TYPES['grass']['texture'],
            parent=scene,
            origin_y=0.5,
            collider='box'
        )
        boxes.append(box)

def input(key):
    global current_block_type
    
    # Block selection
    if key == '1':
        current_block_type = 'grass'
    elif key == '2':
        current_block_type = 'stone'
    elif key == '3':
        current_block_type = 'brick'
    
    # Block placement/removal
    for box in boxes:
        if box.hovered:
            if key == 'left mouse down':
                new = Button(
                    color=BLOCK_TYPES[current_block_type]['color'],
                    model='cube',
                    position=box.position + mouse.normal,
                    texture=BLOCK_TYPES[current_block_type]['texture'],
                    parent=scene,
                    origin_y=0.5,
                    collider='box'
                )
                boxes.append(new)
            if key == 'right mouse down':
                if box in boxes:
                    boxes.remove(box)
                    destroy(box)
    
    # Exit game
    if key == 'escape':
        quit()

# Current block indicator - centered at bottom
block_indicator = Text(
    text=f"Current Block: {current_block_type}",
    position=(0, -0.45),    # Centered at bottom
    origin=(0, 0),          # Center origin
    scale=1.5,              # Slightly larger text
    color=color.white,
    background=True,         # Adds background
    background_color=color.black66
)

def update():
    # Update the current block indicator
    block_indicator.text = f"Current Block: {current_block_type}"

app.run()