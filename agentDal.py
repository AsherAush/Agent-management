import mysql.connector

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="eagleEyeDB"
    )
    print("✅ הצלחה! חיבור ל-MySQL דרך XAMPP בוצע בהצלחה.")
    conn.close()
except mysql.connector.Error as err:
    print("❌ שגיאה בהתחברות:", err)
