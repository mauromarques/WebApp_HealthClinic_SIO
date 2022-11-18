import sqlite3 as sql
import sys
import json
import os
import datetime
import encryption
import base64

#Checks if table exists, otherwise create it
def tableExists(cs, tableCreation):
    cs.execute("CREATE TABLE IF NOT EXISTS " +tableCreation+";")

def create_connection(db_file):
    conn = None
    try:
        conn = sql.connect(db_file)
        return conn
    except Exception as e:
        print(e)
    return conn

def getServices(database):
    db = create_connection(database)
    if db is not None:
        cs = db.cursor()
        tableExists(cs, "services(name TEXT, price REAL, description TEXT, serviceID INTEGER PRIMARY KEY, picture TEXT)" )
        #cs.execute("INSERT INTO services(name, price, description, picture) VALUES(?,?,?,?)", ("Service1", 19.52, "This is service 1", "/WebResources/cardiology.jpg"))
        #cs.execute("INSERT INTO services(name, price, description, picture) VALUES(?,?,?,?)", ("Service2", 21.78, "This is service 2", "/WebResources/orthopedic.jpg"))
        #cs.execute("INSERT INTO services(name, price, description, picture) VALUES(?,?,?,?)", ("Service3", 35.45, "This is service 3", "/WebResources/pulmonoly.jpg"))
        #db.commit()
        result = cs.execute("SELECT * FROM services")
        rows = result.fetchall()
        array = []
        if rows != None:
            for row in rows:
                dic = {}
                dic["name"] = row[0]
                dic["price"] = row[1]
                dic["description"] = row[2]
                dic["serviceID"] = row[3]
                dic["picture"] = row[4]
                array.append(dic)
        cs.close()
        db.close()
        return json.dumps(array)

def getDoctorsByService(database, serviceID):
    db = create_connection(database)
    if db is not None:
        cs = db.cursor()
        tableExists(cs, "doctors(name TEXT, ratings REAL, specialties TEXT, doctorID INTEGER PRIMARY KEY, picture TEXT)")
        sID = "%"+str(serviceID)+"%"
        result = cs.execute("SELECT * FROM doctors WHERE specialties LIKE ?",[sID])
        rows = result.fetchall()
        array = []
        if rows != None:
            for row in rows:
                dic = {}
                dic["name"] = row[0]
                dic["ratings"] = row[1]
                dic["specialties"] = row[2]
                dic["doctorID"] = row[3]
                dic["picture"] = row[4]
                array.append(dic)
        for r in array:
            print(r)
        cs.close()
        db.close()
        return json.dumps(array)

def getDoctorsByID(database, doctorID):
    db = create_connection(database)
    if db is not None:
        cs = db.cursor()
        tableExists(cs, "doctors(name TEXT, ratings REAL, specialties TEXT, doctorID INTEGER PRIMARY KEY, picture TEXT)")
        dID = "%"+str(doctorID)+"%"
        result = cs.execute("SELECT * FROM doctors WHERE doctorID LIKE %?%",[dID])
        rows = result.fetchall()
        array = []
        if rows != None:
            for row in rows:
                dic = {}
                dic["name"] = row[0]
                dic["ratings"] = row[1]
                dic["specialties"] = row[2]
                dic["doctorID"] = row[3]
                dic["picture"] = row[4]
                array.append(dic)
        for r in array:
            print(r)
        cs.close()
        db.close()
        return json.dumps(array)

