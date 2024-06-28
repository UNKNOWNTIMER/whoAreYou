import os
import re
import sys
import subprocess
import threading
import queue
from openai import OpenAI
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from api_llama3 import chat_preprocessing
from text_QA import QA

def create_openai_client(api_key):
    return OpenAI(
        base_url="https://integrate.api.nvidia.com/v1",
        api_key = api_key
    )
    
#游戏心脏
def generate_response(client, context):
    try:
        completion = client.chat.completions.create(
            model="meta/llama3-70b-instruct",
            messages=context,
            temperature=0.5,
            top_p=1,
            max_tokens=6000,
            stream=True
        )
        response = ""
        for chunk in completion:
            if chunk.choices[0].delta.content is not None:
                response += chunk.choices[0].delta.content
        return response
    except Exception as e:
        print(f"Error generating response: {e}")
        return "Sorry, there was an error processing your request."

#这里是调用的人物名人询问，见text/QA.py文件列表
def wiki_human(client):
    context = []
    user_input = QA.wAY()
    context.append({"role": "user", "content": user_input})
    response = generate_response(client, context)
    context.append({"role": "assistant", "content": response})
    return response 

#这里是调用的游戏程序询问
def game_code(client,A,B):
    print("\n\n%%%%%%%%%%%%%%%%%%%正在白嫖%%%%%%%%%%%%%%%%%%%\n%%%%%%%%%%%%%%%%%%%请稍等啦%%%%%%%%%%%%%%%%%%%\n%%%%%%%%%%%%%%%%%%%正在白嫖%%%%%%%%%%%%%%%%%%%\n")
    context = []
    user_input = QA.ai_game(A,B)
    context.append({"role": "user", "content": user_input})
    response = generate_response(client, context)
    context.append({"role": "assistant", "content": response})
    user_input = "给代码添加更多内容以及丰富的故事,更多的功能,玩家交互方式为输入数字,让代码完善,提供更多的用户UI交互提示"
    context.append({"role": "user", "content": user_input})
    print("\n\n%%%%%%%%%%%%%%%%%%%正在疯狂白嫖%%%%%%%%%%%%%%%%%%%\n%%%%%%%%%%%%%%%%%%%再稍等一下下%%%%%%%%%%%%%%%%%%%\n%%%%%%%%%%%%%%%%%%%正在疯狂白嫖%%%%%%%%%%%%%%%%%%%\n")
    response = generate_response(client, context)
    #context.append({"role": "assistant", "content": response})
    return response 

#打开CMD弹窗口运行程序
def enqueue_output(out, queue):
    try:
        for line in iter(out.readline, ''):
            queue.put(line)
        out.close()
    except ValueError:
        pass  # 忽略因为流关闭而引发的异常
    return 

def run_aIgame_in_cmd(client,UI_flag):

    #启动一个子进程来运行 Python 脚本，并使用线程从其标准输出中非阻塞地读取数据。
    script_path = "generated_data\\game_code\\extracted_game_code.py"
    # 启动子进程
    process = subprocess.Popen(['python', script_path], stdout=subprocess.PIPE, text=True)

    q = queue.Queue()  # 创建一个线程安全的队列
    t = threading.Thread(target=enqueue_output, args=(process.stdout, q))
    t.daemon = True  # 设置线程为守护线程，确保主线程结束时子线程也会结束
    t.start()
    
    printed_prompt = True  # 标志变量，用于跟踪是否已经打印过提示符
    uitext = ""
    flag = 0
    # 主线程持续运行，处理子进程的输出
    while True:
        if not t.is_alive() and q.empty():
            # 如果线程不再活跃并且队列为空，跳出循环
            break
        try:
            line = q.get_nowait()  # 尝试从队列中获取输出
            uitext = uitext + line
            if 1-UI_flag:
                print(line.strip())  # 打印输出，去除前后空白字符
            printed_prompt = True  # 重置提示符打印标志
        except queue.Empty:
            if  printed_prompt:
                # 队列为空时在控制台输出提示符号
                #print("^^^"+uitext,end='',flush=True)
                context = []
                if UI_flag:
                    os.system('cls')
                    print("\n\n%%%%%%%%%%%%%%%%%%%正在计算%%%%%%%%%%%%%%%%%%%\n%%%%%%%%%%%%%%%%%%%请稍稍等%%%%%%%%%%%%%%%%%%%\n%%%%%%%%%%%%%%%%%%%美化UI中%%%%%%%%%%%%%%%%%%%\n")
                    user_input = QA.ui_game(uitext)
                    context.append({"role": "user", "content": user_input})
                    response = generate_response(client, context)
                    os.system('cls')
                    print(response)
                    printed_prompt = False  # 标记已经打印过提示符，防止再次打印
                    print("\n\n输入选择数字后回车,0为退出:")                    
                uitext =""

    process.wait()  # 等待子进程结束
    os.system('cls')
    print("####哎呀!程序结束了####\n\n看来这位程序员犯了一些小错误。\n您可以回到<WhoAreYou>远程面试窗口继续面试\n对方发你的测试题我已经放到您的generated_data/game_code文件夹中了\n下次编写时会替换掉这位程序员写的代码~\n")
    return 

api_key = "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"  #程序的心脏放这里哇~API
client = create_openai_client(api_key)



    


