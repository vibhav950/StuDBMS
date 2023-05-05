## StuDBMS
Grade 12 Finals Project (Python/MySQL)

## Vital MySQL table structures
(view in raw mode)

# Setup instructions

1. Create the following structures in the respective database with the structures mentioned below.
2. Tables usernames_1 and usernames_2 hold login data (username and md5 password hash).

# Tables
+----------------+
| Tables_in_db |
+----------------+
| 11a_sa1        |
| 11a_sa2        |
| 11b_sa1        |
| 11b_sa2        |
| usernames_1    |
| usernames_2    |
+----------------+

# Table descriptions

11a_sa1, 11a_s12, 11b_sa1, 11b_sa2
+-----------+-------------+------+-----+---------+-------+
| Field     | Type        | Null | Key | Default | Extra |
+-----------+-------------+------+-----+---------+-------+
| RollNo    | int         | NO   | PRI | NULL    |       |
| Name      | varchar(20) | NO   |     | NULL    |       |
| Physics   | float(5,2)  | YES  |     | NULL    |       |
| Chemistry | float(5,2)  | YES  |     | NULL    |       |
| Maths     | float(5,2)  | YES  |     | NULL    |       |
| Computer  | float(5,2)  | YES  |     | NULL    |       |
| English   | float(5,2)  | YES  |     | NULL    |       |
+-----------+-------------+------+-----+---------+-------+

usernames_1, usernames_2
+----------+-------------+------+-----+---------+-------+
| Field    | Type        | Null | Key | Default | Extra |
+----------+-------------+------+-----+---------+-------+
| Username | varchar(20) | NO   | PRI | NULL    |       |
| Pass     | char(32)    | YES  |     | NULL    |       |
+----------+-------------+------+-----+---------+-------+
