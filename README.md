# CMSC 127 Project

### Developers
- Benitez, Ramil
- Samson, Hannah Patricia
- Rondain, Andrea Louise
- CMSC 127 ST3L

**Note:** The following instructions are for Linux machines or WSL terminals.

### Prerequisites
- **MariaDB**: [Installation Instructions](https://drive.google.com/file/d/1W-q_y0cwEiPLrd3diJgEeXO1NkVDXAEG/view)
- **Python 3**: 
    ```
    sudo apt install python3
    ```
- **bcrypt**:
    ```
    pip install bcrypt
    ```

### How to set up and run
1. **Open a terminal**
2. **Navigate to the project files**
3. **Go to the Database folder**
    ```cd Database```
4. **Set up the database** 
    ```python3 setup_database.py```
    Wait for the success prompt to appear.
5. **After the success prompt, navigate back to the previous directory**
    ```cd ..``
6. **You should now be in the ~/cmsc127-project/**
7. **Run the application** 
    ```python3 main.py```

### Project Description
This information system will allow us to record, in electronic form, data on food reviews and food items from food establishments.

### Features
- Add, update, and delete a food review (on a food establishment or a food item);
- Add, delete, search, and update a food establishment;
- Add, delete, search, and update a food item.
- Search food items from any establishment based on a given price range and/or food type.
 
**Reports to be generated:**
- View all food establishments;
- View all food reviews for an establishment or a food item; 
- View all food items from an establishment;
- View all food items from an establishment that belong to a food type {meat | veg | etc.};
- View all reviews made within a month for an establishment or a food item;
- View all establishments with a high average rating (rating >= 4). (ratings from 1-5; highest is 5);
- View all food items from an establishment arranged according to price;
