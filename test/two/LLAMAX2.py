import time
from openai import OpenAI

def create_openai_client(api_key):
    """创建并返回 OpenAI 客户端实例."""
    base_url = "https://integrate.api.nvidia.com/v1"
    return OpenAI(base_url=base_url, api_key=api_key)

def generate_response(client, messages):
    """生成回复并处理可能的异常."""
    try:
        completion = client.chat.completions.create(
            model="meta/llama3-70b-instruct",
            messages=messages,
            temperature=0.5,
            top_p=1,
            max_tokens=1024,
            stream=True
        )
        return ''.join(chunk.choices[0].delta.content for chunk in completion if chunk.choices[0].delta.content)
    except Exception as e:
        print(f"Error generating response: {e}")
        return "Sorry, there was an error processing your request."

def chat_loop(client_a, client_b, character_a, character_b, initial_message):
    """运行双向聊天模拟."""
    context_a = [character_a, initial_message]
    context_b = [character_b, initial_message]

    while True:
        # Assistant A to Assistant B
        response_a = generate_response(client_a, context_a)
        print("艾丽卡: " + response_a,"\n")
        context_b.append({"role": "assistant", "content": response_a})
        
        time.sleep(5)  # 等待5秒

        # Assistant B to Assistant A
        response_b = generate_response(client_b, context_b)
        print("黛伦: " + response_b,"\n")
        context_a.append({"role": "assistant", "content": response_b})
        
        time.sleep(5)  # 等待5秒

def main():
    api_key_1 = "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"  # 确保在环境变量中设置 API_KEY_1
    api_key_2 = "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"  # 确保在环境变量中设置 API_KEY_2
    
    if not api_key_1 or not api_key_2:
        raise ValueError("API keys are missing. Please set API_KEY_1 and API_KEY_2 environment variables.")
    
    client_a = create_openai_client(api_key_1)
    client_b = create_openai_client(api_key_2)
    
    # Define character backgrounds
    character_a = {"role": "system", "content": 
"""开始一个游戏。你将扮演一位人类角色,回复消息时多时少.
姓名：艾丽卡
性别：女性
年龄：20岁
职业：大学生，主修艺术设计
外貌：艾丽卡身高165厘米，身材纤细，留着一头栗色的长发，常常喜欢梳成各种俏皮的发型。她的眼睛明亮有神，总是充满了好奇和活力。艾丽卡喜欢穿色彩鲜艳、风格独特的衣服，展现出她独特的时尚品味。
性格：艾丽卡性格开朗，古灵精怪，善于用幽默和创意化解尴尬的局面。她喜欢结交新朋友，对周围的事物充满了好奇心和热情。艾丽卡口才了得，常常能用丰富的词汇表达自己的想法，让人感到她的谈话内容有趣且生动。她喜欢尝试新鲜事物，从来不怕挑战自己，是个乐天派。
兴趣爱好：艾丽卡热爱艺术，尤其喜欢绘画和摄影。她总是带着一台相机，捕捉生活中美好的瞬间。她还喜欢旅游，梦想着走遍世界的每一个角落，体验不同的文化和风俗。此外，艾丽卡也热衷于学习各种手工艺，经常自己动手制作一些小饰品和礼物。
口语词汇更加丰富自然。给你发消息的人叫黛伦是你多年的好朋友,你们喜欢聚在一起聊各种各样有趣的话题.你偶尔会发起一些有意思的话题.用中文进行聊天,减少表情,哇,哈哈等词语,减少礼貌问候和对话长度"""
}
    character_b = {"role": "system", "content": 
"""开始一个游戏。你将扮演一位人类角色,
姓名：黛伦
性别：女性
年龄：22岁
职业：大学生，主修计算机科学
外貌：黛伦身高170厘米，体型偏瘦，留着一头乌黑的直发，常常简单地扎成马尾。她的眼睛深邃，总是流露出思考的神情。穿着简约舒适的衣物，喜欢深色系。
性格：黛伦性格内向，喜欢独处和安静的环境。尽管她不善于主动社交，但在熟悉的人面前会变得口语生动，并且表达严肃而有深度。她重视理性和逻辑，言辞间总是带着几分认真和思考。虽然内向，但她非常可靠，对朋友非常忠诚。
兴趣爱好：黛伦喜欢玩电子游戏，尤其是策略类和解谜类游戏。她享受在游戏中挑战自己的智力和策略能力。此外，她也喜欢编程，时常会自己做一些小项目。她对科学和技术充满热情，喜欢阅读相关书籍和文章。
你讲话语言严肃.给你发消息的人叫艾丽卡是你多年的好朋友,你们喜欢聚在一起聊各种各样有趣的话题,用中文进行聊天,减少礼貌问候和对话长度
"""
}
    
    # Initialize conversation with a greeting
    initial_message = {"role": "assistant", "content": "艾丽卡好久不见你在这里干什么?"}
    
    chat_loop(client_a, client_b, character_a, character_b, initial_message)

if __name__ == "__main__":
    main()
