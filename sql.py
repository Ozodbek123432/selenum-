#ALTER TABLE calumin_nomi = tabledagi malumotalrni ozgartiradi  = birgs yozilsihi mukun pastta ketrilgan barcha malumotlar bu kod orqli yozilshi shart
#ADD COLUMON  calumin_nomi = calumin qosha va bu 2 qator birga yozilshi mkun=^
#RENAME TO  yang_calumni_nomi= table nomni ozgartitadi
#---------------------------------------------------------------------------------------------------------------------------------------------------------
#TRUNCATE TABLE calumni_nomi =  calumni ochirmasndan tozalaydi va bundan olin yoki bundan keyin hchnarsa yozish hsart emas
# DELETE TABLE  table_nomi = aynan birini butunlayy ochrib tashlaydi va where yozilshi kerak
# WHERE calumin_nomi < qiymat
#id SERIAL PRIYMARY KEY = aftomatik id qoshadi hamda dublikatlar hosil bolshni oldni oladdi
#---------------------------------------------------------------------------------------------------------------------------------------------------------

#CRATE TABLE user(
# id SERIAL PRIYMARY KEY
# email VARCHAR(100) UNIQUE NOT NULL, = 1  maumot 2 marta yozishi mukun emas
# name VARCHAR(50) NOT NULL, = name da malumot yoq bolmashi kerak
# )

#CRATE table yaratyotganda 2 calumni 1 tabliga boglab qoyish
#maslan
#caalumin_id INT REFERECES calumin(id)
#UPDATE table_nomi
#SET = 24
#WHERE maluumot
# -- DDL - Data definition languange (Yaratish, o'zgartirish, o'chirish)
# CREATE TABLE students (
#   id SERIAL PRIMARY KEY,
#   name VARCHAR(50),
#   age INT,
#   grade CHAR(2)
# )
#
# -- ALTER TABLE - bu buyrug' orqali table ga ustun qo'shish, o'chirish va o'zgartirish mumkin
#
# -- table ga ustun qo'shish
# ALTER TABLE students
# ADD COLUMN address VARCHAR(255)
#
# -- table ni nomini o'zgartiradi
# ALTER TABLE hackerlar_jadvali
# RENAME TO backendchilar_jadvali
#
# -- Column name ni o'zgartirish
# ALTER TABLE backendchilar_jadvali
# RENAME COLUMN grade TO class
#
# -- column ni type ni o'zgartiradi
# ALTER TABLE backendchilar_jadvali
# ALTER COLUMN age SET DATA TYPE SMALLINT
#
# SELECT *
# FROM students
#
# -- column ni o'chirish
# ALTER TABLE backendchilar_jadvali
# DROP COLUMN address
#
# -- Table ni o'chirish
# DROP TABLE users
#
# -- ---------------------------------------TUNCATE TABLE ----------------------------
# -- TUNCATE TABLE - table ni ichidagi hamma ma'lumotlarni o'chiradi
# INSERT INTO students (name, age, grade) VALUES ('Ziyobek', 12, '8');
# INSERT INTO students (name, age, grade) VALUES ('Ozodbek', 15, '8');
# INSERT INTO students (name, age, grade) VALUES ('Sayodbek', 12, '8');
# INSERT INTO students (name, age, grade) VALUES ('Muhammadumar', 12, '8')
#
# TRUNCATE TABLE students
#
# DELETE FROM students
# WHERE age > 12
#
# ------------------------------------------Data types------------------------------------
# CREATE TABLE course (
#   id SERIAL PRIMARY KEY,
#   title VARCHAR(50)
# )
#
# SELECT *
# FROM course
#
# INSERT INTO course (title) VALUES ('JavaScript');
# -- INSERT INTO users (email, name) VALUES ('ziyobek@gmail.com', 'Sayodbek');
#
# -- REFERENCES - boshqa table larni id sini ayni shu table ga bog'lab beradi
# CREATE TABLE enrollments (
#   id SERIAL PRIMARY KEY,
#   student_id INT REFERENCES students(id),
#   course_id INT REFERENCES course(id)
# )
#
# SELECT *
# FROM students
#
# INSERT INTO enrollments (student_id, course_id) VALUES (5, 2);
# INSERT INTO enrollments (student_id, course_id) VALUES (7, 2);
# INSERT INTO enrollments (student_id, course_id) VALUES (8, 2);
# INSERT INTO enrollments (student_id, course_id) VALUES (10, 6)
#
# -- table ichidagi columndagi ma'lumotlarni yangilab beradi
# UPDATE students
# SET grade = 65
#
# DROP TABLE employees1
#
# CREATE TABLE employees1 (
#   id SERIAL PRIMARY KEY,
#   name VARCHAR(50) NOT NULL,
#   salary INT CONSTRAINT positive_salary CHECK (salary > 100),
#   country VARCHAR(30) DEFAULT 'Uzbekistan'
# )
#
# INSERT INTO employees1 (name, salary) VALUES ('Ozodbek', 200)
# INSERT INTO employees1 (name, salary, country) VALUES ('Sayodbek', 200, 'China');
# INSERT INTO employees1 (name, salary) VALUES ('Ozodbek', 200)
#
# SELECT *
# FROM students
#
# -- uzunlik
# SELECT name, LENGTH(name) AS name_length
# -- bo'sh joylarni o'chirib chiqaradi
# SELECT name, TRIM('  Ozodbek  ') AS name_length
# FROM employees1
#
# UPDATE students
# SET grade = 65
# WHERE id = 7
# -- oxirgi natijani qaytarish
# RETURNING name, grade