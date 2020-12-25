#python3.7
#Filename:爬取火车票信息(已知时间和始终站).py

#固定（可更改）的始终站、时间
#保存位置和输出方式自选（代码最后）

import requests,openpyxl
import re,os,json

path = "C:\\Users\\15394\\Desktop\\"
print("保存在：",path)

urls = "https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2019-05-01&leftTicketDTO.from_station=IOQ&leftTicketDTO.to_station=WHN&purpose_codes=ADULT"

#网址处理
def url(urls):
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36"}
    #urls = "https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2019-05-01&leftTicketDTO.from_station=IOQ&leftTicketDTO.to_station=WHN&purpose_codes=ADULT"
    res = requests.get(urls,headers=headers)

    res = json.loads(res.text)
    datas = res["data"]["result"]
    #print(datas)     #页面的所有火车票信息（字符串列表）
    return datas

#对单条信息删选
def _re(data):
    message = data.split("|")    #经过拆分可看出“预定”都是在第二个（索引为1）
    #print(message)
    return message    #单条火车信息组成的列表

#对信息整理
def prt(mes):
    a = mes[3]      #车次
    b1 = mes[4]     #出发站
    b2 = mes[7]     #到达站
    time1 = mes[8]  #出发时间
    time2 = mes[9]  #到达时间
    time3 = mes[10] #历时
    time4 = mes[13] #日期
    c1 = mes[32]    #商务座（特等座）
    c2 = mes[31]    #一等座
    c3 = mes[30]    #二等座
    c4 = mes[26]    #无座
    l = [a,b1,b2,time1,time2,time3,time4,c1,c2,c3,c4]
    for i in range(len(l)):
        if l[i]=="":
            l[i] = "无"
    dic = {"车次：":a,"出发站：":b1,"到达站：":b2,
            "出发时间：":time1,"到达时间：":time2,"历时：":time3,"日期：":time4,
            "商务座：":c1,"一等座：":c2,"二等座：":c3,"无座：":c4}
    list0 = ["车次：",l[0],"出发站：",l[1],"到达站：",l[2],
            "出发时间：",l[3]," 到达时间：",l[4],"历时：",l[5],"日期：",l[6],
            "  商务座：",l[7],"一等座：",l[8],"二等座：",l[9],"无座：",l[10]]
    return list0,dict

#文件保存
def txt_format(l):
    """
    文本格式优化
     """
    for i in range(1,len(l),2):
        #l[i] = l[i].ljust(10," ")
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
    wb.save(path+"火车票.xlsx")

#运行顺序
def go_txt():
    datas = url(urls)
    for data in datas:
        mes = _re(data)
        prt_txt = prt(mes)[0]
        m = txt_format(prt_txt)
        print(m,"\n")
        _file(m)     #保存为txt

def go_excel():
    datas = url(urls)
    i = 2
    for data in datas:
        mes = _re(data)
        prt_txt = prt(mes)[0]
        _excel(prt_txt,i)   #保存为excel
        i += 2


if __name__ == "__main__":
    go_txt()
    #go_excel()
    print("Done")
