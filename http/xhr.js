const host='https://restapi.amap.com/v3'

function requestQuery(method,data,callback){
    const data2=obj1(data)
    const xhr = new XMLHttpRequest()
    //是否是异步的，true
    xhr.open(method,`${host}/weather/weatherInfo?${data2}`,true)
    xhr.send()
    xhr.addEventListener('load',function(){
        callback(JSON.parse(xhr.response))
    })
}

function becomePromise(method,data){
return new Promise((resolve)=>{
    requestQuery(method,data,resolve)
})
}
function obj1(obj){
    return Object.keys(obj).map(key=>`${key}=${obj[key]}`).join('&')
}

export {
    requestQuery,
    becomePromise,
}

