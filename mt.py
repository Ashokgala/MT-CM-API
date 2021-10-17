import json
from typing import Counter
import requests
import cherrypy


import time
import codecs
import datetime 

import os

import json


from flask import Flask, request, url_for , render_template

app = Flask(__name__)

@app.route('/hello')
def index():
    with app.test_request_context(
            url_for('hello'),
           # headers=request.headers.to_list(),
            query_string=request.query_string
    ):
        return app.dispatch_request()

@app.route('/')
def hello():

    return render_template('mt.html')

    
    #return 'Hello, {}!'.format(request.args.get('name', 'World'))

app.run(debug=True, port = 8080)


if(not os.path.exists("mt.txt")):
    f = open("mt.txt",'w')
    f.write("0")
    f.close()




stat = 0

import gspread
from oauth2client.service_account import ServiceAccountCredentials

def maino():

    try:
        scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

        creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

        client = gspread.authorize(creds)

        sheet2 = client.open("MT_CRM_Dump") # Open the spreadhseet

        

        sheet = sheet2.worksheet("Sheet1")

        print(sheet)
        data = sheet.get_all_records()
        print(data)

        hs = datetime.datetime.now().hour
        ms = datetime.datetime.now().min

        f = open("mt.txt","r")
        z1 = f.read()
        f.close()

        z1 = int(z1)
        print(z1)


        count = 1

        prev = 0


    except:

        
        print("Error Detected in google sheets")
        # url = f"https://script.google.com/macros/s/AKfycbzdqSbrwOZIc2zgAX0c2KkE_5sslZN8I0mWbqhXGmquhDwym8uYpegsrPVMmrNUJCx0/exec?error=true"

        # payload={}
        # headers = {}

        # print("Error")

        # response = requests.request("GET", url, headers=headers, data=payload)

        time.sleep(10.0)

        

        print(data)

        print("error detected in google sheet")

        maino()



    try:

        
        if len(data) != 0 or len(data) != 1:

            try:
                for i in data:

                    if count>=z1:

                        class index(object):
                            @cherrypy.expose
                            def html(self):

                                file = codecs.open("mt.html", "r", "utf-8")
                                print(file.read())

                        with app.test_request_context('/', method='POST'):
                            app.hello()

                        order_id = str(i["Order Ids"])

                        address = str(i["Modern Trade - Warehouse Location"])



                        print("Queue name value assigned")
                        
                        print(i)
                        print("Your id is below: " + order_id)

                        print("Your id is below: " + address)
                       
                       # name1 = str(i['house_type'])
                        name = str(i["client"])
                        # contact = str(i["mobile"])

                      

                        print(order_id)
                        

                    
                        # if(len(contact)>10):
                        #     contact = contact[-10:]
                        #     print(i)

                        # if len(contact)<=9:  
                        #     break

                        print(name,order_id)
                        index = open("mt.html").read()
                        return index


                        response = self.full_dispatch_request()

                        def myfunc():
                            with app.test_request_context('/', method='POST'):
                                app.maino()



                        maino()


            except Exception as e:

                print(e)

            
                payload={}
                headers = {}

                print("Error")

                time.sleep(30.0)

                main()




    except:
        
            print("Error Found in Queuing or sheet !")
            print("Queue Name is incorrect ! or left Blank !")
            time.sleep(5.0)
            main()

def main():
    try:
        for i in range(36000):
            print("Loop count",i)
            if i == 35999:
                main()
            if  i == 0:
                maino()
            else:
                time.sleep(5)
                maino()
    except:
        print("Logs Unfilled")
        main()
        



main()


        

