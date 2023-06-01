
import json
student_id = "Name"
groups_list = []

try: 
    with open('database.json', 'r') as file:
        database_dict = json.load(file)
except FileNotFoundError:
    database_dict = {}

while True:
    
    while True:  
        with open('database.json', 'w') as file:
            json.dump(database_dict,file)
        print("Введите (1) для создания новой группы. ")
        print("Введите (2) для перехода в раздел \"Управление данными\". Здесь вы сможете добавить студента в группу или добавить/обновить отметки.")
        print("Введите (3) для редактирования базы данных учебного заведения ")
        print("Введите (4) для просмотра нужной вам информации")
        print("Введите (5) для выхода из программы")
    
        enter_choice = int(input("Введите нужное вам действие: "))  
        
        if enter_choice == 1:
            
            def group_number_function():
                if len(database_dict) == 0:
                    print("Системе не удалось найти ни одной группы. Создайте первую группу.")
                else:
                    print("Группы которые уже существуют:")
                    for groups in database_dict.keys():
                        print(groups)
                enter_group_name = str(input("Создайте номер группы: "))
                if enter_group_name not in database_dict:
                    print("Группа", enter_group_name, "верифицирована")
                elif enter_group_name in database_dict:
                    enter_group_name = False
                    print("Эта группа уже есть в базе данных. Создайте новую или редактируйте уже сущесвующую в разделе \"Редактирования базы данных учебного заведения\" в главном меню")
                return enter_group_name
                
            check_group_number = group_number_function()
            if check_group_number == False:
                print("Вы возвращены в главное меню")
            else:
                group_number = check_group_number
            
            try:
                database_dict[group_number] = {}
                print(database_dict)
            except: NameError
            
        elif enter_choice == 2:
            print("Система обнаружила следующие группы:")
            for groups in database_dict.keys():
                print(groups)
            finding_group = input("Введите в какую группу вы хотите внести данные или обновить её: ")
            if finding_group in database_dict:
                print("Введите \"Enter\" для добавления студента в группу", finding_group, "или нажмите \"R\" для возвращения в главное меню.")
            elif finding_group not in database_dict:
                print("Группа", finding_group, "не была найдена системой. Пожалуйста, проверьте правильнсть введенных данных.")
                break
            
            # Блок добавления студентов и их отметок
            while True:
                action = input("Добавить данные ENTER, главное меню \"R\" " ).lower()
                if action == "r":
                    break
                def student_id_function():
                    while True:
                        enter_student_name = input("Введите имя ученика: ").upper()
                        if enter_student_name.strip() == '':
                            print("Имя не может быть пустым. Пожалуйста, введите имя заново.")
                        else:
                            break
                    
                    while True:
                        enter_student_surname = input("Введите фамилию ученика: ").upper()
                        if enter_student_surname.strip() == '':
                            print("Фамилия не может быть пустой. Пожалуйста, введите фамилию заново.")
                        else:
                            break
                        
                    student_id = enter_student_name + "_" + enter_student_surname
                    return str(student_id)
                
                student_id = student_id_function()
                if student_id not in database_dict[finding_group]:
                    database_dict[finding_group][student_id] = {}
                def adding_marks():
                    print("Вводите отметки для ученика", student_id, "в строке ввода. По завершению введите E")
                    print(database_dict)
                    while True:
                        enter_marks = input("Ввод отметок: ").lower()

                        if enter_marks == "e":
                            break
                        
                        enter_marks = int(enter_marks)
                        if enter_marks == 0 or enter_marks > 10:
                            print("Минимальная оценка 1, максимальная 10")
                            continue                  
                        else:
                            if len(database_dict[finding_group][student_id]) == 0:
                                database_dict[finding_group][student_id] = []
                            database_dict[finding_group][student_id].append(enter_marks)
                            print(database_dict)
                            continue
                final_marks = adding_marks()
        
        elif enter_choice == 3:
            while True:
                print("Найдены следующие группы:")
                for group, students in database_dict.items():
                    print(f'№Группы {group} Кол-во студентов {len(students)}')
                    
                enter_group_data = input("Введите номер группы: ")
                if enter_group_data not in database_dict:
                    print("Системе не удалось найти группу", enter_group_data, "в баззе данных.")
                    break
                elif enter_group_data in database_dict:
                    print("Введите \"1\" для редактирования группы или \"2\" ДЛЯ редактирования студентов группы", enter_group_data)
                    enter_action = int(input("Выберите действи: "))
                if enter_action == 1:
                    print("Для удаления группы в строке ввода введите \"D\", для переименования группы \"R\" ")
                    del_rename_choice = input("Ввод: ").lower()
                    if del_rename_choice == "d":
                        del database_dict[enter_group_data]
                        print(f"Группа {enter_group_data} была удалена")
                    elif del_rename_choice == "r":
                        print("Для переименования группы", enter_group_data, "введите новый номер группы")
                        enter_new_group_number = input("Ввод нового номера группы: ")
                        if enter_new_group_number in database_dict:
                            print("Изменить группу невозможно т.к. она уже существует")
                        else:
                            database_dict[enter_new_group_number] = database_dict.pop(enter_group_data)
                            print("Название группы успешно изменено на", enter_new_group_number)
                            print(database_dict)
                            break
                if enter_action == 2:
                    enter_student_name = input("Введите имя студента: ")
                    enter_student_surname = input("Введите фамилию студента: ")
                    check_id = enter_student_name.upper() + "_" + enter_student_surname.upper()
                    if check_id in database_dict[enter_group_data]:
                        print("Выберите дейсвие:")
                    else: 
                        print("Проверьте правильность данных. Система не распознала студента", enter_student_name.title(), enter_student_surname.title(), "в группе", enter_group_data)
                        break
                    print("Введите \"1\" для удаления или замены оценок ученика", enter_student_name.title(), enter_student_surname.title())
                    print("Введите \"2\" для переименования студента в группе", enter_group_data)
                    editing_choice = int(input("Введите номер нужного вам действия: "))
                    if editing_choice == 1:
                        print(database_dict)
                        print("Введите \"S\" для замены оценок или \"R\" для удаления отметок студента", enter_student_name.title(), enter_student_surname.title())
                        while True:
                            enter_replacement_removal = input(">>> ").upper()
                            if enter_replacement_removal == "S":
                                enter_delete_mark = int(input("Введите оценку которую хотите удалить: "))
                                mark_index = enter_delete_mark
                                index_for_replace = database_dict[enter_group_data][check_id].index(mark_index)
                                if enter_delete_mark not in database_dict[enter_group_data][check_id]:
                                    print("К сожалению системе не удалось найти указанную вами отметку у студента", enter_student_name, enter_student_surname, "\nПожалуйста проверьте правильность ваши данные.")
                                    continue
                                enter_new_mark = int(input("Введите новую отметку: "))
                                database_dict[enter_group_data][check_id].remove(enter_delete_mark)
                                database_dict[enter_group_data][check_id].insert(index_for_replace,enter_new_mark)
                                print("Для ученика", enter_student_name.title(), enter_student_surname.title(), "были применена следующие изменения:")
                                print("Оценка", enter_delete_mark, "была успешно заменена на новую отметку", enter_new_mark)
                                print(database_dict)
                                break
                                
                            elif enter_replacement_removal == "R":
                                enter_delete_mark = int(input("Введите оценку которую хотите удалить: "))
                                if len(database_dict[enter_group_data][check_id]) == 0:
                                    print("У студента нету ни одной отметки. Удаление невозможно. Для начала добавьте студенту отметки.")
                                print(database_dict)
                                database_dict[enter_group_data][check_id].remove(enter_delete_mark)
                                print("Для ученика", enter_student_name.title(), enter_student_surname.title(), "были применена следующие изменения:")
                                print("Оценка", enter_delete_mark, "была успешно удалена")
                                print(database_dict)
                                
                    elif editing_choice == 2:
                        print("Теперь введите новое имя и фамилию для студента ", enter_student_name.title(), enter_student_surname.title())
                        while True:
                            enter_student_name = input("Новое имя студента: ")
                            enter_student_surname = input("Новая фамилия студента: ")
                            student_id = enter_student_name.upper() + "_" + enter_student_surname.upper()
                            if student_id in database_dict[enter_group_data]:
                                print("Такой студент уже существует. Повторите попытку.")
                                continue
                            else:
                                new_key = student_id
                                database_dict[enter_group_data][new_key] = database_dict[enter_group_data].pop(check_id)                        
                                print("Имя ученика успешно изменено!")
                                print(database_dict)
                                break

                
        elif enter_choice == 4:
            print("Для просмотра всех групп в базе данных нажмите \"1\" ")
            print("Для просмотра студентов в одной группе введите \"2\" ")
            print("Для просмотра оценок студентов введите \"3\" ")
            enter_search_choice = int(input("Выберите действие: "))
            if enter_search_choice == 1:
                for groups in database_dict.keys():
                    print(groups)

            elif enter_search_choice == 2:
                enter_group_number = int(input("Введите номер группы: "))
                enter_group_number = str(enter_group_number)
                print(f"Все студенты в группе {enter_group_number}:")
                for students in database_dict[enter_group_number].keys():
                    print(students)
            elif enter_search_choice == 3:
                enter_group_number = input("Введите номер группы: ")
                print(f"Отметки студентов в группе {enter_group_number}")
                for group, students in database_dict.items():
                    for student, marks in students.items():
                        print(f"Студент: {student}")
                        for mark in marks:
                            print(mark)
        elif enter_choice == 5:
            break
    break
# 
