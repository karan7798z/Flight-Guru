#This is the code for API Creation. We have used the Flask Web Application Framework for this,
# as it offers a simple, lucid set of statements derived from it's numerous classes,
# making the process of routing endpoints very easy.

#For establishing SQL Connections, creating and executing SQL Queries we have used MySQLdb Library of python.
from flask import Flask, jsonify
import MySQLdb

app = Flask(__name__)

#Below is the connection string that we will use to connect to the EC2 instance of Centos,
# upon which resides our MariaDB Galera Cluster
conn = MySQLdb.connect(
        host='ec2-18-191-91-177.us-east-2.compute.amazonaws.com',
        port=3306,
        user='jack',
        password='pleasework',
        db='flights'
    )

#In the section below, we have created 3 endpoints, each of which correpsond to 3 different functionalities
#for which our front end would be calling our API.

#Below endpoint - /getAllAirports would be called on the front page,
#to populate the drop downs for selection of Origin and Destination.
#It returns the entire list of Airport Codes and Names as stored in the Database

@app.route('/getAllAirports')
def getAirports():
    curr = conn.cursor()
    curr.execute("select Code, REPLACE(REPLACE(Name, '\n', ''), '\r', '') as Name from airport;")

    #Below section was added to convert the returned dataset, into a parsable JSON object to make it readable for the front end.
    rows = curr.fetchall()
    columns = [desc[0] for desc in curr.description]
    result = []
    for row in rows:
        row = dict(zip(columns, row))
        result.append(row)
    response = jsonify(result)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

#Below endpoint - /getBetFlights would be called after user submits his request to find the best flights on the first page.
#We will be using his inputs, to parameterize the written SQL Query, that fetches the best flights (flights with minimum delay)
#for his route during his requested time of the year.

@app.route('/getBestFlights')
def getFlights():
    curr = conn.cursor(prepared=True)
    curr.execute("SELECT a.AIRLINE, OP_CARRIER, ORIGIN, DEST, CONVERT(AVG(DEP_DELAY + ARR_DELAY), int) as 'TOTAL_AV_DELAY' from flight f join airline a on a.IATA_CODE = f.OP_CARRIER where ORIGIN = 'DFW' and DEST = 'IAH' group by(OP_CARRIER) order by AVG(DEP_DELAY + ARR_DELAY) LIMIT 5;")    

    #Below section was added to convert the returned dataset, into a parsable JSON object to make it readable for the front end.
    rows = curr.fetchall()
    columns = [desc[0] for desc in curr.description]
    result = []
    for row in rows:
        row = dict(zip(columns, row))
        result.append(row)
    response = jsonify(result)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

#Below endpoint - /getTopDestinations would be called after user submits his request on the first page, by inputting his origin, destination
#and travel date information.
#This endpoint would in turn execute the SQL query that will return top 5 destinations based on their popularity,
#that the user can plan visiting during his requested time of the year.

@app.route('/getTopDestinations')
def getDestinations():
    curr = conn.cursor(prepared=True)
    curr.execute("select DEST, ORIGIN, convert(Month, int) as Month, count(*) as 'No_Of_Flights' from flight_plan where ORIGIN = 'DFW' and Month = MONTH('2009/12/21') group by DEST order by count(*) desc LIMIT 5;")

    #Below section was added to convert the returned dataset, into a parsable JSON object to make it readable for the front end.
    rows = curr.fetchall()
    columns = [desc[0] for desc in curr.description]
    result = []
    for row in rows:
        row = dict(zip(columns, row))
        result.append(row)
    response = jsonify(result)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == '__main__':
    app.run(debug=True, host='192.168.0.104')