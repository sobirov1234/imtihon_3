from connect_db import Database


def create_tables():

    city_tables = """
        CREATE TABLE city(
            city_id SERIAL PRIMARY KEY,
            name VARCHAR(30),
            create_date TIMESTAMP DEFAULT now()
        )
    """

    best_before_tables = """
        CREATE TABLE best_before(
            best_before_id SERIAL PRIMARY KEY,
            before VARCHAR(20),
            create_date TIMESTAMP DEFAULT now()
        )
    """

    addres_tables = """
        CREATE TABLE addres(
            addres_id SERIAL PRIMARY KEY,
            name VARCHAR(30),
            create_date TIMESTAMP DEFAULT now()
        )
    """

    payment_type_tables = """
        CREATE TABLE payment_type(
            payment_type_id SERIAL PRIMARY KEY,
            name VARCHAR(30),
            create_date TIMESTAMP DEFAULT now()
        )
    """

    product_status_tables = """
        CREATE TABLE product_status(
            product_status_id SERIAL PRIMARY KEY,
            status VARCHAR(30),
            create_date TIMESTAMP DEFAULT now()
        )
    """

    cash_tables = """
        CREATE TABLE cash(
            cash_id SERIAL PRIMARY KEY,
            payment_type_id INT REFERENCES payment_type(payment_type_id),
            create_date TIMESTAMP DEFAULT now()
        )
    """

    plastic_tables = """
        CREATE TABLE plastic(
            plastic_id SERIAL PRIMARY KEY,
            name VARCHAR(30),
            payment_type_id INT REFERENCES payment_type(payment_type_id),
            plastic_number VARCHAR(30),
            plastic_password INT,
            create_date TIMESTAMP DEFAULT now()
        )
    """

    product_tables = """
        CREATE TABLE product(
            product_id SERIAL PRIMARY KEY,
            name VARCHAR(30),
            description VARCHAR(30),
            product_status_id INT REFERENCES product_status(product_status_id),
            best_before_id INT REFERENCES best_before(best_before_id),
            price NUMERIC,
            arrival_time DATE,
            create_date TIMESTAMP DEFAULT now()
        )
    """

    client_tables = """
        CREATE TABLE client(
            client_id SERIAL PRIMARY KEY,
            first_name VARCHAR(20),
            last_name VARCHAR(20),
            age SMALLINT,
            cash_id INT REFERENCES cash(cash_id),
            addres_id INT REFERENCES addres(addres_id),
            city_id INT REFERENCES city(city_id),
            plastic_id INT REFERENCES plastic(plastic_id),
            product_id INT REFERENCES product(product_id),
            email VARCHAR(30),
            password VARCHAR(30),
            birth_date DATE,
            create_date TIMESTAMP DEFAULT now()
        )
    """

    worker_tables = """
        CREATE TABLE worker(
            worker_id SERIAL PRIMARY KEY,
            first_name VARCHAR(20),
            last_name VARCHAR(20),
            age SMALLINT,
            product_status_id INT REFERENCES product_status(product_status_id),
            best_before_id INT REFERENCES best_before(best_before_id),
            address_id INT REFERENCES addres(addres_id),
            city_id INT REFERENCES city(city_id),
            email VARCHAR(30),
            password VARCHAR(30),
            birth_date DATE,
            create_date TIMESTAMP DEFAULT now()
        )
    """

    vendor_tables = """
        CREATE TABLE vendor(
            vendor_id SERIAL PRIMARY KEY,
            first_name VARCHAR(20),
            last_name VARCHAR (20),
            age SMALLINT,
            product_id INT REFERENCES product(product_id),
            product_status_id INT REFERENCES product_status(product_status_id),
            best_before_id INT REFERENCES best_before(best_before_id),
            address_id INT REFERENCES addres(addres_id),
            city_id INT REFERENCES city(city_id),
            email VARCHAR(30),
            password VARCHAR(30),
            birth_date DATE,
            create_date TIMESTAMP DEFAULT now()
        )
    """

    data = {
        "city_tables": city_tables,
        "best_before_tables": best_before_tables,
        "address_tables": addres_tables,
        "payment_type_tables": payment_type_tables,
        "product_status_tables": product_status_tables,
        "cash_tables": cash_tables,
        "plastic_tables": plastic_tables,
        "product_tables": product_tables,
        "client_tables": client_tables,
        "worker_tables": worker_tables,
        "vendor_tables": vendor_tables
    }

    for i in data:
        print(f"{i} {Database.connect(data[i], "create")}")


if __name__ == '__main__':
    create_tables()