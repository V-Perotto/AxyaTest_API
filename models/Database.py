from models.db import mysql

class Database:
    
    def get_connection_and_cursor(self):
        conn = mysql.connect()
        cursor = conn.cursor()
        return conn, cursor
    
    def close(self, conn, cursor) -> None:
        cursor.close()
        conn.close()
        
    def commit_and_close(self, conn, cursor) -> None:
        conn.commit()
        self.close(conn, cursor)