def getDoctors(database):
    db = create_connection(database)
    if db is not None:
        cs = db.cursor()
        tableExists(cs, "doctors(name TEXT, ratings REAL, specialties TEXT, doctorID INTEGER PRIMARY KEY, picture TEXT)")
        #cs.execute("INSERT INTO doctors(name, ratings, specialties, picture) VALUES(?,?,?,?)", ("Maria do Carmo", 4.95, "id1, id2", "/WebResources/cardiology.png"))
        #cs.execute("INSERT INTO doctors(name, ratings, specialties, picture) VALUES(?,?,?,?)", ("Arnaldo Silva", 3.67, "id1", "/WebResources/cardiology.png"))
        #cs.execute("INSERT INTO doctors(name, ratings, specialties, picture) VALUES(?,?,?,?)", ("Mirela Algores", 4.5, "id3", "/WebResources/cardiology.png"))
        #db.commit()
        result = cs.execute("SELECT * FROM doctors")
        rows = result.fetchall()
        array = []
        if rows != None:
            for row in rows:
                dic = {}
                dic["name"] = row[0]
                dic["ratings"] = row[1]
                dic["specialties"] = row[2]
                dic["doctorID"] = row[3]
                dic["picture"] = row[4]
                array.append(dic)
        for r in array:
            print(r)
        cs.close()
        db.close()
        return json.dumps(array)

def getServiceByID(database, serviceID):
    db = create_connection(database)
    if db is not None:
        cs = db.cursor()
        tableExists(cs, "services(name TEXT, price REAL, description TEXT, serviceID INTEGER PRIMARY KEY, picture TEXT)" )
        result = cs.execute("SELECT * FROM services WHERE serviceID = ?",[str(serviceID)])
        rows = result.fetchall()
        array = []
        if rows != None:
            for row in rows:
                dic = {}
                dic["name"] = row[0]
                dic["price"] = row[1]
                dic["description"] = row[2]
                dic["serviceID"] = row[3]
                dic["picture"] = row[4]
                array.append(dic)
        cs.close()
        db.close()
        return json.dumps(array)

def getBookings(database):
    db = create_connection(database)
    if db is not None:
        cs = db.cursor()
        tableExists(cs, "bookings(date TEXT, doctorID INTEGER, userID INTEGER, serviceID INTEGER, bookingID INTEGER PRIMARY KEY)" )
        #cs.execute("INSERT INTO bookings(date, doctorID, userID, serviceID, bookingID) VALUES(?,?,?,?,?)", ("15-10-2022", "id1", "id1", "id1", "id1"))
        #cs.execute("INSERT INTO bookings(date, doctorID, userID, serviceID, bookingID) VALUES(?,?,?,?,?)", ("24-12-2022", "id1", "id2", "id1", "id2"))
        #cs.execute("INSERT INTO bookings(date, doctorID, userID, serviceID, bookingID) VALUES(?,?,?,?,?)", ("05-11-2022", "id1", "id3", "id2", "id3"))
        #db.commit()
        result = cs.execute("SELECT * FROM bookings")
        rows = result.fetchall()
        array = []
        if rows != None:
            for row in rows:
                dic = {}
                dic["date"] = row[0]
                dic["doctorID"] = row[1]
                dic["userID"] = row[2]
                dic["serviceID"] = row[3]
                dic["bookingID"] = row[4]
                array.append(dic)
        cs.close()
        db.close()
        return json.dumps(array)

def getBookingsByDoctors(database, doctorID):
    bookings = json.loads(getBookings(database))
    array = []
    for booking in bookings:
        if booking["doctorID"] == int(doctorID):
            array.append(booking)
    return json.dumps(array)

def getBookingsByUser(database, userID):
    bookings = json.loads(getBookings(database))
    array = []
    for booking in bookings:
        if booking["userID"] == userID:
            array.append(booking)
    return json.dumps(array)

def getTestResultByCode(database, code, userID):
    db = create_connection(database)

    if db is not None:
        cs = db.cursor()
        tableExists(cs, "results(content TEXT, doctorID INTEGER, userID INTEGER, serviceID INTEGER, resultID INTEGER PRIMARY KEY)" )
        #cs.execute("INSERT INTO results(content, doctorID, userID, serviceID) VALUES(?,?,?,?)", ("This is the result of a test 3", "1", "1", "1"))
        #db.commit()
        result = cs.execute("SELECT * FROM results WHERE resultID = ? AND userID = ?;",(str(code),str(userID)))
        rows = result.fetchall()
        array = []
        if rows != None:
            for row in rows:
                dic = {}
                dic["content"] = row[0]
                dic["doctorID"] = row[1]
                dic["userID"] = row[2]
                dic["serviceID"] = row[3]
                dic["resultID"] = row[4]
                array.append(dic)
        cs.close()
        db.close()
        return json.dumps(array)

