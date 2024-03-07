import { Pool } from "pg";
import { drizzle } from "drizzle-orm/node-postgres";
import {migrate} from "drizzle-orm/node-postgres/migrator"
import "dotenv/config";

const url = process.env.DATABASE_URL
console.log("db URL:",url)
const pool = new Pool({
	connectionString: url
	// connectionString:"postgresql://postgres:postgres123@127.0.0.1:5432/postgres"
})

const db = drizzle(pool)

async function main() {
	console.log("migration started...")
	await migrate(db,{migrationsFolder: "./drizzle"})
	console.log("migration ended...")
	process.exit(0)
}

main().catch((e) => {
	console.error(e)
	process.exit(1)
})

