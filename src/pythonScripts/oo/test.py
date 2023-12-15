# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def get_turn_list(serial):
    turn_list = []
    for times in range(0, 4000):
        turn_list.append(times / 4000)
    calculated_turn_list = []
    if serial == 1:
        calculated_turn_list = turn_list[0:4000]
    if serial == 2:
        calculated_turn_list = turn_list[333:4000] + turn_list[0:333]
    if serial == 3:
        calculated_turn_list = turn_list[666:4000] + turn_list[0:666]
    if serial == 4:
        calculated_turn_list = turn_list[1000:4000] + turn_list[0:1000]
    if serial == 5:
        calculated_turn_list = turn_list[1333:4000] + turn_list[0:1333]
    if serial == 6:
        calculated_turn_list = turn_list[1666:4000] + turn_list[0:1666]
    if serial == 7:
        calculated_turn_list = turn_list[2000:4000] + turn_list[0:2000]
    if serial == 8:
        calculated_turn_list = turn_list[2333:4000] + turn_list[0:2333]
    if serial == 9:
        calculated_turn_list = turn_list[2666:4000] + turn_list[0:2666]
    if serial == 10:
        calculated_turn_list = turn_list[3000:4000] + turn_list[0:3000]
    if serial == 11:
        calculated_turn_list = turn_list[3333:4000] + turn_list[0:3333]
    if serial == 12:
        calculated_turn_list = turn_list[3666:4000] + turn_list[0:3666]
    return calculated_turn_list

def get_scale_list(serial):
    scale_list = []
    for times in range(0, 4000):
        if times < 2000:
            scale_list.append(times / 2000 * 0.4)
        else:
            scale_list.append((1 - ((times - 2000) / 2000)) * 0.4)

    scale_list = [value + 0.8 for value in scale_list]

    calculated_scale_list = []
    if serial == 11:
        calculated_scale_list = scale_list[0:4000]
    if serial == 12:
        calculated_scale_list = scale_list[333:4000] + scale_list[0:333]
    if serial == 1:
        calculated_scale_list = scale_list[666:4000] + scale_list[0:666]
    if serial == 2:
        calculated_scale_list = scale_list[1000:4000] + scale_list[0:1000]
    if serial == 3:
        calculated_scale_list = scale_list[1333:4000] + scale_list[0:1333]
    if serial == 4:
        calculated_scale_list = scale_list[1666:4000] + scale_list[0:1666]
    if serial == 5:
        calculated_scale_list = scale_list[2000:4000] + scale_list[0:2000]
    if serial == 6:
        calculated_scale_list = scale_list[2333:4000] + scale_list[0:2333]
    if serial == 7:
        calculated_scale_list = scale_list[2666:4000] + scale_list[0:2666]
    if serial == 8:
        calculated_scale_list = scale_list[3000:4000] + scale_list[0:3000]
    if serial == 9:
        calculated_scale_list = scale_list[3333:4000] + scale_list[0:3333]
    if serial == 10:
        calculated_scale_list = scale_list[3666:4000] + scale_list[0:3666]
    return calculated_scale_list

