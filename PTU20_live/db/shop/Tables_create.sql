-- SQLite
CREATE TABLE IF NOT EXISTS costumer (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name VARCHAR(200),
    last_name VARCHAR(200)
);

CREATE TABLE IF NOT EXISTS product (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(200),
    price FLOAT
);

CREATE TABLE IF NOT EXISTS cashier (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name VARCHAR(200),
    last_name VARCHAR(200)
);

CREATE TABLE IF NOT EXISTS bill (
   id INTEGER PRIMARY KEY AUTOINCREMENT,
   purchase_datetime TIME,
   cashier_id INTEGER REFERENCES cashier(id),
   custumer_id INTEGER REFERENCES costumer(id)
);


CREATE TABLE IF NOT EXISTS bill_line (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    bill_id INTEGER REFERENCES bill(id),
    product_id INTEGER REFERENCES product(id),
    quantity INTEGER
);