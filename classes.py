from connect_db import Database



class Base:
    @staticmethod
    def select_1(table):
        query = """
        SELECT course.course_id, course.name, course.description, course.rating, mentor.first_name, mentor.last_name, course_status. name, language.name, course.price FROM course
            INNER JOIN mentor
                ON course.mentor_id = mentor.mentor_id
            INNER JOIN course_status
                ON course_status.course_status_id = course.course_status_id
            INNER JOIN language
                ON language.language_id = course.language_id
                """
        return Database.connect(query, "select")

    @staticmethod
    def korish(table, column, data):
        query = f"SELECT * FROM {table} WHERE {column} = {data}"
        return Database.connect(query, "select")

    @staticmethod
    def select(table):
        query = f"SELECT * FROM {table} ORDER BY {table}_id"
        return Database.connect(query, "select")

    @staticmethod
    def delete(table, column_name, data):
        if type(data) == int:
            query = f"DELETE FROM {table} WHERE {column_name} = {data}"
        else:
            query = f"DELETE FROM {table} WHERE {column_name} = '{data}'"

        return Database.connect(query, "delete")


class City(Base):
    def __init__(self, name):
        self.name = name
        self.table = "city"

    @staticmethod
    def update(column_name, old_data, new_data):
        if type(old_data) == int:
            query = f"UPDATE city SET {column_name} = {new_data} WHERE {column_name} = {old_data}"

        else:
            query = f"UPDATE city SET {column_name} = '{new_data}' WHERE {column_name} = '{old_data}'"

        return Database.connect(query, "update")

    @staticmethod
    def update_id(id, new_id):
        query = f"UPDATE city SET city_id = {new_id} WHERE city_id = {id}"
        return Database.connect(query, "update")

    @staticmethod
    def delete_id(id):
        query = f"DELETE FROM city WHERE city_id={id}"
        return Database.connect(query, "delete")

    def insert(self):
        query = f"""INSERT INTO {self.table} (name) VALUES ('{self.name}')"""
        return Database.connect(query, "insert")

class BestBefore(Base):
    def __init__(self, before):
        self.before = before
        self.table = "best_before"

    @staticmethod
    def update(column_name, old_data, new_data):
        if type(old_data) == int:
            query = f"UPDATE best_before SET {column_name} = {new_data} WHERE {column_name} = {old_data}"

        else:
            query = f"UPDATE best_before SET {column_name} = '{new_data}' WHERE {column_name} = '{old_data}'"

        return Database.connect(query, "update")

    @staticmethod
    def update_id(id, new_id):
        query = f"UPDATE best_before SET best_before_id = {new_id} WHERE best_before_id = {id}"
        return Database.connect(query, "update")

    @staticmethod
    def delete_id(id):
        query = f"DELETE FROM best_before WHERE best_before_id={id}"
        return Database.connect(query, "delete")

    def insert(self):
        query = f"""INSERT INTO {self.table} (before) VALUES ('{self.before}')"""
        return Database.connect(query, "insert")


class Addres(Base):
    def __init__(self, name):
        self.name = name
        self.table = "addres"

    @staticmethod
    def update(column_name, old_data, new_data):
        if type(old_data) == int:
            query = f"UPDATE addres SET {column_name} = {new_data} WHERE {column_name} = {old_data}"

        else:
            query = f"UPDATE addres SET {column_name} = '{new_data}' WHERE {column_name} = '{old_data}'"

        return Database.connect(query, "update")

    @staticmethod
    def update_id(id, new_id):
        query = f"UPDATE addres SET addres_id = {new_id} WHERE addres_id = {id}"
        return Database.connect(query, "update")

    @staticmethod
    def delete_id(id):
        query = f"DELETE FROM addres WHERE addres_id={id}"
        return Database.connect(query, "delete")

    def insert(self):
        query = f"""INSERT INTO {self.table} (name) VALUES ('{self.name}')"""
        return Database.connect(query, "insert")


class PaymentType(Base):
    def __init__(self, name):
        self.name = name
        self.table = "payment_type"

    @staticmethod
    def update(column_name, old_data, new_data):
        if type(old_data) == int:
            query = f"UPDATE payment_type SET {column_name} = {new_data} WHERE {column_name} = {old_data}"

        else:
            query = f"UPDATE payment_type SET {column_name} = '{new_data}' WHERE {column_name} = '{old_data}'"

        return Database.connect(query, "update")

    @staticmethod
    def update_id(id, new_id):
        query = f"UPDATE payment_type SET payment_type_id = {new_id} WHERE payment_type_id = {id}"
        return Database.connect(query, "update")

    @staticmethod
    def delete_id(id):
        query = f"DELETE FROM payment_type WHERE payment_type_id={id}"
        return Database.connect(query, "delete")

    def insert(self):
        query = f"""INSERT INTO {self.table} (name) VALUES ('{self.name}')"""
        return Database.connect(query, "insert")


