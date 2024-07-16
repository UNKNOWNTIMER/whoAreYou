from RNG.RNG_list import random_country,random_game_element,random_Experience,random_game
import random
global _country,change_language
change_language = "english"
# Core game startup random number, not necessarily a programmer, can replace the programmer with other professions
def wAY():
    global change_language,_country
    _country = random_country()
    wAY = "Country: "+_country+", randomly provide a globally recognized real-world programmer from Wikipedia who is approximately "+str(random.randint(1,9)*10)+" years old. Answer in "+change_language+". Python text structure as follows:name=\"xxx\"age=\"xxx\"gender=\"xxx\"background=\"xxx\""
    return wAY

# Generate game code structure
def ai_game(A_element,B_type):
    global change_language
    ai_game = "Generate a game related to "+A_element+" using Python, of type "+B_type+", with rich content. Players interact by inputting numbers, and inputting 0 ends the game. The language should be "+change_language+". Provide the complete code."
    return ai_game

# Beautify the generated game UI during runtime
def ui_game(ui_text):
    global change_language
    ui_game = "\""+ui_text+"\""+":The above is a UI interaction interface. Without changing the original UI, add content in "+change_language+" inside parentheses for a touch of refinement and add emojis. Just answer with the UI interface."
    return ui_game

# Standard role-playing
def ui_YourExperience(name,background,RNG_Experience):
    global change_language
    ui_Experience = "Let's play a role-playing game. Pretend you are the famous programmer "+name+". You have: "+background+". What can you share about "+RNG_Experience+"? Please answer within 100 words, in "+change_language+"."        
    return ui_Experience

# Program menu random keyword code construction
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