def gen_animation(serial, animation_text):
    times_list = []
    percent_list = []
    for times in range(0, 4000):
        times_list.append(times)
        percent_list.append(times / 4000 * 100)
    # 1 备品备件 —> 1
    if serial == 1:
        animation_text += "@keyframes ellipse_pic1 {"
        calculated_turn_list = get_turn_list(1)
        calculated_scale_list = get_scale_list(1)
        for times in times_list:
            animation_text += f'''
  {percent_list[times]}% {{
    transform: translateX(calc(320% * cos({calculated_turn_list[times]}turn) + 10% * cos(5 * {calculated_turn_list[times]}turn) + 6% * cos(7 * {calculated_turn_list[times]}turn) + 3% * cos(13 * {calculated_turn_list[times]}turn)))
      translateY(calc(105% * sin({calculated_turn_list[times]}turn) + 20% * sin(2 * {calculated_turn_list[times]}turn) + 15% * sin(3 * {calculated_turn_list[times]}turn) + 10% * sin(7 * {calculated_turn_list[times]}turn)))
      scale({calculated_scale_list[times]});
  }}
'''
        animation_text += f'''
  {100}% {{
    transform: translateX(calc(320% * cos({calculated_turn_list[0]}turn) + 10% * cos(5 * {calculated_turn_list[0]}turn) + 6% * cos(7 * {calculated_turn_list[0]}turn) + 3% * cos(13 * {calculated_turn_list[0]}turn)))
      translateY(calc(105% * sin({calculated_turn_list[0]}turn) + 20% * sin(2 * {calculated_turn_list[0]}turn) + 15% * sin(3 * {calculated_turn_list[0]}turn) + 10% * sin(7 * {calculated_turn_list[0]}turn)));
  }}
'''
    # 12 安全管控 —> 2
    if serial == 2:
        animation_text += "@keyframes ellipse_pic2 {"
        calculated_turn_list = get_turn_list(12)
        calculated_scale_list = get_scale_list(12)
        for times in times_list:
            animation_text += f'''
  {percent_list[times]}% {{
    transform: translateX(calc(320% * cos({calculated_turn_list[times]}turn) + 10% * cos(5 * {calculated_turn_list[times]}turn) + 6% * cos(7 * {calculated_turn_list[times]}turn) + 3% * cos(13 * {calculated_turn_list[times]}turn)))
      translateY(calc(105% * sin({calculated_turn_list[times]}turn) + 20% * sin(2 * {calculated_turn_list[times]}turn) + 15% * sin(3 * {calculated_turn_list[times]}turn) + 10% * sin(7 * {calculated_turn_list[times]}turn)))
      scale({calculated_scale_list[times]});
  }}
'''
        animation_text += f'''
  {100}% {{
    transform: translateX(calc(320% * cos({calculated_turn_list[0]}turn) + 10% * cos(5 * {calculated_turn_list[0]}turn) + 6% * cos(7 * {calculated_turn_list[0]}turn) + 3% * cos(13 * {calculated_turn_list[0]}turn)))
      translateY(calc(105% * sin({calculated_turn_list[0]}turn) + 20% * sin(2 * {calculated_turn_list[0]}turn) + 15% * sin(3 * {calculated_turn_list[0]}turn) + 10% * sin(7 * {calculated_turn_list[0]}turn)));
  }}
'''
    # 11 采购管理 —> 3
    if serial == 3:
        animation_text += "@keyframes ellipse_pic3 {"
        calculated_turn_list = get_turn_list(11)
        calculated_scale_list = get_scale_list(11)
        for times in times_list:
            animation_text += f'''
  {percent_list[times]}% {{
    transform: translateX(calc(320% * cos({calculated_turn_list[times]}turn) + 10% * cos(5 * {calculated_turn_list[times]}turn) + 6% * cos(7 * {calculated_turn_list[times]}turn) + 3% * cos(13 * {calculated_turn_list[times]}turn)))
      translateY(calc(105% * sin({calculated_turn_list[times]}turn) + 20% * sin(2 * {calculated_turn_list[times]}turn) + 15% * sin(3 * {calculated_turn_list[times]}turn) + 10% * sin(7 * {calculated_turn_list[times]}turn)))
      scale({calculated_scale_list[times]});
  }}
'''
        animation_text += f'''
  {100}% {{
    transform: translateX(calc(320% * cos({calculated_turn_list[0]}turn) + 10% * cos(5 * {calculated_turn_list[0]}turn) + 6% * cos(7 * {calculated_turn_list[0]}turn) + 3% * cos(13 * {calculated_turn_list[0]}turn)))
      translateY(calc(105% * sin({calculated_turn_list[0]}turn) + 20% * sin(2 * {calculated_turn_list[0]}turn) + 15% * sin(3 * {calculated_turn_list[0]}turn) + 10% * sin(7 * {calculated_turn_list[0]}turn)));
  }}
'''
    # 10 作业票管理 —> 4
    if serial == 4:
        animation_text += "@keyframes ellipse_pic4 {"
        calculated_turn_list = get_turn_list(10)
        calculated_scale_list = get_scale_list(10)
        for times in times_list:
            animation_text += f'''
  {percent_list[times]}% {{
    transform: translateX(calc(320% * cos({calculated_turn_list[times]}turn) + 10% * cos(5 * {calculated_turn_list[times]}turn) + 6% * cos(7 * {calculated_turn_list[times]}turn) + 3% * cos(13 * {calculated_turn_list[times]}turn)))
      translateY(calc(105% * sin({calculated_turn_list[times]}turn) + 20% * sin(2 * {calculated_turn_list[times]}turn) + 15% * sin(3 * {calculated_turn_list[times]}turn) + 10% * sin(7 * {calculated_turn_list[times]}turn)))
      scale({calculated_scale_list[times]});
  }}
'''
        animation_text += f'''
  {100}% {{
    transform: translateX(calc(320% * cos({calculated_turn_list[0]}turn) + 10% * cos(5 * {calculated_turn_list[0]}turn) + 6% * cos(7 * {calculated_turn_list[0]}turn) + 3% * cos(13 * {calculated_turn_list[0]}turn)))
      translateY(calc(105% * sin({calculated_turn_list[0]}turn) + 20% * sin(2 * {calculated_turn_list[0]}turn) + 15% * sin(3 * {calculated_turn_list[0]}turn) + 10% * sin(7 * {calculated_turn_list[0]}turn)));
  }}
'''
    # 9 设备保养 —> 5
    if serial == 5:
        animation_text += "@keyframes ellipse_pic5 {"
        calculated_turn_list = get_turn_list(9)
        calculated_scale_list = get_scale_list(9)
        for times in times_list:
            animation_text += f'''
  {percent_list[times]}% {{
    transform: translateX(calc(320% * cos({calculated_turn_list[times]}turn) + 10% * cos(5 * {calculated_turn_list[times]}turn) + 6% * cos(7 * {calculated_turn_list[times]}turn) + 3% * cos(13 * {calculated_turn_list[times]}turn)))
      translateY(calc(105% * sin({calculated_turn_list[times]}turn) + 20% * sin(2 * {calculated_turn_list[times]}turn) + 15% * sin(3 * {calculated_turn_list[times]}turn) + 10% * sin(7 * {calculated_turn_list[times]}turn)))
      scale({calculated_scale_list[times]});
  }}
'''
        animation_text += f'''
  {100}% {{
    transform: translateX(calc(320% * cos({calculated_turn_list[0]}turn) + 10% * cos(5 * {calculated_turn_list[0]}turn) + 6% * cos(7 * {calculated_turn_list[0]}turn) + 3% * cos(13 * {calculated_turn_list[0]}turn)))
      translateY(calc(105% * sin({calculated_turn_list[0]}turn) + 20% * sin(2 * {calculated_turn_list[0]}turn) + 15% * sin(3 * {calculated_turn_list[0]}turn) + 10% * sin(7 * {calculated_turn_list[0]}turn)));
  }}
'''
    # 8 设备维修 —> 6
    if serial == 6:
        animation_text += "@keyframes ellipse_pic6 {"
        calculated_turn_list = get_turn_list(8)
        calculated_scale_list = get_scale_list(8)
        for times in times_list:
            animation_text += f'''
  {percent_list[times]}% {{
    transform: translateX(calc(320% * cos({calculated_turn_list[times]}turn) + 10% * cos(5 * {calculated_turn_list[times]}turn) + 6% * cos(7 * {calculated_turn_list[times]}turn) + 3% * cos(13 * {calculated_turn_list[times]}turn)))
      translateY(calc(105% * sin({calculated_turn_list[times]}turn) + 20% * sin(2 * {calculated_turn_list[times]}turn) + 15% * sin(3 * {calculated_turn_list[times]}turn) + 10% * sin(7 * {calculated_turn_list[times]}turn)))
      scale({calculated_scale_list[times]});
  }}
'''
        animation_text += f'''
  {100}% {{
    transform: translateX(calc(320% * cos({calculated_turn_list[0]}turn) + 10% * cos(5 * {calculated_turn_list[0]}turn) + 6% * cos(7 * {calculated_turn_list[0]}turn) + 3% * cos(13 * {calculated_turn_list[0]}turn)))
      translateY(calc(105% * sin({calculated_turn_list[0]}turn) + 20% * sin(2 * {calculated_turn_list[0]}turn) + 15% * sin(3 * {calculated_turn_list[0]}turn) + 10% * sin(7 * {calculated_turn_list[0]}turn)));
  }}
'''
    # 7 故障检测 —> 7
    if serial == 7:
        animation_text += "@keyframes ellipse_pic7 {"
        calculated_turn_list = get_turn_list(7)
        calculated_scale_list = get_scale_list(7)
        for times in times_list:
            animation_text += f'''
  {percent_list[times]}% {{
    transform: translateX(calc(320% * cos({calculated_turn_list[times]}turn) + 10% * cos(5 * {calculated_turn_list[times]}turn) + 6% * cos(7 * {calculated_turn_list[times]}turn) + 3% * cos(13 * {calculated_turn_list[times]}turn)))
      translateY(calc(105% * sin({calculated_turn_list[times]}turn) + 20% * sin(2 * {calculated_turn_list[times]}turn) + 15% * sin(3 * {calculated_turn_list[times]}turn) + 10% * sin(7 * {calculated_turn_list[times]}turn)))
      scale({calculated_scale_list[times]});
  }}
'''
        animation_text += f'''
  {100}% {{
    transform: translateX(calc(320% * cos({calculated_turn_list[0]}turn) + 10% * cos(5 * {calculated_turn_list[0]}turn) + 6% * cos(7 * {calculated_turn_list[0]}turn) + 3% * cos(13 * {calculated_turn_list[0]}turn)))
      translateY(calc(105% * sin({calculated_turn_list[0]}turn) + 20% * sin(2 * {calculated_turn_list[0]}turn) + 15% * sin(3 * {calculated_turn_list[0]}turn) + 10% * sin(7 * {calculated_turn_list[0]}turn)));
  }}
'''
    # 6 系统管理 —> 8
    if serial == 8:
        animation_text += "@keyframes ellipse_pic8 {"
        calculated_turn_list = get_turn_list(6)
        calculated_scale_list = get_scale_list(6)
        for times in times_list:
            animation_text += f'''
  {percent_list[times]}% {{
    transform: translateX(calc(320% * cos({calculated_turn_list[times]}turn) + 10% * cos(5 * {calculated_turn_list[times]}turn) + 6% * cos(7 * {calculated_turn_list[times]}turn) + 3% * cos(13 * {calculated_turn_list[times]}turn)))
      translateY(calc(105% * sin({calculated_turn_list[times]}turn) + 20% * sin(2 * {calculated_turn_list[times]}turn) + 15% * sin(3 * {calculated_turn_list[times]}turn) + 10% * sin(7 * {calculated_turn_list[times]}turn)))
      scale({calculated_scale_list[times]});
  }}
'''
        animation_text += f'''
  {100}% {{
    transform: translateX(calc(320% * cos({calculated_turn_list[0]}turn) + 10% * cos(5 * {calculated_turn_list[0]}turn) + 6% * cos(7 * {calculated_turn_list[0]}turn) + 3% * cos(13 * {calculated_turn_list[0]}turn)))
      translateY(calc(105% * sin({calculated_turn_list[0]}turn) + 20% * sin(2 * {calculated_turn_list[0]}turn) + 15% * sin(3 * {calculated_turn_list[0]}turn) + 10% * sin(7 * {calculated_turn_list[0]}turn)));
  }}
'''
    # 5 生产检查 —> 9
    if serial == 9:
        animation_text += "@keyframes ellipse_pic9 {"
        calculated_turn_list = get_turn_list(5)
        calculated_scale_list = get_scale_list(5)
        for times in times_list:
            animation_text += f'''
  {percent_list[times]}% {{
    transform: translateX(calc(320% * cos({calculated_turn_list[times]}turn) + 10% * cos(5 * {calculated_turn_list[times]}turn) + 6% * cos(7 * {calculated_turn_list[times]}turn) + 3% * cos(13 * {calculated_turn_list[times]}turn)))
      translateY(calc(105% * sin({calculated_turn_list[times]}turn) + 20% * sin(2 * {calculated_turn_list[times]}turn) + 15% * sin(3 * {calculated_turn_list[times]}turn) + 10% * sin(7 * {calculated_turn_list[times]}turn)))
      scale({calculated_scale_list[times]});
  }}
'''
        animation_text += f'''
  {100}% {{
    transform: translateX(calc(320% * cos({calculated_turn_list[0]}turn) + 10% * cos(5 * {calculated_turn_list[0]}turn) + 6% * cos(7 * {calculated_turn_list[0]}turn) + 3% * cos(13 * {calculated_turn_list[0]}turn)))
      translateY(calc(105% * sin({calculated_turn_list[0]}turn) + 20% * sin(2 * {calculated_turn_list[0]}turn) + 15% * sin(3 * {calculated_turn_list[0]}turn) + 10% * sin(7 * {calculated_turn_list[0]}turn)));
  }}
'''
    # 4 固定资产 —> 10
    if serial == 10:
        animation_text += "@keyframes ellipse_pic10 {"
        calculated_turn_list = get_turn_list(4)
        calculated_scale_list = get_scale_list(4)
        for times in times_list:
            animation_text += f'''
  {percent_list[times]}% {{
    transform: translateX(calc(320% * cos({calculated_turn_list[times]}turn) + 10% * cos(5 * {calculated_turn_list[times]}turn) + 6% * cos(7 * {calculated_turn_list[times]}turn) + 3% * cos(13 * {calculated_turn_list[times]}turn)))
      translateY(calc(105% * sin({calculated_turn_list[times]}turn) + 20% * sin(2 * {calculated_turn_list[times]}turn) + 15% * sin(3 * {calculated_turn_list[times]}turn) + 10% * sin(7 * {calculated_turn_list[times]}turn)))
      scale({calculated_scale_list[times]});
  }}
'''
        animation_text += f'''
  {100}% {{
    transform: translateX(calc(320% * cos({calculated_turn_list[0]}turn) + 10% * cos(5 * {calculated_turn_list[0]}turn) + 6% * cos(7 * {calculated_turn_list[0]}turn) + 3% * cos(13 * {calculated_turn_list[0]}turn)))
      translateY(calc(105% * sin({calculated_turn_list[0]}turn) + 20% * sin(2 * {calculated_turn_list[0]}turn) + 15% * sin(3 * {calculated_turn_list[0]}turn) + 10% * sin(7 * {calculated_turn_list[0]}turn)));
  }}
'''
    # 3 培训教育 —> 11
    if serial == 11:
        animation_text += "@keyframes ellipse_pic11 {"
        calculated_turn_list = get_turn_list(3)
        calculated_scale_list = get_scale_list(3)
        for times in times_list:
            animation_text += f'''
  {percent_list[times]}% {{
    transform: translateX(calc(320% * cos({calculated_turn_list[times]}turn) + 10% * cos(5 * {calculated_turn_list[times]}turn) + 6% * cos(7 * {calculated_turn_list[times]}turn) + 3% * cos(13 * {calculated_turn_list[times]}turn)))
      translateY(calc(105% * sin({calculated_turn_list[times]}turn) + 20% * sin(2 * {calculated_turn_list[times]}turn) + 15% * sin(3 * {calculated_turn_list[times]}turn) + 10% * sin(7 * {calculated_turn_list[times]}turn)))
      scale({calculated_scale_list[times]});
  }}
'''
        animation_text += f'''
  {100}% {{
    transform: translateX(calc(320% * cos({calculated_turn_list[0]}turn) + 10% * cos(5 * {calculated_turn_list[0]}turn) + 6% * cos(7 * {calculated_turn_list[0]}turn) + 3% * cos(13 * {calculated_turn_list[0]}turn)))
      translateY(calc(105% * sin({calculated_turn_list[0]}turn) + 20% * sin(2 * {calculated_turn_list[0]}turn) + 15% * sin(3 * {calculated_turn_list[0]}turn) + 10% * sin(7 * {calculated_turn_list[0]}turn)));
  }}
'''
    # 2 设备运行 —> 12
    if serial == 12:
        animation_text += "@keyframes ellipse_pic12 {"
        calculated_turn_list = get_turn_list(2)
        calculated_scale_list = get_scale_list(2)
        for times in times_list:
            animation_text += f'''
  {percent_list[times]}% {{
    transform: translateX(calc(320% * cos({calculated_turn_list[times]}turn) + 10% * cos(5 * {calculated_turn_list[times]}turn) + 6% * cos(7 * {calculated_turn_list[times]}turn) + 3% * cos(13 * {calculated_turn_list[times]}turn)))
      translateY(calc(105% * sin({calculated_turn_list[times]}turn) + 20% * sin(2 * {calculated_turn_list[times]}turn) + 15% * sin(3 * {calculated_turn_list[times]}turn) + 10% * sin(7 * {calculated_turn_list[times]}turn)))
      scale({calculated_scale_list[times]});
  }}
'''
        animation_text += f'''
  {100}% {{
    transform: translateX(calc(320% * cos({calculated_turn_list[0]}turn) + 10% * cos(5 * {calculated_turn_list[0]}turn) + 6% * cos(7 * {calculated_turn_list[0]}turn) + 3% * cos(13 * {calculated_turn_list[0]}turn)))
      translateY(calc(105% * sin({calculated_turn_list[0]}turn) + 20% * sin(2 * {calculated_turn_list[0]}turn) + 15% * sin(3 * {calculated_turn_list[0]}turn) + 10% * sin(7 * {calculated_turn_list[0]}turn)));
  }}
'''
    animation_text += """}
"""
    return animation_text

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    animation_text = ""
    animation_text = gen_animation(1, animation_text)
    animation_text = gen_animation(2, animation_text)
    animation_text = gen_animation(3, animation_text)
    animation_text = gen_animation(4, animation_text)
    animation_text = gen_animation(5, animation_text)
    animation_text = gen_animation(6, animation_text)
    animation_text = gen_animation(7, animation_text)
    animation_text = gen_animation(8, animation_text)
    animation_text = gen_animation(9, animation_text)
    animation_text = gen_animation(10, animation_text)
    animation_text = gen_animation(11, animation_text)
    animation_text = gen_animation(12, animation_text)
    # with open("result.txt", "w") as fp:
    #     fp.write(animation_text)
    animation_text

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
