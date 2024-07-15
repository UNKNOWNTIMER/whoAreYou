import pygame
import threading
import sys
import os
import time
import random
from RNG.RNG_list import random_game,random_game_element,random_Experience
from api_llama3.chat_preprocessing import extract_and_save_code,extract_info,save_program
from api_llama3.engine_llama3 import client,run_aIgame_in_cmd,game_code,wiki_human,Experience_code,C_RNG_random_game,C_RNG_element,C_RNG_Experience
from RNG.pixelMan import create_pixel_person
from text_QA import QA
#通过LLM构建库,重构新的RNG
def main_menu():
    global RNG_Experience,flag_menu
    flag_menu = 1
    return ["让我瞧瞧你的推荐信!", "你有关于"+RNG_Experience+"内容分享给我吗?", "我想测试下你的游戏开发水平","让我再玩一次你写的游戏!", "下一位"]

def UI_switch():
    global UI_flag,UI_switch_tag,current_menu, current_option,voice_p
    #是否将LLM生成的小游戏的UI也接入大模型。开关
    UI_flag = 1 - UI_flag
    if  UI_flag:
        play_music("coffeeTime_loop")
        UI_switch_tag = "等下测试时不要美化UI!"
        voice_p.stop()
        play_voice("UIon")
        print_t("嗯,我会让UI变得好看~")
        current_menu = main_menu()
        current_option = 0
    else:
        play_music("coffeeTime_loop")
        UI_switch_tag = "测试时记得美化UI!"
        voice_p.stop()
        play_voice("UIoff")
        print_t("好的,我不会去美化UI的")
        current_menu = main_menu()
        current_option = 0
    return
    
def game_again():
    global game_flag,voice_p,UI_flag
    voice_p.stop()
    if not UI_flag or not game_flag:
        play_voice("again")
    if not game_flag:
        print_t("哎?我还什么都没写呢")
    else:
        print_t("好滴!请您查看终端窗口")
        play_music("gameTime_loop")
        thread = threading.Thread(target=run_aIgame_in_cmd, args=(client,UI_flag))
        thread.start()
    return

def game_dev_menu():
    global tag_1,tag_2,tag_3,RNG_Experience,random_game_element2,random_game_type2,random_game_element3,random_game_type3,flag_menu
    flag_menu = 0
    #刷新
    tag_1 = "既然你对"+RNG_Experience+"很有了解,那么编写一个和它相关的游戏吧!"
    tag_2 = "测试一下你"+random_game_element2+"有关的"+random_game_type2+"类型游戏编写..."
    tag_3 = "那你能帮我写一个"+random_game_element3+"有关的"+random_game_type3+"类型游戏吗?"
    return [UI_switch_tag,tag_1, tag_2, tag_3, "你再想想还能写什么?"]
#讲述故事模块

def story():
    global background,voice_p
    voice_p.stop()
    play_voice("Describe")
    print_t("你打开了像素推荐信,上面赫然写着:             "+background)
    return

#作为这个程序员分享经验
def share_experience():
    global voice_p,client,game_Experience
    voice_p.stop()
    play_voice("showme")
    print_t(game_Experience)
    return
#程序生成程序代码选择1
def op_1():
    global voice_p,game_flag
    voice_p.stop()
    play_music("gameTime_loop")
    global client,RNG_Experience,random_game_type1,UI_flag,game_flag
    print_t("我写了一个关于"+RNG_Experience+"的游戏代码,发送到你的终端了")
    game_flag = 1
    game_txet = game_code(client,RNG_Experience,random_game_type1)
    extract_and_save_code(game_txet, 'extracted_game_code.py')
    thread = threading.Thread(target=run_aIgame_in_cmd, args=(client,UI_flag))
    thread.start() 
    return
#程序生成程序代码选择2
def op_2():
    global voice_p,game_flag
    voice_p.stop()
    play_music("gameTime_loop")
    global client,random_game_element2,random_game_type2,UI_flag
    print_t("这是一个"+random_game_type2+"类型的游戏测试,您过目")
    game_flag = 1
    game_txet = game_code(client,random_game_element2,random_game_type2)
    extract_and_save_code(game_txet, 'extracted_game_code.py')
    thread = threading.Thread(target=run_aIgame_in_cmd, args=(client,UI_flag))
    thread.start()
    return
