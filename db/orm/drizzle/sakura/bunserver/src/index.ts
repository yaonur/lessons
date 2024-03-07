import { Elysia } from "elysia";
import { getUser } from "../../index.ts";

const app = new Elysia();
app.get("/", () => "Hello Elysia");
app.get("/user", () => {
	const user = getUser()
	return user
})
app.listen(3001);
console.log("server running at http://localhost:3000");
