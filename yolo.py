from ultralytics import YOLO
import pic
import os
import sql
import shutil

def predict(path,img_name,user_name,now):
    try:
        shutil.rmtree('runs')
    except:
        print("no such file or dic")
    a1=YOLO("best.pt")
    res=a1(source=path,save=True,save_txt=True)
    time=res[0].speed['preprocess']+res[0].speed['inference']+res[0].speed['postprocess']

    img_path='runs/detect/predict/base64.jpg'
    lab_path='runs/detect/predict/labels/base64.txt'
    rse=pic.encode_base64(img_path)
    try:
        ans=txt_to_list(lab_path)  
    except:
        ans=[]
    sql.insert(img_path,lab_path,img_name,user_name,time,now)
    shutil.rmtree('runs') 
    return rse,ans

def txt_to_list(filename):
    ans=[]
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
        lis=content.splitlines()
        for _ in lis:
            l=_.split(" ")
            dic={"type":l[0],"x":l[1],"y":l[2],"w":l[3],"h":l[4]}
            ans.append(dic)
        # 假设文件内容每行是一个元素，使用splitlines将其转化为列表
        return ans
'''
a1.train(
    data='data.yaml',
    epochs=100,
    imgsz=640,
    batch=32,
    device=0
)
'''
if __name__=="__main__":
    path="./crazing_11.jpg"
    a1=YOLO("best.pt")
    res=a1(source=path,save=True,save_txt=True)
    time=res[0].speed['preprocess']+res[0].speed['inference']+res[0].speed['postprocess']
    print(time,type(time))
