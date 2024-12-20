# Piyush Cafe Ordering System with Tkinter and MySQL

This is a Cafe Ordering System built using Python's Tkinter for the graphical user interface (GUI) and MySQL for storing order data. The application allows users to select items from a menu, input their name and age, and place an order. The order details are stored in a MySQL database.

## Features

- **Menu Selection**: 
  - The available menu items include:
    - Maggi (50 Rs)
    - Sandwich (70 Rs)
    - Pasta (90 Rs)
    - Pizza (120 Rs)
    - Paneer Tacos (140 Rs)
  - Users can select quantities (from 1 to 10) for each item.

- **Order Details**: 
  - The system displays the current order details, showing the selected items, their quantities, and the total bill.

- **Database Integration**: 
  - The order details are stored in the `o_details` table in the MySQL database. The table records the name, age, food item, quantity, and total bill amount.

- **Place Order**: 
  - After selecting the items and quantities, the user can click "Place Order". The system shows a confirmation message with the total bill amount.

- **Exit**: 
  - Users can exit the application at any time by clicking the "Exit" button.

## Requirements

- **Python 3.x**: Ensure Python 3 or higher is installed to run the application.
- **Tkinter**: This is used for creating the GUI of the application.
- **MySQL**: A MySQL database is required to store order data.

## Prerequisites

- Install Python 3.x: [Download Python](https://www.python.org/downloads/)
- Install MySQL: [Download MySQL](https://dev.mysql.com/downloads/installer/)

### Install Required Libraries:

```bash
pip install mysql-connector-python

```

### Setting Up the MySQL Database:
- Before running the application, ensure you have a MySQL database set up.
- You can create the caffee database and o_details table using the following SQL commands:
- 
CREATE DATABASE caffee;

- USE caffee;

```bash
CREATE TABLE o_details 

(

    Name VARCHAR(50),
    
    Age INT,
    
    food VARCHAR(50),
    
    Quantity INT,
    
    Bill DECIMAL(10, 2)
  
);

```

### How to Run the Application:
1.  Clone or download this repository to your local machine.
2.  Open a terminal/command prompt and navigate to the project directory.
3.  Run the application using the following command:
   
   ```bash
    python cafe_ordering_system.py
  ```


### Screenshots
 Here are some screenshots of the application in action:
 

#### 1. WELCOME TO PIYUSH CAFE

  ![Screenshot 2024-12-20 131338](https://github.com/user-attachments/assets/d43760bb-0c36-42bf-8e6f-7055d0b04b03)


#### 2. MENU WITH PRICE , ADD TO INCREASE QUANTITY,
   ### ORDER DETAILS ,PLACE ORDER AND EXIT
   
   
![Screenshot 2024-12-20 131338](https://github.com/user-attachments/assets/620a7a78-2fe3-443f-96e7-7ddcf8f83162)




### 3 LETS ODER SOMETHING:

![Screenshot 2024-12-20 132309](https://github.com/user-attachments/assets/af7821de-2b61-47e3-89e6-250fac078ae9) 


### 4. AFTER ADD 


![Screenshot 2024-12-20 132234](https://github.com/user-attachments/assets/ecc2a2d5-90dd-4163-9c6e-b2688dd2c589)


 ### 5.IT WILL ASK TO CONTINUE ORDER MORE:


  ![Screenshot 2024-12-20 132700](https://github.com/user-attachments/assets/f5ef35fa-e2ea-4da4-bdc7-660dc041984b)
  

  ### 6.  IF IS SELECT YES AND 2 ADD TO PASTA IT WITLL ADD IN ORDER DETAILS
  

  ![Screenshot 2024-12-20 132902](https://github.com/user-attachments/assets/e872c5f3-2cc7-43ed-aa90-ab194ccca45d)

  
### 7. Place Order :


![Screenshot 2024-12-20 133017](https://github.com/user-attachments/assets/084b5b59-df4b-4b37-a6b5-99d540a5404f)

## Contributing
  Feel free to fork the repository and submit a pull request with any improvements or bug fixes.

## Author
 ### Piyush Ghavari

## How to Use:
 - Replace the screenshot file paths with your actual paths in the README.
 - Ensure your database setup matches the o_details table structure.
 - You can also add more items or modify the GUI as needed.

## Download the Application

