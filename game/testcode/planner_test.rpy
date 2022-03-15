
init python:
    # 一些initialization的data
    slot_selected = 0 # 目前选择正在modify的事项
    # dictionary
    # 1. action event
    # 2. discription
    # 3. cost - 这个只会在16岁的那一年出现，第一年是没有cost的
    study_list = {
    0:{1:"n/a", 2:"n/a", 3:"n/a"},
    1:{1:"艺术课", 2:"学习艺术，balabala", 3:"10g"},
    2:{1:"编程课", 2:"programming，编程", 3:"10g"},
    3:{1:"课程1", 2:"课程1", 3:"10g"},
    4:{1:"课程2", 2:"课程2", 3:"10g"},
    5:{1:"课程3", 2:"课程3", 3:"10g"},
    6:{1:"课程4", 2:"课程4", 3:"10g"}
    }
    relax_list = {
    0:{1:"n/a", 2:"n/a", 3:"n/a"},
    1:{1:"休息", 2:"休息1", 3:"10g"},
    2:{1:"发呆", 2:"发呆ing", 3:"10g"},
    3:{1:"看书", 2:"看书<>", 3:"10g"},
    4:{1:"放松", 2:"放松<><>", 3:"10g"}
    }
    act_list = {
    0:{1:"n/a", 2:"n/a", 3:"n/a"},
    1:{1:"聊天", 2:"聊天", 3:"10g"},
    2:{1:"义工活动", 2:"聊天", 3:"10g"},
    3:{1:"跑步", 2:"聊天", 3:"10g"}
    }
    work_list = []

    #length 用于loop
    study_len = len(study_list)
    relax_len = len(relax_list)
    act_len = len(act_list)
    work_len = len(work_list)
    # 每一个list都会有一个出身限定款，会首先出现，然后是general的list display

    # 其他variable
    select_status = 0
    select_num = 0
    select_list_type = 1

    ref_list = {1:{1:"ref", 2:"ref", 3:"ref"}} # placeholder
    ref_len = 0

    select_slot = 0
    select_submit = 0

    ## 选择结果 ##
    # 1: 类型, 2: 名称, 3: 简介
    week_acts = {
    1: {1: "", 2: ""},
    2: {1: "", 2: ""},
    3: {1: "", 2: ""},
    4: {1: "", 2: ""}
    }

    ## 一些用于display的text
    left_piority = ['主要', '重要', '普通', '普通']
    act_lst = ['学习', '放松', '活动']

    def week_act_list_generate(slot, name, detail):
        week_acts[slot][1] = name
        week_acts[slot][2] = detail
        return week_acts

screen planner_test():
    # 注意：call这个之前要清空两个select的variable
    # 背景图片
    add "testcal.png"
    $ select_submit = 0

    #### 左侧四个column的hover...等等 ####
    vbox xpos 0.25:
        for i in range(1, 5):
            imagebutton:
                ypos (1.4 + 0.1*i)
                idle "agenda.png"
                hover "agenda_hover.png"
                action SetVariable("select_slot", i)

    ## 显示目前正在编辑的slot ##
    vbox xpos 0.25:
        for i in range(1, 5):
            showif select_slot == i:
                imagebutton:
                    ypos (42 + 118*i)
                    idle "agenda_hover.png"
                    hover "agenda_hover.png"

    #### 上面的三个button ####
    hbox xpos 0.53:
        ypos 98
        for i in range(1, 4):
            $ act_txt = act_lst[i-1]
            button:
                xmaximum 70
                ymaximum 35
                xpos (0.3 + 0.3*(i-1))
                action [SetVariable("select_list_type", i), SetVariable("select_num", i-1)]
    hbox xpos 0.55:
        ypos 100
        for i in range(1, 4):
            $ act_txt = act_lst[i-1]
            text "[act_txt]":
                xpos (0.3 + 1*(i-1))

    ## Scroll Bar内容
    vpgrid:
        #### 相关数值 ####
        area (0.55,0.2,350,300) # for the whole scroll bar
        cols 2
        xspacing -280 # this is for multiple columns
        draggable True
        mousewheel True
        scrollbars "vertical"
        # Since we have scrollbars, we have to position the side, rather
        # than the vpgrid proper.
        side_xalign 0.5
        ## 根据上面的butoon改变list##
        if select_list_type == 1:
            $ ref_list = study_list
            $ ref_len = study_len
        elif select_list_type == 2:
            $ ref_list = relax_list
            $ ref_len = relax_len
        elif select_list_type == 3:
            $ ref_list = act_list
            $ ref_len = act_len

        # 显示image button
        vbox:
            for i in range(1, ref_len):
                button:
                    xsize 300
                    ysize 70
                    # xysize (300, 80) # xysize是整体的，它会根据有多少button来除得到button之间的空隙
                    action [SetVariable("select_status", 1),
                    SetVariable("select_num", i)]
        vbox ypos 22:
            for i in range(1, ref_len):
                $ name_info = ref_list[i][1]
                text '[name_info]':
                    xsize 300
                    # xysize (300, 100)
                    line_spacing 42

    ## scroll bar选择在下面的textbox内容
    showif select_status == 1:
        $ text_info = ref_list[select_num][2]
        text "[text_info]" style "textbox_info"

    # 右侧的选择button
    showif select_status == 1 and select_slot != 0:
        textbutton "选择":
            xcenter 0.6
            ypos 0.8
            action Jump ('plan_submit')
        textbutton "开始一周":
            xcenter 0.7
            ypos 0.8
            action Jump ('plan_submit')

    # 左侧的选择的文字填写
    vbox xpos 0.27:
        for i in range(1, 5):
            $ name_txt = week_acts[i][1]
            $ info_txt = week_acts[i][2]
            text " [name_txt]\n[info_txt]" style "plan_slot":
                ypos (120 + 63*i)

    # 左侧的title，显示日期
    text "2022年，Week3，三月" style "plan_title"

    # 左侧的piority数字
    vbox xcenter 0.21:
        for i in range(1, 5):
            $ pio_show = left_piority[i-1]
            text "[pio_show]":
                size 30
                ypos (124 + 78*i)

label plan_submit:
    if select_list_type == 1:
        $ select_act_name = study_list[select_num][1]
        $ select_act_detail = study_list[select_num][2]
        $ week_acts = week_act_list_generate(select_slot, select_act_name, select_act_detail)
    elif select_list_type == 2:
        $ select_act_name = relax_list[select_num][1]
        $ select_act_detail = relax_list[select_num][2]
        $ week_acts = week_act_list_generate(select_slot, select_act_name, select_act_detail)
    elif select_list_type == 3:
        $ select_act_name = act_list[select_num][1]
        $ select_act_detail = act_list[select_num][2]
        $ week_acts = week_act_list_generate(select_slot, select_act_name, select_act_detail)
    call screen planner_test

style textbox_info is text:
    xmaximum 250
    size 20
    xpos 0.57
    ypos 0.65
style plan_slot is text:
    xmaximum 250
style plan_title is text:
    size 30
    xcenter 0.33
    ypos 0.12
