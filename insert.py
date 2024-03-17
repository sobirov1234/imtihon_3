import classes
import main


def vendor():
    vendor_1 = input("""
       ______________________________\n
                    SERVICES

       ------------------------------\n
           1. SELECT _>
           2. INSERT _>
           3. UPDATE _>
           4. DELETE _>
           0. Back _>

               """)

    if vendor_1 == "1":
        if len(classes.Vendor.select("vendor")) == 0:
            print("""
                ------------------------------\n
                    MA'LUMOTLAR MAVJUD EMAS
                ------------------------------\n
                """)

        else:
            for i in classes.Vendor.select("vendor"):
                print(f"""
                        ID: {i[0]}
                        first_name: {i[1]}
                        last_name: {i[2]}
                        Age: {i[3]}
                        Product ID: {i[4]}
                        Product Status ID : {i[5]}
                        Best Before ID: {i[6]}
                        Addres ID: {i[7]}
                        City ID: {i[8]}
                        Email : {i[9]}
                        Password : {i[10]}
                        birth Date: {i[11]}
                        Create Date: {i[12]}
                    """)
        return vendor()



    elif vendor_1 == "2":
        first_name = input("First Name: ")
        last_name = input("Last Name: ")
        age = input("Age: ")
        product_id = input("Product ID: ")
        product_status_id = input("Product Status ID: ")
        best_before = input("Best Before ID: ")
        addres_id = input("Addres ID: ")
        city_id = input("City ID: ")
        email = input("Email: ")
        password = input("Password: ")
        birth_date = input("Birth")
        vendor_1_1 = classes.Vendor(first_name, last_name, age, product_id, product_status_id, best_before, addres_id, city_id, email, password, birth_date)
        print(vendor_1_1.insert())
        return vendor()

    elif vendor() == "3":
        column_name = input("Column name: ")
        old_data = input("Now date: ")
        new_data = input("New date: ")
        if column_name.lower() == "id":
            print(classes.Vendor.update_id(int(old_data), int(new_data)))

        else:
            print(classes.Vendor.update(column_name.lower(), old_data, new_data))

        return vendor()

    elif vendor_1 == "4":
        table = "vendor"
        column_name = input("Column name: ")
        old_data = input("Now date: ")
        if column_name.lower() == "id":
            print(classes.Vendor.delete_id(int(old_data)))

        else:
            print(classes.Vendor.delete(table, column_name.lower(), old_data))

        return vendor()

    elif vendor_1 == "0":
        return main.main()

    else:
        print("""
            <<<<<<_____________________>>>>>>
                     ERROR COMMAND!
            <<<<<<_____________________>>>>>>
            """)
        return vendor()


def worker():
    worker_1 = input("""
       ______________________________\n
                    SERVICES

       ------------------------------\n
           1. SELECT _>
           2. INSERT _>
           3. UPDATE _>
           4. DELETE _>
           0. Back _>

               """)

    if worker_1 == "1":
        if len(classes.Worker.select("worker")) == 0:
            print("""
                ------------------------------\n
                    MA'LUMOTLAR MAVJUD EMAS
                ------------------------------\n
                """)

        else:
            for i in classes.Worker.select("worker"):
                print(f"""
                        ID: {i[0]}
                        first_name: {i[1]}
                        last_name: {i[2]}
                        Age: {i[3]}
                        Product Status ID : {i[4]}
                        Best Before ID: {i[5]}
                        Addres ID: {i[6]}
                        City ID: {i[7]}
                        Email : {i[8]}
                        Password : {i[9]}
                        birth Date: {i[10]}
                        Create Date: {i[11]}
                    """)
        return worker()



    elif worker_1 == "2":
        first_name = input("First Name: ")
        last_name = input("Last Name: ")
        age = input("Age: ")
        product_status_id = input("Product Status ID: ")
        best_before = input("Best Before ID: ")
        addres_id = input("Addres ID: ")
        city_id = input("City ID: ")
        email = input("Email: ")
        password = input("Password: ")
        birth_date = input("Birth")
        worker_1_1 = classes.Worker(first_name, last_name, age, product_status_id, best_before, addres_id, city_id, email, password, birth_date)
        print(worker_1_1.insert())
        return worker()

    elif worker_1 == "3":
        column_name = input("Column name: ")
        old_data = input("Now date: ")
        new_data = input("New date: ")
        if column_name.lower() == "id":
            print(classes.Worker.update_id(int(old_data), int(new_data)))

        else:
            print(classes.Worker.update(column_name.lower(), old_data, new_data))

        return worker()

    elif worker_1 == "4":
        table = "worker"
        column_name = input("Column name: ")
        old_data = input("Now date: ")
        if column_name.lower() == "id":
            print(classes.Worker.delete_id(int(old_data)))

        else:
            print(classes.Worker.delete(table, column_name.lower(), old_data))

        return worker()

    elif worker_1 == "0":
        return main.main()

    else:
        print("""
            <<<<<<_____________________>>>>>>
                     ERROR COMMAND!
            <<<<<<_____________________>>>>>>
            """)
        return worker()



def client():
    client_1 = input("""
       ______________________________\n
                    SERVICES

       ------------------------------\n
           1. SELECT _>
           2. INSERT _>
           3. UPDATE _>
           4. DELETE _>
           0. Back _>

               """)

    if client_1 == "1":
        if len(classes.Client.select("client")) == 0:
            print("""
                ------------------------------\n
                    MA'LUMOTLAR MAVJUD EMAS
                ------------------------------\n
                """)

        else:
            for i in classes.Client.select("client"):
                print(f"""
                        ID: {i[0]}
                        first_name: {i[1]}
                        last_name: {i[2]}
                        Age: {i[3]}
                        Cash ID : {i[4]}
                        Addres ID: {i[5]}
                        City ID: {i[6]}
                        Plastic ID: {i[7]}
                        Product ID: {i[8]}
                        Email : {i[9]}
                        Password : {i[10]}
                        birth Date: {i[11]}
                        Create Date: {i[12]}
                    """)
        return client()



    elif client_1 == "2":
        first_name = input("First Name: ")
        last_name = input("Last Name: ")
        age = input("Age: ")
        cash_id = input("Cash ID: ")
        address = input("Address: ")
        city_id = input("City ID: ")
        plastic_id = input("Plastic ID: ")
        product_id = input("Product ID: ")
        email = input("Email: ")
        password = input("Password: ")
        birth_date = input("Birth")
        client_1_1 = classes.Client(first_name, last_name, age, cash_id, address, city_id, plastic_id, product_id, email, password, birth_date)
        print(client_1_1.insert())
        return client()

    elif client_1 == "3":
        column_name = input("Column name: ")
        old_data = input("Now date: ")
        new_data = input("New date: ")
        if column_name.lower() == "id":
            print(classes.Client.update_id(int(old_data), int(new_data)))

        else:
            print(classes.Client.update(column_name.lower(), old_data, new_data))

        return client()

    elif client_1 == "4":
        table = "client"
        column_name = input("Column name: ")
        old_data = input("Now date: ")
        if column_name.lower() == "id":
            print(classes.Client.delete_id(int(old_data)))

        else:
            print(classes.Client.delete(table, column_name.lower(), old_data))

        return client()

    elif client_1 == "0":
        return main.main()

    else:
        print("""
            <<<<<<_____________________>>>>>>
                     ERROR COMMAND!
            <<<<<<_____________________>>>>>>
            """)
        return client()