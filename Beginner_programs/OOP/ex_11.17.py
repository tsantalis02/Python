# -*- coding: utf-8 -*-
"""
   File name: ex_11.17.py
   
   *-------------------------------------------------------------------
   
   Να δημιουργηθεί πρόγραμμα για την παρακολούθηση της αποθήκης μιας εταιρείας με προϊόντα. Για κάθε προϊόν θα υπάρχει 
   πληροφορ΄΄ια ως προς το πλήθος και την τιμή, καθώς και για το πόσα τέτοια αντικείμενα πρέπει να υπάρχουν στην αποθήκη ως
   απόθεμα. Οι σχετικές λειτουργίες θα αφορούν την εμφάνιση πλαονάσματος ή ελλείμματος, την αξία τους και την πώληση 
   ή/και αγορά τους.
"""

class Product():
    
    population = 0
    stock = 0
    required_stock = 5
    
    def __init__(self,code,quantity,price):
        
        self.code = code
        self.quantity = quantity
        self.price = price
        Product.stock += quantity
        Product.population += 1
        
    def sale_purchase(self):
        
        print("Στοιχεία προϊόντος: Κωδικός:'",self.code,"', Τιμή: ",self.price,"€",sep = "")
        sale_num = int(input("Δώσε τις πωλήσεις του προϊόντος: "))
        while sale_num > self.quantity:
            sale_num = int(input("Δώσε ξανά τις πωλήσεις του προϊόντος: "))
        purchase_num = int(input("Δώσε την αγορά του προϊόντος: "))
        sale_value = sale_num * self.price
        purchase_value = purchase_num * (self.price * 66 / 100)
        print("Είχαμε πώληση",sale_num,"προϊόντων αξίας %.2f" %sale_value,"€")
        print("Είχαμε αγορά",purchase_num,"προϊόντων αξίας %.2f" %purchase_value,"€")
        Product.stock = Product.stock - sale_num + purchase_num
   
    
   
    def checkStock(self):
        
        if Product.stock == 0:
            print("Έχουμε έλλειμμα προϊόντος.")
        elif Product.stock < Product.required_stock:
            print("Χαμηλό απόθεμα (",Product.stock," προϊόντα)", sep = "")
        elif Product.stock >= Product.required_stock and Product.stock < 10:
            print("Ικανοποιητικό απόθεμα (",Product.stock," προϊόντα)", sep = "")
        else:
            print("Έχουμε πλεόνασμα προϊόντος.")
        print()    
            
            
            
p01 =Product('123',20,5.99)
p01.sale_purchase()
p01.checkStock()
p02 = Product('234',14,7.99)
p02.sale_purchase()
p02.checkStock()            
print("Συνολικά",Product.population,"προϊόντα.")