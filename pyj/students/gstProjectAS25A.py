#!/usr/bin/env python
# coding: utf-8

# # GST Billing System
# - Roll No - 1 : AGRIMA SRIVASTAVA
# - COMPUTER SCIENCE
# - In this project few fields where chosen to be entered into mySQL database and
#    a system of query, updating, deleting etc records was developed which was menu
#    driven through options
# - Last Update on 12 Jan 2025

# ## Certificate
# - This is to certify that this Computer Science Project on GST Billing System 
#     has been successfully completed by Agrima Srivastava of Class XII-B of 
#     Loreto Convent School as part of CBSE New Delhi for Academic Year : 2024-25
# - ...............
# - Teachers Sign

# ## Software Used
# - Anaconda - Python, Jupyter Notebook
# - Windows
# - MySQL 

# # Application / Projects
# - Install Libraries
#     - !pip install mysql.connector
#     - !pip install pandas
#     - !pip install mysql-connector-python
#     - !pip install --upgrade tabulate  # markdown
#     - !pip show tabulate # for pdf
#     - !pip install datetime
#     - !pip install fpdf

# !pip install mysql.connector
# !pip install pandas
# !pip install mysql-connector-python
# !pip install --upgrade tabulate  # markdown
# !pip show tabulate # for pdf
# !pip install datetime
# !pip install fpdf

# ## Libraries

# In[ ]:


# Libraries Used in the Project
import mysql.connector  # connecting to Mysql
from mysql.connector import Error # for capturing errors due to no connection
from IPython.display import clear_output #not used 
import pandas as pd # show table as pandas
from fpdf import FPDF
from datetime import datetime


# In[ ]:


#options
pd.set_option('display.max_columns',10)
pd.set_option("display.width", 1000)


# ## MySQL Connection
# - https://www.mysql.com/downloads/
# - Start MySQL, Login
# - Create Database : GSTBILLING 
#     - create database GSTBILLING;
# - Create USER : shubha with PASSWORD : Agrima2024# and GRANT \
#      ALL PRIVILIGES to 
#      this user for database GSTBILLING
#     - create user 'shubha'@'localhost' identified by 'Agrima2024#';
#     - grant all on *.* to 'shubha'@'localhost' with GRANT OPTION;
# - Use Database : GSTBILLING
#     - USE GSTBILLING;
#     - show tables;

# In[ ]:


# Connection
con = mysql.connector.connect( host='localhost', user='shubha',
                              password='Agrima2024#', database='GSTBILLING')


# In[ ]:


print(con , ' on ', datetime.now())


# In[ ]:


if con.is_connected():
    print("Connection Successful")
    print("Welcome to GST Billing - Product Table interface")
    cur=con.cursor()


# ## Create Empty Table
# - Create Table only if does not exist

# In[ ]:


# Create Empty Table for Products and Invoice
def create_table():
    q1 = ''' CREATE TABLE IF NOT EXISTS products ( SNO INT PRIMARY KEY,PNAME 
    VARCHAR(255) NOT NULL, PRANK CHAR(5) NOT NULL, COY VARCHAR(255) NOT NULL, 
    DOM DATE NOT NULL,  PRICE DECIMAL(10, 2) ,  GST DECIMAL(5, 2) NOT NULL,  
    FPRICE DECIMAL(10, 2) NOT NULL  )'''
    cur=con.cursor()
    cur.execute(q1)
    print("An Empty Table - PRODUCTS has been created in Database - GSTBILLING")
    cur.close()
    q2 = ''' CREATE TABLE IF NOT EXISTS invoice (INVOICE_ID INT 
    AUTO_INCREMENT PRIMARY KEY,  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
    SNO INT, QTY INT NOT NULL  )'''
    cur=con.cursor()
    cur.execute(q2)
    print("An Empty Table - INVOICE has been created in Database - GSTBILLING")
    cur.close()


# In[ ]:


#create_table()  #run the function to test only


# ## Describe Products Table

# In[ ]:


