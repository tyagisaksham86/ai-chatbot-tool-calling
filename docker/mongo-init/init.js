db = db.getSiblingDB("company_db");

db.sales.insertMany(require("/data/sales.json"));
db.admin.insertMany(require("/data/admin.json"));
