CREATE TABLE IF NOT EXISTS "testTable" (
	"id" serial PRIMARY KEY NOT NULL,
	"name" char(12),
	"qty" bigint,
	"price" numeric(10, 2),
	"score" double precision,
	"delivered" boolean,
	"data" jsonb,
	"startAt" time(6) with time zone DEFAULT now()
);
--> statement-breakpoint
CREATE TABLE IF NOT EXISTS "users" (
	"id" serial PRIMARY KEY NOT NULL,
	"full_name" text,
	"phone" varchar(256)
);
