import classes
import insert


def product():
    product_1 = input("""
       ______________________________\n
                    SERVICES

       ------------------------------\n
           1. SELECT _>
           2. INSERT _>
           3. UPDATE _>
           4. DELETE _>
           0. Back _>

               """)

    if product_1 == "1":
        if len(classes.Product.select("product")) == 0:
            print("""
                ------------------------------\n
                    MA'LUMOTLAR MAVJUD EMAS
                ------------------------------\n
                """)

        else:
            for i in classes.Product.select("product"):
                print(f"""
                        ID: {i[0]}
                        Name: {i[1]}
                        Description: {i[2]}
                        Payment Status ID: {i[3]}
                        Best Before : {i[4]}
                        Price: {i[5]}
                        Arrival Time: {i[6]}
                        Craeta Date: {i[7]}
                    """)
        return product()

    elif product_1 == "2":
        name = input("Name: ")
        description = input("Description: ")
        payment_status_id = input("Payment Status ID: ")
        best_before_id = input("Best Before ID: ")
        price = input("Price: ")
        arrival_time = input("Arrival Time: ")
        product_1_1 = classes.Product(name, description,  payment_status_id, best_before_id, price, arrival_time)
        print(product_1_1.insert())
        return product()

    elif product_1 == "3":
        column_name = input("Column name: ")
        old_data = input("Now date: ")
        new_data = input("New date: ")
        if column_name.lower() == "id":
            print(classes.Product.update_id(int(old_data), int(new_data)))

        else:
            print(classes.Product.update(column_name.lower(), old_data, new_data))

        return product()

    elif product_1 == "4":
        table = "product"
        column_name = input("Column name: ")
        old_data = input("Now date: ")
        if column_name.lower() == "id":
            print(classes.Product.delete_id(int(old_data)))

        else:
            print(classes.Product.delete(table, column_name.lower(), old_data))

        return product()

    elif product_1 == "0":
        return main()

    else:
        print("""
            <<<<<<_____________________>>>>>>
                     ERROR COMMAND!
            <<<<<<_____________________>>>>>>
            """)
        return product()


def plastic():
    plastic_1 = input("""
       ______________________________\n
                    SERVICES

       ------------------------------\n
           1. SELECT _>
           2. INSERT _>
           3. UPDATE _>
           4. DELETE _>
           0. Back _>

               """)

    if plastic_1 == "1":
        if len(classes.Plastic.select("plastic")) == 0:
            print("""
                ------------------------------\n
                    MA'LUMOTLAR MAVJUD EMAS
                ------------------------------\n
                """)

        else:
            for i in classes.Plastic.select("plastic"):
                print(f"""
                        ID: {i[0]}
                        Name: {i[1]}
                        Payment Type ID: {i[2]}
                        Plastic Number: {i[3]}
                        Plastic Password: {i[4]}
                        Craeta Date: {i[5]}
                    """)
        return plastic()

    elif plastic_1 == "2":
        name = input("Name: ")
        payment_type_id = input("Payment Type ID: ")
        plastic_number = input("Plastic Number: ")
        plastic_password = input("<PASSWORD>: ")
        plastic_1_1 = classes.Plastic(name, payment_type_id, plastic_number, plastic_password)
        print(plastic_1_1.insert())
        return plastic()

    elif plastic_1 == "3":
        column_name = input("Column name: ")
        old_data = input("Now date: ")
        new_data = input("New date: ")
        if column_name.lower() == "id":
            print(classes.Plastic.update_id(int(old_data), int(new_data)))

        else:
            print(classes.Plastic.update(column_name.lower(), old_data, new_data))

        return plastic()

    elif plastic_1 == "4":
        table = "plastic"
        column_name = input("Column name: ")
        old_data = input("Now date: ")
        if column_name.lower() == "id":
            print(classes.Plastic.delete_id(int(old_data)))

        else:
            print(classes.Plastic.delete(table, column_name.lower(), old_data))

        return plastic()

    elif plastic_1 == "0":
        return main()

    else:
        print("""
            <<<<<<_____________________>>>>>>
                     ERROR COMMAND!
            <<<<<<_____________________>>>>>>
            """)
        return plastic()


