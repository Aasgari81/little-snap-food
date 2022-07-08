from restaurant_db import *

def email_check(text):
    mycursor.execute("SELECT email, password FROM customer")
    customers_info = mycursor.fetchall()
    for customer in customers_info:
        if text not in customer:
            return "متاسفانه ایمیل شما یافت نشد 🥲"
        else:
            return "لطفا رمز عبور خودتو برا ما بفرستید."


def password_check(text):
    mycursor.execute("SELECT email, password FROM customer")
    customers_info = mycursor.fetchall()
    for customer in customers_info:
        if text == customer[1]:
            return "دوباره خوش اومدید \n لطفا از بین گزینه ها دسته بندی غذای مورد علاقتو انتخاب کن✌️"
        else:
            return 'رمز عبور شما اشتباه است. \n 2 فرصت دیگر باقی است در غیر اینصورت رمز جدید برای شما ایمیل خواهد شد.'

def choose_catagory(catagory):
    restaurant_id_list = []
    food_restaurant = {"PIZZA" : "SELECT * FROM restuarantinfo WHERE pizza = 'yes'", "HAMBURGER" : "SELECT * FROM restuarantinfo WHERE hamburger = 'yes'", "KEBAB" : "SELECT * FROM restuarantinfo WHERE kebab = 'yes'", "OTHERS" : "SELECT * FROM restuarantinfo"}
    mycursor.execute(food_restaurant[catagory])
    restaurants = mycursor.fetchall() 

    for restaurant in restaurants:
        print(f"id: {restaurant[0]} \t name:{restaurant[2]}") 
        restaurant_id_list.append(restaurant[0])

    print("لطفا ایدی رستوران مورد نظرتون رو وارد کنید.")

def choose_food(text):
    restaurant_id = text 

    mycursor.execute(f"SELECT * FROM foodofrestuarant WHERE restuarant_id = {restaurant_id}")
    foods = mycursor.fetchall()

    for food in foods: 
        print(f"id:{food[1]}: |name:{food[3]}-price:{food[7]}-material:{food[5]}|")

    print("لطفا آیدی غذای مورد نظر خود را وارد کنید \n در صورت به اتمام رسیدن سفارش شما عدد 0 را وارد کنید")

    
    
