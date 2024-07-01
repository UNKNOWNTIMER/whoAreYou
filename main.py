import pygame
import threading
import sys
import os
import random
from RNG.RNG_list import random_game,random_game_element
from RNG.pixelMan import create_pixel_person
from api_llama3.engine_llama3 import run_aIgame_in_cmd,game_code,client,wiki_human
from api_llama3.chat_preprocessing import extract_and_save_code,extract_info
from text_QA import QA
def main_menu():
    return ["介绍一下你的经历!", "你有什么经验分享给我吗？", "我想测试下你的游戏开发水平","让我再玩一次你写的游戏!", "下一位"]

def UI_switch():
    global UI_flag,UI_switch_tag,current_menu, current_option
    #开关
    UI_flag = 1 - UI_flag
    if  UI_flag:
        UI_switch_tag = "等下测试时不要美化UI!"
        print_t("嗯,我会让UI变得好看~")
        current_menu = main_menu()
        current_option = 0
    else:
        UI_switch_tag = "测试时记得美化UI!"
        print_t("好的,我不会去美化UI的")
        current_menu = main_menu()
        current_option = 0
    return
    
def game_again():
    global game_flag
    if not game_flag:
        print_t("哎?我还什么都没写呢")
    else:
        print_t("好滴!请您查看CMD窗口")
    return

def game_dev_menu():
    global tag_1,tag_2,tag_3
    return [UI_switch_tag,tag_1, tag_2, tag_3, "你再想想还能写什么?"]

#讲述故事模块
def story():
    global background
    print_t(background)
    return

#作为这个程序员分享经验
def share_experience():
    print_t("分享一些经验。")
    return

def op_1():
    global client,random_game_element1,random_game_type1,UI_flag
    print_t(random_game_type1)
    game_txet = game_code(client,random_game_element1,random_game_type1)
    #print(game_txet)
    extract_and_save_code(game_txet, 'extracted_game_code.py')
    thread = threading.Thread(target=run_aIgame_in_cmd, args=(client,UI_flag))
    thread.start()
    #run_aIgame_in_cmd(client)    
    return

def op_2():
    global client,random_game_element2,random_game_type2,UI_flag
    print_t(random_game_type2)
    game_txet = game_code(client,random_game_element2,random_game_type2)
    #print(game_txet)
    extract_and_save_code(game_txet, 'extracted_game_code.py')
    thread = threading.Thread(target=run_aIgame_in_cmd, args=(client,UI_flag))
    thread.start()
    return

def op_3():
    global client,random_game_element3,random_game_type3,UI_flag
    print_t(random_game_type3)
    game_txet = game_code(client,random_game_element3,random_game_type3)
    #print(game_txet)
    extract_and_save_code(game_txet, 'extracted_game_code.py')
    thread = threading.Thread(target=run_aIgame_in_cmd, args=(client,UI_flag))
    thread.start()
    return

#返回菜单
def return_to_main():
    global current_menu, current_option, tag_1, tag_2, tag_3,random_game_type1,random_game_type2,random_game_type3
    global random_game_element1,random_game_element2,random_game_element3
    current_menu = main_menu()
    current_option = 0
    print_t("好吧")
    random_game_type1 = random_game()
    random_game_type2 = random_game()
    random_game_type3 = random_game()
    random_game_element1 = random_game_element()
    random_game_element2 = random_game_element()
    random_game_element3 = random_game_element()
    tag_1 = "我想要你编写一个"+random_game_element1+"有关的"+random_game_type1+"类型游戏!"
    tag_2 = "测试一下你"+random_game_element2+"有关的"+random_game_type2+"类型游戏编写..."
    tag_3 = "那你能帮我写一个"+random_game_element3+"有关的"+random_game_type3+"类型游戏吗?"
    return

def test_game_dev():
    global current_menu, current_option
    current_menu = game_dev_menu()
    current_option = 0
    return

