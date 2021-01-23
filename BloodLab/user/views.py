from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.

import pyodbc

server = 'sajjad\SQLSERVER2021'
database = 'BloodLab'
username = 'sa'
password = 's@j1563j@d'
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()
# tsql = "SELECT snn, firstName, lastName FROM [dbo].[User];"
# with cursor.execute(tsql):
#     row = cursor.fetchone()
#     while row:
#         print (str(row[0]) + " " + str(row[1])+ " "+str(row[2]))
#         row = cursor.fetchone()

class Signin (APIView) :

    def post (self, *args, **kwargs) :
        tsql = f"INSERT INTO [dbo].[User] (snn, password, firstName, lastName, sex, email, phone) VALUES (?,?,?,?,?,?,?);" 
        data = self.request.data
        with cursor.execute(tsql,data['snn'],data['password'],data['firstName'],data['lastName'],data['sex'],data['email'],data['phone'],):
            print ('Successfully Inserted!')

        return Response(data={
            "message" : "Successfuly inserted!"
        }, status=status.HTTP_201_CREATED)
        