def cash():
    cash_1 = input("""
       ______________________________\n
                    SERVICES

       ------------------------------\n
           1. SELECT _>
           2. INSERT _>
           3. UPDATE _>
           4. DELETE _>
           0. Back _>

               """)

    if cash_1 == "1":
        if len(classes.Cash.select("cash")) == 0:
            print("""
                ------------------------------\n
                    MA'LUMOTLAR MAVJUD EMAS
                ------------------------------\n
                """)

        else:
            for i in classes.Cash.select("cash"):
                print(f"""
                        ID: {i[0]}
                        Payment Type ID: {i[1]}
                        Craeta Date: {i[2]}
                    """)
        return cash()

    elif cash_1 == "2":
        payment_type_id = input("Payment Type ID: ")
        cash_1_1 = classes.ProductStatus(payment_type_id)
        print(cash_1_1.insert())
        return cash()

    elif cash_1 == "3":
        column_name = input("Column name: ")
        old_data = input("Now date: ")
        new_data = input("New date: ")
        if column_name.lower() == "id":
            print(classes.Cash.update_id(int(old_data), int(new_data)))

        else:
            print(classes.Cash.update(column_name.lower(), old_data, new_data))

        return cash()

    elif cash_1 == "4":
        table = "cash"
        column_name = input("Column name: ")
        old_data = input("Now date: ")
        if column_name.lower() == "id":
            print(classes.Cash.delete_id(int(old_data)))

        else:
            print(classes.Cash.delete(table, column_name.lower(), old_data))

        return cash()

    elif cash_1 == "0":
        return main()

    else:
        print("""
            <<<<<<_____________________>>>>>>
                     ERROR COMMAND!
            <<<<<<_____________________>>>>>>
            """)
        return cash()


def payment_status():
    payment_status_1 = input("""
       ______________________________\n
                    SERVICES

       ------------------------------\n
           1. SELECT _>
           2. INSERT _>
           3. UPDATE _>
           4. DELETE _>
           0. Back _>

               """)

    if payment_status_1 == "1":
        if len(classes.ProductStatus.select("payment_status")) == 0:
            print("""
                ------------------------------\n
                    MA'LUMOTLAR MAVJUD EMAS
                ------------------------------\n
                """)

        else:
            for i in classes.ProductStatus.select("payment_status"):
                print(f"""
                        ID: {i[0]}
                        Status: {i[1]}
                        Craeta Date: {i[2]}
                    """)
        return payment_status()

    elif payment_status_1 == "2":
        status = input("Status: ")
        payment_status_1_1 = classes.ProductStatus(status)
        print(payment_status_1_1.insert())
        return payment_status()

    elif payment_status_1 == "3":
        column_name = input("Column name: ")
        old_data = input("Now date: ")
        new_data = input("New date: ")
        if column_name.lower() == "id":
            print(classes.ProductStatus.update_id(int(old_data), int(new_data)))

        else:
            print(classes.ProductStatus.update(column_name.lower(), old_data, new_data))

        return payment_status()

    elif payment_status_1 == "4":
        table = "payment_status"
        column_name = input("Column name: ")
        old_data = input("Now date: ")
        if column_name.lower() == "id":
            print(classes.ProductStatus.delete_id(int(old_data)))

        else:
            print(classes.ProductStatus.delete(table, column_name.lower(), old_data))

        return payment_status()
    elif payment_status_1 == "0":
        return main()

    else:
        print("""
            <<<<<<_____________________>>>>>>
                     ERROR COMMAND!
            <<<<<<_____________________>>>>>>
            """)
        return payment_status()


