from RNG.RNG_list import random_country
import random
global _country,change_language
change_language = "中文"
#模型全局语言回答控制
def wAY():
    global change_language,_country
    _country = random_country()
    wAY = "国家:"+_country+",随机提供一位年龄在"+str(random.randint(1,9)*10)+"岁左右的wiki全球真实世界知名程序员,只用"+change_language+"回答,python文本结构如name=\"xxx\"age=\"xxx\"gender=\"xxx\"background=\"xxx\""
    return wAY

#代码调用语言交互
def ai_game(A_element,B_type):
    global change_language
    ai_game = "用python生成一个"+A_element+"有关的"+B_type+"游戏,内容丰富,玩家输入数字方式交互,输入0代表游戏结束,代码UI部分为"+change_language+",回答完整代码"
    return ai_game

#UI美化语言交互
def ui_game(ui_text):
    global change_language
    ui_game = "\""+ui_text+"\""+":以上为一个UI交互界面,在不改变原本UI的情况下，在后面加()进行一个"+change_language+"的内容润色并添加表情符号,只回答UI界面"
    return ui_game

#询问内容交互
def ui_YourExperience(name,background,RNG_Experience):
    global change_language
    ui_Experience = "我们来玩一个角色扮演游戏,假装你是知名程序员"+name+",你曾经:"+background+"你有什么关于"+RNG_Experience+"的分享?回答控制在100字以内,只用"+change_language+"回答"        
    return ui_Experience