# Describe Products table
def describe_table():
    cur=con.cursor()
    if con.is_connected():
        print('Connected to Database : GST BILLING')
        tables = ["invoice", "products"]
        #cur = con.cursor()
        for table in tables:
            describe_query = f"DESCRIBE {table}"
            cur.execute(describe_query)
            tableDescp = cur.fetchall()
            print(f"Table `{table}` Description printed (if it existed).")
            for column in tableDescp:
                print(column)
            print('====================')
        cur.close()
    else:
        print('No connection to database/ mysql')


# In[ ]:


#describe_table()


# In[ ]:


# Write the SQL query to count rows
cur = con.cursor()
qc1 = "SELECT COUNT(*) FROM products"
# Execute the query
cur.execute(qc1)
# Fetch the result
count = cur.fetchone()[0]
print(f"Number of records in the table: {count}")
cur.close()

## Delete Table
# In[ ]:


#fun to delete products table
def delete_table():
    tables = ["invoice", "products"]
    cur = con.cursor()
    for table in tables:
        drop_query = f"DROP TABLE IF EXISTS {table}"
        cur.execute(drop_query)
        print(f"Table `{table}` dropped successfully (if it existed).")
    con.commit()
    cur.close()


# In[ ]:


#delete_table() # do only if required or to tests


# ## Add Sample Records

# In[ ]:


# insert sample rowsc to products table
def insert_sample():
    sData = [
            (10001, 'Product A', 'A', 'Company X', 100, '2024-01-01', 30, 130),
            (20001, 'Product B', 'B', 'Company Y', 200, '2024-02-01', 15, 230),
            (30001, 'Product C', 'C', 'Company Z', 300, '2024-03-01', 5, 315),
            (40001, 'Product D', 'B', 'Company X', 400, '2024-04-01', 15, 460),
            (50001, 'Product E', 'A', 'Company Y', 500, '2024-05-01', 30, 650)
        ]
    print('Sample Data inserted' , sData)
    cur = con.cursor()
    iq1 =  ''' INSERT INTO products (SNO, PNAME, PRANK, COY, PRICE, DOM,
    GST, FPRICE) VALUES (%s, %s, %s, %s, %s, %s, %s, %s) '''
    #if con.is_connected():
    cur.executemany(iq1, sData)
    con.commit()
    cur.close()
    #print(f'{cur.rowcount} rows inserted successfully !')


# In[ ]:


#insert_sample() # for testing only

cur = con.cursor()
cur.execute("SELECT COUNT(*) FROM products")
count = cur.fetchone()[0]
print(f"Number of records in the table now : {count}")
cur.close()
# ## Add Product One by One 

# In[ ]:


# Add Products
def add_products():
    opt='y'
    while opt == 'y':
        qa2 = '''insert into products( SNO,PNAME, PRANK, COY,  DOM, 
        PRICE, GST, FPRICE) values (%s,%s,%s, %s, %s, %s,%s,%s)'''
        iSNO = int(input("enter the product serial number (integer):"))
        iPNAME = input("enter the product name (text) :")
        iCOY = input("enter the company name (Text) ")
        iDOM = input("enter the Date of manufacutre: YYYY-MM-DD format")
        iPRANK = input("Enter the Rank Category (A/B/C) :")
        iPRICE = int(input("Enter the product price (no):"))
        iFPRICE = 0
        iGST = 0
        print(" GST percentages are given below according to their ranks")
        print(" Rank - A ->30%, B-> 15%, C- 5%")
        
        if iPRANK=="A":
            iGST = 30
            iFPRICE = iPRICE + iPRICE * iGST/100
        elif iPRANK == "B":
            iGST = 15
            iFPRICE = iPRICE + iPRICE * iGST/100
        elif iPRANK == "C":
            iGST = 5
            iFPRICE = iPRICE + iPRICE * iGST/100
        else:
            iGST = 0
            iFPRICE = iPRICE + iPRICE * iGST/100
        cur = con.cursor()
        data = (iSNO, iPNAME, iPRANK, iCOY, iDOM,  iPRICE,  iGST, iFPRICE)
        print('You have entered these values', iSNO, iPNAME, iPRANK, iCOY, iDOM,
              iPRICE, iGST, iFPRICE)
        cur.execute(qa2, data)
        con.commit()
        print(f"One Record insertion {iSNO} completed with values \n")
        #print(SNO, PNAME, COY, DOM, PRANK, PRICE, GST, FPRICE)
        opt = input("Do you want to add another product detail (y/n):")
