CREATE DATABASE IF NOT EXISTS cmsc127_project;
USE cmsc127_project;

CREATE TABLE IF NOT EXISTS User (
    Username VARCHAR(10) NOT NULL,
    Password LONGTEXT NOT NULL,
    Name VARCHAR(50) NOT NULL,
    Usertype ENUM('Owner', 'Customer') NOT NULL DEFAULT 'Customer',
    PRIMARY KEY (Username),
    CONSTRAINT user_username_uk UNIQUE(Username)
);

CREATE TABLE IF NOT EXISTS Food_Establishment (
    Food_establishment_id INT NOT NULL AUTO_INCREMENT,
    Food_establishment_name VARCHAR(50) NOT NULL,
    PRIMARY KEY (Food_establishment_id)
);

CREATE TABLE IF NOT EXISTS Food_Establishment_Rating (
    Food_establishment_id INT NOT NULL,
    Food_establishment_rating FLOAT,
    CONSTRAINT Food_Establishment_Rating_Food_establishment_id_fk 
        FOREIGN KEY(Food_establishment_id) REFERENCES Food_Establishment(Food_establishment_id)
);

CREATE TABLE IF NOT EXISTS Food_Item (
    Food_id INT NOT NULL AUTO_INCREMENT,
    Food_name VARCHAR(20) NOT NULL,
    Food_price INT NOT NULL,
    Food_establishment_id INT NOT NULL,
    PRIMARY KEY (Food_id),
    CONSTRAINT Food_Item_Food_establishment_id_fk 
        FOREIGN KEY(Food_establishment_id) REFERENCES Food_Establishment(Food_establishment_id)
);

CREATE TABLE IF NOT EXISTS Food_Item_Type (
    Food_id INT NOT NULL AUTO_INCREMENT,
    Food_name VARCHAR(20) NOT NULL,
    Food_item_type VARCHAR(10) NOT NULL,
    PRIMARY KEY (Food_id),
    CONSTRAINT Food_Item_Type_Food_id_fk 
        FOREIGN KEY(Food_id) REFERENCES Food_Item(Food_id)
);

CREATE TABLE IF NOT EXISTS Food_Review (
    Food_review_id INT NOT NULL AUTO_INCREMENT,
    Rating INT NOT NULL,
    Content TEXT,
    Date DATE DEFAULT CURDATE(),
    Username VARCHAR(10) NOT NULL,
    Food_name VARCHAR(20) NOT NULL,
    Food_establishment_id INT,
    PRIMARY KEY (Food_review_id),
    CONSTRAINT Food_Review_Rating CHECK (Rating >= 0 AND Rating <= 5),
    CONSTRAINT Food_Review_Username_fk 
        FOREIGN KEY(Username) REFERENCES User(Username),
    CONSTRAINT Food_Review_Food_name_fk 
        FOREIGN KEY(Food_name) REFERENCES Food_Item(Food_name),
    CONSTRAINT Food_Review_Food_establishment_id_fk 
        FOREIGN KEY(Food_establishment_id) REFERENCES Food_Establishment(Food_establishment_id)
);

CREATE TABLE IF NOT EXISTS Creates (
    Username VARCHAR(10) NOT NULL,
    Food_establishment_id INT NOT NULL,
    Food_name VARCHAR(20),
    CONSTRAINT Creates_Username_fk 
        FOREIGN KEY(Username) REFERENCES User(Username),
    CONSTRAINT Creates_Food_establishment_id_fk 
        FOREIGN KEY(Food_establishment_id) REFERENCES Food_Establishment(Food_establishment_id),
    CONSTRAINT Creates_Food_name_fk 
        FOREIGN KEY(Food_name) REFERENCES Food_Item(Food_name)
);
