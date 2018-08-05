import pandas as pd
def SaveBus(received_data):
    names = received_data['name']
    results = received_data['result']
    data = []
    via_stops = []
    for i in range(len(results['via_stops'])):
        via_stops.append(results['via_stops'][i]['name'])
    data.append(names)
    data.append(results['name'])
    data.append(results['company'])
    data.append(results['start_stop'])
    data.append(results['end_stop'])
    data.append(results['stime'])
    data.append(results['etime'])
    data.append(results['basic_price'])
    data.append(results['total_price'])
    data.append(results['path'])
    data.append(via_stops)
    output = open('BJBus.xls', 'a', encoding='gbk')
    for i in range(len(data)):
            output.write(str(data[i]))  # write函数不能写int类型的参数，所以使用str()转化
            output.write('\t')  # 相当于Tab一下，换一个单元格
    output.write('\n')  # 写完一行立马换行
    output.close()
    print("{}存储成功".format(names))
