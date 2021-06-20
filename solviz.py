import datetime as dt
import pandas as pd
import os
import matplotlib.pyplot as plt

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
    #print("Last batch process contained",3,"days of sun above 50 %")
    print("""
    ------------------------------------------------------------------------""")


def combine_excel_files():
    """Take and combine excel files from the INPUT folder and place a
    collated version into the OUTPUT folder.
    Also save a faster version in feather to do the processes on."""
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
    df.to_pickle("soloutdat.pkl")

'''
def df_from_comb_excel():
    print("getting the combined excel file from:")
    print(os.getcwd())
    print("changing to DIR:")
    os.chdir('OUTPUT')
    print(os.getcwd())
    print("Reading Combined excel file....this can take a bit..")
    elect = pd.read_excel(r'output.xlsx')
    print("done getting...")
    print("taking output file and saving as a feather file")
    elect.to_feather("datafrm.ftr")
    print("saved")
    return elect
'''

def read_pickle_data():
    print("changing to DIR:")
    os.chdir('OUTPUT')
    print(os.getcwd()) 
    sdf = pd.read_pickle("soloutdat.pkl")
    print("pickle read")
    #os.chdir("..")
    return sdf

def clean_data(d):
    print("--------------------Cleaning Data------------------\n")
    print("finding zeros or nans and replacing with empty string?")
    d.isna().sum().reset_index(name="n").plot.bar('index',y='n',rot=45)
    print(d.columns)
    plt.savefig('zeros_per_category.png')
    print("see OUTPUT DIR for .png of zereos in each column")

    #find NAN's and blank problem cells
    #find date-times that cause issuess
    print(">>>CLEANED")

def analyze_data(d):
    print("----------------analyzing data--------------")
    print(d.describe())
    #write new modified file to OUTPUT DIR
    #and graphs.
    print("see OUTPUT Dir for files and pictures.")



def fin():
    print("PROGRAM END....")

def main():

    menu()
    #combine_excel_files()
    #Bring in all of the excel files and place collated vers. in OUTPUT
    #import_data()
    #Organize the Output file so that all the dates are in the right order
    #Display the data and save some graphs to the OUTPUT folder with date-stamp.
    #curdat = file_play()
    #return curdat
    #df_from_comb_excel()
    mdata = read_pickle_data()
    clean_data(mdata)
    analyze_data(mdata)
    fin()

if __name__ == "__main__":
    main()

