from extraLogic import shouldBePreFormatted
import psycopg2
try:
    connection = psycopg2.connect(user = "postgres",
                                  password = "Mango@008",
                                  host = "localhost",
                                  port = "5432",
                                  database = "postgres")

    cursor = connection.cursor()
    # Print PostgreSQL Connection properties
    print ( connection.get_dsn_parameters(),"\n")

    # Print PostgreSQL version
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("You are connected to - ", record,"\n")
    print("--------------------------------------------")
    cursor.execute("SELECT * FROM review;")
    for row in cursor:
        review = row[2]
        isPreFormatted = shouldBePreFormatted(review)
        cursor2 = connection.cursor()
        cursor2.execute(f"UPDATE review SET ispreformatted = {isPreFormatted} WHERE isbn = '{row[1]}';")
    connection.commit()


except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)
finally:
    #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