class ProductStatus(Base):
    def __init__(self, status):
        self.status = status
        self.table = "product_status"

    @staticmethod
    def update(column_name, old_data, new_data):
        if type(old_data) == int:
            query = f"UPDATE product_status SET {column_name} = {new_data} WHERE {column_name} = {old_data}"

        else:
            query = f"UPDATE product_status SET {column_name} = '{new_data}' WHERE {column_name} = '{old_data}'"

        return Database.connect(query, "update")

    @staticmethod
    def update_id(id, new_id):
        query = f"UPDATE product_status SET product_status_id = {new_id} WHERE product_status_id = {id}"
        return Database.connect(query, "update")

    @staticmethod
    def delete_id(id):
        query = f"DELETE FROM product_status WHERE product_status_id={id}"
        return Database.connect(query, "delete")

    def insert(self):
        query = f"""INSERT INTO {self.table} (status) VALUES ('{self.status}')"""
        return Database.connect(query, "insert")


class Cash(Base):
    def __init__(self, payment_type_id):
        self.payment_type_id = payment_type_id
        self.table = "cash"


    @staticmethod
    def update(column_name, old_data, new_data):
        if type(old_data) == int:
            query = f"UPDATE cash SET {column_name} = {new_data} WHERE {column_name} = {old_data}"

        else:
            query = f"UPDATE cash SET {column_name} = '{new_data}' WHERE {column_name} = '{old_data}'"

        return Database.connect(query, "update")

    @staticmethod
    def update_id(id, new_id):
        query = f"UPDATE cash SET cash_id = {new_id} WHERE cash_id = {id}"
        return Database.connect(query, "update")

    @staticmethod
    def delete_id(id):
        query = f"DELETE FROM cash WHERE cash_id={id}"
        return Database.connect(query, "delete")

    def insert(self):
        query = f"""INSERT INTO {self.table} (payment_type_id) VALUES ('{self.payment_type_id}')"""
        return Database.connect(query, "insert")


class Plastic(Base):
    def __init__(self, name, payment_type_id, plastic_number, plastic_password):
        self.name = name
        self.payment_type_id = payment_type_id
        self.plastic_number = plastic_number
        self.plastic_password = plastic_password
        self.table = "plastic"

    @staticmethod
    def update(column_name, old_data, new_data):
        if type(old_data) == int:
            query = f"UPDATE plastic SET {column_name} = {new_data} WHERE {column_name} = {old_data}"

        else:
            query = f"UPDATE plastic SET {column_name} = '{new_data}' WHERE {column_name} = '{old_data}'"

        return Database.connect(query, "update")

    @staticmethod
    def update_id(id, new_id):
        query = f"UPDATE plastic SET plastic_id = {new_id} WHERE plastic_id = {id}"
        return Database.connect(query, "update")

    @staticmethod
    def delete_id(id):
        query = f"DELETE FROM plastic WHERE plastic_id={id}"
        return Database.connect(query, "delete")

    def insert(self):
        query = f"""INSERT INTO {self.table} (name, payment_type_id, plastic_number, plastic_password) VALUES ('{self.name}', '{self.payment_type_id}', '{self.plastic_number}', '{self.plastic_password}')"""
        return Database.connect(query, "insert")


class Product(Base):
    def __init__(self, name, description, product_status_id, best_before_id, price, arrival_time):
        self.name = name
        self.description = description
        self.product_status_id = product_status_id
        self.best_before_id = best_before_id
        self.price = price
        self.arrival_time = arrival_time
        self.table = "product"

    @staticmethod
    def update(column_name, old_data, new_data):
        if type(old_data) == int:
            query = f"UPDATE product SET {column_name} = {new_data} WHERE {column_name} = {old_data}"

        else:
            query = f"UPDATE product SET {column_name} = '{new_data}' WHERE {column_name} = '{old_data}'"

        return Database.connect(query, "update")

    @staticmethod
    def update_id(id, new_id):
        query = f"UPDATE product SET product_id = {new_id} WHERE product_id = {id}"
        return Database.connect(query, "update")

    @staticmethod
    def delete_id(id):
        query = f"DELETE FROM product WHERE product_id={id}"
        return Database.connect(query, "delete")

    def insert(self):
        query = f"""INSERT INTO {self.table} (name, descrpition, product_status_id, best_before_id, price, arrival_time) VALUES ('{self.name}', '{self.description}', '{self.product_status_id}', '{self.best_before_id}', '{self.best_before_id}', '{self.price}', '{self.arrival_time}')"""
        return Database.connect(query, "insert")


