TRUNCATE TABLE pizza_menupizzas,pizza_pizzatoppings,pizza_pizzaimage,user_user;




INSERT INTO pizza_pizzatoppings (name,price) VALUES ('Pepperoni',300);
INSERT INTO pizza_pizzatoppings (name,price) VALUES ('Mushrooms',200);
INSERT INTO pizza_pizzatoppings (name,price) VALUES ('Onions',100);
INSERT INTO pizza_pizzatoppings (name,price) VALUES ('Sausage',400);
INSERT INTO pizza_pizzatoppings (name,price) VALUES ('Bacon',500);
INSERT INTO pizza_pizzatoppings (name,price) VALUES ('Extra cheese',200);
INSERT INTO pizza_pizzatoppings (name,price) VALUES ('Black olives',100);
INSERT INTO pizza_pizzatoppings (name,price) VALUES ('Green peppers',100);
INSERT INTO pizza_pizzatoppings (name,price) VALUES ('Pineapple',100);
INSERT INTO pizza_pizzatoppings (name,price) VALUES ('Spinach',100);
INSERT INTO pizza_pizzatoppings (name,price) VALUES ('Tomatoes',100);
INSERT INTO pizza_pizzatoppings (name,price) VALUES ('Ham',300);
INSERT INTO pizza_pizzatoppings (name,price) VALUES ('Chicken',300);
INSERT INTO pizza_pizzatoppings (name,price) VALUES ('Beef',300);
INSERT INTO pizza_pizzatoppings (name,price) VALUES ('Beans',800);
INSERT INTO pizza_pizzatoppings (name,price) VALUES ('Corn',300);
INSERT INTO pizza_pizzatoppings (name,price) VALUES ('Tuna',1800);
INSERT INTO pizza_pizzatoppings (name,price) VALUES ('Prawns',2800);
INSERT INTO pizza_pizzatoppings (name,price) VALUES ('Anchovies',100);
INSERT INTO pizza_pizzatoppings (name,price) VALUES ('Chilli',200);
INSERT INTO pizza_pizzatoppings (name,price) VALUES ('Garlic',100);
INSERT INTO pizza_pizzatoppings (name,price) VALUES ('Olives',100);
INSERT INTO pizza_pizzatoppings (name,price) VALUES ('Cream cheese',300);
INSERT INTO pizza_pizzatoppings (name,price) VALUES ('Mozzarella',300);
INSERT INTO pizza_pizzatoppings (name,price) VALUES ('Parmesan',300);
INSERT INTO pizza_pizzatoppings (name,price) VALUES ('Feta',300);

INSERT INTO pizza_menupizzas (name,description,toppings_id,base_price,on_sale) VALUES ('Margherita','Tomato sauce, mozzarella cheese',258,1000,false);
INSERT INTO pizza_menupizzas (name,description,toppings_id,base_price,on_sale) VALUES ('Hawaiian','Tomato sauce, mozzarella cheese, ham, pineapple',243,1200,false);
INSERT INTO pizza_menupizzas (name,description,toppings_id,base_price,on_sale) VALUES ('Pepperoni','Tomato sauce, mozzarella cheese, pepperoni',235,1300,false);

INSERT INTO pizza_pizzaimage (image,pizza_id) VALUES ('https://pizza.az/upload/iblock/cb0/cb0abb92f9b512713c74bf03dbb70723.jpg',15);
INSERT INTO pizza_pizzaimage (image,pizza_id) VALUES ('https://pizza.az/upload/iblock/f4f/f4f3e2cce270517c62adbd4ae6a95656.jpg',16);
INSERT INTO pizza_pizzaimage (image,pizza_id) VALUES ('https://pizza.az/upload/iblock/809/80956e09d302a120d49b6fd1071fe5b7.jpg',17);

INSERT INTO user_user (name,member_since,image,email,password,favorite_pizza_id) VALUES ('John Doe','2020-01-01','https://randomuser.me/api/portraits/men/93.jpg','johndoe@gmail.com','123456',15);
INSERT INTO user_user (name,member_since,image,email,password,favorite_pizza_id) VALUES ('Jane Doe', '2002-02-02','https://randomuser.me/api/portraits/women/92.jpg','jane@yahoo.co.uk','123456',16);
INSERT INTO user_user (name,member_since,image,email,password,favorite_pizza_id) VALUES ('Juan Jose', '2001-09-11','https://randomuser.me/api/portraits/lego/6.jpg','juan@doe.is','123456',17);


select *
from user_user;

select *
from pizza_pizzatoppings;

select *
from pizza_menupizzas;

select *
from pizza_pizzaimage;
