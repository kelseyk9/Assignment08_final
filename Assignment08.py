# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# Kelsey Kawaguchi,12.2.2019,Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
strFileName = 'products.txt'
lstOfProductObjects = []

class Product:
    """Stores data about a product:

    properties:
        product_name: (string) with the products's  name
        product_price: (float) with the products's standard price
    methods:
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        Kelsey Kawaguchi,12.2.2019,Modified code to complete assignment 8
    """
    # Code added to the Product class
    # -- Constructor --
    def __init__(self, product_name:str, product_price:float):
        self.ProdName = product_name
        self.ProdPrice = product_price
        # -- Attributes --
        try:
            self.__product_name = str(product_name)
            self.__product_price = float(product_price)
        except Exception as e:
            raise Exception("Error setting initial values: \n" + str(e))
        
    # -- Properties --
    # ----- Product Name -------
    @property
    def product_name(self):
        return str(self.__product_name)
    
    @product_name.setter
    def product_name(self, value:str):
        if str(value).isnumber() == False:
            self.__product_name = value
        else:
            raise Exception ("Names cannot be numbers")
  
    # ----- Product Price -------
    @property
    def product_price(self):
        return float(self.__product_price)
    
    @product_price.setter
    def product_price(self, value:float):
        if str(value).isnumber():
            self.__product_price = float(value)
        else:
            raise Exception ("Prices must be numbers")    
    
    # -- Methods --
    def to_string(self): 
        """ alias of __str__(), converts product data to string """ 
        return self.__str__()
    
    def __str__(self):
        """ Converts product data to string """
        return self.product_name + ',' + str(self.product_price)
# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):

        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        Kelsey Kawaguchi,12.2.2019,Modified code to complete assignment 8
    """
    # Code to process data from a file
    @staticmethod
    def save_data_to_file(file_name:str, list_of_product_objects:list):
        """Write a list of product rows to a file
        
        :param file_name: (string) with name of file
        :param list_of_product_objects: (list) of product objects to save to file
        :return: (bool) with the status of success
        """
        success_status = False 
        try:
            file = open(file_name,"w")
            for product in list_of_product_objects:
                file.write(product.__str__() + "\n")
            file.close()
            success_status = True 
        except Exception as e: 
            print("There was a general error!") 
            print(e, e.__doc__, type(e), sep='\n')
        return success_status
    
    # Code to process data to a file
    @staticmethod
    def read_data_from_file(file_name:str):
        """ Read data from a file into a list of product rows
        
        :param file_name: (string) with file name
        :return: (list) of product rows
        """
        list_of_product_rows = []
        try: 
            file = open(file_name, "r")
            for line in file:
                data = line.split(",")
                row = Product(data[0],data[1])
                list_of_product_rows.append(row)
            file.close()
        except Exception as e: 
            print("There was a general error!") 
            print(e, e.__doc__, type(e), sep='\n')
        return list_of_product_rows
        

# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    # Added docstring
    """ Class to perform Input and Output
    
        methods:
            print_menu():
            input_menu_choice():
            print_current_list_items(list_of_rows):
            input_product_data():

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        Kelsey Kawaguchi,12.2.2019,Modified code to complete assignment 8
    """
    

    # Code to show menu to user
    @staticmethod
    def print_menu():
        """  Display a menu of choices to the user
        :return: nothing
        """
        print('''
        Menu of Options
        1) Show current data.
        2) Add a new item.
        3) Save Data to File
        4) Exit Program
        ''')
        print()  # Add an extra line for looks

    # Code to get user's choice
    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user
        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 4] - ")).strip()
        print()  # Add an extra line for looks
        return choice    
    
    # Code to show the current data from the file to user
    @staticmethod
    def print_current_list_items(list_of_rows:list):
        """ Prints the current items in the list of dictionaries rows

        :param list_of_rows: (list) of rows you want to display
        """
        print("******* The current product items are: *******")
        for row in list_of_rows:
            print(str(row.product_name) + "(" + str(row.product_price) + ")")
        print("*******************************************")
        print()  # Add an extra line for looks    
        
    # Code to get product data from user
    @staticmethod
    def input_product_data():
        """ Gets the product and price from a user
        :return: (product) object with input data
        """
        try:
            name = str(input("What is the product name? - ").strip())  # Get product from user
            price = float(input("What is the price? - ").strip())  # Get price from user
            print()  # Add an extra line for looks
            p = Product(product_name=name, product_price=price)
        except Exception as e:
            print(e)
        return p 
    

# Presentation (Input/Output)  -------------------------------------------- #

# Main Body of Script  ---------------------------------------------------- #
# Data Code to the Main body
# Load data from file into a list of product objects when script starts
try: 
    ListOfProdObj = FileProcessor.read_data_from_file(strFileName)
    
    while True:
        # Show user a menu of options
        IO.print_menu()
        # Get user's menu option choice
        strChoice = IO.input_menu_choice()
        if strChoice.strip() == '1':
            # Show user current data in the list of product objects
            IO.print_current_list_items(ListOfProdObj)
            continue 
        elif strChoice.strip() == '2':
            # Let user add data to the list of product objects
            ListOfProdObj.append(IO.input_product_data())
            continue 
        elif strChoice.strip() == '3':
            # let user save current data to file and exit program
            FileProcessor.save_data_to_file(strFileName, ListOfProdObj)
            continue
        elif strChoice.strip() == '4':
            break
except Exception as e: 
    print("There was an error! Check file permissions.") 
    print(e, e.__doc__, type(e), sep='\n')    
        
# Main Body of Script  ---------------------------------------------------- #

