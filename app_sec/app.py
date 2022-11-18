import os
import cherrypy
import DatabaseFunctions
import sys
import json
import encryption
import base64

#Init server in port 10009
cherrypy.config.update({'server.socket_port':10009})
path = os.path.abspath(os.path.dirname("../"))

databaseFileName = "Database.db"

#Directories for resources
conf = {
    "/WebResources": {
        "tools.staticdir.on": True,
        "tools.staticdir.dir": os.path.join(path, "WebResources")
    }
}

class Root(object):
    def __init__(self):
        pass

    @cherrypy.expose
    def default(self):
        return open("../WebResources/index.html").read()
    @cherrypy.expose
    def appointments(self):
        return open("../WebResources/appointments.html").read()
    @cherrypy.expose
    def loginregister(self):
        return open("../WebResources/loginregister.html").read()
    @cherrypy.expose
    def profile(self):
        return open("../WebResources/profile.html").read()

    @cherrypy.expose
    def getServices(self):
        return DatabaseFunctions.getServices(databaseFileName)

    @cherrypy.expose
    def getDoctors(self):
        return DatabaseFunctions.getDoctors(databaseFileName)

    @cherrypy.expose
    def getDoctorsByService(self, serviceID):
        return DatabaseFunctions.getDoctorsByService(databaseFileName, serviceID)

    @cherrypy.expose
    def getBookingsByDoctor(self, doctorID):
        return DatabaseFunctions.getBookingsByDoctors(databaseFileName, doctorID)

    @cherrypy.expose
    def getAvailability(self, doctorID, date):
        bookings = json.loads(DatabaseFunctions.getBookingsByDoctors(databaseFileName, doctorID))
        if len(bookings) != 0:
            for booking in bookings:
                if booking["date"]==date:
                    return json.dumps(False)
            return json.dumps(True)
        else:
            return json.dumps(True)

    @cherrypy.expose
    def getTestResultByCode(self, code, userID):
        result = json.loads(DatabaseFunctions.getTestResultByCode(databaseFileName, str(code), str(userID)))
        if len(result) != 0:
            f = open("TestResults/"+str(code)+".txt", "r")
            #doctorInfo = json.loads(DatabaseFunctions.getDoctorsByID(databaseFileName, result[0]["doctorID"]))
            #serviceInfo = json.loads(DatabaseFunctions.getServiceByID(databaseFileName, result[0]["serviceID"]))
            #fileText = "|||---TEST RESULT --------------------|||\n" + "DOCTOR: " + doctorInfo[0]["name"] 
            #fileText = fileText + "\nSERVICE: " + serviceInfo[0]["name"]
            #fileText = fileText + "\n\n" + f.read()
            #fileText = fileText + "\n|||-----------------------------------|||"
            #return json.dumps(fileText)
            return(json.dumps(f.read()))
        else:
            return json.dumps(False)
        
    @cherrypy.expose
    def getProfileForLogin(self, email, password):
        result = json.loads(DatabaseFunctions.getProfileForLogin(databaseFileName, email, password))
        if len(result) !=0:
            return json.dumps(result[0])
        else:
            return json.dumps(False)

    @cherrypy.expose
    def getUserInfo(self, userID):
        return DatabaseFunctions.getUserInfo(databaseFileName, userID)

    @cherrypy.expose
    def postContact(self, title, text, date, email, name):
        info = {"title" : title, "text" : text, "date" : date, "email" : email, "name" : name}
        return DatabaseFunctions.postContact(databaseFileName, info)

    @cherrypy.expose
    def postBooking(self, date, doctorID, userID, serviceID, encryptedEmail):
        userPassword = json.loads(DatabaseFunctions.getUserInfo(databaseFileName, userID))[0]["password"]
        b = base64.b64decode(encryptedEmail.encode('utf-8'))
        print(userPassword)
        print(encryption.decryptBytes(b, userPassword, "cryptoKeys/"+str(userID)+"_privK.pem"))
        info = {"date": date, "doctorID": doctorID, "userID": userID, "serviceID": serviceID}
        return DatabaseFunctions.postBooking(databaseFileName,info)

    @cherrypy.expose
    def getBookingsByUser(self, userID):
        return DatabaseFunctions.getBookingsByUser(databaseFileName, int(userID))

    @cherrypy.expose
    def postProfile(self, name, email, password):
        info ={"name": name, "email": email, "password": password}
        return DatabaseFunctions.postProfile(databaseFileName,info)

cherrypy.quickstart(Root(), '/', config=conf)