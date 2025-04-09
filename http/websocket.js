// const websocketUrl = `ws://192.168.242.194:8001`
const websocketUrl = `ws://127.0.0.1:8001`
// 实列
let websock = null
let isSuccess = false
// 是否结束重连
let flag = 'false'
// 连接成功执行的回调函数，获取到数据
let messageCallback = null
function webSocketOnOpen(e) {
  console.log('与服务端连接打开->', e)
  isSuccess = true
  // websocket.send('Hello, WebSocket!');
}
function webSocketOnMessage(e) {
  //  console.log('来自服务端的消息->', e)
  // 将json数据转化为对象
  messageCallback(e)
}
function webSocketOnError(e) {
  console.log('与服务端连接异常->', e)
  isSuccess = false
  // 三秒之后重连
  setTimeout(() => {
    initWebSocket()
  }, 3000)
}
function webSocketOnClose(e) {
  console.log('与服务端连接关闭->', e)
  // initWebSocket()
}
function initWebSocket() {
  // 连接失败并且主动断开连接，浏览器报错无需重连
  if (flag === 'true') {
    flag = 'false'
  //  console.log('停止')
    return
  }
  if (typeof WebSocket === 'undefined') {
    return console.log('您的浏览器不支持websocket')
  }
  console.log('正在尝试建立连接。。。。。')
  websock = new WebSocket(websocketUrl)
  websock.onopen = webSocketOnOpen
  websock.onmessage = webSocketOnMessage
  websock.onerror = webSocketOnError
  websock.onclose = webSocketOnClose
}
export function connectWebsocket(successCallback) {
  messageCallback = successCallback
  initWebSocket()
}
export async function sendMessage(msg){
  if(isSuccess) await websock.send(msg)
}
export function destroyWebsocket() {
  websock.close()
  // 如果连接成功，主动断开后可以继续重连
  if (isSuccess)flag = false
  else
    // 否则主动关闭连接，无需重连
    flag = 'true'
}

