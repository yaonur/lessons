import { bigint, boolean, char, decimal, doublePrecision, json, jsonb, pgEnum, pgTable, serial, text, time, varchar } from "drizzle-orm/pg-core";

export const users = pgTable("users", {
  id: serial("id").primaryKey(),
  fullName: text("full_name"),
  phone: varchar("phone", { length: 256 }),
});
export const Enum  =pgEnum("Enum",[])
export const testTable = pgTable("testTable", {
  id: serial("id").primaryKey(),
  // description: text("name"),
  description: varchar("name",{length:256}),
  name:char("name",{length:12}),
  qty: bigint("qty",{mode:"bigint"}),
  price:decimal("price",{precision:10,scale:2}),
  score:doublePrecision("score"),
  delivered: boolean("delivered"),
  // data:json("data")
  data:jsonb("data"),
  startAt: time("startAt",{precision:6, withTimezone: true}).defaultNow()

});

