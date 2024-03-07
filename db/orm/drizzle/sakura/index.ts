import {drizzle}  from "drizzle-orm/node-postgres"
import { Client } from "pg";
import * as schema from "./schema"
const client = new Client(
	{
		connectionString: process.env.DATABASE_URL
	}
)

client.connect()

const db = drizzle(client, {schema: schema})

const result =await db.select().from(schema.users)

console.log("result",JSON.stringify(result))

process.exit(0)

