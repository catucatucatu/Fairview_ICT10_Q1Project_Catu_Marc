# Project Receipt Generator and SKU Generator
from pyscript import display, document

def receipt(e): # function for button
    product1 = document.getElementById('dip') # ID dip is put into variable product1
    product2 = document.getElementById('sundae') # ID sundae is put into variable product2
    product3 = document.getElementById('bsplit') # ID bsplit is put into variable product3
    product4 = document.getElementById('cup1') # ID cup1 is put into variable product4
    product5 = document.getElementById('cup2') # ID cup2 is put into variable product5
    product6 = document.getElementById('cup3') # ID cup3 is put into variable product6
    product7 = document.getElementById('cup4') # ID cup4 is put into variable product7
    product8 = document.getElementById('cone1') # ID cone1 is put into variable product8
    product9 = document.getElementById('cone2') # ID cone2 is put into variable product9
    product10 = document.getElementById('cone3') # ID cone3 is put into variable product10
    product11 = document.getElementById('cone4') # ID cone4 is put into variable product11
    vat = 0.12 # 12% VAT 
    subtotal = 
    float((product1).value) * product1.checked +
    float((product2).value) * product2.checked + 
    float((product3).value) * product3.checked + 
    float((product4).value) * product4.checked + 
    float((product5).value) * product5.checked + 
    float((product6).value) * product6.checked + 
    float((product7).value) * product7.checked + 
    float((product8).value) * product8.checked + 
    float((product9).value) * product9.checked + 
    float((product10).value) * product10.checked + 
    float((product11).value) * product11.checked # .value to use the value of each product, .checked to see if the checkbox is checked, and float to make the number a floating point
    valueaddedtax = subtotal * float(vat) # takes 12% of the subtotal
    total = subtotal + valueaddedtax # adds the VAT to the subtotal
    display("Subtotal: " + str(subtotal) + " Php", target="output") # displays the subtotal
    display("VAT: " + str(valueaddedtax) + " Php", target="output") # displays the VAT
    display("Total: " + str(total) + " Php", target="output") # displays the total

def sku(e):
    category1 = document.getElementById('category').value # finds the category picked
    product1 = document.getElementById('product').value # finds the product inputted
    quantity1 = document.getElementById('quantity').value # finds the amount of the product
    display((category1[:3] + product1[:3]).upper() + str(quantity1), target="output") # combines the three to create a SKU. uses offsetting to use only the first 3 letters and uses upper() to make all letters uppercase
