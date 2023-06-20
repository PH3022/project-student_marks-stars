import json

try: 
    with open('database.json', 'r') as file:
        database_dict = json.load(file)
except FileNotFoundError:
    database_dict = {}

except json.JSONDecodeError:
    print("Системе не удалось прочитать файл базы данных. Данные повреждены ввиду ручного вмешательства во внутренние файлы системы или следствием повреждения данных.")
    database_dict = {}
    

    
def group_creation_space(database_main):
    def displaying_group_numbers(database_local):
        if len(database_local) == 0:
            print("Системе не удалось найти ни одной группы. Создайте первую группу.")
        else:
            print("Группы которые уже существуют:")
            for groups in database_local.keys():
                print(groups)
    displaying_group_numbers(database_main)
    
    def checking_and_creating_group(database_local):
        enter_group_name = str(input("Создайте номер группы: "))
        if enter_group_name.strip() == '':
            print("Имя группы не может быть пустым!")   
                       
        elif enter_group_name in database_local:
            print("Эта группа уже есть в базе данных. Создайте новую или редактируйте уже сущесвующую в разделе \"Редактирования базы данных учебного заведения\" в главном меню")

        elif enter_group_name not in database_local:
            print("Группа", enter_group_name, "верифицирована")
            database_local[enter_group_name] = {}
            print(database_dict)
        return database_local
    
    valid_group_number = checking_and_creating_group(database_main)
    return valid_group_number

 
            
def data_management_space(database_main):
    while True:
        def checking_data(database_local):
            print("Система обнаружила следующие группы:")
            for groups in database_local.keys():
                print(groups)
            finding_group = input("Введите в какую группу вы хотите внести данные или обновить её: ")
            if finding_group in database_local:
                print("Введите \"Enter\" для добавления студента в группу", finding_group, "или нажмите \"R\" для возвращения в главное меню.")
            elif finding_group not in database_local:
                finding_group = None
                print("Группа", finding_group, "не была найдена системой. Пожалуйста, проверьте правильнсть введенных данных.")              
            return finding_group
        valid_group_number = checking_data(database_main)
        if valid_group_number == None:
            break
    
    
        # Блок добавления студентов и их отметок
        def adding_marks(database_local,group_number):               
            while True:
                action = input("Добавить данные ENTER, главное меню \"R\" " ).lower()
                if action == "r":
                    break
                def creating_student_id():
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
                
                student_id = creating_student_id()
                formated_name = student_id.replace('_',' ').title()
                if student_id not in database_local[group_number]:
                    database_local[group_number][student_id] = {}
                    
                print("Вводите отметки для ученика", formated_name, "в строке ввода. По завершению введите E")
                print(database_local)
                while True:
                    enter_marks = input("Ввод отметок: ").lower()

                    if enter_marks == "e":
                        break
                    
                    enter_marks = int(enter_marks)
                    if enter_marks == 0 or enter_marks > 10:
                        print("Минимальная оценка 1, максимальная 10")
                        continue                  
                    else:
                        if len(database_local[group_number][student_id]) == 0:
                            database_local[group_number][student_id] = []
                        database_local[group_number][student_id].append(enter_marks)
                        print(database_local)
                        continue
            return database_local
        publication_marks = adding_marks(database_main,valid_group_number)
        return publication_marks

