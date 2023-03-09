#bmi = weight / height**2
weight = float(input("Esciu el teu pes: "))
height = float(input("Escriu la teva alçada: "))
def bmi_calculator(weight,height):
    bmi = weight / (height**2)
    if bmi <= 18.5:
        print("Underweight")
    elif bmi <= 25.0:
        print("Normal")
    elif bmi <= 30.0:
        print("Overweight")
    elif bmi > 30:
        print("Obese")
    print(bmi)
    
bmi_calculator(weight, height)