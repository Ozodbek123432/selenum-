# import mysql.connector
#
# # 🔹 Ma’lumotlar bazasiga ulanish
# db = mysql.connector.connect(
#     host="localhost",     # server manzili
#     user="linux",          # foydalanuvchi
#     password="linux128",     # parol
#     database="school_db "  # bazaning nomi
# )
#
# cursor = db.cursor()
#
# # 🔹 So‘rov yuborish
# cursor.execute("SELECT COUNT(*) AS count FROM students WHERE grade = '10 B';")
#
# # 🔹 Natijani olish
# result = cursor.fetchone()
# print("10-B sinfidagi o‘quvchilar soni:", result[0])
#
# # 🔹 Yopish
# cursor.close()
# db.close()
class Person:
    def __init__(self,ism,yosh):
        self.name = ism
        self.age = yosh

    def commare_age(self,other):
        if self.age < other.yosh:
            return f"{other.ism} mendan kata"
        elif self.age > other.yosh:
            return f"{other.ism} mendan kichik"
        else:
            return f"men { other.ism} bilanan teng"
p1 = Person("sayod",15)
p2 = Person("ziyo",15)
p3 = Person("isim", 14)

print(p1.commare_age(p1))
print(p2.commare_age(p2))
print(p3.commare_age(p3))
