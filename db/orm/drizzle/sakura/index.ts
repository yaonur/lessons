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

export const getUser = async () => await db.select().from(schema.users)