def getProfileForLogin(database, email, password):
    db = create_connection(database)
    if db is not None:
        cs = db.cursor()
        tableExists(cs, "users(name TEXT, email TEXT, password TEXT, userID INTEGER PRIMARY KEY)" )
        #cs.execute("INSERT INTO users(name, birthday, gender, email, password, userID) VALUES(?,?,?,?,?,?)", ("Mauro Marques", "15-10-1999", "M", "mmcanhao@gmail.com", "Barnabe", "id1"))
        #db.commit()
        email = email.replace("'","")
        result = cs.execute("SELECT * FROM users WHERE email = ? AND password = ?;",(email,password))
        rows = result.fetchall()
        array = []
        if rows != None:
            for row in rows:
                dic = {}
                dic["email"] = row[1]
                dic["password"] = row[2]
                dic["userID"] = row[3]
                dic["name"] = encryption.decryptBytes( row[0], dic["password"], "cryptoKeys/"+str(dic["userID"])+"_privK.pem")
                dic["email"] = base64.b64encode(encryption.encryptString(row[1], "cryptoKeys/"+str(dic["userID"])+"_pubK.pem")).decode('utf-8')
                array.append(dic)
        cs.close()
        db.close()
        return json.dumps(array)

def getUserInfo(database,userID):
    db = create_connection(database)
    if db is not None:
        cs = db.cursor()
        tableExists(cs, "users(name TEXT, email TEXT, password TEXT, userID INTEGER PRIMARY KEY)" )
        #cs.execute("INSERT INTO users(name, birthday, gender, email, password) VALUES(?,?,?,?,?)", ("Mauro Marques", "15-10-1999", "M", "mmcanhao@gmail.com", "Barnabe"))
        #db.commit()
        result = cs.execute("SELECT * FROM users WHERE userID=?",[str(userID)])
        rows = result.fetchall()
        array = []
        if rows != None:
            for row in rows:
                dic = {}
                dic["name"] = row[0]
                dic["email"] = row[1]
                dic["password"] = row[2]
                dic["userID"] = row[3]
                dic["name"] =  encryption.decryptBytes( dic["name"], row[2], "cryptoKeys/"+str(dic["userID"])+"_privK.pem")
                array.append(dic)
        cs.close()
        db.close()
        return json.dumps(array)

def postContact(database,contactInfo):
    db = create_connection(database)
    if db is not None:
        cs = db.cursor()
        tableExists(cs, "contacts(title TEXT, text TEXT, date TEXT, name TEXT, email TEXT, contactID INTEGER PRIMARY KEY)" )
        cs.execute("INSERT INTO contacts(title, text, date, name, email) VALUES(?,?,?,?,?)", (contactInfo["title"], contactInfo["text"], contactInfo["date"], contactInfo["name"], contactInfo["email"]))
        db.commit()
    now = datetime.datetime.now()
    dt_string = now.strftime("%d_%m_%Y %H:%M:%S")
    dt_string.replace("/", "_")
    arr = dt_string.split()
    pat = os.path.join("Contacts", arr[0]+arr[1]+".txt")
    f = open(pat,"w")
    #f = open("Contacts/"+contactInfo["title"],"w")
    f.write(contactInfo["date"] + " || " + contactInfo["email"] + " || " + contactInfo["name"] +"\n")
    f.write(contactInfo["title"]+"\n")
    f.write(contactInfo["text"])
    f.close()
    return

