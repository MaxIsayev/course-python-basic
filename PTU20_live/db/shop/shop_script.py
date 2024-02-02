import sqlite3

class Customer:
    def create_table(self, connector: sqlite3.Connection, cursor: sqlite3.Cursor):
        query = '''
    CREATE TABLE IF NOT EXISTS costumer (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name VARCHAR(200),
    last_name VARCHAR(200)
    );
    '''
        cursor.execute(query)
        connector.commit()

    def insert_customer(self, connector: sqlite3.Connection, cursor: sqlite3.Cursor):
        print("Inserting a customer...")
        first_name = input("First Name: ")
        last_name = input("Last Name: ")        
        with connector:
            cursor.execute("INSERT INTO costumer (first_name, last_name)"
                       "VALUES (?, ?)", (first_name, last_name))
        print("Done.")
    
    def delete_customer(self, connector: sqlite3.Connection, cursor: sqlite3.Cursor):
        print("Deleting a customer by id ...")
        id = input("Customer id: ")            
        with connector:
            cursor.execute("DELETE FROM costumer "
                       "WHERE id=?", (id,))
        print("Done.")

    def update_customer(self, connector: sqlite3.Connection, cursor: sqlite3.Cursor):
        print("Updating a customer...")
        id = input("Customer id to update: ")   
        first_name = input("First Name: ")
        last_name = input("Last Name: ")           
        with connector:
            cursor.execute(''' UPDATE costumer
                                SET first_name = ? ,
                                last_name = ?                                 
                              WHERE id = ?''', (first_name, last_name, id))
        print("Done.")
    
    def print_customers(self, connector: sqlite3.Connection, cursor: sqlite3.Cursor):
        print("Customers List:")
        with connector:
            cursor.execute("SELECT * FROM costumer")
            customer_list = cursor.fetchall()
            for row in customer_list:               
                print(row[0], row[1], row[2])
                
    
    def find_by(self, connector: sqlite3.Connection, cursor: sqlite3.Cursor, find_by: str):
        query = f'SELECT * FROM costumer WHERE {find_by} = ?'
        search_argument = input("Customers search text: ")
        with connector:
            cursor.execute(query, (search_argument, ))
            costumers = cursor.fetchall()
            if len(costumers) > 0:
                for row in costumers:               
                    print(row[0], row[1], row[2])
            else:
                print("No customers found.")    
        

class Product:
    def create_table(self, connector: sqlite3.Connection, cursor: sqlite3.Cursor):
        query = '''
    CREATE TABLE IF NOT EXISTS product (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(200),
    price FLOAT
    );
    '''
        cursor.execute(query)
        connector.commit()

class Cashier:
    def create_table(self, connector: sqlite3.Connection, cursor: sqlite3.Cursor):
        query = '''
    CREATE TABLE IF NOT EXISTS cashier (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name VARCHAR(200),
    last_name VARCHAR(200)
    );
    '''
        cursor.execute(query)
        connector.commit()

    def insert_cashier(self, connector: sqlite3.Connection, cursor: sqlite3.Cursor):
        print("Inserting a cashier...")
        first_name = input("First Name: ")
        last_name = input("Last Name: ")        
        with connector:
            cursor.execute("INSERT INTO cashier (first_name, last_name)"
                       "VALUES (?, ?)", (first_name, last_name))
        print("Done.")    

class Bill:
    def create_table(self, connector: sqlite3.Connection, cursor: sqlite3.Cursor):
        query = '''
    CREATE TABLE IF NOT EXISTS bill (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    purchase_datetime TIME,
    cashier_id INTEGER REFERENCES cashier(id),
    custumer_id INTEGER REFERENCES costumer(id)
    );
    '''
        cursor.execute(query)
        connector.commit()

class Bill_line:
    def create_table(self, connector: sqlite3.Connection, cursor: sqlite3.Cursor):
        query = '''
    CREATE TABLE IF NOT EXISTS bill_line (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    bill_id INTEGER REFERENCES bill(id),
    product_id INTEGER REFERENCES product(id),
    quantity INTEGER
    );
    '''
        cursor.execute(query)
        connector.commit()    

def main():
    connector = sqlite3.connect('shop.db')
    cursor = connector.cursor()

    customer = Customer()
    product = Product()
    cashier = Cashier()
    bill = Bill()
    bill_line = Bill_line()

    customer.create_table(connector=connector, cursor=cursor)
    product.create_table(connector, cursor)
    cashier.create_table(connector, cursor)
    bill.create_table(connector, cursor)
    bill_line.create_table(connector, cursor)

    while True:
        choice = input("Enter Command (h or help for help): ")
        if choice.lower() in ["q", "quit"]:
            break
        if choice.lower() in ["h", "help"]:
            print('h,   help\t\tthis help')
            print('q,   quit\t\tquit this program')
            print('ic,  insert customer\t  insert a customer')            
            print('ip,  insert product\t   insert a product')
            print('ics, insert cashier\t   insert a cashier')
            print('ib,  insert bill\t      insert a bill')
            print('ibl, insert bill line\t insert a bill_line') 
            print('dc,  delete customer\t  delete a customer')            
            print('dp,  delete product\t   delete a product')
            print('dcs, delete cashier\t   delete a cashier')
            print('db,  delete bill\t      delete a bill')
            print('dbl, delete bill line\t delete a bill_line')
            print('uc,  update customer\t  update a customer')            
            print('up,  update product\t   update a product')
            print('ucs, update cashier\t   update a cashier')
            print('ub,  update bill\t      update a bill')
            print('ubl, update bill line\t update a bill_line')
            print('fc,  find customer\t    find a customer')            
            print('fp,  find product\t     find a product')
            print('fcs, find cashier\t     find a cashier')
            print('fb,  find bill\t        find a bill')
            print('fbl, find bill line\t   find a bill_line') 
            print('ac,  all customers\t    print all customers')            
            print('ap,  all products\t     print all products')
            print('acs, all cashiers\t     print all cashiers')
            print('ab,  all bills\t        print all bills')
            print('abl, all bill lines\t   print all bill_lines')                

        if choice.lower() in ["ic", "insert customer"]:
            customer.insert_customer(connector, cursor) 
        if choice.lower() in ["dc", "delete customer"]:
            customer.delete_customer(connector, cursor)
        if choice.lower() in ["uc", "update customer"]:           
            customer.update_customer(connector, cursor)
        if choice.lower() in ["fc", "find customer"]: 
            print('Find customer by what?')  
            print('fcfn,  find customer first name\t    find a customer by first name')         
            print('fcln,  find customer last name\t    find a customer by last name')
            choice2 = input("Enter search criteria:")
            if choice2.lower() in ["fcfn", "find customer first name"]:
               customer.find_by(connector, cursor, "first_name")
            if choice2.lower() in ["fcln", "find customer last name"]:
               customer.find_by(connector, cursor, "last_name")     
        if choice.lower() in ["ac", "all customers"]:     
            customer.print_customers(connector=connector, cursor=cursor)        

    connector.close()

if __name__ == "__main__":
    main()