import mysql.connector, json

# CREATE CONNECTIONS & CURSORS
def mysql_connect():
    conn = mysql.connector.connect(
        host="localhost",
        user="your_username",
        password="your_password",
        database="your_database"
    )
    return conn

# UPDATE DATABASE
def JSON_to_table(JSON_DIR, TABLE_NAME):
    conn = mysql_connect()
    cursor = conn.cursor()
    with open(JSON_DIR) as file:
        data = json.load(file)
    sensor_id = data['sensor_id']
    date = data['date']
    value = data['value']
    query = f"INSERT INTO {TABLE_NAME} (sensor_id, date, value) \
              VALUES ({sensor_id}, {date}, {value})"
    cursor.execute(query)
    conn.commit()