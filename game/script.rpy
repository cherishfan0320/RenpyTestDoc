init python:
    import csv

    # 周选择dictioanry
    def creat_activity_dic(excelName):
        dict_from_csv = {}
        with open(renpy.loader.transfn(excelName),"r") as inp:
            reader = csv.reader(inp)
            for rows in reader:
                dict_from_csv[rows[0]] = {'W1': rows[1], 'W2': rows[2], 'W3': rows[3],'W4': rows[4]}
        return dict_from_csv


label start:
    "test"
    call test_cal
    "test"
    return


label test_cal:
    python:
        cal_address = "csv-test.csv"
        cal_dic = creat_activity_dic(cal_address) # create dictionary name as cal_dic
        # "[cal_dic]"
        cal_test_item = cal_dic["M8"]["W4"]

    # 成功读取specific event
    "测试读取：[cal_test_item]"
    return
