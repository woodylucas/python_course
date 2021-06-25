print("How many kilometers did you cycle today?")
kms = input()
miles = float(kms) / 1.60934
miles = round(miles, 2)
print(f"You {kms} km ride is {miles}mi ")
