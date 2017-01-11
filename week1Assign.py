## Gas pump Informer

amtOfGas_float = float(input("# of gallons of gas:"))
print("Equivalent # of liters of gas:",amtOfGas_float * 3.7854)
print("# of barrels of oil required to produce it:",amtOfGas_float/19.5)
print("price in U.S dollars: $",amtOfGas_float*3.65)


## Pig Latin Translator

name = input("Please input your name:")
opt= name[1].upper() + name[2:] + name[0].lower() +"ay"
print(opt)
