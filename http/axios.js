import axios from'axios'
const gao1=axios.create({
    baseURL:'https://restapi.amap.com/v3',
    timeout:1000,
})

const gao2=axios.create({
    baseURL:'http://127.0.0.1:4523/m1/3150959-0-default',
    timeout:1000,
})

const myserver=axios.create({
    baseURL:'http://localhost:8080',
})
const Book=axios.create({
  baseURL:'http://localhost:8080',
})
const steelHistory = axios.create({
    baseURL:'http://127.0.0.1:8080/api/'
//   baseURL:'http://192.168.242.194:8080/api/'
})
//拦截器
gao2.interceptors.request.use((config)=>{
    //console.log(config)
    if(config.url!=='/login'){
    config.headers['token']=localStorage.getItem('token')}
   return config
})
export{
    gao1,
    gao2,
    myserver,
    Book,
    steelHistory
}