#程序生成程序代码选择3
def op_3():
    global voice_p,game_flag
    voice_p.stop()
    play_music("gameTime_loop")
    global client,random_game_element3,random_game_type3,UI_flag
    print_t("关于"+random_game_type3+"?那可是我的拿手好戏!")
    game_flag = 1
    game_txet = game_code(client,random_game_element3,random_game_type3)
    extract_and_save_code(game_txet, 'extracted_game_code.py')
    thread = threading.Thread(target=run_aIgame_in_cmd, args=(client,UI_flag))
    thread.start()
    return

#返回菜单
def return_to_main():
    global current_menu, current_option, tag_1, tag_2, tag_3,random_game_type1,random_game_type2,random_game_type3
    global RNG_Experience,random_game_element2,random_game_element3,voice_p,loge_7,loge_8
    current_menu = main_menu()
    current_option = 0
    play_music("coffeeTime_loop")
    voice_p.stop()
    play_voice("interested")
    print_t("好吧,您再看看有什么感兴趣的内容")
    random_game_type1 = random_game()
    random_game_type2 = random_game()
    random_game_type3 = random_game()
    random_game_element2 = random_game_element()
    random_game_element3 = random_game_element()
    loge_7 = pygame.image.load('background\\Skillicon\\L ('+str(random.randint(0,32))+').png')
    loge_8 = pygame.image.load('background\\Skillicon\\L ('+str(random.randint(0,32))+').png')
    return
#二级菜单，LLM游戏开发选择
def test_game_dev():
    global current_menu, current_option,voice_p,name
    current_menu = game_dev_menu()
    play_music("menu_loop")
    voice_p.stop()
    play_voice("test")
    print_t(name+"透过那为数不多的像素眼睛看着你,满脸期待...")
    current_option = 0
    return
#下一位面试者
def next_person():
    global second_image_path,result_text,name,age,gender,background,game_flag,b_image,voice_p,RNG_Experience
    global current_menu,game_Experience,loge_1
    os.system('cls')
    voice_p.stop()
    play_voice("next")
    print("###"+name+"退出了面试软件###\n###正在建立下一位面试者的连接中,请稍等###\n\n虽然"+name+"面无表情,但是你还是从他30X30的像素脸庞上捕捉到了一丝不甘")
    name, age, gender, background = extract_info(wiki_human(client))
    print_t ("您好呀，我是"+name+",来自"+QA._country+",今年"+age+"岁")
    RNG_Experience = random_Experience()
    #调用模型中生成的人物再生成回答
    game_Experience = Experience_code(client,name,background,RNG_Experience)
    second_image_index = random.randint(0, 99)  # 生成1到99的随机数
    second_image_path = os.path.join(folder_path, f"Transparent_Pixel_Art_Person_{second_image_index}.png")
    b_image = pygame.image.load('background\\BG\\BG_'+str(random.randint(0,7))+'.png') 
    loge_1 = pygame.image.load('background\\Skillicon\\L ('+str(random.randint(0,32))+').png')
    game_flag = 0
    current_menu = main_menu()
    return  
#用来控制pygame打印对话
def print_t(result_t):
    global result_text
    result_text = result_t
    text_lines = wrap_text(result_text, 26)
    y_offset = 10  #行间距控制
    for line in text_lines:
        text_surface = font.render(line, True, (255, 255, 255))
        screen.blit(text_surface, (50, y_offset))
        y_offset += font.get_linesize()
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

#BGM控制函数
def play_music(music_file):
    # 停止
    pygame.mixer.music.stop()
    # 加载
    pygame.mixer.music.load("music\\"+music_file+".mp3")
    # 播放
    pygame.mixer.music.play(-1)
    return
    
#播放角色语音
def play_voice(voice_file):
    global voice_p
    # 不同的语音读取
    voice_p = pygame.mixer.Sound("music\\voice\\"+voice_file+"_"+str(random.randint(0,2))+".wav")
    # 播放！播放！！
    voice_p.play()
    
    return

