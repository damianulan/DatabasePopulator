import cx_Oracle
import mimesis
import random
import sys


def getLastID(tablename):
    dsnStr = cx_Oracle.makedsn("217.173.198.135", "1522", "orcltp")
    con = cx_Oracle.connect(user="s97888", password="s97888", dsn=dsnStr)
    cursor = con.cursor()
    cursor.execute("select id_" + tablename + " from " + tablename + " where rownum = 1 order by id_" + tablename + " DESC")
    for x in cursor:
        y = str(x)
        index = int(y[1])
        return index


def importToLocation():
    try:
        dsnStr = cx_Oracle.makedsn("217.173.198.135", "1522", "orcltp")
        con = cx_Oracle.connect(user="s97888", password="s97888", dsn=dsnStr)
        num = int(input("How many rows should be entered? "))
        last_id = getLastID("location")
        print("Fetching rows...")
        for x in range(num):
            y = mimesis.Address('en')
            city = y.city()
            name = city + ' Office'
            address = y.address() + ', ' + city
            query = "INSERT INTO location (id_location, name, address) VALUES  (:1, :2, :3)"
            cursor = con.cursor()
            last_id = last_id + 1
            cursor.execute(query, (last_id, name, address))
            print(query)
            cursor.close()
        con.commit()
        print("Rows added successfully")
    except cx_Oracle.Error as error:
        print("Error occurred:")
        print(error)
    consoleInput()


def importToSupplier():
    try:
        dsnStr = cx_Oracle.makedsn("217.173.198.135", "1522", "orcltp")
        con = cx_Oracle.connect(user="s97888", password="s97888", dsn=dsnStr)
        num = int(input("How many rows should be entered? "))
        last_id = getLastID("supplier")
        print("Fetching rows...")
        for x in range(num):
            a = mimesis.Address('en')
            p = mimesis.Person('en')
            b = mimesis.Business('en')
            address = a.city()
            name = b.company()
            print(name)
            contact_person = p.full_name()
            phone = p.telephone()
            email = p.email(domains=['mail.com'])
            query = "INSERT INTO supplier (id_supplier, address, name, contact_person, phone, email) VALUES  (:1, :2, " \
                    ":3, :4, :5, :6) "
            cursor = con.cursor()
            last_id = last_id + 1
            cursor.execute(query, (last_id, address, name, contact_person, phone, email))
            print(query)
            cursor.close()
        con.commit()
        print("Rows added successfully")
    except cx_Oracle.Error as error:
        print("Error occurred:")
        print(error)
    consoleInput()


def importToProducer():
    try:
        dsnStr = cx_Oracle.makedsn("217.173.198.135", "1522", "orcltp")
        con = cx_Oracle.connect(user="s97888", password="s97888", dsn=dsnStr)
        num = int(input("How many rows should be entered? "))
        last_id = getLastID("producer")
        print("Fetching rows...")
        for x in range(num):
            a = mimesis.Address('en')
            h = mimesis.Hardware('en')
            country = a.country()
            name = h.manufacturer()
            query = "INSERT INTO producer (id_producer, name, country) VALUES  (:1, :2, :3) "
            cursor = con.cursor()
            last_id = last_id + 1
            cursor.execute(query, (last_id, name, country))
            print(query)
            cursor.close()
        con.commit()
        print("Rows added successfully")
    except cx_Oracle.Error as error:
        print("Error occurred:")
        print(error)
    consoleInput()


def importToEmployee():
    try:
        dsnStr = cx_Oracle.makedsn("217.173.198.135", "1522", "orcltp")
        con = cx_Oracle.connect(user="s97888", password="s97888", dsn=dsnStr)
        num = int(input("How many rows should be entered? "))
        last_id = getLastID("employee")
        print("Fetching rows...")
        for x in range(num):
            y = mimesis.Person('en')
            name = y.first_name()
            surname = y.last_name()
            code = '#' + y.identifier(mask='###')
            position = y.occupation()
            phone = y.telephone()
            email = y.email(domains=['mail.com'])
            login = y.username()
            passwd = y.password()
            location_id = random.randint(1, getLastID("location"))
            query = "INSERT INTO employee (id_employee, name, surname, code, position, phone, email, location_id, " \
                    "login, password) VALUES (:1, :2, :3, :4, :5, :6, :7, :8, :9, :10) "
            cursor = con.cursor()
            last_id = last_id + 1
            cursor.execute(query, (last_id, name, surname, code, position, phone, email, location_id, login, passwd))
            print(query)
            cursor.close()
        con.commit()
        print("Rows added successfully")
    except cx_Oracle.Error as error:
        print("Error occurred:")
        print(error)
    consoleInput()


