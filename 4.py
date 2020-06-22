cstp=float(input("Enter cost price"))
sllp=float(input("Enter selling price"))
pft=sllp-cstp
print("Profit from this sell is ",pft)
newsllp=cstp+1.05*pft
print("Selling price should be",newsllp)
