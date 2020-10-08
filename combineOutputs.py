import pandas as pd
import sqlalchemy
#replace xxxx with password in the following line
engine = sqlalchemy.create_engine('mysql+pymysql://root:xxxx@localhost/acbtask1')

listOfTables = list(pd.read_sql_query('show tables;',engine)['Tables_in_acbtask1'])
dfList = []
global firstOccurrence
global finalTableDF
for i in listOfTables:
	if 'stu_op' in i:
		finalTableDF = pd.read_sql_table(i,engine) 
        #first 'stu_op20xxxxxx' occurrence in the list of tables
		firstOccurrence = i 
		break

finalTableDF.to_sql(
                name='Course_List_all_ACB', 
                # final table to store courses of all ACB students registered in GUI
                con=engine,
                if_exists='replace',
                index=False
            )

for i in listOfTables:
	if 'stu_op' in i:
		if i == firstOccurrence:
			continue
		
		outputDF = pd.read_sql_table(i,engine)
		outputDF.to_sql(
                name='Course_List_all_ACB', 
                con=engine,
                if_exists='append', 
                #append each registered ACB students course detail to the table named Course_List_all_ACB
                index=False
            )
