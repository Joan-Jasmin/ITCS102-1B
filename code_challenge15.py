import os

os.system('cls')

print('Student Info System')
print('============================')

student_record = {}

while True:
    print('Options:')
    print('A - Add Record')
    print('B - Print Record')
    print('C - Search Record')
    print('D - Delete Record')
    print('E - Edit Record')
    print('F - Export Record')
    print('G - Exit')
    
    choice = input('Select an Option = ').lower()
    
    if choice == 'a':
        os.system('cls')
        print('Add Record')
        id_no = input('ID Number? ')
        first_name = input('Name? ')
        last_name = input('Name? ')
        age = eval(input('Age? '))
        course = input('Course? ').upper()
        section = input('Section? ').upper()
        
        student_record[id_no] = [first_name, last_name, age, course, section]
        print(f'Added')
        continue
    elif choice == 'b':
        os.system('cls')
        print('Print Records')
        for j, g in student_record.items():
            print(f"Code {j}, Info {g}\n")
        continue
    elif choice == 'c':
        os.system('cls')
        print('Search Records')
        search_id = input('ID Number? ')
        if search_id in student_record:
            print(f"{student_record[search_id]}\n")
        else:
            print('None')
        continue
    elif choice == 'd':
        os.system('cls')
        print('Delete Record')
        delete_id = input('ID Number? ')
        if delete_id in student_record:
            del student_record[delete_id]
            print(f'Deleted')
        else:
            print('None')
        continue
    elif choice == 'e':
        os.system('cls')
        print('Edit Record')
        edit_id = input('ID Number? ')
        if edit_id in student_record:
            print('New Details? ')
            first_name = input(f'First name ({student_record[edit_id][0]}): ') or student_record[edit_id][0]
            last_name = input(f'Last name ({student_record[edit_id][1]}): ') or student_record[edit_id][1]
            age = input(f'Age ({student_record[edit_id][2]}): ') or student_record[edit_id][2]
            course = input(f'Course ({student_record[edit_id][3]}): ') or student_record[edit_id][3]
            section = input(f'Section ({student_record[edit_id][4]}): ') or student_record[edit_id][4]  
            student_record[edit_id] = [first_name, last_name, age, course, section]
            print(f'Updated')
        continue
    elif choice == 'f':
        os.system('cls')
        print('Exporting Records')
        with open('student_records.txt', 'w') as file:
            for j, g in student_record.items():
                file.write(f"Code {j}, Info {g}\n")
        continue
    elif choice == 'g':
        os.system('cls')
        print('Exiting')
        break
    else:
        os.system('cls')
        print('Retry')
        continue