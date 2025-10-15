people = {
    1: {'name': 'John', 'sex': 'Male'},
    2: {'name': 'Marie', 'sex': 'Female'},
    3: {'name': 'Paul', 'sex': 'Male'}
}

list_people = list(people.values())

male_count = 0
female_count = 0

for person in list_people:
    if person['sex'] == 'Male':
        male_count += 1
    elif person['sex'] == 'Female':
        female_count += 1
print("Number of male:", male_count)
print("Number of female:", female_count)
