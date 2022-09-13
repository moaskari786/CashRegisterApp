''' What this file does is allow an user to checkout items from README.txt'''
#Mohammad Askari
#MCS260 Project 4 Cash Register
#I acknowlefge the code of conduct and attest that I've worked on this project by myself
import csv
from csv import writer
from csv import DictWriter
import pandas as pd

jj=[]
alist=[]
prices=[]
le=[]
reciept=['Serial Number','Item Name','SKU','Price','Type']
with open('grocery.csv', 'r') as file:  # what this has done 
    reader = csv.reader(file) 
    for row1 in reader:
        alist.append(row1[1])

with open('rewardsmember.csv', 'r') as file2:  # what this has done 
    reader2 = csv.reader(file2)
    for row in reader2:
        jj.append(row)
with open('grocery.csv', 'r') as file3:  # what this has done 
    reader = csv.reader(file3) 
    for row1 in reader:
        prices.append(row1[3])
with open('reciept.csv', 'w', encoding='UTF8') as f:
                            
    writer2 = csv.writer(f)
    writer2.writerow(reciept)

inventory = reader
basket=[]
total=[]
itemdata=[]

def cashier():
    '''main program that allows the user to checkout'''
    customer=input("Hello are you a rewards remember \n if yes enter yes \n if no enter no \n if you want to sign up for rewards enter signup \n IF anytime you want to cancel the transaction just write exit\n ->")
    if customer=="exit":
        exit()
    if customer =="yes":
        rewardsnumberq= input("Enter your phone number ")
    if customer== "signup":

            newcustomerentry=input("Enter a phone number")

            le.append(newcustomerentry)

            with open('rewardsmember.csv', 'a', newline='\n') as f_object:

                writer_object = writer(f_object,)
                writer_object.writerow(le)
            while True:        
                scanner=input("scan your items ") 
                if scanner ==("exit"):
                            exit()
                            looked_up_item = None
                if scanner in alist:             #if the scanned item is in the list of product
                    with open('rmgrocery.csv', newline='') as csvfile:     #open up grocery csv and read it
                        
                        reader3 = csv.DictReader(csvfile)              #then make a dictionary out of the data

                        for row in reader3:                             #for every row of the csv file
                            itemdata.append(row)                        #add each row to the list of item data
                        
                        for item in itemdata:                           #for each value of item data aka each dictionary(e.g {'Serial Number': '01512947232', ' Item Name': 'Sugar', 'SKU': '15', ' Price': '$69', ' Type': 'Grocery'})
                            if item[" Item Name"] == scanner:           #if any of the dictionaries
                                looked_up_item = item
                                break        
                        
                        print(looked_up_item)
                        
                        with open ('reciept.csv','a')as f2:
                            field_names = ['Serial Number',' Item Name','SKU',' Price',' Type']
                            dictwriter_object = DictWriter(f2, fieldnames=field_names)
                                
                            dictwriter_object.writerow(looked_up_item)
                        with open ('reciept.csv','r')as csv_file1:
                            reader4=csv.reader(csv_file1)
                            csv_file1.__next__()
                            total=sum(int(row[3])for row in reader4)
                            print ("total:$",total)
                if scanner ==("Done"):
                    alist.append(scanner)
                    reciept_data=pd.read_csv('reciept.csv')
                    l=reciept_data.head()
                    print("heres your reciept\n",l,"\n total->$",total,"\n Come again" )
                    exit() 
                if scanner not in alist:
                        print("Item not found")  
                
                # if scanner == ("Done"):
                #         with open ('reciept.csv')as jfile:
                #             reader8=csv.reader(jfile)
                #             for row8 in reader8:
                #                 print(row8)
                #             exit()


    while True:
        
        if customer=="no":   
            looked_up_item = None
            scanner=input("scan your items ") #whatever the customer entered
            
            if scanner ==("exit"):
                exit()
                looked_up_item = None
            if scanner in alist:             #if the scanned item is in the list of product
                with open('grocery.csv', newline='') as csvfile:     #open up grocery csv and read it
                    
                    reader3 = csv.DictReader(csvfile)              #then make a dictionary out of the data

                    for row in reader3:                             #for every row of the csv file
                        itemdata.append(row)                        #add each row to the list of item data
                    
                    for item in itemdata:                           #for each value of item data aka each dictionary(e.g {'Serial Number': '01512947232', ' Item Name': 'Sugar', 'SKU': '15', ' Price': '$69', ' Type': 'Grocery'})
                        if item[" Item Name"] == scanner:           #if any of the dictionaries
                            looked_up_item = item
                            break        
                    if looked_up_item == None:
                        print("Item not found")
                    else:
                        print(looked_up_item)
                    
                    with open ('reciept.csv','a')as f2:
                        field_names = ['Serial Number',' Item Name','SKU',' Price',' Type']
                        dictwriter_object = DictWriter(f2, fieldnames=field_names)
                            
                        dictwriter_object.writerow(looked_up_item)
                    with open ('reciept.csv','r')as csv_file1:
                        reader4=csv.reader(csv_file1)
                        csv_file1.__next__()
                        total=sum(int(row[3])for row in reader4)
                        print ("total:$",total)
            if scanner ==("Done"):
                alist.append(scanner)
                reciept_data=pd.read_csv('reciept.csv')
                l=reciept_data.head()
                print("heres your reciept\n",l,"\n total->$",total,"\n Come again" )
                exit()
            if scanner not in alist:
                print("Item not found")
            
        if customer =="yes":
            for it in jj:
                if rewardsnumberq in it:
                    scanner=input("scan your items ") #whatever the customer entered
            
                    if scanner ==("exit"):
                        exit()
                        looked_up_item = None
                    if scanner in alist:             #if the scanned item is in the list of product
                        with open('rmgrocery.csv', newline='') as csvfile:     #open up grocery csv and read it
                            
                            reader3 = csv.DictReader(csvfile)              #then make a dictionary out of the data

                            for row in reader3:                             #for every row of the csv file
                                itemdata.append(row)                        #add each row to the list of item data
                            
                            for item in itemdata:                           #for each value of item data aka each dictionary(e.g {'Serial Number': '01512947232', ' Item Name': 'Sugar', 'SKU': '15', ' Price': '$69', ' Type': 'Grocery'})
                                if item[" Item Name"] == scanner:           #if any of the dictionaries
                                    looked_up_item = item
                                    break        
                           
                            print(looked_up_item)
                            
                            with open ('reciept.csv','a')as f2:
                                field_names = ['Serial Number',' Item Name','SKU',' Price',' Type']
                                dictwriter_object = DictWriter(f2, fieldnames=field_names)
                                    
                                dictwriter_object.writerow(looked_up_item)
                            with open ('reciept.csv','r')as csv_file1:
                                reader4=csv.reader(csv_file1)
                                csv_file1.__next__()
                                total=sum(int(row[3])for row in reader4)
                                print ("total:$",total)
                    if scanner ==("Done"):
                        alist.append("Done")
                        reciept_data=pd.read_csv('reciept.csv')
                        l=reciept_data.head()
                        print("heres your reciept\n",l,"\n total->$",total,"\n Come again" )
                        exit()
                    if scanner not in alist:
                            print("Item not found")
                
                
                    

        
cashier()

