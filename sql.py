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
        #   country
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
#---------------------------------------------------------------------------------------------------------------------------------------keyingi dars
#SELECT unit_price
#CASE
#       WHEN unit_price < 10 THEN 'arzon'
#       WHEN unit_price < 10 THEN 'ortcha' AND unit_price < 20 THEN 'qimagtrioq'
#       ELSE  'qimat'
#END AS teble_nomi
#FROM product
#--------#---------------------------------------------------------------------------------------------------------------------------------------keyingi dars-------------------------------------------------------------------------------------------------------------------------------keyingi dars
#API bizni serverbilan boglaydi
#UY ISHHI
#API haqida malumot toplash
#wep dastur ishlab chiqh uchun  asturlar
#1 Flask == mikro
#2 Djson == polnotsening
#3 Fastapi == polnotsening
#bu 3 tasi fremvorklar deyiladi
#2 tuga bolinadi 1 mikor
#django = bu umumiy dasturlash uchun
#django-rest-framerok - ni faqat beackend uchun
#HTTPS = umumiy internetda
#HTTP = lokal
#HTTPS protacol = bu

#beknetni asosiy vazifasi
#1)yaratish)
#2)yaratish)
#3)korish  ) == (CRUD)
#4)ochirish)
#predstavlniya = malumotlani fililaydi
#serialusers = malaamutolarni jsonga yoki textga ogiradi
#---------------------------------------------------------------------------------------------------------------------------------------keyingi
# 🟩 2xx – Muvaffaqiyatli
# Kod	Nomi	Tushuntirish
# 200 OK	✅	So‘rov muvaffaqiyatli, hamma narsa joyida.
# 201 Created	🧱	Yangi resurs yaratildi (masalan, POST orqali ma’lumot qo‘shilganda).
# 204 No Content	🕳️	So‘rov bajarildi, lekin javobda hech narsa yo‘q.
# 🟦 3xx – Yo‘naltirishlar
# Kod	Nomi	Tushuntirish
# 301 Moved Permanently	🔁	Resurs butunlay boshqa manzilga ko‘chirilgan.
# 302 Found	📍	Resurs vaqtincha boshqa joyda joylashgan.
# 304 Not Modified	💾	Resurs o‘zgarmagan (cache dan foydalanish mumkin).
# 🟧 4xx – Mijoz xatolari
# Kod	Nomi	Tushuntirish
# 400 Bad Request	🚫	So‘rov noto‘g‘ri yuborilgan.
# 401 Unauthorized	🔐	Avtorizatsiya kerak (login/token yo‘q).
# 403 Forbidden	⛔	Kirish taqiqlangan, lekin login to‘g‘ri.
# 404 Not Found	❓	Resurs topilmadi (eng mashhuri 😅).
# 405 Method Not Allowed	❌	Bu URL uchun bu usul (masalan, POST) ruxsat etilmagan.
# 429 Too Many Requests	🚨	Juda ko‘p so‘rov yuborilgan (rate limit).
# 🟥 5xx – Server xatolari
# Kod	Nomi	Tushuntirish
# 500 Internal Server Error	💥	Server ichida kutilmagan xato.
# 501 Not Implemented	🧩	Server bu funksiyani qo‘llab-quvvatlamaydi.
# 502 Bad Gateway	⚡	Server boshqa serverdan noto‘g‘ri javob oldi.
# 503 Service Unavailable	💤	Server vaqtincha ishlamayapti (masalan, texnik xizmatda).
# 504 Gateway Timeout	⏰	Serverdan javob keldi, lekin kechikib.
#-----------------------------------------------------------------------------------------uy ishi
#from django.db import models
# class Student(models.Model):
#     name = models.CharField(max_length=100)
#     age = models.IntegerField()
#     grade = models.CharField(max_length=10)
#
#     def __str__(self):
#         return self.name
#models ga shular yoziladi va
#1.save()
# student = Student(name="Ali", age=16, grade="10A")
# student.save()
# malumot qoshadi


# 3. objects.all()
# Barcha yozuvlarni (recordlarni) chiqaradi.
# students = Student.objects.all()

# 4. objects.filter()
# Filtrlash uchun ishlatiladi (ya’ni WHERE sharti).
# ten_b_students = Student.objects.filter(grade="10B")
#
# 5. objects.get()
# Bitta yozuvni olish uchun (agar 1 ta bo‘lsa).
# student = Student.objects.get(id=1)
#
# 6. objects.exclude()
# Berilgan shartga mos bo‘lmagan ma’lumotlarni oladi.
# not_10b = Student.objects.exclude(grade="10B")
#
# 7. objects.order_by()
# Ma’lumotlarni tartiblash.
# students = Student.objects.order_by("age")       # yosh bo‘yicha o‘sish tartibida
# students = Student.objects.order_by("-age")      # kamayish tartibida
#
# 8. count()
# Nechta yozuv borligini hisoblaydi.
# Student.objects.count()
#
# 9. update()
# Bir nechta yozuvlarni yangilash.
# Student.objects.filter(grade="10A").update(grade="11A")
#
# 10. delete()
# Ma’lumotni o‘chirish.
# Student.objects.get(id=3).delete()
#
# 11. values() / values_list()
# Ma’lumotni lug‘at (dict) yoki ro‘yxat (list) sifatida qaytaradi.
# Student.objects.values("name", "grade")
# Student.objects.values_list("name", flat=True)
#-----------------------------------------------------------------------------------------uy ishi
# 🌐 Django’da WSGI va ASGI nima?
#
# Django — bu web-framework, ya’ni u brauzerdan keladigan so‘rovlarni (HTTP request) qabul qilib, javob (response) qaytaradi.
# Lekin Django o‘zi buni to‘g‘ridan-to‘g‘ri qilolmaydi — bu ishni server interfeysi degan narsa bajaradi.
#
# Shu yerda ikkita muhim texnologiya mavjud 👇
#
# Texnologiya	To‘liq nomi	Django versiyasi
# 🧩 WSGI	Web Server Gateway Interface	Django 3.0 gacha (klassik usul)
# ⚡ ASGI	Asynchronous Server Gateway Interface