import random

file = open('fixture.csv', 'r+b')

for i in range(10000000):
    file.write(str(i) + ',' +
               random.choice(['Dr.', 'Mr.', 'Ms.', 'Sir', 'Rev.', 'Our Lord', 'The Dreaded', 'that guy'])
               + " "
               + random.choice(['Andy', 'Dan', 'Georgina', 'Luke', 'John', 'Jasmine', 'Killalot', 'Your'])
               + " "
               + random.choice(['Smith', 'Smithson', 'Roberts', 'Jacobs', 'Oswald', 'Tyler', '9000'])
               + "\n")

file.close()
