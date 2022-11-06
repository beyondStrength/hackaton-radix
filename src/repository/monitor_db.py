import mysql.connector
vitals_monitor_db = mysql.connector.connect(
  host="localhost",
  user="apl.vitals_monitor",
  password="vitals_monitor_user_pwd",
  database="db_vitals_monitor"
)

sql_insert = """
    INSERT INTO vitals_monitor (
        name,
        age,
        role,
        heart_rate,
        blood_presure_high,
        blood_presure_low,
        sleep,
        datetime,
        accident)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""


def insert(values):
  db_cursor = vitals_monitor_db.cursor()
  db_cursor.execute(sql_insert, values)


def commit():
  vitals_monitor_db.commit()
