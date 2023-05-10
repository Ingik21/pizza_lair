


INSERT INTO pizza_pizzacategory (name) VALUES ('Bestseller');
INSERT INTO pizza_pizzacategory (name) VALUES ('Classic');
INSERT INTO pizza_pizzacategory (name) VALUES ('Vegetarian');
INSERT INTO pizza_pizzacategory (name) VALUES ('Meat');
INSERT INTO pizza_pizzacategory (name) VALUES ('Spicy');


INSERT INTO offer_offer (name, offer_image, offer_price) VALUES ('Get two random pizzas for a bargain price', 'https://pizza.az/upload/iblock/2ab/2ab979936a45e3d9007aa2e7bfce201d.png', 690.00);
INSERT INTO offer_offer (name, offer_image, offer_price) VALUES ('Get three random pizzas for a bargain price', 'https://st2.depositphotos.com/12490800/46913/i/600/depositphotos_469138240-stock-photo-three-pizzas-isolated-white-background.jpg', 990.00);
INSERT INTO offer_offer (name, offer_image, offer_price) VALUES ('Get four random pizzas for a bargain price', 'https://previews.123rf.com/images/wihtgod/wihtgod1609/wihtgod160900026/65216156-four-different-pizzas-in-one-set-top-view-isolated-on-white.jpg', 1290.00);
INSERT INTO offer_offer (name, offer_image, offer_price) VALUES ('Get three random pizzas and some leftover soda', 'https://popmenucloud.com/cdn-cgi/image/width%3D600%2Cheight%3D600%2Cfit%3Dscale-down%2Cformat%3Dauto%2Cquality%3D60/bfexzhkw/20ae2b2d-6702-4415-af94-dfb0fe7980a3.jpg', 1590.00);

INSERT INTO pizza_pizza (name, description, category_id, base_price, on_sale,offer_id) VALUES ('Margherita', 'Tomato sauce, mozzarella, and oregano',2,1000.00 , false,1);
INSERT INTO pizza_pizza (name, description, category_id, base_price, on_sale,offer_id) VALUES ('Marinara', 'Tomato sauce, garlic and basil',3 ,900.00, false,1);
INSERT INTO pizza_pizza (name, description, category_id, base_price, on_sale,offer_id) VALUES ('Quattro Stagioni', 'Tomato sauce, mozzarella, mushrooms, ham, artichokes, olives, and oregano',2,1800.00 , false,2);
INSERT INTO pizza_pizza (name, description, category_id, base_price, on_sale,offer_id) VALUES ('Meat Lover', 'Tomato sauce, mozzarella, ham, pepperoni, chicken, pulled pork, and bacon',4,3000.00 , false,2);
INSERT INTO pizza_pizza (name, description, category_id, base_price, on_sale,offer_id) VALUES ('Diavola', 'Tomato sauce, mozzarella, spicy salami, chilli peppers, and garlic',5,1500.00 , false,2);
INSERT INTO pizza_pizza (name, description, category_id, base_price, on_sale,offer_id) VALUES ('Napoletana', 'Tomato sauce, mozzarella, oregano, anchovies',2,2500.00 , false,3);
INSERT INTO pizza_pizza (name, description, category_id, base_price, on_sale,offer_id) VALUES ('Hawaiian', 'Tomato sauce, mozzarella, bacon, and pineapple',1,2000.00 , false,3);
INSERT INTO pizza_pizza (name, description, category_id, base_price, on_sale,offer_id) VALUES ('Pepperoni', 'Tomato sauce, mozzarella, and pepperoni',1,1500.00 , false,3);
INSERT INTO pizza_pizza (name, description, category_id, base_price, on_sale,offer_id) VALUES ('Barbie que', 'BBQ sauce, Gouda, pulled pork, corn on the cob, bbq chicken wings, and beef jerky',4,3000.00 , false,3);
INSERT INTO pizza_pizza (name, description, category_id, base_price, on_sale,offer_id) VALUES ('Veggie', 'Tomato sauce, vegan mozzarella, mushrooms, onions, peppers, and olives',3,2000.00 , false,4);
INSERT INTO pizza_pizza (name, description, category_id, base_price, on_sale,offer_id) VALUES ('Mexicana', 'Hot salsa sauce, mexican cheese mix, chicken strips, chilli, and  beans',5,2500.00 , false,4);
INSERT INTO pizza_pizza (name, description, category_id, base_price, on_sale,offer_id) VALUES ('BBQ Chicken', 'BBQ sauce, mozzarella, chicken, bacon, and onions',4,2000.00 , false,4);

INSERT INTO pizza_pizzaimage(pizza_id, image) VALUES (13, 'https://pizza.az/upload/iblock/cb0/cb0abb92f9b512713c74bf03dbb70723.jpg');
INSERT INTO pizza_pizzaimage(pizza_id, image) VALUES (14, 'https://pizza.az/upload/iblock/0dd/0dd9107dcce95c0821d3a2683a03672f.jpg');
INSERT INTO pizza_pizzaimage(pizza_id, image) VALUES (3, 'https://pizza.az/upload/iblock/709/709b9db9c69cde80afbe5592ce881dd5.jpg');
INSERT INTO pizza_pizzaimage(pizza_id, image) VALUES (4, 'https://pizza.az/upload/iblock/94a/94a793fb83f1a72d27eabc920f7928b8.png');
INSERT INTO pizza_pizzaimage(pizza_id, image) VALUES (5, 'https://pizza.az/upload/iblock/e2b/e2b6c837564b1cfd4be0dfe3ef10c391.jpg');
INSERT INTO pizza_pizzaimage(pizza_id, image) VALUES (6, 'https://pizza.az/upload/iblock/95e/95ef3777825d84f3fe9ba4a65d2a1bcb.jpg');
INSERT INTO pizza_pizzaimage(pizza_id, image) VALUES (7, 'https://pizza.az/upload/iblock/344/344d52e15b3c4bf1eff0b06aa0b0d9c4.jpg');
INSERT INTO pizza_pizzaimage(pizza_id, image) VALUES (8, 'https://pizza.az/upload/iblock/f4f/f4f3e2cce270517c62adbd4ae6a95656.jpg');
INSERT INTO pizza_pizzaimage(pizza_id, image) VALUES (9, 'https://pizza.az/upload/iblock/3fd/3fd2ddc518e442ca561c193c2393878c.jpg');
INSERT INTO pizza_pizzaimage(pizza_id, image) VALUES (10, 'https://pizza.az/upload/iblock/94b/94b0f985a6c7ec2e94da5fc406efe584.jpg');
INSERT INTO pizza_pizzaimage(pizza_id, image) VALUES (11, 'https://pizza.az/upload/iblock/da5/da50df37c3a5ba08ea4689aad0cf7714.jpg');
INSERT INTO pizza_pizzaimage(pizza_id, image) VALUES (12, 'https://pizza.az/upload/iblock/37e/37eb63cda8f0ffca5b732896c3780187.png');

INSERT INTO offer_offer (name, offer_image, offer_price) VALUES ('2f1 offer, only pay for the more expensive on', 'https://pizza.az/upload/iblock/2ab/2ab979936a45e3d9007aa2e7bfce201d.png', 0.0);

select *
from cart_orderitemoffer;

DELETE FROM cart_shippingaddress
WHERE id = 1;

DELETE FROM cart_contactinformation
WHERE id = 1;