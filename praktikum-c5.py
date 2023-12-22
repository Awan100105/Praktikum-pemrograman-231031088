import os
os.system('clear')

a = True
limit = 5
i = 0 # 1.2.3....limit

while a:
    i += 1
    print(f'Menjalankan Program {limit-i+1}')
    if i == limit:
        print('Program berhenti di sini!')
        a = False
    else:
        a = True
    
    


