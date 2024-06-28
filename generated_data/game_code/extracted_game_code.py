
# encoding: utf-8

# 游戏标题
print("格斗技术恐怖游戏")

# 游戏介绍
print("你是一名格斗技术高手，拥有强大的战斗力。但是，你却被困在一个恐怖的世界中。你的目标是逃脱这个世界，并揭开隐藏的秘密。")

# 游戏变量
player_health = 100
player_strength = 50
player_agility = 30
player_intelligence = 20
player_experience = 0

# 游戏场景
scenes = {
    "start": {
        "description": "你站在一个黑暗的房间中，周围都是阴影。你听到一些奇怪的声音。",
        "choices": ["1. 探索房间", "2. 等待一会儿", "3. 大喊一声", "0. 退出游戏"]
    },
    "explore_room": {
        "description": "你开始探索房间，发现了一个暗门和一个书架。",
        "choices": ["1. 打开暗门", "2. 查看书架", "3. 等待一会儿", "0. 退出游戏"]
    },
    "open_door": {
        "description": "你打开暗门，发现了一个恐怖的实验室。",
        "choices": ["1. 探索实验室", "2. 返回房间", "3. 大喊一声", "0. 退出游戏"]
    },
    "lab": {
        "description": "你看到一个恐怖的实验台，上面有一个怪物。",
        "choices": ["1. 攻击怪物", "2. 探索实验台", "3. 返回房间", "0. 退出游戏"]
    },
    "fight_monster": {
        "description": "你攻击了怪物，但它太强了。",
        "choices": ["1. 继续攻击", "2. 逃跑", "3. 使用格斗技巧", "0. 退出游戏"]
    },
    "use_martial_arts": {
        "description": "你使用了格斗技巧，攻击了怪物。",
        "choices": ["1. 继续攻击", "2. 逃跑", "3. 使用特殊技巧", "0. 退出游戏"]
    },
    "special_skill": {
        "description": "你使用了特殊技巧，击败了怪物。",
        "choices": ["1. 探索实验室", "2. 返回房间", "3. 大喊一声", "0. 退出游戏"]
    },
    "bookshelf": {
        "description": "你查看了书架，发现了一本古老的书。",
        "choices": ["1. 读取书籍", "2. 返回房间", "3. 大喊一声", "0. 退出游戏"]
    },
    "read_book": {
        "description": "你读取了书籍，发现了一个隐藏的秘密。",
        "choices": ["1. 探索实验室", "2. 返回房间", "3. 大喊一声", "0. 退出游戏"]
    },
    "hallway": {
        "description": "你来到了一个长长的走廊，看到了一扇门。",
        "choices": ["1. 打开门", "2. 探索走廊", "3. 返回房间", "0. 退出游戏"]
    },
    "door": {
        "description": "你打开了门，发现了一个新的世界。",
        "choices": ["1. 探索新世界", "2. 返回走廊", "3. 大喊一声", "0. 退出游戏"]
    },
    "new_world": {
        "description": "你来到了一个新的世界，看到了一座山。",
        "choices": ["1. 攀登山", "2. 探索周围", "3. 大喊一声", "0. 退出游戏"]
    },
    "climb_mountain": {
        "description": "你攀登了山，发现了一个隐藏的寺庙。",
        "choices": ["1. 探索寺庙", "2. 返回山脚", "3. 大喊一声", "0. 退出游戏"]
    },
    "temple": {
        "description": "你探索了寺庙，发现了一个强大的法师。",
        "choices": ["1. 攻击法师", "2. 与法师对话", "3. 返回山脚", "0. 退出游戏"]
    },
    "fight_master": {
        "description": "你攻击了法师，但它太强了。",
        "choices": ["1. 继续攻击", "2. 逃跑", "3. 使用格斗技巧", "0. 退出游戏"]
    },
    "use_martial_arts_master": {
        "description": "你使用了格斗技巧，攻击了法师。",
        "choices": ["1. 继续攻击", "2. 逃跑", "3. 使用特殊技巧", "0. 退出游戏"]
    },
    "special_skill_master": {
        "description": "你使用了特殊技巧，击败了法师。",
        "choices": ["1. 探索寺庙", "2. 返回山脚", "3. 大喊一声", "0. 退出游戏"]
    },
    "end_game": {
        "description": "你逃脱了恐怖的世界，揭开了隐藏的秘密。",
        "choices": ["0. 退出游戏"]
    }
}

