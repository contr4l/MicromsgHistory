import csv
import time
import re

def write_chat_txtfile():
    """
    Write the csv file

    Args:
    """
    chat_txtfile = open(r'C:\Users\ctrl\Desktop\chat.txt','w',encoding='gb18030')
    count = 0
    with open(r'C:\Users\ctrl\Desktop\chathistory.csv','r',encoding='gb18030') as f:
        reader = csv.DictReader(f)
        for row in reader:
            newlist = []
            if row['talker'] == 'chhhhhhensy' and row['imgPath'] == '' and 'content' not in row['content']:
                if row['isSend'] == '1':
                    time_str = str(time.gmtime(int(row['createTime'])/10e2))
                    match_list = re.findall('=(\d+)', time_str)
                    match_list[3] = str(int(match_list[3]) + 8)
                    for i in match_list:
                        if len(i) == 1:
                            newlist.append('0'+i)
                        else:
                            newlist.append(i)
                    time_standard = '{0}-{1}-{2} {3}:{4}:{5}'.format(newlist[0],newlist[1],newlist[2],newlist[3],newlist[4],newlist[5])
                    chat_txtfile.write(time_standard + '       哥哥：' + row['content'] + '\n')
                else:
                    time_str = str(time.gmtime(int(row['createTime'])/10e2))
                    match_list = re.findall('=(\d+)', time_str)
                    match_list[3] = str(int(match_list[3]) + 8)
                    for i in match_list:
                        if len(i) == 1:
                            newlist.append('0'+i)
                        else:
                            newlist.append(i)
                    time_standard = '{0}-{1}-{2} {3}:{4}:{5}'.format(newlist[0], newlist[1], newlist[2],newlist[3], newlist[4], newlist[5])
                    chat_txtfile.write(time_standard + '       宝贝：' + row['content'] + '\n')
                count += 1
                print(count)

def write_sorted_chathistory():
    """
    Write a list of - csv to csv file.

    Args:
    """
    chat_txtfile = open(r'C:\Users\ctrl\Desktop\chat_tk.txt', 'w', encoding='gb18030')
    count = 0
    chathistory_dict = {}
    with open(r'C:\Users\ctrl\Desktop\chathistory.csv', 'r', encoding='gb18030') as f:
        reader = csv.DictReader(f)
        for row in reader:
            newlist = []
            if row['talker'] == 'tiankun_007' and row['imgPath'] == '' and 'content' not in row['content']:
                if row['isSend'] == '1':
                    time_str = str(time.gmtime(int(row['createTime']) / 10e2 + 36000))
                    match_list = re.findall('=(\d+)', time_str)
                    for i in match_list:
                        if len(i) == 1:
                            newlist.append('0' + i)
                        else:
                            newlist.append(i)
                    time_standard = '{0}-{1}-{2} {3}:{4}:{5}'.format(newlist[0], newlist[1], newlist[2], newlist[3],
                                                                     newlist[4], newlist[5])
                    chathistory_dict[row['createTime']] = time_standard + '       园小方：' + row['content'] + '\n'
                else:
                    time_str = str(time.gmtime(int(row['createTime']) / 10e2 + 36000))
                    match_list = re.findall('=(\d+)', time_str)
                    for i in match_list:
                        if len(i) == 1:
                            newlist.append('0' + i)
                        else:
                            newlist.append(i)
                    time_standard = '{0}-{1}-{2} {3}:{4}:{5}'.format(newlist[0], newlist[1], newlist[2], newlist[3],
                                                                     newlist[4], newlist[5])
                    chathistory_dict[row['createTime']] = time_standard + '       古叶田：' + row['content'] + '\n'
                count += 1
                print(count)
    chat_history = sorted(chathistory_dict.values())
    for i in chat_history:
        chat_txtfile.write(i)
write_sorted_chathistory()