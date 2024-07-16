from RNG.RNG_list import random_country,random_game_element,random_Experience,random_game
import random
global _country,change_language
change_language = "英文"
#游戏核心启动随机数,不一定为程序员,可把程序员换成其他职业都行
def wAY():
    global change_language,_country
    _country = random_country()
    wAY = "国家:"+_country+",随机提供一位年龄在"+str(random.randint(1,9)*10)+"岁左右的wiki全球真实世界知名程序员,只用"+change_language+"回答,python文本结构如name=\"xxx\"age=\"xxx\"gender=\"xxx\"background=\"xxx\""
    return wAY

#生成游戏代码构造
def ai_game(A_element,B_type):
    global change_language
    ai_game = "用python生成一个"+A_element+"有关的"+B_type+"游戏,内容丰富,玩家输入数字方式交互,输入0代表游戏结束,代码UI部分为"+change_language+",回答完整代码"
    return ai_game

#美化生成后运行中的游戏的UI
def ui_game(ui_text):
    global change_language
    ui_game = "\""+ui_text+"\""+":以上为一个UI交互界面,在不改变原本UI的情况下，在后面加()进行一个"+change_language+"的内容润色并添加表情符号,只回答UI界面"
    return ui_game

#标准身份扮演
def ui_YourExperience(name,background,RNG_Experience):
    global change_language
    ui_Experience = "我们来玩一个角色扮演游戏,假装你是知名程序员"+name+",你曾经:"+background+"你有什么关于"+RNG_Experience+"的分享?回答控制在100字以内,只用"+change_language+"回答"        
    return ui_Experience

#程序菜单随机关键词代码构造
def RNG_random_game():
    global change_language
    RNG_game = "def random_game():game_types = [\""+random_game()+"\", \""+random_game()+"\", \""+random_game()+"\",  \""+random_game()+"\", \""+random_game()+"\", \""+random_game()+"\", \""+random_game()+"\", \""+random_game()+"\",\""+random_game()+"\", \""+random_game()+"\", \""+random_game()+"\", \""+random_game()+"\",] return random.choice(game_types)根据以上代码,在代码原本基础上扩写100个"+change_language+"的随机关键词内容关于游戏类型,不重复,python结构代码"
    return RNG_game

def RNG_random_game_element():
    global change_language
    RNG_element = "def random_game_element():game_elements = [\""+random_game_element()+"\", \""+random_game_element()+"\", \""+random_game_element()+"\",  \""+random_game_element()+"\", \""+random_game_element()+"\", \""+random_game_element()+"\", \""+random_game_element()+"\", \""+random_game_element()+"\",\""+random_game_element()+"\", \""+random_game_element()+"\", \""+random_game_element()+"\", \""+random_game_element()+"\",] return random.choice(game_elements)根据以上代码,在代码原本基础上扩写100个"+change_language+"的随机关键词关于游戏内容,不重复,python结构代码"
    return RNG_element

def RNG_random_Experience():
    global change_language
    RNG_Experience = "def random_Experience():game_Experience = [\""+random_Experience()+"\", \""+random_Experience()+"\", \""+random_Experience()+"\",  \""+random_Experience()+"\", \""+random_Experience()+"\", \""+random_Experience()+"\", \""+random_Experience()+"\", \""+random_Experience()+"\",\""+random_Experience()+"\", \""+random_Experience()+"\", \""+random_Experience()+"\", \""+random_Experience()+"\",] return random.choice(game_Experience)根据以上代码,在代码原本基础上扩写100个"+change_language+"的随机关键词内容,不重复,python结构代码"
    return RNG_Experience

