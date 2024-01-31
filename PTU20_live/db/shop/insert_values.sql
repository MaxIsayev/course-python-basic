-- SQLite
INSERT INTO costumer (first_name, last_name)
VALUES ('John', 'Smith'),
       ('Maxim', 'Isayev'),
       ('Miroslava', 'Bystrova'),
       ('Viktor', 'Kiško'),
       ('Vytautas', 'Radavičius'),
       ('Irmantas', 'Radavičius'),
       ('Vadim', 'Isayev'),
       ('Vadim', 'Lukoškov'),
       ('Itachi', 'Uchiha'),
       ('Yuki', 'Onna');

INSERT INTO cashier (first_name, last_name)
VALUES ('Bernard', 'Barukh'),
       ('David', 'Rockfeller'),
       ('Arvydas', 'Turonis'),
       ('Kuzunokha', 'Abe'),
       ('Agnė', 'Kičaitė'),
       ('Ana', 'Chaleckaja'),
       ('Nathaniel', 'Rothschild'),
       ('Anatoly', 'Chubays');

INSERT INTO product (name, price)
VALUES ('Samsung A55 phone', 550.5),        --1
       ('Fujitsu Celsius laptop', 430.66),  --2
       ('Torch', 5.00),                     --3
       ('F&D Speakers', 20.00),             --4
       ('Maxell Earphones', 15.20),         --5
       ('Ketchup', 1.99),                   --6
       ('Saguaro mineral water', 0.5),      --7
       ('Milk', 1.5),                       --8
       ('Apple', 0.8),                      --9
       ('Bread', 1.3),                      --10
       ('Japanese legends book', 30.2),     --11
       ('Newspaper', 1.4);                  --12

INSERT INTO bill (purchase_datetime, cashier_id, custumer_id)
VALUES ('00:12:00', 1, 1),  --1
       ('01:23:00', 6, 2),  --2
       ('02:14:00', 5, 3),  --3
       ('03:56:00', 8, 4),  --4
       ('04:45:00', 2, 5),  --5
       ('05:12:00', 3, 6),  --6
       ('06:25:00', 4, 7),  --7
       ('07:42:00', 7, 8),  --8
       ('08:56:00', 8, 9),  --9
       ('09:13:00', 1, 10), --10
       ('10:07:00', 2, 2),  --11
       ('11:14:00', 3, 2),  --12
       ('12:23:00', 4, 5),  --13
       ('13:12:00', 5, 5),  --14
       ('14:45:00', 6, 5),  --15
       ('15:23:00', 7, 3),  --16
       ('16:08:00', 8, 6),  --17
       ('17:09:00', 3, 7),  --18
       ('18:54:00', 2, 8),  --19
       ('19:12:00', 1, 10), --20
       ('20:26:00', 4, 1);  --21

INSERT INTO bill_line (bill_id, product_id, quantity)
VALUES (5, 1, 4),
       (5, 2, 1),
       (5, 4, 1),
       (13, 6, 1),
       (14, 9, 12),
       (15, 12, 2),
       (1, 12, 6),
       (2, 4, 1),
       (3, 6, 1),
       (4, 9, 12),
       (5, 4, 1),
       (6, 6, 1),
       (7, 9, 12),
       (8, 4, 1),
       (9, 6, 1),
       (10, 9, 12),
       (11, 4, 1),
       (12, 6, 1),
       (13, 9, 12),
       (14, 4, 1),
       (15, 6, 1),
       (16, 9, 12),
       (17, 4, 1),
       (18, 6, 1),
       (19, 9, 12),
       (20, 4, 1),
       (21, 6, 1);
       
