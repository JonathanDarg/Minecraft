from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

# Player setup
player = FirstPersonController()

# Sky
Sky()

# Load textures
grass_texture = load_texture('green_grass.png')
grass_side_texture = load_texture('grass_side.png')  # not used in this version
dirt_texture = load_texture('dirt.png')              # not used in this version
stone_texture = load_texture('smooth_stone.png')
brick_texture = load_texture('bricks.png')

# Block types dictionary
BLOCK_TYPES = {
    'grass': {'texture': grass_texture},
    'stone': {'texture': stone_texture},
    'brick': {'texture': brick_texture}
}
current_block_type = 'grass'

# List to hold block references
boxes = []

# Create a block at the given position with the selected type
def create_block(position, block_type):
    block = Button(
        model='cube',
        position=position,
        texture=BLOCK_TYPES[block_type]['texture'],
        color=color.white,
        parent=scene,
        origin_y=0.5,
        collider='box'
    )
    return block

# Create initial 20x20 grass platform
for x in range(20):
    for z in range(20):
        block = create_block((x, 0, z), 'grass')
        boxes.append(block)

# Input handling
def input(key):
    global current_block_type

    # Block selection keys
    if key == '1':
        current_block_type = 'grass'
    elif key == '2':
        current_block_type = 'stone'
    elif key == '3':
        current_block_type = 'brick'

    # Place or remove blocks
    for block in boxes:
        if block.hovered:
            if key == 'left mouse down':
                new_block = create_block(block.position + mouse.normal, current_block_type)
                boxes.append(new_block)
            if key == 'right mouse down':
                boxes.remove(block)
                destroy(block)

    if key == 'escape':
        quit()

# Block type indicator UI
block_indicator = Text(
    text=f"Current Block: {current_block_type}",
    position=(0, -0.45),
    origin=(0, 0),
    scale=1.5,
    color=color.white,
    background=True,
    background_color=color.rgba(0, 0, 0, 180)
)

# Update UI text dynamically
def update():
    block_indicator.text = f"Current Block: {current_block_type}"

# Run the app
app.run()
