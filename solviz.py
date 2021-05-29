import datetime
import pandas as pd
import os
print("Starting at: ",os.getcwd())
d = {}
def menu():
    print("I'm the main menue")
    print("What would you like to do?")
    print('''
            Welcome to SOLVIZ, visualize your solar production''')

def import_data():
    """Take and combine excel files from the INPUT folder and place a
    collated version into the OUTPUT folder."""
    print(os.getcwd())
    os.chdir('INPUT')
    print("Now in: ",os.getcwd())
    fl = os.listdir()
    print(fl)
    df = pd.DataFrame()
    for file in fl:
        df = df.append(pd.read_excel(file), ignore_index=True)
        print(df.shape)
    os.chdir('..')
    os.chdir('OUTPUT')
    print(os.getcwd())

    writer = pd.ExcelWriter('output.xlsx')
    df.to_excel(writer)
    writer.save()

def Organize_Output_File():
    print(Organizing the files)

def main():
    menu()
    #Bring in all of the excel files and place collated vers. in OUTPUT
    #import_data()

    #Organize the Output file so that all the dates are in the right order
    Organize_Output_File()

    #Display the data and save some graphs to the OUTPUT folder with date-stamp.


if __name__ == "__main__":
    main()

