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