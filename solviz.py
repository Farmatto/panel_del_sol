import datetime as dt
import pandas as pd
import os
print("Starting at: ",os.getcwd())
d = {}
def menu():
    print('''
            Welcome to SOLVIZ, visualize your solar production
           --------------------------------------------------- 
           SAVED USER DATA
            ''')
    today = dt.date.today()
    sol_install = dt.date(2008, 7, 14)
    days_since_install = (today - sol_install).days
    print("Today is:", today, "and it has been", days_since_install, "days since your installation")
    print("Last batch process contained",3,"days of sun above 50 %")
    print("""
    ------------------------------------------------------------------------""")


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

def file_play():
    print("Organizing the files, finding DIR")
    print(os.getcwd())
    os.chdir('OUTPUT')
    print(os.getcwd())
    print("Getting files...........this can take a bit..")
    elect = pd.read_excel(r'output.xlsx')
    print("done getting...")
    return elect


def Organize_Output_File():
    print("Organizing the files, finding DIR")
    print(os.getcwd())
    os.chdir('OUTPUT')
    print(os.getcwd())
    print("Getting files...........this can take a bit..")
    elect = pd.read_excel(r'output.xlsx')
    print(elect.head())
    print("Total size : ", elect.shape)


def fin():
    print("PROGRAM END....")
def main():
    menu()
    #Bring in all of the excel files and place collated vers. in OUTPUT
    #import_data()
    #Organize the Output file so that all the dates are in the right order
    #Organize_Output_File()
    #Display the data and save some graphs to the OUTPUT folder with date-stamp.
    file_play()
    fin()

if __name__ == "__main__":
    main()