def importToAsset():
    try:
        dsnStr = cx_Oracle.makedsn("217.173.198.135", "1522", "orcltp")
        con = cx_Oracle.connect(user="s97888", password="s97888", dsn=dsnStr)
        num = int(input("How many rows should be entered? "))
        last_id = getLastID("asset")
        print("Fetching rows...")
        for x in range(num):
            y = mimesis.Person('en')
            d = mimesis.Datetime()
            name = 'Personal Computer'
            model_id = random.randint(1, getLastID("model"))
            supplier_id = random.randint(1, getLastID("supplier"))
            price = y.identifier(mask="####")
            date_of_creation = d.date(start=2015, end=2021)
            date_of_purchase = d.date(start=2015, end=2021)
            serial = y.identifier(mask="######")
            query = "INSERT INTO asset (id_asset, name, model_id, supplier_id, price, date_of_creation, date_of_purchase, serial) VALUES (:1, :2, :3, :4, :5, :6, :7, :8)"
            cursor = con.cursor()
            last_id = last_id + 1
            cursor.execute(query, (last_id, name, model_id, supplier_id, price, date_of_creation, date_of_purchase, serial))
            print(query)
            cursor.close()
        con.commit()
        print("Rows added successfully")
    except cx_Oracle.Error as error:
        print("Error occurred:")
        print(error)
    consoleInput()


def importToModel():
    try:
        dsnStr = cx_Oracle.makedsn("217.173.198.135", "1522", "orcltp")
        con = cx_Oracle.connect(user="s97888", password="s97888", dsn=dsnStr)
        num = int(input("How many rows should be entered? "))
        last_id = getLastID("model")
        print("Fetching rows...")
        for x in range(num):
            y = mimesis.Person()
            producer_id = random.randint(1, getLastID("producer"))
            type_id = random.randint(1, getLastID("type"))
            name = 'T' + y.identifier(mask="####")
            query = "INSERT INTO model (id_model, name, producer_id, type_id) VALUES (:1, :2, :3, :4)"
            cursor = con.cursor()
            last_id = last_id + 1
            cursor.execute(query, (last_id, name, producer_id, type_id))
            print(query)
            cursor.close()
        con.commit()
        print("Rows added successfully")
    except cx_Oracle.Error as error:
        print("Error occurred:")
        print(error)
    consoleInput()


def importToPin():
    try:
        dsnStr = cx_Oracle.makedsn("217.173.198.135", "1522", "orcltp")
        con = cx_Oracle.connect(user="s97888", password="s97888", dsn=dsnStr)
        num = int(input("How many rows should be entered? "))
        last_id = getLastID("pin")
        print("Fetching rows...")
        for x in range(num):
            d = mimesis.Datetime()
            state_id = random.randint(1, getLastID("state"))
            asset_id = random.randint(1, getLastID("asset"))
            date_pinned = d.date(start=2015, end=2021)
            employee_id = random.randint(1, getLastID("employee"))
            query = "INSERT INTO PIN (id_pin, state_id, asset_id, date_pinned, employee_id) VALUES (:1, :2, :3, :4, :5)"
            cursor = con.cursor()
            last_id = last_id + 1
            cursor.execute(query, (last_id, state_id, asset_id, date_pinned, employee_id))
            print(query)
            cursor.close()
        con.commit()
        print("Rows added successfully")
    except cx_Oracle.Error as error:
        print("Error occurred:")
        print(error)
    consoleInput()


# Help instruction
def helpInstruction():
    print("Hi, Welcome in DatabasePopulator! Here are some instructions, that might be helpful:")
    print("push tablename -- define the name of the table u want to populate, then u will be asked about the number of rows")
    print("help -- show this message \n")
    consoleInput()


def consoleInput():
    command = input("/ ").lower()
    if command == "help":
        helpInstruction()
    elif command == "push location":
        importToLocation()
    elif command == "push employee":
        importToEmployee()
    elif command == "push supplier":
        importToSupplier()
    elif command == "push producer":
        importToProducer()
    elif command == "push asset":
        importToAsset()
    elif command == "push model":
        importToPin()
    elif command == "push pin":
        importToPin()
    elif command == "quit":
        sys.exit()
    else:
        print("Unrecognized command. Try again, or type 'help' to see the options.")
        consoleInput()


helpInstruction()
consoleInput()