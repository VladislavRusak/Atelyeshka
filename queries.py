import sqlite3


database = 'Atelye.sqlite3'

sqlite_connection = sqlite3.connect(database)
cursor = sqlite_connection.cursor()
print("База данных успешно подключена")


# class addOrder(customer_name, service_name, things, status, phone_num):

#     def add():
#         pass

# queryOrder = f"INSERT INTO orders(customer_name, service_name, things, status)  VALUES ({customer},{service_name},{things},{status})"
# queryCustomer = f"INSERT INTO customers(customer_name, phone_num) VALUES({full_name}, {phone_number})"


class OrderList():
    create_query = 'SELECT order_name, customer, '


class CustomerTable():
    def add():
        pass

    def delete():
        pass

    def add():
        pass

    def add():
        pass