def postBooking(database,bookingInfo):
    db = create_connection(database)
    if db is not None:
        cs = db.cursor()
        tableExists(cs, "bookings(date TEXT, doctorID INTEGER, userID INTEGER, serviceID INTEGER, bookingID INTEGER PRIMARY KEY)" )
        bookings = json.loads(getBookingsByDoctors(database,bookingInfo["doctorID"]))
        bookDate = str(bookingInfo["date"]).split('-')
        if len(bookDate) != 3 or not bookDate[0].isnumeric() or not bookDate[1].isnumeric() or not bookDate[2].isnumeric():
            return json.dumps(False)
        for b in bookings:
            if b["date"] == bookingInfo["date"]:
                return json.dumps(False)
        cs.execute("INSERT INTO bookings(date, doctorID, userID, serviceID) VALUES(?,?,?,?)", (bookingInfo["date"], bookingInfo["doctorID"], bookingInfo["userID"], bookingInfo["serviceID"]))
        db.commit()
    return json.dumps(True)

def postProfile(database,profileInfo):
    db = create_connection(database)
    if db is not None:
        cs = db.cursor()
        tableExists(cs, "users(name TEXT, email TEXT, password TEXT, userID INTEGER PRIMARY KEY)" )
        result = cs.execute("SELECT * FROM users WHERE email=?", [str(profileInfo["email"])])
        rows = result.fetchall()
        if rows:
            return json.dumps(False)
        #cs.execute("INSERT INTO users(name, email, password) VALUES("+profileInfo["name"]+","+profileInfo["email"]+","+encryptedPass+");")
        values_to_insert = (profileInfo["name"], profileInfo["email"], profileInfo["password"])
        cs.execute("INSERT INTO users(name, email, password) VALUES(?, ?, ?)", values_to_insert)
        profile = cs.execute("SELECT * FROM users WHERE email=?", [str(profileInfo["email"])]).fetchall()[0][3]
        email = cs.execute("SELECT * FROM users WHERE email=?", [str(profileInfo["email"])]).fetchall()[0][1]
        encryption.generateKeys(profileInfo["password"], str(profile))
        encryptedName = encryption.encryptString(profileInfo["name"], "cryptoKeys/"+str(profile)+"_pubK.pem")
        cs.execute("UPDATE users SET name = ? WHERE email = ?", (encryptedName, profileInfo["email"]))
        db.commit()
    return json.dumps([profile, base64.b64encode(encryption.encryptString(email, "cryptoKeys/"+str(profile)+"_pubK.pem")).decode('utf-8')])


#cs.execute("ALTER TABLE services ADD picture TEXT;")
#cs.execute("UPDATE services SET picture ='/WebResources/cardiology.jpg' WHERE serviceID=1;")
#cs.execute("UPDATE services SET picture ='/WebResources/orthopedic.jpg' WHERE serviceID=2;")
#cs.execute("UPDATE services SET picture ='/WebResources/pulmonoly.jpg' WHERE serviceID=3;")
#db.commit()
#print(json.loads(getServices("Database.db")))
#info = {"date": "2022-11-15", "doctorID": "1", "userID": "1", "serviceID": "1"}
#print(postBooking("Database.db", info))
#print(getBookingsByDoctors("Database.db", info["doctorID"]))

#db = create_connection("Database.db")
#cs = db.cursor()
#cs.execute("ALTER TABLE users DROP COLUMN birthday ;")
#cs.execute("ALTER TABLE users DROP COLUMN gender ;")
#db.commit()
#result = cs.execute("SELECT * FROM users").fetchall()
#print(result)
#c = "i"



#cs.execute("ALTER TABLE contacts ADD email TEXT;")
#info = {"title" : "title", "text" : "text", "date" : "date", "email" : "email", "name" : "name"}
#postContact("Database.db", info)

"""def getContactsByUserID(database, userID):
    db = create_connection(database)
    if db is not None:
        cs = db.cursor()
        tableExists(cs, "contacts(title TEXT, text TEXT, date TEXT, name TEXT, email TEXT, contactID INTEGER PRIMARY KEY)" )
        result = cs.execute("SELECT * FROM contacts WHERE userID = '"+userID+"';")
        rows = result.fetchall()
        array = []
        if rows != None:
            for row in rows:
                dic = {}
                dic["title"] = row[0]
                dic["text"] = row[1]
                dic["date"] = row[2]
                dic["userID"] = row[3]
                dic["contactID"] = row[4]
                array.append(dic)
        cs.close()
        db.close()
        return json.dumps(array)"""