# 游戏主循环
current_scene = "start"
while True:
    print("\n" + scenes[current_scene]["description"])
    for i, choice in enumerate(scenes[current_scene]["choices"]):
        print(f"{i+1}. {choice}")
    user_input = input("请输入你的选择（数字）：")
    if user_input == "0":
        print("游戏结束。")
        break
    elif user_input == "1":
        if current_scene == "start":
            current_scene = "explore_room"
        elif current_scene == "explore_room":
            current_scene = "open_door"
        elif current_scene == "open_door":
            current_scene = "lab"
        elif current_scene == "lab":
            current_scene = "fight_monster"
        elif current_scene == "fight_monster":
            current_scene = "use_martial_arts"
        elif current_scene == "use_martial_arts":
            current_scene = "special_skill"
        elif current_scene == "special_skill":
            current_scene = "hallway"
        elif current_scene == "hallway":
            current_scene = "door"
        elif current_scene == "door":
            current_scene = "new_world"
        elif current_scene == "new_world":
            current_scene = "climb_mountain"
        elif current_scene == "climb_mountain":
            current_scene = "temple"
        elif current_scene == "temple":
            current_scene = "fight_master"
        elif current_scene == "fight_master":
            current_scene = "use_martial_arts_master"
        elif current_scene == "use_martial_arts_master":
            current_scene = "special_skill_master"
        elif current_scene == "special_skill_master":
            current_scene = "end_game"
    elif user_input == "2":
        if current_scene == "start":
            current_scene = "start"
        elif current_scene == "explore_room":
            current_scene = "bookshelf"
        elif current_scene == "open_door":
            current_scene = "explore_room"
        elif current_scene == "lab":
            current_scene = "open_door"
        elif current_scene == "fight_monster":
            current_scene = "lab"
        elif current_scene == "use_martial_arts":
            current_scene = "fight_monster"
        elif current_scene == "special_skill":
            current_scene = "use_martial_arts"
        elif current_scene == "hallway":
            current_scene = "start"
        elif current_scene == "door":
            current_scene = "hallway"
        elif current_scene == "new_world":
            current_scene = "door"
        elif current_scene == "climb_mountain":
            current_scene = "new_world"
        elif current_scene == "temple":
            current_scene = "climb_mountain"
        elif current_scene == "fight_master":
            current_scene = "temple"
        elif current_scene == "use_martial_arts_master":
            current_scene = "fight_master"
        elif current_scene == "special_skill_master":
            current_scene = "use_martial_arts_master"
    elif user_input == "3":
        if current_scene == "start":
            print("你大喊了一声，但没有任何反应。")
        elif current_scene == "explore_room":
            print("你大喊了一声，但没有任何反应。")
        elif current_scene == "open_door":
            print("你大喊了一声，但没有任何反应。")
        elif current_scene == "lab":
            print("你大喊了一声，但没有任何反应。")
        elif current_scene == "fight_monster":
            print("你大喊了一声，但怪物没有任何反应。")
        elif current_scene == "use_martial_arts":
            print("你大喊了一声，但怪物没有任何反应。")
        elif current_scene == "special_skill":
            print("你大喊了一声，但没有任何反应。")
        elif current_scene == "hallway":
            print("你大喊了一声，但没有任何反应。")
        elif current_scene == "door":
            print("你大喊了一声，但没有任何反应。")
        elif current_scene == "new_world":
            print("你大喊了一声，但没有任何反应。")
        elif current_scene == "climb_mountain":
            print("你大喊了一声，但没有任何反应。")
        elif current_scene == "temple":
            print("你大喊了一声，但没有任何反应。")
        elif current_scene == "fight_master":
            print("你大喊了一声，但法师没有任何反应。")
        elif current_scene == "use_martial_arts_master":
            print("你大喊了一声，但法师没有任何反应。")
        elif current_scene == "special_skill_master":
            print("你大喊了一声，但没有任何反应。")
    else:
        print("无效的输入，请重新输入。")
