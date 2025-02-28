import pandas as pd
import datetime as dt

df_product = pd.read_csv('products.csv') #load product csv
df_transactions = pd.read_csv('transactions.csv') #load transactions csv
df_transactions = df_transactions.drop_duplicates(subset = ["RECEIPT_ID"], keep = 'first') #remove duplicate records
df_users = pd.read_csv('users.csv') #load users csv
df_users['CREATED_DATE'] = pd.to_datetime(df_users['CREATED_DATE']) #change created date column from str to datetime

firstmerge_df = pd.merge(df_users, df_transactions, left_on = 'ID', right_on = 'USER_ID', how = 'inner') #first merge

finalmerge_df = pd.merge(firstmerge_df, df_product, on = 'BARCODE', how = 'inner') #final merge, all three tables
finalmerge_df['CREATED_DATE'] = pd.to_datetime(finalmerge_df['CREATED_DATE']) #change created date column from str to datetime
finalmerge_df['BIRTH_DATE'] = pd.to_datetime(finalmerge_df['BIRTH_DATE']) #change birth date column from str to datetime
finalmerge_df['SCAN_DATE'] = pd.to_datetime(finalmerge_df['SCAN_DATE']) #change scanned date column from str to datetime
finalmerge_df['FINAL_QUANTITY'] = pd.to_numeric(finalmerge_df['FINAL_QUANTITY'], errors = 'coerce') #converts quantity figures to numerical values
finalmerge_df['FINAL_SALE'] = pd.to_numeric(finalmerge_df['FINAL_SALE'], errors = 'coerce') #converts sales figures to numerical values

""" 1. What are the top 5 brands by receipts scanned among users 21 and over? """
def top5brands_21():
    df_21 = finalmerge_df[finalmerge_df['BIRTH_DATE'] <= '2004-02-28'] #filter for 21+ (hard coding here, sorry)
    df_brand = df_21.groupby('BRAND')['BRAND'].count() #aggregates instances of each brands
    top_5 = df_brand.nlargest(5) #sorts and filters the top 5 brands
    print(top_5)

#top5brands_21()

###

""" 2. What are the top 5 brands by sales among users that have had their account for at least six months? """
def top5brands_6mon():
    df_6months = finalmerge_df[finalmerge_df['CREATED_DATE'] <= '2024-08-28'] #filter for accounts 6 months or older (again, apologies for hard coding)
    df_brandbysales = df_6months.groupby('BRAND')['FINAL_SALE'].sum()
    top_5 = df_brandbysales.nlargest(5)
    print(top_5)

#top5brands_6mon()

###

""" 3. What is the percentage of sales in the Health & Wellness category by generation? """
def wellness_bygeneration():
    finalmerge_df['Year'] = finalmerge_df['BIRTH_DATE'].dt.year #make column for year of birth
    year_ranges = [1901, 1925, 1946, 1965, 1980, 1995, 2012] #list of edges of year ranges
    gens = ['Centennial', 'Silent', 'Boomer', 'Gen-X', 'Millenial', 'Gen-Z'] #generation labels associated with year ranges
    finalmerge_df['Generations'] = pd.cut(finalmerge_df['Year'], bins = year_ranges, labels = gens, right = False) #create column to label user's generation
    df_health_wellness = finalmerge_df[finalmerge_df['CATEGORY_1'] == 'Health & Wellness'] #filter on health + wellness
    df_generation = df_health_wellness.groupby('Generations')['FINAL_SALE'].sum() #grouping generation by sales
    total_sales = df_health_wellness['FINAL_SALE'].sum() #total sales to use in percentage calculation
    percentage_by_gen = (df_generation / total_sales) * 100 #percentage of sales by generation
    print(percentage_by_gen)

#wellness_bygeneration()

######

""" 4. Who are Fetchs power users? """
def power_users():
    df_power = df_transactions.groupby('USER_ID')['RECEIPT_ID'].count() #grouping users by their associated reciepts
    top5 = df_power.nlargest(5) #filtering top 5 users
    print(top5)

#power_users()

###

""" 5. Which is the leading brand in the Dips & Salsa category? """
def salsaverde():
    df_salsa = finalmerge_df[finalmerge_df['CATEGORY_2'] == 'Dips & Salsa'] #filter on dips+salsa
    top_dips = df_salsa.groupby('BRAND')['FINAL_QUANTITY'].sum() #aggregate the quantities for each brand
    big_dipper = top_dips.nlargest(1) #show the top brand
    print(big_dipper)

#salsaverde()

###

""" 6. At what percent has Fetch grown year over year? """
def yearly_growth():
    df_users['Year'] = df_users['CREATED_DATE'].dt.year #make column for year of account creation
    df_yearly_signups = df_users.groupby('Year')['Year'].count() #counting
    df_yearly_signups = df_yearly_signups.reset_index(name = 'New Users')
    df_yearly_signups['Percent Growth'] = df_yearly_signups['New Users'].pct_change() * 100
    print(df_yearly_signups)

yearly_growth()