# 0214 
def editing_space(database_main): 
    
    def сhecking_entered_group_and_action(database_local):
        while True:
            print("Найдены следующие группы:")
            for group, students in database_local.items():
                print(f'Группа{group}. Кол-во студентов {len(students)}')
                
            enter_group_number = input("Введите номер группы: ")
            if enter_group_number not in database_local:
                print("Системе не удалось найти группу", enter_group_number, "в баззе данных.")
                break
            elif enter_group_number in database_local:
                print("Введите \"1\" для редактирования группы или \"2\" ДЛЯ редактирования студентов группы", enter_group_number)
                enter_action = int(input("Выберите действи: "))
                return enter_group_number, enter_action
           
    valid_group_number, selected_action = сhecking_entered_group_and_action(database_main)
    
    if selected_action == 1:
        def deleting_renaming_group(database_local, group_number):
            while True:               
                print("Для удаления группы в строке ввода введите \"D\", для переименования группы \"R\" ")
                del_rename_choice = input("Ввод: ").lower()
                if del_rename_choice == "d":
                    def deleting_group_number():
                        del database_local[group_number]
                        print(f"Группа {group_number} была удалена")
                        return database_local
                    database_local = deleting_group_number()                   
                    
                elif del_rename_choice == "r":
                    def renaming_group_number():
                        while True:
                            print("Для переименования группы", group_number, "введите новый номер группы")
                            enter_new_group_number = input("Ввод нового номера группы: ")
                            if enter_new_group_number in database_local:
                                print("Изменить группу невозможно т.к. она уже существует")
                            else:
                                database_local[enter_new_group_number] = database_local.pop(group_number)
                                print("Название группы успешно изменено на", enter_new_group_number)
                                print(database_local)
                                return database_local
                            
                    database_local = renaming_group_number()
                return database_local        
        database_main = deleting_renaming_group(database_main, valid_group_number)
        return database_main
    
    if selected_action == 2:
        
        def checking_entered_student_id(database_local,group_number):         
            while True:
                enter_student_name = input("Введите имя студента: ").upper()
                enter_student_surname = input("Введите фамилию студента: ").upper()
                if enter_student_name.strip() == '' or enter_student_surname.strip() == '':
                    print("Поле не может быть пустым. Пожалуйста, введите значение заново.")
                    continue
                check_id = enter_student_name + "_" + enter_student_surname
                if check_id not in database_local[group_number]:
                    formatted_name = check_id.replace("_", " ").title()
                    print("Проверьте правильность данных. Система не распознала студента", formatted_name, "в группе", group_number)
                    continue
                elif check_id in database_local[group_number]:
                    return check_id
                break        
        valid_student_id = checking_entered_student_id(database_main, valid_group_number)
        
        
        def checking_user_choice():
            formatted_name = valid_student_id.replace("_", " ").title()
            print("Выберите дейсвие:")
            print("Введите \"1\" для переименования студента в группе", valid_group_number)
            print("Введите \"2\" для удаления или замены оценок ученика", formatted_name)
            enter_user_choice = int(input("Введите номер нужного вам действия: "))
            if enter_user_choice > 2:
                print("Введите номер от 1 или 2 для работы с данными!")
            else:
                return enter_user_choice
        selected_choice = checking_user_choice()
        
        if selected_choice == 1:
                           
            def rename_student_id(database_local, old_student_id, group_number):
                formatted_name = old_student_id.replace("_", " ").title()
                print("Теперь введите новое имя и фамилию для студента", formatted_name)
                while True:                   
                    enter_new_student_name = input("Новое имя студента: ").upper()
                    enter_new_student_surname = input("Новая фамилия студента: ").upper()
                    new_student_id = enter_new_student_name + "_" + enter_new_student_surname
                    if new_student_id in database_dict[group_number]:
                        print("Такой студент уже существует. Повторите попытку.")
                        continue
                    else:
                        database_local[group_number][new_student_id] = database_dict[group_number].pop(old_student_id)                        
                        print("Данные ученика успешно изменены!")
                        print(database_local)
                        return database_local
            database_main = rename_student_id(database_main, valid_student_id, valid_group_number)        
    return database_main
    #     elif selected_choice == 2:
    #         def replacing_deleting_marks(database_local, group_number, student_id_local):
    #             formatted_name = .replace("_", " ").title()
    #             print("Введите \"S\" для замены оценок или \"R\" для удаления отметок студента", formatted_name())
    #             while True:
    #                 enter_replacement_removal = input(">>> ").upper()
    #                 if enter_replacement_removal == "S":
    #                     enter_delete_mark = int(input("Введите оценку которую хотите удалить: "))
    #                     mark_index = enter_delete_mark
    #                     index_for_replace = database[group_number][check_id].index(mark_index)
    #                     if enter_delete_mark not in database[group_number][check_id]:
    #                         print("К сожалению системе не удалось найти указанную вами отметку у студента", enter_student_name, enter_student_surname, "\nПожалуйста проверьте правильность ваши данные.")
    #                         continue
    #                     enter_new_mark = int(input("Введите новую отметку: "))
    #                     database_dict[group_number][check_id].remove(enter_delete_mark)
    #                     database_dict[group_number][check_id].insert(index_for_replace,enter_new_mark)
    #                     print("Для ученика", enter_student_name.title(), enter_student_surname.title(), "были применена следующие изменения:")
    #                     print("Оценка", enter_delete_mark, "была успешно заменена на новую отметку", enter_new_mark)
    #                     print(database_dict)
    #                     break
                        
    #                 elif enter_replacement_removal == "R":
    #                     enter_delete_mark = int(input("Введите оценку которую хотите удалить: "))
    #                     if len(database_dict[group_number][check_id]) == 0:
    #                         print("У студента нету ни одной отметки. Удаление невозможно. Для начала добавьте студенту отметки.")
    #                     print(database_dict)
    #                     database_dict[group_number][check_id].remove(enter_delete_mark)
    #                     print("Для ученика", enter_student_name.title(), enter_student_surname.title(), "были применена следующие изменения:")
    #                     print("Оценка", enter_delete_mark, "была успешно удалена")
    #                     print(database_dict)
    #         replacing_deleting_marks(database_main, valid_group_number, valid_student_id)

    #     # 0214    
    
    
    # database_main = delete_rename_student_id(database_main, valid_student_id, valid_group_number)
    # # was here
            
            
            
            
                


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
            database_dict = group_creation_space(database_dict)
             
            
        elif enter_choice == 2:
            database_dict = data_management_space(database_dict)

        elif enter_choice == 3:
            database_dict = editing_space(database_dict)
        
    #     # 915    
    #     elif enter_choice == 4:
    #         print("Для просмотра всех групп в базе данных нажмите \"1\" ")
    #         print("Для просмотра студентов в одной группе введите \"2\" ")
    #         print("Для просмотра оценок студентов введите \"3\" ")
    #         enter_search_choice = int(input("Выберите действие: "))
    #         if enter_search_choice == 1:
    #             for groups in database_dict.keys():
    #                 print(groups)

    #         elif enter_search_choice == 2:
    #             enter_group_number = int(input("Введите номер группы: "))
    #             enter_group_number = str(enter_group_number)
    #             print(f"Все студенты в группе {enter_group_number}:")
    #             for students in database_dict[enter_group_number].keys():
    #                 print(students)
    #         elif enter_search_choice == 3:
    #             enter_group_number = input("Введите номер группы: ")
    #             print(f"Отметки студентов в группе {enter_group_number}")
    #             for group, students in database_dict.items():
    #                 for student, marks in students.items():
    #                     print(f"Студент: {student}")
    #                     for mark in marks:
    #                         print(mark)
    #     # 915
    #     elif enter_choice == 5:
    #         break
    # break