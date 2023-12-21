import sqlite3
import pandas as pd
import matplotlib.pyplot as plt



def insert_data (file_path, table_name, connection):
    cursor = connection.cursor()
    df = pd.read_csv(file_path)
    df.to_sql(table_name, connection, index=False, if_exists='replace')
    connection.commit()
    print(f'Data from {file_path} successfully inserted into {table_name}.')




sale_csv_file_path = r'datasets\sales.csv'
user_csv_file_path = r'datasets\users.csv'
database_name = 'database.db'  

conn = sqlite3.connect(database_name)

insert_data(sale_csv_file_path, 'sale', conn)
insert_data(user_csv_file_path, 'user', conn)


select_sale_statement = """
SELECT sale_id
    , user_id
    , sale_date
    , sale_amount
FROM sale;
"""
df_sale = pd.read_sql_query(select_sale_statement, conn)




select_user_statement = """
SELECT user_id
    , signup_date
    , country
FROM user;
"""
df_user = pd.read_sql_query(select_user_statement, conn)


most_active_users_statement = """
	SELECT 
        user_id
        , SUM(sale_amount) AS full_amount
        , COUNT(sale_amount) AS number_of_sales
	FROM sale
	GROUP BY user_id
	ORDER BY 3 DESC, 2 DESC
    LIMIT 10;
"""
active_users = pd.read_sql_query(most_active_users_statement, conn)

print(active_users)


all_data_query ="""
SELECT 
	s.sale_id
	, s.user_id
	, u.country
	, u.signup_date
	, s.sale_date
	, s.sale_amount 
FROM
	sale s
JOIN user u ON
	s.user_id = u.user_id 
"""
df_all = pd.read_sql_query(all_data_query, conn)

all_data_query ="""
	SELECT  
        user_id, strftime('%Y-%m', sale_date) AS month
        , sum(sale_amount) AS full_amount
        , count(sale_amount) AS number_of_sales
	FROM sale
	GROUP BY user_id, month
	ORDER BY 4 desc, 3 desc
"""
df = pd.read_sql_query(all_data_query, conn)


fig, axes = plt.subplots(nrows=4, ncols=1, figsize=(9, 9))

df.groupby('month')['full_amount'].sum().plot(kind='bar', ax=axes[0])
axes[0].set_title('Histogram of Amount per Month')
axes[0].set_ylabel('Amount')


df.groupby('month')['number_of_sales'].sum().plot(kind='bar', ax=axes[1], color='orange')
axes[1].set_title('Histogram of Count per Month')
axes[1].set_ylabel('Count')

df_all.groupby('country')['sale_date'].count().plot(kind='bar', ax=axes[2], color='blue')
axes[2].set_title('Histogram of Count per Country')
axes[2].set_ylabel('Count')


df_all.groupby('country')['sale_amount'].sum().plot(kind='bar', ax=axes[3], color='green')
axes[3].set_title('Histogram of Amount per Country')
axes[3].set_ylabel('Amount')

plt.tight_layout()
plt.show()


conn.close()