import json
import requests
from django.shortcuts import render,HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from .models import premier_users
import csv
import time
import os
import requests
import json
from os import chdir

# Create your views here.
def premium_users(request):
    paramdetails = {'fullDetails':'True', 'offset':'0', 'limit':'1000'}
    url = "https://premierkenya.sandbox.mambu.com/api/users"
    
    premier_users = requests.get(url, auth=('api.user', 'apiuser@2018#'))
    premier_usersjson =prem_user.json()
    for rw in premier_usersjson:
        firstName=rw.get('firstName')
        lastName=rw.get('lastName')
        status=rw.get('userState')
        title=rw.get('title')
        email=rw.get('email')

        try:
            branch=rw.get('assignedBranchKey')
        except ObjectDoesNotExist:
            branch=''

        names=str(firstName) + " " + str(lastName)
        premier_users(
            names=names,
            status=status,
            title=title,
            email=email,
            branch_key=branch
        ).save()
    return HttpResponse('It posted')

def get_csv(request):
    url ="https://premierkenya.mambu.com/api/"
    user = ('DEPAPI', '[&7B&Hq#MchM')
    with open('/home/evans/Desktop/premium/prem/prem_test/static/Assets/Clients-premierkenya.csv') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            clientsurl = url+"clients/{0}".format(', '.join(row))
            client = requests.get(clientsurl, auth=user)
            clientsload = client.json()
        
            assignedBranchkey=clientsload['assignedBranchKey']
            email_add=''
            all_users=premier_users.objects.filter(branch_key=assignedBranchkey)
            for rw in all_users:
                email = rw.email
                title = rw.title
                status = rw.status
                names=rw.names

                if title == 'Branch Manager' and status == 'ACTIVE':
                    email_add = email
        return email_add

             
        