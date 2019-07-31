from csv import reader
pets_csv = open("pets.csv")
pets_list = list(reader(pets_csv))
print(pets_list[0:5])
pets_header = pets_list[0]
pets_body = pets_list[1:]

procedures_csv = open("procedures.csv")
procedures_list = list(reader(procedures_csv))
procedures_header = procedures_list[0]
procedures_body = procedures_list[1:]
print(procedures_header)
print(procedures_body[0:5])

pet_id_count = {}
for procedure in procedures_body:
    pet_id = procedure[0]
    if pet_id in pet_id_count:
        pet_id_count[pet_id]+=1
    else:
        pet_id_count[pet_id] = 1
        
print(pet_id_count)

for pet in pets_body:
    pet_id = pet[0]
    if pet_id == 'J8-7429':
        pet_name = pet[1]
        
print(pet_name)

procedure_details_csv = open("procedure_details.csv")
procedure_details_list = list(reader(procedure_details_csv))
procedure_details_header = procedure_details_list[0]
procedure_details_body = procedure_details_list[1:]
print(procedure_details_header)
print(procedure_details_body[0:5])

pet_procedure_cost = {}
for key in pet_id_count:
    pet_procedure_cost[key]=0
    for procedure in procedures_body:
        pet_id = procedure[0]
        procedure_type = procedure[2]
        sub_code = procedure[3]
        for procedure_detail in procedure_details_body:
            if procedure_detail[0] == procedure_type and procedure_detail[1] == sub_code:
                if pet_id == key:
                    pet_procedure_cost[key]+=int(procedure_detail[3])
                        
print(pet_procedure_cost)

owners = {}
for key in pet_procedure_cost:
    for pet in pets_body:
        pet_id = pet[0]
        owner_id = pet[5]
        if pet_id == key:
            if owner_id not in owners:
                owners[owner_id]=1
            else:
                owners[owner_id]+=1
            
print(owners)

thrty_eighty_nine = []
for pet in pets_body:
    if pet[5] == '3089':
        thrty_eighty_nine.append(pet[0])
        
print(thrty_eighty_nine)

each_list = []
for each in thrty_eighty_nine:
    if each in pet_procedure_cost:
        each_list.append(each)
        
print(each_list)

owners_csv = open("owners.csv")
owners_list = list(reader(owners_csv))
owners_header = owners_list[0]
owners_body = owners_list[1:]
print(owners_header)
print(owners_body[0:5])

big_spender = str()
for pet in pets_body:
    if pet[0] == 'J1-6366':
        big_spender = pet[5]
        
print(big_spender)

pet_and_owner = {}
for key in pet_procedure_cost:
    pet_and_owner[key] = str()
    for pet in pets_body:
        if pet[0] == key:
            pet_and_owner[key] = pet[5]
            
print(pet_and_owner)

owner_zip = []
for key, value in pet_and_owner.items():
    for owner in owners_body:
        if owner[0] == value and owner[7] == '49503':
            if owner[0] not in owner_zip:
                owner_zip.append(owner[0])
            else:
                pass
            
print(owner_zip)

zip_pets = []
for owner in owner_zip:
    for key, value in pet_and_owner.items():
        if value == owner:
            zip_pets.append(key)
            
print(zip_pets)

cost = []
for pet in zip_pets:
    for key, value in pet_procedure_cost.items():
        if key == pet:
            cost.append(value)
            
print(cost)

sum_cost = sum(cost)
print(sum_cost)
mean_cost = sum_cost/len(cost)
print(mean_cost)

print(pets_header) 
pet_c = []
for pet in pets_body:
    if pet[2] == 'Dog':
        if 'c' in pet[1]:
            pet_c.append(pet[1])
        
print(pet_c)   
print(len(pet_c))

male_pet = 0
for each in pets_body:
    if each[1] in pet_c:
        if each[3] == 'male':
            male_pet+=1
                
print(male_pet)
dog_prcnt = male_pet/len(pet_c)
print(dog_prcnt)

import numpy
pet_age = []
for pet in pets_body:
    age = int(pet[4])
    pet_age.append(age)
    
print(pet_age)
age_deviation = numpy.std(pet_age)
print(age_deviation)

parrot_age = 0
for pet in pets_body:
    if pet[2] == 'Parrot'and int(pet[4]) > parrot_age:
        parrot_age = int(pet[4])
        
print(parrot_age)

cat_age = []
for pet in pets_body:
    if pet[2] == 'Cat':
        cat_age.append(int(pet[4]))
        
print(cat_age)
print(sum(cat_age)/len(cat_age))

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
pets = pd.read_csv("pets.csv")
pets = pets[['Kind', 'Age']]

x = 'Kind'
y = 'Age'

ax = sns.boxplot(x=x, y=y, data=pets)

box_dog = ax.artists[0]
box_cat = ax.artists[1]
box_parrot = ax.artists[2]
box_dog.set_facecolor('green')
box_cat.set_facecolor('purple')
box_parrot.set_facecolor('orange')
plt.show()

plt.savefig('plot.png')
