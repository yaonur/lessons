import {Application} from "abc"
import {user} from "../index.ts"
const PORT = 3001
const app  = new Application()

console.log(`Server is running on port ${PORT}`)
app.get("/hello",(c)=>{
  return c.string("Hello World")
})
app.get("/user", (c)=>{
  return c.json({name:"John Doe", age: 30})
})

app.start({port:PORT})


