import asyncio
import websockets
import pic
from yolo import predict
#import pymysql
import json
import time

# WebSocket 服务器处理函数
async def echo(websocket, path):
    global flg
    global pici
    now=time.time()
    if now-pici<=3:
        flg=True
    else:
        pici=now
    async for message in websocket:
        data=json.loads(message)
        print(type(data))
        bas64=data['img'].encode("utf-8")
        bas64=bas64[len('data:image/jpeg;base64,')::]
        user_name=data['id']
        img_name=data['img_name']
        
        print(type(user_name),user_name,img_name)
        path=pic.decode_base64(bas64)
        img,lb=predict(path,img_name,user_name,now)
        dic={"img":img.decode("utf-8"),"lb":lb,"img_name":img_name}
        sendmsg=json.dumps(dic)
        await websocket.send(f'{sendmsg}')

flg=True
pici=time.time()
asyncio.set_event_loop(asyncio.new_event_loop())
# 启动 WebSocket 服务器
start_server = websockets.serve(echo, "0.0.0.0", 8001)

# 运行事件循环
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
