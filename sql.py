import pymysql
import base64
import time

def insert(img_path,lab_path,img_name,user_name,predict_time,pici):
    conn = pymysql.connect(host='localhost',user='root',passwd='Jd040818',db='steel')
    cursor = conn.cursor()
    with open(img_path, 'rb') as f:
        binary_data = f.read()
    try:
        with open(lab_path, 'rb') as f:
            lab_data = f.read()
    except:
        with open("empty.txt", 'rb') as f:
            lab_data=f.read()
    time_now=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    pc=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(pici))
    sql_insert = "INSERT INTO data (pic_name,user_name,img,lab,time,predict_time,pici) VALUES (%s, %s, %s, %s, %s, %s,%s)"
    cursor.execute(sql_insert, (img_name, user_name, pymysql.Binary(binary_data), pymysql.Binary(lab_data), time_now, predict_time,pc) )
    conn.commit()
    cursor.close()
    conn.close()

def sel_name(user_name):
    conn = pymysql.connect(host='localhost',user='root',passwd='Jd040818',db='steel')
    cursor = conn.cursor()
    sql_select = "SELECT * FROM data WHERE user_name=%s"
    cursor.execute(sql_select, user_name)
    result = cursor.fetchall()
    ans=[]
    for i in result:
        img_name=i[0]
        user_name=i[1]
        img=i[2]
        img=base64.b64encode(img).decode("utf-8")
        lab_str=i[3]
        time=i[4]
        lab=[]
        lis=lab_str.splitlines()
        for _ in lis:
            l=_.split(" ")
            dic={"type":l[0],"x":l[1],"y":l[2],"w":l[3],"h":l[4]}
            lab.append(dic)
        ans.append({"img_name":img_name,"user_name":user_name,"img":img,"lab":lab,"time":time})
    cursor.close()
    conn.close()
    return ans

def sel_pc(pici):
    conn = pymysql.connect(host='localhost',user='root',passwd='Jd040818',db='steel')
    cursor = conn.cursor()
    sql_select = "SELECT * FROM data WHERE pici=%s"
    cursor.execute(sql_select, pici)
    result = cursor.fetchall()
    ans=[]
    for i in result:
        img_name=i[0]
        user_name=i[1]
        img=i[2]
        img=base64.b64encode(img).decode("utf-8")
        lab_str=i[3]
        time=i[4]
        lab=[]
        lis=lab_str.splitlines()
        for _ in lis:
            l=_.split(" ")
            dic={"type":l[0],"x":l[1],"y":l[2],"w":l[3],"h":l[4]}
            lab.append(dic)
        ans.append({"img_name":img_name,"user_name":user_name,"img":img,"lab":lab,"time":time})
    cursor.close()
    conn.close()
    return ans

def sel_name1(user_name):
    conn = pymysql.connect(host='localhost',user='root',passwd='Jd040818',db='steel')
    cursor = conn.cursor()
    sql_select = "SELECT predict_time,pici FROM data WHERE user_name=%s"
    cursor.execute(sql_select, user_name)
    result = cursor.fetchall()
    print(result)
    ans={}
    for x in result:
        predic_time=x[0]
        pici=x[1]
        if pici not in ans:
            ans[pici]=[float(predic_time),1]
        else :
            ans[pici][0]+=float(predic_time)
            ans[pici][1]+=1
    return ans

if __name__=='__main__':
    '''
    img_path="./runs/detect/predict/crazing_11.jpg"
    lab='./runs/detect/predict/labels/crazing_11.txt'
    img_name="crazing_3"
    user_name="张三1"
    insert(img_path,lab,img_name,user_name)
    ans=sel_name(user_name)
    print(len(ans))
    '''
    #sel_name1("张三")
    print(sel_pc("2025-03-23 17:01:24"))

