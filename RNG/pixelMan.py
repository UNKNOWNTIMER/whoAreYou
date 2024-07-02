from PIL import Image, ImageDraw
import random

# 随机颜色生成
def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# 选择随机的发型
def random_hair(draw, x_start, y_start, hair_color):
    hair_styles = [
        [(x_start, y_start - 30), (x_start + 60, y_start)],
        [(x_start, y_start - 20), (x_start + 60, y_start)],
        [(x_start + 10, y_start - 30), (x_start + 50, y_start)]
    ]
    chosen_style = random.choice(hair_styles)
    draw.rectangle(chosen_style, fill=hair_color)

# 绘制随机姿势的手臂
def random_arms(draw, x_start, y_start, arm_width, body_width, skin_color):
    arm_height = 100  # 手臂长度
    arm_styles = [
        # 左手臂向下
        (x_start - arm_width, y_start + 10, x_start, y_start + arm_height),
        # 右手臂向下
        (x_start + body_width, y_start + 10, x_start + body_width + arm_width, y_start + arm_height),
        # 左手臂向上
        (x_start - arm_width, y_start - arm_height, x_start, y_start),
        # 右手臂向上
        (x_start + body_width, y_start - arm_height, x_start + body_width + arm_width, y_start)
    ]
    # 随机选取不同姿势的手臂
    selected_arms = random.sample(arm_styles, 2)  # 选择两个姿势
    for arm in selected_arms:
        draw.rectangle(arm, fill=skin_color)
        
def random_skin_color():
    # 生成一种更自然的皮肤颜色，使用浅色到深色的范围
    red = random.randint(80, 205)
    green = random.randint(50, 133)
    blue = random.randint(40, 63)
    return (red, green, blue)

# 创建像素人
def create_pixel_person():
    # 创建一个300x300的图像，透明背景
    img = Image.new('RGBA', (300, 300), (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)

    # 设定颜色
    skin_color = random_skin_color()
    hair_color = random_color()
    shirt_color = random_color()
    pants_color = random_color()
    shoe_color = random_color()
    eye_color = 'white'  # 眼睛颜色
    mouth_color = 'black'  # 嘴巴颜色

    # 随机体型特征
    body_width = random.randint(40, 70)  # 身体宽度
    body_height = random.randint(70, 110)  # 身体高度
    leg_height = random.randint(70, 100)  # 腿部高度
    arm_width = 10  # 手臂宽度
    x_start = 150 - body_width // 2
    y_start = 150 - body_height

    # 头部
    head_height = random.randint(40, 60)
    head_top = y_start - head_height
    draw.rectangle([x_start, head_top, x_start + body_width, y_start], fill=skin_color)
    # 随机发型
    random_hair(draw, x_start, head_top, hair_color)
    # 身体
    draw.rectangle([x_start, y_start, x_start + body_width, y_start + body_height], fill=shirt_color)
    # 随机姿势的手臂
    random_arms(draw, x_start, y_start, arm_width, body_width, skin_color)
    # 腿部
    draw.rectangle([x_start, y_start + body_height, x_start + body_width // 2, y_start + body_height + leg_height], fill=pants_color)
    draw.rectangle([x_start + body_width // 2, y_start + body_height, x_start + body_width, y_start + body_height + leg_height], fill=pants_color)
    # 脚
    draw.rectangle([x_start, y_start + body_height + leg_height, x_start + body_width // 2, y_start + body_height + leg_height + 30], fill=shoe_color)
    draw.rectangle([x_start + body_width // 2, y_start + body_height + leg_height, x_start + body_width, y_start + body_height + leg_height + 30], fill=shoe_color)
    # 眼睛
    draw.rectangle([x_start + 10, head_top + 10, x_start + 20, head_top + 20], fill=eye_color)
    draw.rectangle([x_start + body_width - 20, head_top + 10, x_start + body_width - 10, head_top + 20], fill=eye_color)
    # 嘴巴
    draw.rectangle([x_start + 15, head_top + 30, x_start + body_width - 15, head_top + 40], fill=mouth_color)

    return img