class Client(Base):
    def __init__(self, first_name, last_name, age, cash_id, addres_id, city_id, plastic_id, product_id, email, password, birth_date):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.cash_id = cash_id
        self.addres_id = addres_id
        self.city_id = city_id
        self.plastic_id = plastic_id
        self.product_id = product_id
        self.email = email
        self.password = password
        self.birth_date = birth_date
        self.table = "client"


    @staticmethod
    def update(column_name, old_data, new_data):
        if type(old_data) == int:
            query = f"UPDATE client SET {column_name} = {new_data} WHERE {column_name} = {old_data}"

        else:
            query = f"UPDATE client SET {column_name} = '{new_data}' WHERE {column_name} = '{old_data}'"

        return Database.connect(query, "update")

    @staticmethod
    def update_id(id, new_id):
        query = f"UPDATE client SET client_id = {new_id} WHERE client_id = {id}"
        return Database.connect(query, "update")

    @staticmethod
    def delete_id(id):
        query = f"DELETE FROM client WHERE client_id={id}"
        return Database.connect(query, "delete")

    def insert(self):
        query = f"""INSERT INTO {self.table} (first_name, last_name, age, cash_id, addres_id, city_id, plastic_id, product_id, email, password, birth_date) VALUES ('{self.first_name}', '{self.last_name}', '{self.age}', '{self.cash_id}', '{self.addres_id}', '{self.city_id}', '{self.plastic_id}', '{self.product_id}', '{self.email}', '{self.password}', '{self.birth_date}')"""
        return Database.connect(query, "insert")


class Worker(Base):
    def __init__(self, first_name, last_name, age, product_status_id, best_before_id, addres_id, city_id, email, password, birth_date):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.product_status_id = product_status_id
        self.best_before_id = best_before_id
        self.addres_id = addres_id
        self.city = city_id
        self.email = email
        self.password = password
        self.birth_date = birth_date
        self.table = "worker"

    @staticmethod
    def update(column_name, old_data, new_data):
        if type(old_data) == int:
            query = f"UPDATE worker SET {column_name} = {new_data} WHERE {column_name} = {old_data}"

        else:
            query = f"UPDATE worker SET {column_name} = '{new_data}' WHERE {column_name} = '{old_data}'"

        return Database.connect(query, "update")

    @staticmethod
    def update_id(id, new_id):
        query = f"UPDATE worker SET worker_id = {new_id} WHERE worker_id = {id}"
        return Database.connect(query, "update")

    @staticmethod
    def delete_id(id):
        query = f"DELETE FROM worker WHERE worker_id={id}"
        return Database.connect(query, "delete")

    def insert(self):
        query = f"""INSERT INTO {self.table} (first_name, last_name, age, product_status_id, best_before_id,  addres_id, city_id, email, password, birth_date) VALUES ('{self.first_name}', '{self.last_name}', '{self.age}', '{self.product_status_id}','{self.best_before_id}', '{self.addres_id}', '{self.email}', '{self.password}', '{self.birth_date}')"""
        return Database.connect(query, "insert")

class Vendor(Base):
    def __init__(self, first_name, last_name, age, product_id, product_status_id, best_before_id, addres_id, city_id, email, password, birth_date):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.product_id = product_id
        self.product_status_id = product_status_id
        self.best_before_id = best_before_id
        self.addres_id = addres_id
        self.city_id = city_id
        self.email = email
        self.password = password
        self.birth_date = birth_date
        self.table = "vendor"

    @staticmethod
    def update(column_name, old_data, new_data):
        if type(old_data) == int:
            query = f"UPDATE vendor SET {column_name} = {new_data} WHERE {column_name} = {old_data}"

        else:
            query = f"UPDATE vendor SET {column_name} = '{new_data}' WHERE {column_name} = '{old_data}'"

        return Database.connect(query, "update")

    @staticmethod
    def update_id(id, new_id):
        query = f"UPDATE vendor SET vendor_id = {new_id} WHERE vendor_id = {id}"
        return Database.connect(query, "update")

    @staticmethod
    def delete_id(id):
        query = f"DELETE FROM vendor WHERE vendor_id={id}"
        return Database.connect(query, "delete")

    def insert(self):
        query = f"""INSERT INTO {self.table} (first_name, last_name, age, product_id, product_status_id, best_before_id,  addres_id, city_id, email, password, birth_date) VALUES ('{self.first_name}', '{self.last_name}', '{self.age}','{self.product_id}', '{self.product_status_id}','{self.best_before_id}', '{self.addres_id}', '{self.email}', '{self.password}', '{self.birth_date}')"""
        return Database.connect(query, "insert")