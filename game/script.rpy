
# 还差显示事件详情的layout

init python:
    import csv

    # 通过读取csv，产出完整的日历dic
    def creat_cal_dic(SatCSV, SunCSV):
        cal_dic_days = {}
        # 生成周六
        dict_from_csv = {} # place holder, 用于contain目前读取的dic
        with open(renpy.loader.transfn(SatCSV),"r") as inp:
            reader = csv.reader(inp)
            for rows in reader:
                dict_from_csv[rows[0]] = {'W1': rows[1], 'W2': rows[2], 'W3': rows[3],'W4': rows[4]}
        cal_dic_days['Sat'] = dict_from_csv
        #生成周日
        dict_from_csv = {}
        with open(renpy.loader.transfn(SunCSV),"r") as inp:
            reader = csv.reader(inp)
            for rows in reader:
                dict_from_csv[rows[0]] = {'W1': rows[1], 'W2': rows[2], 'W3': rows[3],'W4': rows[4]}
        # 合并
        cal_dic_days['Sun'] = dict_from_csv
        return cal_dic_days

    # 全部活动索引的dic
    def create_activity_dic(excelName):
        dict_from_csv = {} # place holder, 用于contain目前读取的dic
        with open(renpy.loader.transfn(excelName),"r") as inp:
            reader = csv.reader(inp)
            for rows in reader:
                dict_from_csv[rows[0]] = {'ID': rows[0], 'Story_type': rows[1], 'Event_type': rows[2],'Show': rows[3],
                'Active_status': rows[4], 'Act_name_txt': rows[5], 'Act_info_txt': rows[6],
                'Ab_req_1_id': rows[7], 'Ab_req_1': rows[8],
                'Ab_req_2_id': rows[9], 'Ab_req_2': rows[10],
                'Ab_req_3_id': rows[11], 'Ab_req_3': rows[12],
                'Cost': rows[13], 'Reward': rows[14]
                }
        return dict_from_csv

    # 年月日的文字版，到时候需要和冰岛general variable的dic里面去
    def create_label_dic(excelName):
        dict_from_csv = {}
        with open(renpy.loader.transfn(excelName),"r") as inp:
            reader = csv.reader(inp)
            dict_from_csv = {rows[0]:rows[1] for rows in reader}
        return dict_from_csv

    # create dics:
    # 创建日历
    cal_dic = {}
    sat_cal_address = "sat-events.csv"
    sun_cal_address = "sun-events.csv"
    # 年份生成
    cal_dic['Y14'] = creat_cal_dic(sat_cal_address,sun_cal_address) # create dictionary name as cal_dic
    # 创建活动索引
    act_label_address = "csv-act-test.csv"
    act_dic = create_activity_dic(act_label_address)
    # 创建文字索引
    time_label_address = "time-labels.csv"
    time_label_dic = create_label_dic(time_label_address)

    # 其他的variable
    # 月
    selected_month_id = "M8"
    month_txt = time_label_dic[selected_month_id]
    # 年
    year_id = "Y14"
    year_txt = time_label_dic[year_id]

    cal_text_size = 20
    week_str = "W1"

label start:
    "test"
    call test_cal
    "test"
    return


label test_cal:

    call screen test_frame
    return

# screen, 目前先用frame来做这个calendar的背景
screen test_frame():
    frame:
        xsize 900
        ysize 580
        xcenter 0.5
        ycenter 0.5

        text "[year_txt], [month_txt]":
            size 30
            xcenter 0.5
            ycenter 0.1

        # months, tabel of content:
        $ month_disp_lst = ['M8', 'M9', 'M10', 'M11', 'M12', 'M1', 'M2', 'M3', 'M4']
        vbox:
            xcenter 0.1
            ypos 0.25
            $ month_lst_len = len(month_disp_lst)
            for i in range(0, month_lst_len):
                $ month_id = month_disp_lst[i]
                python:
                    month_txt = time_label_dic[month_id]
                textbutton "[month_txt]" style "cal_text":
                    text_size cal_text_size
                    ypos (10 + 15*i)
                    action SetVariable('selected_month_id', month_id)

        # days
        $ calendar_days = ['周六', '周日']
        hbox:
            ycenter 0.25
            xcenter 0.4
            for i in range(0, 2):
                $cal_day_txt = calendar_days[i]
                text "[cal_day_txt]" style "cal_text":
                    xpos (50 + 150*i)

        # weeks and the displays
        vbox:
            xcenter 0.25
            for i in range(1, 5):
                text "Week [i]" style "cal_text":
                    ypos (100 + 70*i)

        # 测试周六display
        vbox:
            xcenter 0.45
            python:
                disp_Sat = cal_dic[year_id]['Sat'][selected_month_id]
            for i in range(1, 5):
                python:
                    # str_i = str(i)
                    week_str = 'W'+str(i)
                    act_id = cal_dic[year_id]['Sat'][selected_month_id][week_str]
                    act_txt = act_dic[act_id]['Act_name_txt']
                text "[act_txt]" style "cal_text":
                    ypos (100 + 70*i)
        # 测试周日display
        vbox:
            xcenter 0.7
            python:
                disp_Sat = cal_dic[year_id]['Sat'][selected_month_id]
            for i in range(1, 5):
                python:
                    # str_i = str(i)
                    week_str = 'W'+str(i)
                    act_id = cal_dic[year_id]['Sun'][selected_month_id][week_str]
                    act_txt = act_dic[act_id]['Act_name_txt']
                text "[act_txt]" style "cal_text":
                    ypos (100 + 70*i)


style cal_text:
    size cal_text_size
