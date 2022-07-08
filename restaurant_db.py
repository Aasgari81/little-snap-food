import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="09122377957",
    database="Restaurant"
)

mycursor = mydb.cursor()

# mycursor.execute("CREATE TABLE foodofrestuarant (food_id INT AUTO_INCREMENT PRIMARY KEY,food_kind VARCHAR(255), food_name VARCHAR(255), food_inventory INT, food_material VARCHAR(255), food_fixedprice INT, food_customerprice INT, food_comments VARCHAR(255))") 

# mycursor.execute("CREATE TABLE restuarantinfo (restaurant_id INT AUTO_INCREMENT PRIMARY KEY, restaurant_name VARCHAR(250), restaurant_district VARCHAR(250), restuarant_catagory VARCHAR(250), restuarant_address VARCHAR(250))")

# mycursor.execute("CREATE TABLE orders (order_number INT AUTO_INCREMENT PRIMARY KEY, customer_id INT, restaurant_id INT, amount INT, status VARCHAR(250), price INT)")

