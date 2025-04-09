const data ={
  username:'',
  userId:0
}
export function setData(Data){
data.username = Data.username
data.userId = Data.userID
}
export function getData(){
  return data
}