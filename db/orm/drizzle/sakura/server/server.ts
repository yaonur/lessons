import {Application} from "abc"
const PORT = 8001
const app  = new Application()
console.log(`Server is running on port ${PORT}`)
app.get("/hello",(c)=>{
  return c.string("Hello World")
}).start({port:PORT})


