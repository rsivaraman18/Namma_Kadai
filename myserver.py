import sqlite3
connection = sqlite3.connect('purchase.db')
cursor = connection.cursor()
cursor.execute('DROP TABLE customer')
connection.execute("CREATE TABLE customer(Id INTEGER PRIMARY KEY ,Item TEXT ,Price INTEGER , Quantity INTEGER ,Total INTEGER)")
print("customer Table created")
connection.close()



box=''
import sqlite3

def displayitem():
    conn  = sqlite3.connect('main.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM store')
    disData = cur.fetchall()
    print("Todays Offer")
    for eachitem in disData:
        print(eachitem[1]," ->",eachitem[2],end="|   s")
    print()
    print('******************************************')


displayitem()

class namma_kadai:

    def __init__(self,item,price,quantity):
        self.Item     = item
        self.Price    = price
        self.Quantity = quantity
        self.Total    = price * quantity
        print('Total cost for ',self.Item,'is RS',self.Total)
        print()

    def additem(self):
        con  = sqlite3.connect('purchase.db')
        cur  = con.cursor()
        query1 = "INSERT INTO customer(item,price,quantity,total) VALUES (?,?,?,?)"
        data1  = (self.Item,self.Price,self.Quantity,self.Total)
        cur.execute(query1,data1)
        con.commit()
        con.close()
        print(self.Item,'added to the purchase cart')

    def purchased(self):
        con  = sqlite3.connect('purchase.db')
        cur = con.cursor()
        cur.execute('SELECT * FROM customer')
        resData = cur.fetchall()
        add=0
        print()
        print('S.NO','','ITEM',"",'PRICE','','Quantity',"",'TOTAL')
        for row in resData:
            print(row[0],'  ',row[1],'  ',row[2],'  ',row[3],'       ',row[4])
            add = add + row[4]
        print()
        print('\t\t Grand Total is Rs:',add)

shopping = 1
while shopping==1:
    word = input('Enter the ItemName:').capitalize()
    tup_word = tuple(word.split())
    q = "SELECT Rate FROM store WHERE product=?"
    connection= sqlite3.connect('main.db')
    cursor = connection.execute(q,tup_word)
    resData2 = cursor.fetchall()

    if len(resData2)>0:
        for row in resData2:
            a = row[0]
            print('TodaY',word,'price is Rs',a)
            b=float(input('Enter the quantity required:'))

        buyer = namma_kadai(word,a,b)
        add = input('Add this item to cart --> Yes Or No:').lower()
        if add =='yes':
            buyer.additem()
            box='full'

            choice ='repeat'
            while(choice =='repeat'):
                pur = input('continue shopping--> press yes or no:').lower()
                if pur=='yes':
                    print('Select next purchase item')
                    break
                elif pur=='no':
                    buyer.purchased()
                    shopping=2
                    break
                else:
                    print('Press only a valid key')
                    choice='repeat'

        else:
            choice = 'repeat'
            while(choice =='repeat'):
                pur = input('continue shopping--> press yes or no:').lower()
                if pur=='yes':
                    print('Select next purchase item')
                    break
                elif pur=='no':
                    buyer.purchased()
                    shopping=2
                    break
                else:
                    print('Press only a valid key')
                    choice='repeat'
    elif len(resData2)==0:
        print('Sorry!',word,'is out of stock!!')
        choice = 'repeat'
        while (choice == 'repeat'):
            pur = input('continue shopping--> press yes or no:').lower()
            if pur == 'yes':
                print('Next purchase Item')
            elif pur =='no':
                if box=='full':
                    buyer.purchased()
                    shopping = 2
                    break
                else:
                    print('\t Sry for Inconvience \n Visit Again')
                    shopping=2
                    break
            else:
                print('press a valid key')
                choice='repeat'

