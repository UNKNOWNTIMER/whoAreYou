import re
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from text_QA import QA

#游戏代码cut
def extract_and_save_code(text, output_file):
    pattern = r"```python(.*?)```"  # 确保匹配代码块
    match = re.search(pattern, text, re.DOTALL)

    if match:
        code_block = match.group(1)
        
        # 确定文件夹路径
        folder_path = os.path.join('generated_data', 'game_code')
        # 创建文件夹如果不存在
        os.makedirs(folder_path, exist_ok=True)

        # 完整的文件路径
        full_path = os.path.join(folder_path, output_file)

        # 将提取的代码写入指定的 Python 文件
        with open(full_path, 'w', encoding='utf-8') as file:
            file.write(code_block)
        print(f"代码已保存到 {full_path}")
    else:
        print("没有找到符合条件的代码块。")
    return

#text处理
def extract_info(text):
    # 定义正则表达式，以捕捉信息
    name_pattern = r"name=\"(.*?)\""
    age_pattern = r"age=\"(.*?)\""
    gender_pattern = r"gender=\"(.*?)\""
    background_pattern = r"background=\"(.*?)\""
    
    # 使用正则表达式搜索文本
    name = re.search(name_pattern, text)
    age = re.search(age_pattern, text)
    gender = re.search(gender_pattern, text)
    background = re.search(background_pattern, text)
    
    # 提取匹配的字符串，如果没有找到匹配，则返回空字符串
    name = name.group(1) if name else "未知面试者"
    age = age.group(1) if age else "不详"
    gender = gender.group(1) if gender else "不详"
    background = background.group(1) if background else "不愿意透露你的黑客背景"
    
    return name, age, gender, background

