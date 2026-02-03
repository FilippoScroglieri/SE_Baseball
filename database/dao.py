from database.DB_connect import DBConnect
from model.squadra import Squadra


class DAO:
    @staticmethod
    def read_anni():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ SELECT distinct t.year 
                    FROM team t 
                    WHERE year>= 1980"""

        cursor.execute(query)

        for row in cursor:
            result.append(row['year']) # così facendo abbiamo una lista con tutti gli anni

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def read_squadre(anno):
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query= '''SELECT name,team_code 
                  FROM team 
                  WHERE year= %s'''
        cursor.execute(query, (anno,))
        for row in cursor:
            result.append(Squadra(**row))
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def read_stipendi(anno):
        conn = DBConnect.get_connection()
        result = {}
        cursor = conn.cursor(dictionary=True)
        query = """ SELECT team_code , SUM(salary) as StipendioTot
                    FROM salary
                    WHERE year= %s
                    GROUP BY team_code"""

        cursor.execute(query, (anno,))

        for row in cursor:
            result[row['team_code']] = row['StipendioTot'] # ho un dizionario che ha come chiavi i team code e come valori i loro stipendi totali

        cursor.close()
        conn.close()
        return result