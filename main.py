from pyscript import display, document


def Buy(e):
    Product1 = document.getElementById("Morality")
    Product2 = document.getElementById("MEarth")
    Product3 = document.getElementById("Seduction")
    Product4 = document.getElementById("Embellishments")
    Product5 = document.getElementById("Dialectical") # getting the value of variables

    Subtotal = (float(Product1.value) * Product1.checked + 
             float(Product2.value) * Product2.checked + float(Product3.value) * Product3.checked + float(Product4.value) * Product4.checked + float(Product5.value) * Product5.checked)  # adding the selected items

    VAT = Subtotal * 0.12 # multiplying the subtotal to tax to add the VAT

    Total = VAT + Subtotal # final price

    SUBT = (f"Subtotal: ₱{Subtotal:.2f}")

    TAXV = (f"VAT: ₱{VAT:.2f}")

    FINALP = (f"Total: ₱{Total:.2f}")

    display(SUBT, target='RES1')

    display(TAXV, target='RES2')

    display(FINALP, target='RES3') # display the results

def gSKU(e):

    SKU1 = document.getElementById("Selected")
    SKU2 = document.getElementById("pName")
    SKU3 = document.getElementById("sVal") # getting the value of these
    
    display(SKU1.value[0:3].upper() + "-" + SKU2.value[0:3].upper() + "-" + SKU3.value[0:3].upper(), target="SKUR") # getting first 3 letter then making it all big

    
    # Subtotal = SKU1.value * SKU1.checked + SKU1.value * SKU1.checked + SKU1.value * SKU1.checked + SKU1.value * SKU1.checked + 

    # https://www.cosmos.so/e/647626829
             