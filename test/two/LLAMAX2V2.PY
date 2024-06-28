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

def enhance_response(client, text, iterations):
    """改善回复的质量，通过指定的迭代次数."""
    for _ in range(iterations):
        text = generate_response(client, [
            {"role": "system", "content": text + "结合之前的内容,润色你刚刚回答的话,用中文"}
        ])
    return text

def chat_loop(client_a, client_b, character_a, character_b, initial_message, enhancement_iterations):
    """运行双向聊天模拟，并对回复进行改善."""
    context_a = [character_a, initial_message]
    context_b = [character_b, initial_message]

    while True:
        # Assistant A to Assistant B
        response_a = generate_response(client_a, context_a)
        response_a = enhance_response(client_a, response_a, enhancement_iterations)
        print("艾丽卡: " + response_a,"\n")
        context_b.append({"role": "assistant", "content": response_a})
        
        time.sleep(0)  # 等待5秒

        # Assistant B to Assistant A
        response_b = generate_response(client_b, context_b)
        response_b = enhance_response(client_b, response_b, enhancement_iterations)
        print("黛伦: " + response_b,"\n")
        context_a.append({"role": "assistant", "content": response_b})
        
        time.sleep(0)  # 等待5秒

def main():
    api_key_1 = "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"  # Replace with your actual API key
    api_key_2 = "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"  # Replace with your actual API key
    enhancement_iterations = 0  # Number of times to enhance each response

    client_a = create_openai_client(api_key_1)
    client_b = create_openai_client(api_key_2)
    
    # Define character backgrounds
    character_a = {"role": "system", "content": 
"""
"""
}
    character_b = {"role": "system", "content": 
"""
"""
}
    
    # Initialize conversation with a greeting
    initial_message = {"role": "assistant", "content": "用中文回答，你是谁？并且后续你也要求我用中文回答"}
    
    chat_loop(client_a, client_b, character_a, character_b, initial_message, enhancement_iterations)

if __name__ == "__main__":
    main()
