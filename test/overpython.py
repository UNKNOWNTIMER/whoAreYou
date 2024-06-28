def UI_switch():
    global UI_flag
    if UI_flag:
        print(UI_flag)
        UI_flag = 0
    else:
        print(UI_flag)
        UI_flag = 1
    return
global UI_flag
UI_flag =1
while 1:
    UI_switch()