if __name__ == "__main__":
    
    #这一块为全局变量,反正都用python了,程序体量也不大,就不节约内存了直接摆~嘿嘿O(∩_∩)O
    global current_menu, current_option,tag_1,tag_2,tag_3,name, age, gender, background,second_image_path,result_text,random_game_type1,random_game_type2,random_game_type3
    global text_lines,random_game_element1,random_game_element2,random_game_element3,b_image
    global UI_flag,UI_switch_tag,game_flag,button0,button1,voice_p
    global game_Experience,RNG_Experience
    global loge_0,loge_1,loge_2,loge_3,loge_4,loge_5,loge_7,loge_8,loge_9,flag_menu,character_image,face_image,f_out
    f_out = 0
    
    #生成真RNG主程序调用,每个程序会调用4次,因为我觉得不太稳定所以暂时不启用,如果真有人感兴趣我再更新
    '''
    while not os.path.exists("generated_data/generated_RNG_type/RNG_random_game.py"):
        save_program(C_RNG_random_game(client), 'RNG_random_game.py')
        time.sleep(1)
        f_out += 1 
        if os.path.exists("generated_data/generated_RNG_type/RNG_random_game.py") or f_out == 4:
            print("File has been successfully created.")
            break
    f_out = 0      
    while not os.path.exists("generated_data/generated_RNG_type/RNG_random_game_element.py"):
        save_program(C_RNG_element(client), 'RNG_random_game_element.py')
        time.sleep(1)
        f_out += 1
        if os.path.exists("generated_data/generated_RNG_type/RNG_random_game_element.py" or f_out == 4):
            print("File has been successfully created.")
            break
    f_out = 0
    while not os.path.exists("generated_data/generated_RNG_type/RNG_random_Experience.py"):
        save_program(C_RNG_Experience(client), 'RNG_random_Experience.py')
        time.sleep(1) 
        f_out += 1
        if os.path.exists("generated_data/generated_RNG_type/RNG_random_Experience.py" or f_out == 4):
            print("File has been successfully created.")
            break
            
    #生成的代码导入程序
    from  generated_data.generated_RNG_type.RNG_random_game import random_game
    from  generated_data.generated_RNG_type.RNG_random_game_element import random_game_element
    from  generated_data.generated_RNG_type.RNG_random_Experience import random_Experience
    '''
    
    #清理掉启动信息   
    os.system('cls')
    print("\n%%%%%%%%%%%%%%%%%%%对方正在远程连接中%%%%%%%%%%%%%%%%%%%")
    #调用模型中生成的人物信息
    name, age, gender, background = extract_info(wiki_human(client))
    #调用随机参数保存
    RNG_Experience = random_Experience()
    #调用模型中生成的人物再生成回答
    game_Experience = Experience_code(client,name,background,RNG_Experience)
    #初始化全局设置开关
    UI_flag = 1#是否启用LLM用于美化LLM模型写的程序
    flag_menu = 1#检查是在主菜单还是子菜单
    game_flag = 0#检查是否生成了extrated_game_code.py游戏代码文件
    
    # 初始化pygame
    pygame.init()
    pygame.mixer.init()
    
    # 设置pygame窗口为无边框
    #flags = pygame.NOFRAME
    #边框大小
    screen_width = 800
    screen_height = 500
    #初始化图像
    icon = pygame.image.load('background\\TIMER.png')
    b_image = pygame.image.load('background\\BG\\BG_'+str(random.randint(0,7))+'.png') 
    loge_0 = pygame.image.load('background\\Skillicon\\L_M00.png')
    loge_1 = pygame.image.load('background\\Skillicon\\L ('+str(random.randint(0,32))+').png')
    loge_2 = pygame.image.load('background\\Skillicon\\L_M02.png')
    loge_3 = pygame.image.load('background\\Skillicon\\L_M03.png')
    loge_4 = pygame.image.load('background\\Skillicon\\L_M04.png')
    loge_5 = pygame.image.load('background\\Skillicon\\L_M05.png')
    loge_7 = pygame.image.load('background\\Skillicon\\L ('+str(random.randint(0,32))+').png')
    loge_8 = pygame.image.load('background\\Skillicon\\L ('+str(random.randint(0,32))+').png')
    loge_9 = pygame.image.load('background\\Skillicon\L_M01.png')
    #logo TIMER
    pygame.display.set_icon(icon)
    #屏幕初始化
    screen = pygame.display.set_mode((screen_width, screen_height))#,flags)
    # 设置窗口标题
    pygame.display.set_caption('WhoAreYou')
    
    # 设置颜色
    black = (0, 0, 0)
    white = (255, 255, 255)
    # 加载字体，指定黑体
    font_path = 'text_QA\\hzk-pixel-12px.ttf'  # Windows中黑体的典型路径
    font = pygame.font.Font(font_path, 24)   # pixelMan初始化运行，文件夹路径
    #初始化音乐
    play_music("coffeeTime_loop")
    button0 = pygame.mixer.Sound("music/button/down_up.wav")
    button1 = pygame.mixer.Sound("music/button/enter.wav")
    #像素人生成检察
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
    character_image = pygame.image.load('background\\Eily\\body\\Eily_body_'+str(random.randint(0,19))+'.png')
    character_image = pygame.transform.scale(character_image, (200, 200))  # 调整图片大小
    face_image = pygame.image.load('background\\Eily\\face\\Eily_face_'+str(random.randint(0,19))+'.png')
    face_image = pygame.transform.scale(face_image, (200, 200))  # 调整图片大小
    # 随机加载第二张图片
    second_image_index = random.randint(0, 99)  # 生成1到99的随机数
    second_image_path = os.path.join(folder_path, f"Transparent_Pixel_Art_Person_{second_image_index}.png")
    second_image = pygame.image.load(second_image_path)
    second_image = pygame.transform.scale(second_image, (200, 200))
    #初始化子选项
    random_game_type1 = random_game()
    random_game_type2 = random_game()
    random_game_type3 = random_game()
    random_game_element2 = random_game_element()
    random_game_element3 = random_game_element()
    tag_1 = "既然你对"+RNG_Experience+"很有了解,那么编写一个和它相关的游戏吧!"
    tag_2 = "测试一下你"+random_game_element2+"有关的"+random_game_type2+"类型游戏编写..."
    tag_3 = "那你能帮我写一个"+random_game_element3+"有关的"+random_game_type3+"类型游戏吗?"
    UI_switch_tag = "记得测试时不要美化UI!"
    # 显示结果的文本
    result_text ="您好呀，我是"+name+",来自"+QA._country+",今年"+age+"岁"
    current_menu = main_menu()
    current_option = 0
    running = True
    print("\n%%%对方轻敲了下麦克风,提醒您whoAreYou远程面试软件已打开,请点击切换一下窗口%%%")
    play_voice("hello")
    while running:
        # 选项系统,收纳了所有的选项,用于调用函数。
        menu_functions = {
            "让我瞧瞧你的推荐信!": story,
            "你有关于"+RNG_Experience+"内容分享给我吗?": share_experience,
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
                    current_option = (current_option - 1) % len(current_menu) #上?
                    button0.play()
                elif event.key == pygame.K_DOWN:
                    current_option = (current_option + 1) % len(current_menu) #下！
                    button0.play()
                elif event.key == pygame.K_RETURN:
                    menu_functions[current_menu[current_option]]() #回车
                    button1.play()
                    #刷新角色
                    character_image = pygame.image.load('background\\Eily\\body\\Eily_body_'+str(random.randint(0,19))+'.png')
                    character_image = pygame.transform.scale(character_image, (200, 200))  # 调整图片大小
                    face_image = pygame.image.load('background\\Eily\\face\\Eily_face_'+str(random.randint(0,19))+'.png')
                    face_image = pygame.transform.scale(face_image, (200, 200))  # 调整图片大小
                elif event.key == pygame.K_ESCAPE:  # 按 ESC 键退出
                    running = False          
        screen.fill((0, 0, 0))
        for idx, option in enumerate(current_menu):
            color = (255, 255, 255) if idx == current_option else (100, 100, 100)
            option_surface = font.render(option, True, color)
            screen.blit(option_surface, (50, 50 + idx * 50))
        # 填充背景色
        screen.fill(black)
        screen.blit(b_image,(0, 0))
        if flag_menu:
            if current_option == 0:
                screen.blit(loge_0,(320, 288))
            elif current_option == 1:
                screen.blit(loge_1,(245, 328))
            elif current_option == 2:
                screen.blit(loge_2,(275, 368))
            elif current_option == 3:
                screen.blit(loge_3,(293, 408))
            elif current_option == 4:
                screen.blit(loge_4,(394, 448))
        else:
            if current_option == 0:
                screen.blit(loge_5,(307, 288))
            elif current_option == 1:                
                screen.blit(loge_1,(140, 288))
            elif current_option == 2:                
                screen.blit(loge_7,(140, 368))
            elif current_option == 3:                
                screen.blit(loge_8,(120, 408))
            elif current_option == 4:                
                screen.blit(loge_9,(321, 448))
        #身体与脸的显示
        screen.blit(character_image, (0, screen_height - character_image.get_height() - 10))
        #哈哈,面部抖动表情,要是不喜欢就移除random.randint(-3,3)吧~
        screen.blit(face_image, (random.randint(-3,3), screen_height - face_image.get_height() - 10))
        # 生成角色在右上角
        screen.blit(second_image, (screen_width - second_image.get_width() + 20, 20))
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