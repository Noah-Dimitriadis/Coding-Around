'''IMPORTANT
Wont have to do this ever again!! 

dont run it, nothing bad *should* happen but lets just not ok :)
'''


import psycopg2

def openConnection():
    conn = psycopg2.connect(database = "goosenest", 
                        user = "admin", 
                        host= '192.168.2.13',
                        password = "94Ten743!",
                        port = 5432)

    return conn

def getWords():
    file = open("Wordle/WordBank.txt").readlines()
    return [line.strip() for line in file]   

def addWord(index, word, cursor):
    cursor.execute(f"INSERT INTO wordle(id, word) VALUES{index, word};")


if __name__ == "__main__":
    allWords = getWords()
    conn = openConnection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM wordle;")
    result = cursor.fetchall()
    print(result)
    
    index = 8
    for word in allWords[7:]:
        addWord(index, word, cursor)
        index += 1
        
        
    conn.commit()

    cursor.execute("SELECT * FROM wordle;")
    result = cursor.fetchall()
    print(result)
    conn.close()
    cursor.close()


