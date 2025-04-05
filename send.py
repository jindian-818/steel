import asyncio
import websockets
import pic
import json
img_path = 'crazing_11.jpg'
base64_data = pic.encode_base64(img_path)
id="张三1"
img_name="666"
dic={"id":id,"img":base64_data.decode("utf-8"),"img_name":img_name}
sendmsg=json.dumps(dic)
# 客户端处理函数
async def hello():
    async with websockets.connect("ws://192.168.20.194:8001") as websocket:
        #print(sendmsg)
        await websocket.send(f"{sendmsg}")
        response = await websocket.recv()
        print(f"Received: {response}")

# 运行客户端
asyncio.get_event_loop().run_until_complete(hello())