def next_person():
    global second_image_path,result_text,name, age, gender, background
    os.system('cls')
    print("###"+name+"退出了面试软件###\n###正在建立下一位面试者的连接中,请稍等###\n\n虽然"+name+"面无表情,但是你还是从他30X30的像素脸庞上捕捉到了一丝不甘")
    name, age, gender, background = extract_info(wiki_human(client))
    print_t ("您好呀，我是"+name+",来自"+QA._country+",今年"+age+"岁")
    second_image_index = random.randint(1, 99)  # 生成1到99的随机数
    second_image_path = os.path.join(folder_path, f"Transparent_Pixel_Art_Person_{second_image_index}.png")
    return  

#用来控制pygame打印对话
def print_t(result_t):
    global result_text
    result_text = result_t
    text_lines = wrap_text(result_text, 26)
    #行间距控制
    y_offset = 10
    for line in text_lines:
        text_surface = font.render(line, True, (255, 255, 255))
        screen.blit(text_surface, (50, y_offset))
        y_offset += font.get_linesize()
    # 更新屏幕显示
    return
#自动提行    
def wrap_text(text, chars_per_line):
    lines = []
    while text:
        if len(text) > chars_per_line:
            last_space = text.rfind(' ', 0, chars_per_line)
            if last_space == -1:
                last_space = chars_per_line
            lines.append(text[:last_space].strip())
            text = text[last_space:].strip()
        else:
            lines.append(text)
            break
    return lines

#播放指定的音乐文件
def play_music(music_file):
    # 停止
    pygame.mixer.music.stop()
    # 加载
    pygame.mixer.music.load("music\\"+music_file+".mp3")
    # 播放
    pygame.mixer.music.play()

