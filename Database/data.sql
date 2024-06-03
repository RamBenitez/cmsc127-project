INSERT INTO User (Username, Password, Name, Usertype) VALUES ('admin' , 'admin', 'Alice', 'Owner');
INSERT INTO User (Username, Password, Name) VALUES ('ramz', 'pass123', 'Ramil');
INSERT INTO User (Username, Password, Name) VALUES ('hana', 'pass123', 'Hannah');
INSERT INTO User (Username, Password, Name) VALUES ('lou', 'pass123', 'Louise');

INSERT INTO Food_Establishment VALUES ("Seoul Kitchen"), ("The Crunch"), ("WeDeliver");
INSERT INTO Food_Item (Food_name, Food_price, Food_establishment_id) VALUES ('Croffle', 120, 1);
INSERT INTO Food_Item_Type (Food_id, Food_item_type) VALUES (1, "Bread");
INSERT INTO Food_Item (Food_name, Food_price, Food_establishment_id) VALUES ('Mandu', 145, 1);
INSERT INTO Food_Item_Type (Food_id, Food_item_type) VALUES (2, "Vegetable");
INSERT INTO Food_Item (Food_name, Food_price, Food_establishment_id) VALUES ('Ramyun', 140, 1);
INSERT INTO Food_Item_Type (Food_id, Food_item_type) VALUES (3, "Noodles");
INSERT INTO Food_Item_Type (Food_id, Food_item_type) VALUES (3, "Vegetable");

INSERT INTO Food_Item (Food_name, Food_price, Food_establishment_id) VALUES ('Chicken Shots Meal', 70, 2);
INSERT INTO Food_Item_Type (Food_id, Food_item_type) VALUES (4, "Meat");
INSERT INTO Food_Item_Type (Food_id, Food_item_type) VALUES (4, "Grains");
INSERT INTO Food_Item (Food_name, Food_price, Food_establishment_id) VALUES ('Chicken Skin Meal', 50, 2);
INSERT INTO Food_Item_Type (Food_id, Food_item_type) VALUES (5, "Meat");
INSERT INTO Food_Item_Type (Food_id, Food_item_type) VALUES (5, "Grains");
INSERT INTO Food_Item (Food_name, Food_price, Food_establishment_id) VALUES ('Twister Fries', 80, 2);
INSERT INTO Food_Item_Type (Food_id, Food_item_type) VALUES (6, "Vegetable");

INSERT INTO Food_Item (Food_name, Food_price, Food_establishment_id) VALUES ('Silog', 25, 3);
INSERT INTO Food_Item_Type (Food_id, Food_item_type) VALUES (7, "Protein");
INSERT INTO Food_Item_Type (Food_id, Food_item_type) VALUES (7, "Grains");
INSERT INTO Food_Item (Food_name, Food_price, Food_establishment_id) VALUES ('Bacon Silog', 57, 3);
INSERT INTO Food_Item_Type (Food_id, Food_item_type) VALUES (8, "Meat");
INSERT INTO Food_Item_Type (Food_id, Food_item_type) VALUES (8, "Grains");
INSERT INTO Food_Item_Type (Food_id, Food_item_type) VALUES (8, "Protein");
INSERT INTO Food_Item (Food_name, Food_price, Food_establishment_id) VALUES ('Luncheon Meat Silog', 45, 3);
INSERT INTO Food_Item_Type (Food_id, Food_item_type) VALUES (9, "Meat");
INSERT INTO Food_Item_Type (Food_id, Food_item_type) VALUES (9, "Grains");
INSERT INTO Food_Item_Type (Food_id, Food_item_type) VALUES (9, "Protein");

INSERT INTO Food_Review (Rating, Content, Date, Username, Food_id, Food_establishment_id) VALUES (5,'I love their croffle!', '2024-05-14', 'hana', 1, 1);
INSERT INTO Food_Review (Rating, Content, Date, Username, Food_id, Food_establishment_id) VALUES (3,'Okay lang, medyo overpriced', '2024-05-30', 'ramz', 6, 2);
INSERT INTO Food_Review (Rating, Content, Date, Username, Food_id, Food_establishment_id) VALUES (5,'Order ko palagi', '2024-06-01', 'lou', 8, 3);