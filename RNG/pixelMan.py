from PIL import Image, ImageDraw
import random

# Generate random colors
def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Choose a random hairstyle
def random_hair(draw, x_start, y_start, hair_color):
    hair_styles = [
        [(x_start, y_start - 30), (x_start + 60, y_start)],
        [(x_start, y_start - 20), (x_start + 60, y_start)],
        [(x_start + 10, y_start - 30), (x_start + 50, y_start)]
    ]
    chosen_style = random.choice(hair_styles)
    draw.rectangle(chosen_style, fill=hair_color)

# Draw arms in random positions
def random_arms(draw, x_start, y_start, arm_width, body_width, skin_color):
    arm_height = 100  # Arm length
    arm_styles = [
        # Left arm down
        (x_start - arm_width, y_start + 10, x_start, y_start + arm_height),
        # Right arm down
        (x_start + body_width, y_start + 10, x_start + body_width + arm_width, y_start + arm_height),
        # Left arm up
        (x_start - arm_width, y_start - arm_height, x_start, y_start),
        # Right arm up
        (x_start + body_width, y_start - arm_height, x_start + body_width + arm_width, y_start)
    ]
    # Randomly select different arm positions
    selected_arms = random.sample(arm_styles, 2)  # Choose two positions
    for arm in selected_arms:
        draw.rectangle(arm, fill=skin_color)
        
def random_skin_color():
    # Generate a more natural skin color, ranging from light to dark
    red = random.randint(80, 205)
    green = random.randint(50, 133)
    blue = random.randint(40, 63)
    return (red, green, blue)

# Create a pixel person
def create_pixel_person():
    # Create a 300x300 image with a transparent background
    img = Image.new('RGBA', (300, 300), (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)

    # Set colors
    skin_color = random_skin_color()
    hair_color = random_color()
    shirt_color = random_color()
    pants_color = random_color()
    shoe_color = random_color()
    eye_color = 'black'  # Eye color
    mouth_color = 'black'  # Mouth color

    # Random body features
    body_width = random.randint(40, 70)  # Body width
    body_height = random.randint(70, 110)  # Body height
    leg_height = random.randint(70, 100)  # Leg height
    arm_width = 10  # Arm width
    x_start = 150 - body_width // 2
    y_start = 150 - body_height

    # Head
    head_height = random.randint(40, 60)
    head_top = y_start - head_height
    draw.rectangle([x_start, head_top, x_start + body_width, y_start], fill=skin_color)
    # Random hairstyle
    random_hair(draw, x_start, head_top, hair_color)
    # Body
    draw.rectangle([x_start, y_start, x_start + body_width, y_start + body_height], fill=shirt_color)
    # Arms in random positions
    random_arms(draw, x_start, y_start, arm_width, body_width, skin_color)
    # Legs
    draw.rectangle([x_start, y_start + body_height, x_start + body_width // 2, y_start + body_height + leg_height], fill=pants_color)
    draw.rectangle([x_start + body_width // 2, y_start + body_height, x_start + body_width, y_start + body_height + leg_height], fill=pants_color)
    # Feet
    draw.rectangle([x_start, y_start + body_height + leg_height, x_start + body_width // 2, y_start + body_height + leg_height + 30], fill=shoe_color)
    draw.rectangle([x_start + body_width // 2, y_start + body_height + leg_height, x_start + body_width, y_start + body_height + leg_height + 30], fill=shoe_color)
    # Eyes
    draw.rectangle([x_start + 10, head_top + 10, x_start + 20, head_top + 20], fill=eye_color)
    draw.rectangle([x_start + body_width - 20, head_top + 10, x_start + body_width - 10, head_top + 20], fill=eye_color)
    # Mouth
    draw.rectangle([x_start + 15, head_top + 30, x_start + body_width - 15, head_top + 40], fill=mouth_color)

    return img
