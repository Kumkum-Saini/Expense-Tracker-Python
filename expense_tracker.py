import pandas as pd
import os
import matplotlib.pyplot as plt

#file to store expenses
File_name = "expenses.csv"

#function that allow users to add new expense records
def add_expense(date, amount, category , description):
    """Adds a new expense to the csv file"""
   
    data = {               #dictionary to store expense information
        "Date": [date],
        "Amount":[amount],
        "Category":[category],
        "Description":[description]
    }

    df = pd.DataFrame(data) 


    #check if the file exists
    
    if os.path.exists(File_name) and os.path.getsize(File_name)>0:
        #append the new data to the file without overwriting
        df.to_csv(File_name,  index=False, mode = 'a', header= False)   
    else:
        df.to_csv(File_name, index=False)  #create a new csv file with column headers(date,amount,etc)

    print("Expense added successfully!")


#view all the expenses recorded

def view_expense():
    """Displays all the recorded expenses"""
    if os.path.exists(File_name):
        df = pd.read_csv(File_name)   #read the csv into dataframe
        if df.empty:
            print("\nNo expenses recorded!")
        else:
            print("\nRecorded Expenses:")
            print(df.to_string(index=False))  # Print without the index
       # print(df)
    else:
        print("No expense recorded!")

#clear the recorded expenses
def clear_expense():
    if os.path.exists(File_name):
        open(File_name,'w').close()
        print("All the expenses are cleared")
    else:
        print("no response recorded")

 
#summarize the expenses by grouping the data  based on the category 
def expense_summary():
    if os.path.exists(File_name):
        df = pd.read_csv(File_name)
        summary = df.groupby("Category")['Amount'].sum()
        print(summary)
    else:
        print("No expense recorded!")


#plotting spending by category using a bar chart
def plot_expense():
    if os.path.exists(File_name):
        df = pd.read_csv(File_name)
        df.groupby("Category")["Amount"].sum().plot(kind = "bar", color = "Blue")
        plt.title("spending by category")
        plt.xlabel("Category")
        plt.ylabel("Total Amount")
        plt.show()
    else:
        print("No expense recorded!")

#user interactive menu system       
def main():
    while True:
        print("\nExpense Tracker")
        print("1.Add Expense")
        print("2.View expense")
        print("3.Clear expenses")
        print("4.Exit")
        print("5.Expense summary")
        print("6.Plot expenses")

        choice = input("Write your choice here: ")
        if choice == '1':
            date = input("Enter date(YYYY-MM-DD): ")
            amount= float(input("Enter Amount:"))
            category= input("Enter category(food, transport, etc): ")
            description= input("Description(Where did you spend the money? ): ")
            add_expense(date, amount, category, description)
        elif choice == '2':
            view_expense()
        elif choice == '3':
            clear_expense()
        elif choice == '4':
            print("Exiting..")
            break
        elif choice == '5':
            expense_summary()
        elif choice == '6':
            plot_expense()
        else:
            print("Invalid choice!")
if __name__ == "__main__":
    main()





        