def payment_type():
    payment_type_1 = input("""
       ______________________________\n
                    SERVICES

       ------------------------------\n
           1. SELECT _>
           2. INSERT _>
           3. UPDATE _>
           4. DELETE _>
           0. Back _>

               """)

    if payment_type_1 == "1":
        if len(classes.PaymentType.select("payment_type")) == 0:
            print("""
                ------------------------------\n
                    MA'LUMOTLAR MAVJUD EMAS
                ------------------------------\n
                """)

        else:
            for i in classes.PaymentType.select("payment_type"):
                print(f"""
                        ID: {i[0]}
                        Name: {i[1]}
                        Craeta Date: {i[2]}
                    """)
        return payment_type()

    elif payment_type_1 == "2":
        name = input("Name: ")
        payment_type_1_1 = classes.PaymentType(name)
        print(payment_type_1_1.insert())
        return payment_type()

    elif payment_type_1 == "3":
        column_name = input("Column name: ")
        old_data = input("Now date: ")
        new_data = input("New date: ")
        if column_name.lower() == "id":
            print(classes.PaymentType.update_id(int(old_data), int(new_data)))

        else:
            print(classes.PaymentType.update(column_name.lower(), old_data, new_data))

        return payment_type()

    elif payment_type_1 == "4":
        table = "payment_type"
        column_name = input("Column name: ")
        old_data = input("Now date: ")
        if column_name.lower() == "id":
            print(classes.PaymentType.delete_id(int(old_data)))

        else:
            print(classes.PaymentType.delete(table, column_name.lower(), old_data))

        return payment_type()
    elif payment_type_1 == "0":
        return main()

    else:
        print("""
            <<<<<<_____________________>>>>>>
                     ERROR COMMAND!
            <<<<<<_____________________>>>>>>
            """)
        return payment_type()


def addres():
    addres_1 = input("""
       ______________________________\n
                    SERVICES

       ------------------------------\n
           1. SELECT _>
           2. INSERT _>
           3. UPDATE _>
           4. DELETE _>
           0. Back _>

               """)

    if addres_1 == "1":
        if len(classes.Addres.select("addres")) == 0:
            print("""
                ------------------------------\n
                    MA'LUMOTLAR MAVJUD EMAS
                ------------------------------\n
                """)

        else:
            for i in classes.Addres.select("addres"):
                print(f"""
                        ID: {i[0]}
                        Name: {i[1]}
                        Craeta Date: {i[2]}
                    """)
        return addres()

    elif addres_1 == "2":
        name = input("Name: ")
        addres_1_1 = classes.Addres(name)
        print(addres_1_1.insert())
        return addres()

    elif addres_1 == "3":
        column_name = input("Column name: ")
        old_data = input("Now date: ")
        new_data = input("New date: ")
        if column_name.lower() == "id":
            print(classes.Addres.update_id(int(old_data), int(new_data)))

        else:
            print(classes.Addres.update(column_name.lower(), old_data, new_data))

        return addres()

    elif addres_1 == "4":
        table = "addres"
        column_name = input("Column name: ")
        old_data = input("Now date: ")
        if column_name.lower() == "id":
            print(classes.Addres.delete_id(int(old_data)))

        else:
            print(classes.Addres.delete(table, column_name.lower(), old_data))

        return addres()
    elif addres_1 == "0":
        return main()

    else:
        print("""
            <<<<<<_____________________>>>>>>
                     ERROR COMMAND!
            <<<<<<_____________________>>>>>>
            """)
        return addres()



def best_before():
    best_before_1 = input("""
       ______________________________\n
                    SERVICES

       ------------------------------\n
           1. SELECT _>
           2. INSERT _>
           3. UPDATE _>
           4. DELETE _>
           0. Back _>

               """)

    if best_before_1 == "1":
        if len(classes.BestBefore.select("best_before")) == 0:
            print("""
                ------------------------------\n
                    MA'LUMOTLAR MAVJUD EMAS
                ------------------------------\n
                """)

        else:
            for i in classes.BestBefore.select("best_before"):
                print(f"""
                        ID: {i[0]}
                        Before: {i[1]}
                        Craeta Date: {i[2]}
                    """)
        return city()

    elif best_before_1 == "2":
        before = input("Before: ")
        best_before_1_1 = classes.BestBefore(before)
        print(best_before_1_1.insert())
        return best_before()

    elif best_before_1 == "3":
        column_name = input("Column name: ")
        old_data = input("Now date: ")
        new_data = input("New date: ")
        if column_name.lower() == "id":
            print(classes.BestBefore.update_id(int(old_data), int(new_data)))

        else:
            print(classes.BestBefore.update(column_name.lower(), old_data, new_data))

        return best_before()

    elif best_before_1 == "4":
        table = "best_before"
        column_name = input("Column name: ")
        old_data = input("Now date: ")
        if column_name.lower() == "id":
            print(classes.BestBefore.delete_id(int(old_data)))

        else:
            print(classes.BestBefore.delete(table, column_name.lower(), old_data))

        return best_before()
    elif best_before_1 == "0":
        return main()

    else:
        print("""
            <<<<<<_____________________>>>>>>
                     ERROR COMMAND!
            <<<<<<_____________________>>>>>>
            """)
        return best_before()


def city():
    cityt = input("""
       ______________________________\n
                    SERVICES
    
       ------------------------------\n
           1. SELECT _>
           2. INSERT _>
           3. UPDATE _>
           4. DELETE _>
           0. Back _>
    
               """)


    if cityt == "1":
        if len(classes.City.select("city")) == 0:
            print("""
                ------------------------------\n
                    MA'LUMOTLAR MAVJUD EMAS
                ------------------------------\n
                """)

        else:
            for i in classes.City.select("city"):
                print(f"""
                        ID: {i[0]}
                        Name: {i[1]}
                        Craeta Date: {i[2]}
                    """)
        return city()

    elif cityt == "2":
        name = input("Name: ")
        city_1 = classes.City(name)
        print(city_1.insert())
        return city()

    elif cityt == "3":
        column_name = input("Column name: ")
        old_data = input("Now date: ")
        new_data = input("New date: ")
        if column_name.lower() == "id":
            print(classes.City.update_id(int(old_data), int(new_data)))

        else:
            print(classes.City.update(column_name.lower(), old_data, new_data))

        return city()

    elif cityt == "4":
        table = "city"
        column_name = input("Column name: ")
        old_data = input("Now date: ")
        if column_name.lower() == "id":
            print(classes.City.delete_id(int(old_data)))

        else:
            print(classes.City.delete(table, column_name.lower(), old_data))

        return city()
    elif cityt == "0":
        return main()

    else:
        print("""
            <<<<<<_____________________>>>>>>
                     ERROR COMMAND!
            <<<<<<_____________________>>>>>>
            """)
        return city()



def main():
    print("""
    <<<<<<_____________________>>>>>>
                MAIN MENYU
    <<<<<<_____________________>>>>>>
    """)

    servisses = input("""
    1. City _>
    2. Best Before  _>
    3. Addres _>
    4. Payment Type _>
    5. Payment Status _>
    6. Cash _>
    7. Plastic _>
    8. Product _>
    9. Client _>
    10. Worker _>
    11. Vendor _>
    """)

    if servisses == "1":
        return city()

    elif servisses == "2":
        return best_before()

    elif servisses == "3":
        return addres()

    elif servisses == "4":
        return payment_type()

    elif servisses == "5":
        return payment_status()

    elif servisses == "6":
        return cash()

    elif servisses == "7":
        return plastic()

    elif servisses == "8":
        return product()

    elif servisses == "9":
        return insert.client()

    elif servisses == "10":
        return insert.worker()

    elif servisses == "11":
        return insert.vendor()

    else:
        print("""
        <<<<<<_____________________>>>>>>
                 ERROR COMMAND!
        <<<<<<_____________________>>>>>>
        """)
        return main()


if __name__ == '__main__':
    main()