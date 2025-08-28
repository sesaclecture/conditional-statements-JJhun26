"""
Implement User Management System
"""
users = {
    'Al123': {
        'name': 'Alice',
        'password': '123456',
        'birthday': '1999-12-12',
        'role': 'viewer'
    },
    'Bo567': {
        'name': 'Bob',
        'password': '567890',
        'birthday': '2000-01-01',
        'role': 'editor'
    },
    'Ch789': {
        'name': 'Charles',
        'password': '789012',
        'birthday': '1987-04-04',
        'role': 'admin'
    }
}

print(f"Users list: {list(users.keys())}")
while True:
    login_option = input("New ID: 1, Login: 2, Exit: else\n")
    #신규 회원가입
    if login_option == '1':
        id_check = 1
        pw_check = 1
        birth_check = 1
        # id 체크
        new_name = input("Enter your name: ")
        while id_check:
            new_id = input("Enter new ID: ")
            if new_id in users:
                print("ID already exist. Please try again")
                print("="*20)
            else:
                print("ID completed")
                print("="*20)
                id_check = 0
        # 패스워드 체크
        while pw_check:
            new_pw = input("Enter new password: ")
            if len(new_pw) < 5:
                print("Password must be longer than 4 letters.\n")
                print("="*20)
            else:
                pw_check = 0
                print("Password completed")
                print("="*20)
        # 생년월일 체크
        while birth_check:
            new_birthday = input("Enter your birthday(YYYY-MM-DD): ")
            if int(new_birthday[0:4]) < 2025 and 0 < int(new_birthday[5:7]) < 13 and 0 < int(new_birthday[8:10]) < 32:
                print("Birthday completed")
                print("="*20)
                birth_check = 0
            else:
                print("Wrong birthday. Please try again.")
        users[new_id] = {
            'name': new_name,
            'password': new_pw,
            'birthday': new_birthday,
            'role': 'viewer'
        }
        print("You made new ID!")
        print(f"Users list: {list(users.keys())}")
        continue

    #기존 회원 로그인
    if login_option == '2':
        while True:
            login_id = input("ID: ")
            if login_id in users:
                print("ID correct!")
                break
            else:
                print("Invalid ID")
                continue
        while True:
            login_pw = input("Password: ")
            if login_pw == users[login_id]['password']:
                print("Login succeed!")
                break
            else:
                print("Wrong password")
                continue
        #뷰어일경우
        if users[login_id]['role'] == 'viewer':
            while True:
                modify_option = input("Update:1, Delete:2, Exit:else\n")
                if modify_option == '1':
                    info_option = input(
                        "ID:1, Name:2, Password:3, Birthday:4, exit:else\n")
                    new_info = input("Enter new information:")
                    if info_option == '1':
                        users[new_info] = users.pop(login_id)
                        login_id = new_info
                        print(f"Users list: {list(users.keys())}")
                    elif info_option == '2':
                        users[login_id]['name'] = new_info
                        print(f"Users list: {list(users.keys())}")
                    elif info_option == '3':
                        users[login_id]['password'] = new_info
                        print(f"Users list: {list(users.keys())}")
                    elif info_option == '4':
                        users[login_id]['birthday'] = new_info
                        print(f"Users list: {list(users.keys())}")
                    else:
                        break

                elif modify_option == '2':
                    del users[login_id]
                    break
                else:
                    break
        #에디터일경우
        if users[login_id]['role'] == 'editor':
            while True:
                modify_id = input("Enter ID to modify: ")
                if modify_id not in users:
                    print("Wrong ID!")
                    continue
                else:
                    print("Choose option to change")
                modify_option = input("Update:1, Delete:2, Exit:else\n")
                if modify_option == '1':
                    info_option = input(
                        "ID:1, Name:2, Password:3, Birthday:4, exit:else\n")
                    new_info = input("Enter new information:")
                    if info_option == '1' and (login_id!=modify_id):
                        users[new_info] = users.pop(modify_id)
                        print(f"Users list: {list(users.keys())}")
                    if info_option == '1' and (login_id==modify_id):
                        users[new_info] = users.pop(modify_id)
                        login_id = new_info
                        print(f"Users list: {list(users.keys())}")    
                    elif info_option == '2':
                        users[modify_id]['name'] = new_info
                        print(f"Users list: {list(users.keys())}")
                    elif info_option == '3':
                        users[modify_id]['password'] = new_info
                        print(f"Users list: {list(users.keys())}")
                    elif info_option == '4':
                        users[modify_id]['birthday'] = new_info
                        print(f"Users list: {list(users.keys())}")
                    else:
                        continue
                elif modify_option == '2' and modify_id == login_id:
                    del users[modify_id]
                    print(f"Users list: {list(users.keys())}")
                    break
                elif modify_option == '2' and modify_id != login_id:
                    print("Editor cannot delete another account!")
                    continue
                else:
                    break
        #admin일 경우
        if users[login_id]['role'] == 'admin':
            while True:
                modify_id = input("Enter ID to modify: ")
                if modify_id not in users:
                    print("Wrong ID!")
                    continue
                else:
                    print("Choose option to change")
                modify_option = input("Update:1, Delete:2, Exit:else\n")
                if modify_option == '1':
                    info_option = input(
                        "ID:1, Name:2, Password:3, Birthday:4, exit:else\n")
                    new_info = input("Enter new information:")
                    if info_option == '1' and (login_id!=modify_id):
                        users[new_info] = users.pop(modify_id)
                        print(f"Users list: {list(users.keys())}")
                    if info_option == '1' and (login_id==modify_id):
                        users[new_info] = users.pop(modify_id)
                        login_id = new_info
                        print(f"Users list: {list(users.keys())}")   
                    elif info_option == '2':
                        users[modify_id]['name'] = new_info
                        print(f"Users list: {list(users.keys())}")
                    elif info_option == '3':
                        users[modify_id]['password'] = new_info
                        print(f"Users list: {list(users.keys())}")
                    elif info_option == '4':
                        users[modify_id]['birthday'] = new_info
                        print(f"Users list: {list(users.keys())}")
                    else:
                        continue
                elif modify_option == '2':
                    del users[modify_id]
                    break
                else:
                    break

    else:
        print("Exit")
        break