cur.close()


# In[ ]:


#add_products() # this is for testing in script, run it through the menu


# ## Display all records

# In[ ]:


# display all records
def display_all():
    qd1 = 'select * from products'
    cur=con.cursor()
    cur.execute(qd1)
    records = cur.fetchall()
    print(f"{len(records)} found in the products table") 
    if records:
        print('\n All records in the products Table')
        for row in records:
            print(row)
    else:
        print('\n No records found in the products Table')
    cur.close()


# In[ ]:


#display_all()


# ## Display Records in Data Frame Format

# In[ ]:


# display all records
def display_df():
    qd2 = 'select * from products'
    df = pd.read_sql(qd2, con=con)
    print(df)


# In[ ]:


#display_df()


# ## Display Data in Markdown format

# In[ ]:


# Fetch data into a DataFrame
def display_mkdown():
    qd3 = "SELECT * FROM products"
    cur= con.cursor()
    cur.execute(qd3)
    columns = [col[0] for col in cur.description]
    data = cur.fetchall()
    df = pd.DataFrame(data, columns=columns)
    # Display the DataFrame
    print(df.to_markdown())  # For Markdown table-style display
    cur.close()


# In[ ]:


#display_mkdown()


# In[ ]:


#display_all()


# ## Show Records as per SNO

# In[ ]:


# display SNO
def count_SNO():
    cur = con.cursor()
    cName = 'SNO'
    qd2 = 'select SNO from products'
    cur.execute(qd2)
    records = cur.fetchall()
    print(f"{len(records)} found in the products table") 
    if records:
        print('\nAll records in the products Table are - ')
        #for row in records:  print(row, sep=', ')
        print(f"{cName} values: ", end="")
        print(", ".join(str(value[0]) for value in records))
    else:
        print('\n No records found in the products Table')
    cur.close()


# In[ ]:


count_SNO()


# ## Delete Row as per SNO
# - "select * from products where SNO={}".format(sno_value)
# -  cur.execute(qd3, (sno_value,))  (are similar ways)

# In[ ]:


def delete_row():
    count_SNO()
    cName = 'SNO'
    sno_value = input(f"Enter the value for {cName} to delete: ")
    qd3 = f"DELETE FROM products WHERE {cName} = %s"
    cur = con.cursor()
    cur.execute(qd3, (sno_value,))
    con.commit()
    # Check if a row was deleted
    if cur.rowcount > 0:
        print(f"Row(s) deleted successfully! {cur.rowcount} row(s) affected.")
    else:
        print("No rows found matching the criteria.")
    cur.close()


# In[ ]:


#delete_row()


# ## Update data of row
# - Select row based on SNO
# - Select the field to be update
# - Type the new value to be updated

# In[ ]:


def update_data():
    pCol = 'SNO'
    sno_value = input(f"Enter the value for {pCol} to be updated : ")
    print('Columns which can be updated are : PNAME, COY, PRICE, DOM, FPRICE')
    print('GST is updated based on PRANK')
    colUpdate = input("Enter the column name to be updated: ")
    new_value = input(f"Enter the new value for {colUpdate}: ")
    qu1 = f"UPDATE products SET {colUpdate} = %s WHERE {pCol} = %s"
    cur = con.cursor()
    cur.execute(qu1, (new_value, sno_value))
    con.commit()
    if cur.rowcount > 0:
        print(f"Row(s) Updated successfully! {cur.rowcount} row(s) affected.")
    else:
        print("No rows found matching the criteria.")
    cur.close()


# In[ ]:


#update_data()


# In[ ]:


#display_all()


# ## Update PRANK, GST, FPRICE

# In[2]:


def update_prank():
    pCol = 'SNO'
    sno_value = input(f'''Enter the value for {pCol} for whom you want 
                      to update PRANK/GST : ''')
    print('Columns which are being  updated are : PRANK and then GST & FPRICE')
    print('as GST is updated based on PRANK')
    colUpdate = 'PRANK'
    
    #get price
    qu2a = f"SELECT * FROM products WHERE SNO = %s"
    cur = con.cursor()
    cur.execute(qu2a, (sno_value,))
    result = cur.fetchone()
    if result:
        iPRICE = result[5]
        print(f'Price for {sno_value} is {iPRICE}') 
    else:
        print('No existing value found')
        iPRICE = 0
    cur.close()
    
    iPRANK = input(f"Enter the new value for {colUpdate}: ")
    if iPRANK=="A":
        iGST = 30
        iFPRICE = iPRICE + iPRICE * iGST/100
    elif iPRANK == "B":
        iGST = 15
        iFPRICE = iPRICE + iPRICE * iGST/100
    elif iPRANK == "C":
        iGST = 5
        iFPRICE = iPRICE + iPRICE * iGST/100
    else:
        iGST = 0
        iFPRICE = iPRICE + iPRICE * iGST/100
    print(f" New values for {sno_value} are - {iPRANK}, {iGST}, {iFPRICE}")
    
    qu2b = f"UPDATE products SET PRANK = %s, GST = %s, FPRICE = %s  WHERE {pCol} = %s"
    cur = con.cursor()
    cur.execute(qu2b, (iPRANK, iGST, iFPRICE, sno_value))
    con.commit()
    if cur.rowcount > 0:
        print(f"Row(s) Updated successfully! {cur.rowcount} row(s) affected.")
    else:
        print("No rows found matching the criteria.")
    cur.close()


# In[ ]:


#update_prank()


# In[ ]:


#display_all()


# ## Create Invoice
# - !pip install fpdf

# In[ ]:


# Query to fetch invoice data
def fetch_invoicedata():
    qi1 = '''SELECT p.SNO, p.PNAME, p.PRICE, p.GST, p.FPRICE, i.QTY, 
    i.INVOICE_ID, i.created_at, (p.FPRICE * i.QTY) AS TPRICE FROM 
    invoice i INNER JOIN products p ON i.SNO = p.SNO''' 
    df = pd.read_sql(qi1, con=con)
    print(df)


# In[ ]:


#fetch_invoicedata()


# In[ ]:


def additem_invoice():
    cName = 'SNO'
    sno_value = input(f"Enter the value for {cName} to add to Invoice : ")
    qd3 = f"SELECT * FROM products WHERE {cName} = %s"
    cur = con.cursor(buffered=True)
    cur.execute(qd3, (sno_value,))
    product = cur.fetchone()
    if product:
        print(f"Product Found")
        iQTY = input(f"Enter the Quantity for {sno_value} to genarate Invoice for: ")
        qii2 = f"INSERT INTO invoice (SNO, QTY) values (%s, %s)"
        values = (sno_value, iQTY)
        cur = con.cursor(buffered=True)
        cur.execute(qii2, (values))
        cur.close()
        con.commit()
        print(f"Product Serial No: {sno_value} with Quantity: {iQTY} inserted successfully.")
    else:
        print("No rows found matching the criteria.")
    cur.close()


# In[ ]:


#additem_invoice()


# In[ ]:


#fetch_invoicedata()


# In[3]:


def invoice_pdf():
    query = '''SELECT i.INVOICE_ID, p.SNO, p.PNAME, p.PRICE, p.GST,
    p.FPRICE, i.QTY, (p.FPRICE * i.QTY) AS TPRICE FROM invoice
    i INNER JOIN products p ON i.SNO = p.SNO''' 
    cur = con.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    columns = [col[0] for col in cur.description]
    current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    #print(columns)
    # Create PDF invoice
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    # Add title
    pdf.set_font("Arial", style="B", size=16)
    pdf.cell(200, 10,\
             txt=f"Invoice Generated by Agrima Srivastava at ", ln=True, align="C")
    pdf.ln(2)
    pdf.cell(200, 10, txt=f"Date and Time: {current_datetime}", ln=True, align="C")
    pdf.ln(2)
    pdf.cell(200, 10, \
     txt=f"Loreto Convent School - GST Billing System : AY 2024-25", ln=True, align="C")
    pdf.ln(5)

    # Add table headers
    pdf.set_font("Arial", style="B", size=12)
    headers = ["InvID","SNO", "PNAME", "PRICE", "GST", "FPRICE", "QTY", "TPRICE"]
    col_widths = [15, 15, 50, 20, 20, 20, 15, 30]  # Adjust column widths

    for i, header in enumerate(headers):
        pdf.cell(col_widths[i], 10, txt=header, border=1, align="F")
        #print(i, header)
    pdf.ln()  # Move to the next line after headers

    # Add table rows
    pdf.set_font("Arial", size=10)
    grand_total = 0
    for row in rows:
        grand_total += row[7]  # Accumulate total price
        for i, value in enumerate(row):
            pdf.cell(col_widths[i], 10, txt=str(value), border=1, align="C")
        pdf.ln()  # Move to the next line after each row

    # Add grand total
    pdf.set_font("Arial", style="B", size=12)
    pdf.cell(100, 10, txt="Grand Total", border=1, align="C")
    pdf.cell(40, 10, txt=f"Rs {grand_total:.2f}", border=1, align="C")
    pdf.ln(20)
    pdf.cell(200, 10, txt=f"Generated using Python and MySQL ", ln=True, align="C")
   
    # Save the PDF
    pdf.output("GSTinvoice.pdf")
    print("Invoice PDF generated successfully as 'GSTinvoice.pdf'.")
    cur.close()


# In[ ]:


#invoice_pdf()


# ## Main Function

# In[ ]:


def main():
    """Main function to handle user choices"""
    while True:
        # Display menu
        current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"  Welcome to GST Billing {current_datetime} Prepared By Agrima")
        print("\n Choose an operation:")
        print("1.  Create Table")
        print("2.  Drop/Delete the Table")
        print("3.  Insert Sample Data")
        print("4.  Insert One By One Data")
        print("5.  Insert Products to Invoice Table")
        print("6.  Display All the Data in the Products Table")
        print("7.  Display Only 1 Row based on SNO")
        print("8.  Update PRANK -> GST, FPRICE")
        print("9.  Update Other Values")
        print("10. Count rows in the Table")
        print("11. Delete Row in the Table")
        print("12. Describe the structure of the Table")
        print("13. Display Product Data in MarkDown Format")
        print("14. Display Data in Invoice Table")
        print("15. Create Invoice for All Product in Invoice Table")
       
        print("_______________") 
        print("0. Exit")
        
        # Get user choice
        choice = input("Enter your choice (from above): ")

        # Call the appropriate function
        if choice == "1":
            create_table()  # create table
        elif choice == "2":
            delete_table()
        elif choice == "3":
            insert_sample()
        elif choice == "4":
            add_products()
        elif choice == "5":
            additem_invoice()  
        elif choice == "6":
            display_all()
        elif choice == "7":
            count_SNO() 
        elif choice == "8":
            update_prank()
        elif choice == "9":
            update_data()
        elif choice == "10":
            count_SNO() 
        elif choice == "11":
            count_SNO()
            delete_row()
            count_SNO()
        elif choice == "12":
            describe_table()
        elif choice == "13":
            display_mkdown()
        elif choice == "14":
            fetch_invoicedata()
        elif choice == "15":
            invoice_pdf()
        elif choice == "0":
            print("Exiting the program. Goodbye!")
            # Clear the output of the current cell
            clear_output(wait=True)
            break
        else:
            print("Invalid choice. Please try again.")
            clear_output(wait=True)


# In[ ]:


# Call the main function
if __name__ == "__main__":
    main()


# In[ ]:


print('End of File')


# # END of GST BILLING project
# - run the notebook from prompt
# - ipython  (command prompt)
# - %run your_script.ipynb
# - jupyter execute notebook.ipynb  (change Name)

# In[ ]:




