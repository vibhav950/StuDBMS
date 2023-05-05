# StuDBMS

Student DBMS with a Python GUI - Grade 12 Finals Project (Python/MySQL/Tkinter).

## Setup instructions

These tables need to be created in the MySQL backend database.

1. Tables `usernames_1` and `usernames_2` hold login data (username and md5 password hash).

2. The rest of the tables hold student records organized as \<class\>\<section\>_\<exam\>.

### MySQL Tables

|tables          |
|----------------|
| 11a_sa1        |
| 11a_sa2        |
| 11b_sa1        |
| 11b_sa2        |
| usernames_1    |
| usernames_2    |

### Table descriptions

`11a_sa1`, `11a_s12`, `11b_sa1`, `11b_sa2`

| Field     | Type        | Null | Key | Default | Extra |
|-----------|-------------|------|-----|---------|-------|
| RollNo    | int         | NO   | PRI | NULL    |       |
| Name      | varchar(20) | NO   |     | NULL    |       |
| Physics   | float(5,2)  | YES  |     | NULL    |       |
| Chemistry | float(5,2)  | YES  |     | NULL    |       |
| Maths     | float(5,2)  | YES  |     | NULL    |       |
| Computer  | float(5,2)  | YES  |     | NULL    |       |
| English   | float(5,2)  | YES  |     | NULL    |       |

`usernames_1`, `usernames_2`

| Field    | Type        | Null | Key | Default | Extra |
|----------|-------------|------|-----|---------|-------|
| Username | varchar(20) | NO   | PRI | NULL    |       |
| Pass     | char(32)    | YES  |     | NULL    |       |

### Changes to be made to client code

* Complete user directory path.
* Complete media dependency paths.
