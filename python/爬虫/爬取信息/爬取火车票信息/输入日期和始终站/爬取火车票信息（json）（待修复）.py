#python3.7
#Filename:爬取火车票信息(已知时间和始终站).py

#后续：文本文件的返回页面设置
#优化：异常处理，搜索时间的设置（当日往后一个月）

import requests,openpyxl
import os,json,re
import station_name_code

path = "C:\\Users\\15394\\Desktop\\"
print("保存在",path)

def getDatas(year,month,date,_from,_to):
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36"}
    params = [{
        "leftTicketDTO.train_date":str(year)+"-"+str(month)+"-"+str(date),
        "leftTicketDTO.from_station":_from,
        "leftTicketDTO.to_station":_to,
        "purpose_codes":"ADULT"
        }]
    url = "https://kyfw.12306.cn/otn/leftTicket/query"
    for i in params:
        res = requests.get(url,params=i)
        res = json.loads(res.text)
        datas = res["data"]["result"]
    #print(datas)     #页面的所有火车票信息（字符串列表）
    return datas

#对单条信息删选
def _re(data):
    message = data.split("|")    #经过拆分可看出“预定”都是在第二个（索引为1）
    #print(message)
    return message    #单条火车信息组成的列表

#对信息输出
def prt(mes):
    a = mes[3]      #车次
    b1 = code(mes[4])     #始站（更改为汉字）
    b2 = code(mes[5])     #终站（更改为汉字）
    b3 = code(mes[6])     #出发站
    b4 = code(mes[7])     #到达站
    time1 = mes[8]  #出发时间
    time2 = mes[9]  #到达时间
    time3 = mes[10] #历时
    time4 = mes[13] #日期
    c1 = mes[32]    #商务座（特等座）
    c2 = mes[31]    #一等座
    c3 = mes[30]    #二等座
    c4 = mes[21]    #高级软卧
    c5 = mes[23]    #软卧一等卧
    c6 = mes[33]    #动卧
    c7 = mes[28]    #硬卧二等卧
    c8 = mes[24]    #软座
    c9 = mes[29]    #硬座
    c10 = mes[26]    #无座
    l = [a,b1,b2,b3,b4,time1,time2,time3,time4,c1,c2,c3,c4,c5,c6,c7,c8,c9,c10]
    for i in range(len(l)):
        if l[i]=="":
            l[i] = "无"
    dic = {"车次":l[0],"始站":l[1],"终站":l[2],"出发站":l[3],"到达站":l[4],
         "出发时间":l[5],"到达时间":l[6],"历时":l[7],"日期":l[8],
         "商务座":l[9],"一等座":l[10],"二等座":l[11],"高级软卧":l[12],"软卧一等卧":l[13],
           "动卧":l[14],"硬卧二等卧":l[15],"软座":l[16],"硬座":l[17],"无座":l[18]}
    list0 = ["车次：",l[0],"始站：",l[1],"终站：",l[2],"出发站：",l[3],"到达站：",l[4],
         "出发时间：",l[5],"到达时间：",l[6],"历时：",l[7],"日期：",l[8],
         "商务座：",l[9],"一等座：",l[10],"二等座：",l[11],"高级软卧：",l[12],"软卧一等卧：",l[13],
        "动卧：",l[14],"硬卧二等卧：",l[15],"软座：",l[16],"硬座：",l[17],"无座：",l[18]]
    return list0,dic

#文本返回保存
def txt_format(l):  #文本格式优化
    for i in range(1,len(l),2):
        l[i] = "{0:{1}<5}\t".format(l[i],chr(12288))
    l = "".join(l)
    return l

def _file(m):    #保存为txt文件或直接输出
    with open(path+"火车票.txt","a") as f:
        f.write(m)

def _excel(l,i):  #保存为excel文件
    while os.path.exists(path+"火车票.xlsx") == False:
        wb = openpyxl.Workbook()
        sheet = wb.active
        sheet.title = "火车票信息"
        wb.save(path+"火车票.xlsx")
    wb = openpyxl.load_workbook(path+"火车票.xlsx")
    #sheet = wb["火车票信息：{} 至 {}".format(_from,_to)]
    sheet = wb["火车票信息"]
    if sheet["A1"].value == None:
        sheet["A1"] = l[0].replace("：","")
        sheet["B1"] = l[2].replace("：","")
        sheet["C1"] = l[4].replace("：","")
        sheet["D1"] = l[6].replace("：","")
        sheet["E1"] = l[8].replace("：","")
        sheet["F1"] = l[10].replace("：","")
        sheet["G1"] = l[12].replace("：","")
        sheet["H1"] = l[14].replace("：","")
        sheet["I1"] = l[16].replace("：","")
        sheet["J1"] = l[18].replace("：","")
        sheet["K1"] = l[20].replace("：","")
        sheet["L1"] = l[22].replace("：","")
        sheet["M1"] = l[24].replace("：","")
        sheet["N1"] = l[26].replace("：","")
        sheet["O1"] = l[28].replace("：","")
        sheet["P1"] = l[30].replace("：","")
        sheet["Q1"] = l[32].replace("：","")
        sheet["R1"] = l[34].replace("：","")
        sheet["S1"] = l[36].replace("：","")
    i = str(i)
    sheet["A"+i] = l[1]
    sheet["B"+i] = l[3]
    sheet["C"+i] = l[5]
    sheet["D"+i] = l[7]
    sheet["E"+i] = l[9]
    sheet["F"+i] = l[11]
    sheet["G"+i] = l[13]
    sheet["H"+i] = l[15]
    sheet["I"+i] = l[17]
    sheet["J"+i] = l[19]
    sheet["K"+i] = l[21]
    sheet["L"+i] = l[23]
    sheet["M"+i] = l[25]
    sheet["N"+i] = l[27]
    sheet["O"+i] = l[29]
    sheet["P"+i] = l[31]
    sheet["Q"+i] = l[33]
    sheet["R"+i] = l[35]
    sheet["S"+i] = l[37]
    wb.save(path+"火车票.xlsx")


#运行顺序
def go_txt(year,month,date,_from,_to):    #保存为txt
    datas = getDatas(year,month,date,code(_from),code(_to))
    for data in datas:
        mes = _re(data)
        l = prt(mes)[0]
        m = txt_format(l)
        print(m,"\n")   #返回到屏幕
        _file(m)    #保存为txt

def go_excel(year,month,date,_from,_to):     #保存为excel
    datas = getDatas(year,month,date,code(_from),code(_to))
    i = 2
    for data in datas:
        mes = _re(data)
        l = prt(mes)[0]
        _excel(l,i)   #保存为excel
        i += 2

#汉字编码转换
def code(name):
    name_code = station_name_code.dic()[0]
    code_name = station_name_code.dic()[1]
    if name in name_code:
        return name_code[name]
    elif name in code_name:
        return code_name[name]
    else:
        print("站点不存在")

def main():
    year=input("输入年份（如：2019）：")
    month=input("输入月份（如：01）：")
    date=input("输入日期（如：01）：")
    _from=input("输入出发站（如：北京）：")
    _to=input("输入到达站（如：北京）：")
    choice=int(input("返回至屏幕和txt文件输入“0”，返回至excel文件输入“1”："))
    if choice == 0:
        try:
            go_txt(year,month,date,_from,_to)    #txt文件和（或）返回到屏幕
        except:
            print("未找到")
    else:
        try:
            go_excel(year,month,date,_from,_to)     #excel表格
        except:
            print("未找到")

if __name__ == "__main__":
    main()
    print("Done")