if __name__ == "__main__":
    #这一块为全局变量,因为代码内容不多我就不优化内存了~偷懒
    global current_menu, current_option,tag_1,tag_2,tag_3,name, age, gender, background,second_image_path,result_text,random_game_type1,random_game_type2,random_game_type3
    global text_lines,random_game_element1,random_game_element2,random_game_element3
    global UI_flag,UI_switch_tag,game_flag
    os.system('cls')#清理掉启动信息
    print("\n%%%%%%%%%%%%%%%%%%%对方正在远程连接中%%%%%%%%%%%%%%%%%%%")
    #调用模型中生成的人物信息
    name, age, gender, background = extract_info(wiki_human(client))
    #初始化全局设置开关
    UI_flag = 1#是否启用LLM用于美化LLM模型写的程序
    game_flag = 0#检查是否生成了extrated_game_code.py游戏代码文件
    # 初始化pygame
    pygame.init()
    pygame.mixer.init()
    # 设置窗口
    screen_width = 800
    screen_height = 500
    screen = pygame.display.set_mode((screen_width, screen_height))
    # 设置窗口标题
    pygame.display.set_caption('WhoAreYou')
    # 设置颜色
    black = (0, 0, 0)
    white = (255, 255, 255)
    # 加载字体，指定黑体
    font_path = 'C:\\Windows\\Fonts\\simhei.ttf'  # Windows中黑体的典型路径
    font = pygame.font.Font(font_path, 24)
    # pixelMan初始化运行，文件夹路径
    play_music(music_file)
    folder_path = "generated_data/pixelMan"
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)  # 创建文件夹如果不存在
    print("\n%%%%%%%%%%%%%%%%%%%对方正在快速打字回复中%%%%%%%%%%%%%%%%%%%")
    if len(os.listdir(folder_path)) == 0:
        print("\n%%%%%%%%%%%%%%%第一次面试对方有些紧张,正在打扮自己中%%%%%%%%%%%%%%%")
        # 如果文件夹为空，则生成100张图片
        for i in range(100):
            img = create_pixel_person()
            img.save(os.path.join(folder_path, f"Transparent_Pixel_Art_Person_{i}.png"))
    # 加载图片只加载第一张序列图
    character_image_path = os.path.join(folder_path, "Transparent_Pixel_Art_Person_0.png")
    character_image = pygame.image.load(character_image_path)
    character_image = pygame.transform.scale(character_image, (200, 200))  # 调整图片大小
    # 随机加载第二张图片
    second_image_index = random.randint(1, 99)  # 生成1到99的随机数
    second_image_path = os.path.join(folder_path, f"Transparent_Pixel_Art_Person_{second_image_index}.png")
    second_image = pygame.image.load(second_image_path)
    second_image = pygame.transform.scale(second_image, (200, 200))

    #初始化子选项
    random_game_type1 = random_game()
    random_game_type2 = random_game()
    random_game_type3 = random_game()
    random_game_element1 = random_game_element()
    random_game_element2 = random_game_element()
    random_game_element3 = random_game_element()
    tag_1 = "我想要你编写一个"+random_game_element1+"有关的"+random_game_type1+"类型游戏!"
    tag_2 = "测试一下你"+random_game_element2+"有关的"+random_game_type2+"类型游戏编写..."
    tag_3 = "那你能帮我写一个"+random_game_element3+"有关的"+random_game_type3+"类型游戏吗?"
    UI_switch_tag = "记得测试时不要美化UI!"
    # 显示结果的文本
    result_text ="您好呀，我是"+name+",来自"+QA._country+",今年"+age+"岁"

    current_menu = main_menu()
    current_option = 0
    running = True
    print("\n%%%对方轻敲了下麦克风,提醒您whoAreYou远程面试软件已打开,请点击切换一下窗口%%%")
    while running:
        # 选项系统,收纳了所有的选项,用于调用函数。

        menu_functions = {
            "介绍一下你的经历!": story,
            "你有什么经验分享给我吗？": share_experience,
            "我想测试下你的游戏开发水平": test_game_dev,
            "让我再玩一次你写的游戏!":game_again,
            "下一位": next_person,
            UI_switch_tag: UI_switch,
            tag_1: op_1,
            tag_2: op_2,
            tag_3: op_3,
            "你再想想还能写什么?": return_to_main
        }

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    current_option = (current_option - 1) % len(current_menu)
                elif event.key == pygame.K_DOWN:
                    current_option = (current_option + 1) % len(current_menu)
                elif event.key == pygame.K_RETURN:
                    menu_functions[current_menu[current_option]]()
                    
        screen.fill((0, 0, 0))
        for idx, option in enumerate(current_menu):
            color = (255, 255, 255) if idx == current_option else (100, 100, 100)
            option_surface = font.render(option, True, color)
            screen.blit(option_surface, (50, 50 + idx * 50))

        # 填充背景色
        screen.fill(black)
        # 显示图片在左下角
        screen.blit(character_image, (10, screen_height - character_image.get_height() - 10))
        # 显示第二张图片在右上角
        screen.blit(second_image, (screen_width - second_image.get_width() - 10, 10))

        # 显示中间选项系统
        for idx, option in enumerate(current_menu):
            option_surface = font.render(option, True, white if idx == current_option else (100, 100, 100))
            screen.blit(option_surface, (screen_width // 1.7 - option_surface.get_width() // 2, screen_height // 1.6 + idx * 40 - 20))

        second_image = pygame.image.load(second_image_path)
        second_image = pygame.transform.scale(second_image, (200, 200))
        #自动提行函数
        print_t(result_text)

        pygame.display.flip()
        # 退出pygame

    pygame.quit()
    sys.exit()
 
 
'''
#一些历史代码临时保存

#自动化编写模块
game_txet = game_code(client)
#print(game_txet)
extract_and_save_code(game_txet, 'extracted_game_code.py')
thread = threading.Thread(target=run_aIgame_in_cmd, args=(client,))
thread.start()
#run_aIgame_in_cmd(client)        

#下一位
result_text = "HR您好呀，我是XXX       %%%开发中%%%"
second_image_index = random.randint(1, 99)  # 生成1到99的随机数
second_image_path = os.path.join(folder_path, f"Transparent_Pixel_Art_Person_{second_image_index}.png")
second_image = pygame.image.load(second_image_path)
second_image = pygame.transform.scale(second_image, (200, 200))

#将人物信息处理
name, age, gender, background = chat_preprocessing.extract_info(wiki_human(client))
print("Name:", name)
print("Age:", age)
print("Gender:", gender)
print("Background:", background,"\n")
'''
