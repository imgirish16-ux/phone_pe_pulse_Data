!pip install pandas
import pandas as pd
import os

#aggregated_insurance

path1="C:/Users/GIRISH/OneDrive/Desktop/phone pe project/pulse/data/aggregated/insurance/country/india/state"
agg_insurance=os.listdir(path1)

col1={"states":[],"years":[],"quarter":[],"trans_type":[],"trans_amount":[],"trans_count":[]}

for states in agg_insurance:
    prsnt_state=path1 + "/" +states 
    agg_year=os.listdir(prsnt_state)
    
    for year in agg_year:
        current_year=prsnt_state+"/"+year
        agg_file=os.listdir(current_year)

        for files in agg_file:
            c_file=current_year+"/"+files
            data=open(c_file,"r")

            a=json.load(data)
            for i in a["data"]["transactionData"]:
                name=i['name']
                count=i['paymentInstruments'][0]['count']
                amount=i['paymentInstruments'][0]['amount']
                col1["trans_type"].append(name)
                col1["trans_count"].append(count)
                col1["trans_amount"].append(amount)
                col1["states"].append(states)
                col1["years"].append(year)
                col1["quarter"].append(int(files.strip(".json")))


aggregated_insurance=pd.DataFrame(col1)


aggregated_insurance['states']=aggregated_insurance['states'].str.replace("-"," ")
aggregated_insurance["states"]=aggregated_insurance["states"].str.replace('andaman & nicobar islands','Andaman & Nicobar')
aggregated_insurance["states"]=aggregated_insurance["states"].str.title()
aggregated_insurance["states"]=aggregated_insurance["states"].str.replace('Dadra & Nagar Haveli & Daman & Diu','Daman & Diu')


#Aggregated_transaction
path2="C:/Users/GIRISH/OneDrive/Desktop/phone pe project/pulse/data/aggregated/transaction/country/india/state"
ser_path=os.listdir(path2)

col2={"states":[],"years":[],"quarter":[],"trans_count":[],"trans_type":[],"trans_amount":[]}


for states in ser_path:
    cur_states=path2+"/"+states
    agre2_path=os.listdir(cur_states)

    for years in agre2_path:
        cur_year=cur_states+"/"+years
        loc=os.listdir(cur_year)

        for files_1 in loc:
            files_part=cur_year+"/"+files_1
            loc_file=open(files_part,"r")

            b=json.load(loc_file)
            
            for i in b['data']['transactionData']:
                count=i['paymentInstruments'][0]['count']
                amount=i['paymentInstruments'][0]['amount']
                name=i['name']
                col2["states"].append(states)
                col2["years"].append(years)
                col2["quarter"].append(int(files_1.strip(".json")))
                col2["trans_count"].append(count)
                col2["trans_type"].append(name)
                col2["trans_amount"].append(amount)
Aggregated_transaction=pd.DataFrame(col2)
Aggregated_transaction['states']=Aggregated_transaction['states'].str.replace('andaman-&-nicobar-islands','Andaman & Nicobar')
Aggregated_transaction['states']=Aggregated_transaction['states'].str.replace("-"," ")
Aggregated_transaction['states']=Aggregated_transaction['states'] .str.title()                                                                       
Aggregated_transaction['states']=Aggregated_transaction['states'].str.replace('Dadra & Nagar Haveli & Daman & Diu','Daman & Diu')               
Aggregated_transaction


#Aggregated_user
path3="C:/Users/GIRISH/OneDrive/Desktop/phone pe project/pulse/data/aggregated/user/country/india/state"
agre_path=os.listdir(path3)

col3={"states":[],"years":[],"quarter":[],"trans_count":[],"percentage":[],"Brands":[]}

    
for state in agre_path:
    ad_state=path3+"/"+state
    aggre_state=os.listdir(ad_state)

    for year in aggre_state:
        cur_year=ad_state+"/"+year 
        agre_year=os.listdir(cur_year)

        for files in agre_year:
            cur_files=cur_year+"/"+files
            agre_files=open(cur_files,"r")

            c=json.load(agre_files)
            
            try:
                for i in c['data']['usersByDevice']:
                    count=i['count']
                    brands=i['brand']
                    percentage=i['percentage']

                    col3["Brands"].append(brands)
                    col3["trans_count"].append(count)
                    col3["percentage"].append(percentage)
                    col3["states"].append(state )
                    col3["years"].append(year)
                    col3["quarter"].append(int(files.strip(".json")))
            except:
                pass

Aggregated_user=pd.DataFrame(col3)
Aggregated_user['states']=Aggregated_user['states'].str.replace('andaman-&-nicobar-islands','Andaman & Nicobar')
Aggregated_user['states']=Aggregated_user['states'].str.replace("-"," ")
Aggregated_user['states']=Aggregated_user['states'] .str.title()                                                                       
Aggregated_user['states']=Aggregated_user['states'].str.replace('Dadra & Nagar Haveli & Daman & Diu','Daman & Diu')    


#Map_insurance
path4="C:/Users/GIRISH/OneDrive/Desktop/phone pe project/pulse/data/map/insurance/hover/country/india/state"
agre_path_4=os.listdir(path4)

col4={"states":[],"years":[],"quarter":[],"district_name":[],"trans_count":[],"trans_amount":[]}

for states in agre_path_4:
    cur_states=path4+"/"+states
    agr_loc=os.listdir(cur_states)


    for years in agr_loc:
        cur_year=cur_states+"/"+years
        agr_lo=os.listdir(cur_year)

        for files in agr_lo:
            cur_file=cur_year+"/"+files
            cur_file_loc=open(cur_file,"r")

            d=json.load(cur_file_loc)
            
            for i in d['data']['hoverDataList']:
                name=i['name']
                count=i['metric'][0]['count']
                amount=i['metric'][0]['amount']
                col4["states"].append(states)
                col4["years"].append(years)
                col4["quarter"].append(int(files.strip(".json")))
                col4["district_name"].append(name)
                col4["trans_count"].append(count)
                col4["trans_amount"].append(amount)
                
Map_insurance=pd.DataFrame(col4)
Map_insurance["states"]=Map_insurance["states"].str.replace("-"," ")
Map_insurance["states"]=Map_insurance["states"].str.title()
Map_insurance["states"]=Map_insurance["states"].str.replace("andaman-&-nicobar-islands",'Andaman & Nicobar')
Map_insurance["states"]=Map_insurance["states"].str.replace('Dadra & Nagar Haveli & Daman & Diu','Dadar & Diu')
Map_insurance

#Map_Transaction
path5="C:/Users/GIRISH/OneDrive/Desktop/phone pe project/pulse/data/map/transaction/hover/country/india/state"
agree_path=os.listdir(path5)

col5={"states":[],"years":[],"quarter":[],"districts":[],"trans_count":[],"trans_amount":[]}

for states in agree_path:
    cur_states=path5+"/"+states
    agre_list=os.listdir(cur_states)

    for year in agre_list:
        cur_year=cur_states+"/"+year
        agre_path=os.listdir(cur_year)

        for files in agre_path:
            cur_files=cur_year+"/"+files
            check_file=open(cur_files,"r")

            e=json.load(check_file)
            
            for i in e['data']['hoverDataList']:
                name=i['name']
                count=i['metric'][0]['count']
                amount=i['metric'][0]['amount']
                col5["districts"].append(name)
                col5["quarter"].append(int(files.strip(".json")))
                col5["states"].append(states)
                col5["trans_amount"].append(amount)
                col5["trans_count"].append(count)
                col5["years"].append(year)
Map_map=pd.DataFrame(col5)
Map_map['states']=Map_map['states'].str.replace('andaman-&-nicobar-islands','Andaman & Nicobar')
Map_map['states']=Map_map['states'].str.replace("-"," ")
Map_map['states']=Map_map['states'] .str.title()                                                                       
Map_map['states']=Map_map['states'].str.replace('Dadra & Nagar Haveli & Daman & Diu','Daman & Diu')               
Map_map       


#map_user
path6="C:/Users/GIRISH/OneDrive/Desktop/phone pe project/pulse/data/map/user/hover/country/india/state"
agr_path=os.listdir(path6)

col6={"states":[],"years":[],"quarter":[],"district_name":[],"reg_user":[],"app_opens":[]}

for states in agr_path:
    cur_states=path6 +"/"+ states
    agr_loc=os.listdir(cur_states)

    for years in agr_loc:
        cur_year=cur_states +"/"+years
        loc=os.listdir(cur_year)

        for files in loc:
            file_o=cur_year+"/"+files
            file_loc=open(file_o,"r")

            f=json.load(file_loc)
            for i in f['data']['hoverData'].items():
                districts=i[0]
                reg_user=i[1]['registeredUsers']
                app_openes=i[1]['appOpens']
                col6["district_name"].append(districts)
                col6["reg_user"].append(reg_user)
                col6["app_opens"].append(app_openes)
                col6["states"].append(states)
                col6["years"].append(years)
                col6["quarter"].append(int(files.strip(".json")))
map_user=pd.DataFrame(col6)
map_user['states']=map_user['states'].str.replace('andaman-&-nicobar-islands','Andaman & Nicobar')
map_user['states']=map_user['states'].str.replace("-"," ")
map_user['states']=map_user['states'] .str.title()                                                                       
map_user['states']=map_user['states'].str.replace('Dadra & Nagar Haveli & Daman & Diu','Daman & Diu')               
map_user       


#Top_insurance
path7="C:/Users/GIRISH/OneDrive/Desktop/phone pe project/pulse/data/top/insurance/country/india/state"
aggre_path=os.listdir(path7)

col7={"states":[],"years":[],"quarter":[],"district_name":[],"Trans_count":[],"trans_amount":[]}


for states in aggre_path:
    cur_state=path7+"/"+states
    cur_state_1=os.listdir(cur_state)

    for year in cur_state_1:
        cur_year=cur_state+"/"+year
        cur_year_loc=os.listdir(cur_year)

        for files in cur_year_loc:
            cur_file=cur_year+"/"+files
            cur_loc=open(cur_file,"r")

            g=json.load(cur_loc)

            for i in g['data']['districts']:
                name=i['entityName']
                count=i['metric']['count']
                amount=i['metric']['amount']               
                col7["district_name"].append(name)
                col7["quarter"].append(int(files.strip(".json")))
                col7["states"].append(states)
                col7["trans_amount"].append(amount)
                col7["Trans_count"].append(count)
                col7["years"].append(year)

Top_insurance=pd.DataFrame(col7)

Top_insurance['states']=Top_insurance['states'].str.replace('andaman-&-nicobar-islands','Andaman & Nicobar')
Top_insurance['states']=Top_insurance['states'].str.replace("-"," ")
Top_insurance['states']=Top_insurance['states'] .str.title()                                                                       
Top_insurance['states']=Top_insurance['states'].str.replace('Dadra & Nagar Haveli & Daman & Diu','Daman & Diu')               
Top_insurance         

#Top_map
path8="C:/Users/GIRISH/OneDrive/Desktop/phone pe project/pulse/data/top/transaction/country/india/state"
agre_path=os.listdir(path8)

col8={"states":[],"years":[],"quarter":[],"district_name":[],"Trans_count":[],"trans_amount":[],"Pin_codes":[]}



for state in agre_path:
    cur_state=path8+"/"+state
    cur_loc=os.listdir(cur_state)

    for year in cur_loc:
        cur_year=cur_state+"/"+year
        cur_year_loc_=os.listdir(cur_year)

        for files in cur_year_loc_:
            cur_files=cur_year+"/"+files
            cur_loc_file=open(cur_files,"r")

            h=json.load(cur_loc_file)
            
            for i in h['data']['pincodes']:
                ent_name=i['entityName']
                count=i['metric']['count']
                amount=i['metric']['amount']

            for j in h['data']['districts']:
                district_name=j['entityName']

                col8["district_name"].append(district_name)
                col8["Pin_codes"].append(ent_name)
                col8["quarter"].append(int(files.strip(".json")))
                col8["states"].append(state)
                col8["trans_amount"].append(amount)
                col8["Trans_count"].append(count)
                col8["years"].append(year)

Top_map=pd.DataFrame(col8)
Top_map['states']=Top_map['states'].str.replace('andaman-&-nicobar-islands','Andaman & Nicobar')
Top_map['states']=Top_map['states'].str.replace("-"," ")
Top_map['states']=Top_map['states'] .str.title()                                                                       
Top_map['states']=Top_map['states'].str.replace('Dadra & Nagar Haveli & Daman & Diu','Daman & Diu')               
Top_map

#Top_user
import pandas as pd

path9="C:/Users/GIRISH/OneDrive/Desktop/phone pe project/pulse/data/top/user/country/india/state"
agre_path=os.listdir(path9)
col9={"states":[],"district_name":[],"years":[],"quarter":[],"registered_users":[]}
for state in agre_path:
    cur_state=path9+"/"+state
    cur_loc=os.listdir(cur_state)

    for year in cur_loc:
        cur_year=cur_state+"/"+year
        cur_year_loc_=os.listdir(cur_year)

        for files in cur_year_loc_:
            cur_files=cur_year+"/"+files
            cur_loc_file=open(cur_files,"r")

            i=json.load(cur_loc_file)

            for j in i['data']['districts']:
                reg_user=j['registeredUsers']
                district_name=j['name']
                col9["district_name"].append(district_name)
                col9["quarter"].append(int(files.strip(".json")))
                col9["states"].append(state)
                col9["registered_users"].append(reg_user)
                col9["years"].append(year)

Top_user=pd.DataFrame(col9)

Top_user['states']=Top_user['states'].str.replace('andaman-&-nicobar-islands','Andaman & Nicobar')
Top_user['states']=Top_user['states'].str.replace("-"," ")
Top_user['states']=Top_user['states'] .str.title()                                                                       
Top_user['states']=Top_user['states'].str.replace('Dadra & Nagar Haveli & Daman & Diu','Daman & Diu')               
Top_user



#SQL Connection DataFrame 1
import mysql.connector as sql
mydb=sql.connect(
    host='localhost',
    user='root',
    password='GirishGidda@2002',
    database='phone_pe_t_i',
    port="3306",
    auth_plugin='mysql_native_password'
)
cursor=mydb.cursor()
create_query_1='''CREATE TABLE if not exists aggregated_insurance(states varchar(255),
                                                    years int,
                                                    quarter int,
                                                    trans_type varchar(255),
                                                    trans_amont bigint,
                                                    trans_count bigint)'''
cursor.execute(create_query_1)
mydb.commit()
insert_query_1= '''insert into aggregated_insurance(states,years,quarter,trans_type,trans_amount,trans_count)
                                                    values(%s,%s,%s,%s,%s,%s)'''
val=aggregated_insurance.values.tolist()
cursor.executemany(insert_query_1,val)
mydb.commit()

                               
#data frame 2
create_query_2='''CREATE TABLE if not exists Aggregated_transaction(states varchar(255),
                                                                    years int,
                                                                    quarter int,
                                                                    trans_count bigint,
                                                                    trans_type varchar(255),
                                                                    trans_amount bigint)'''
                                                   
cursor.execute(create_query_2)
mydb.commit()
insert_query_2= '''insert into Aggregated_transaction(states,years,quarter,trans_count,trans_type,trans_amount)
                                                    values(%s,%s,%s,%s,%s,%s)'''
data=Aggregated_transaction.values.tolist()
cursor.executemany(insert_query_2,data)
mydb.commit()
                
#DataFrame 3
create_query_3='''CREATE TABLE if not exists Aggregated_user(states varchar(255),
                                                             years int,
                                                             quarter int,
                                                             trans_count bigint,
                                                             percentage float,
                                                             Brands varchar(255))'''
                                                   
cursor.execute(create_query_3)
mydb.commit()
insert_query_3= '''insert into Aggregated_user(states,years,quarter,trans_count,percentage,Brands)
                                                values(%s,%s,%s,%s,%s,%s)'''
data1=Aggregated_user.values.tolist()
cursor.executemany(insert_query_3,data1)
mydb.commit()
          

create_query_4='''CREATE TABLE if not exists Map_insurance(states varchar(255),
                                                            years int,
                                                            quarter int,
                                                            districts varchar(255),
                                                            trans_count bigint,
                                                            trans_amount bigint)'''
                                                   
cursor.execute(create_query_4)
mydb.commit()
insert_query_4= '''insert into Map_insurance(states,years,quarter,districts,trans_count,trans_amount)
                                                values(%s,%s,%s,%s,%s,%s)'''
data=Map_insurance.values.tolist()
cursor.executemany(insert_query_4,data)
mydb.commit()
                
create_query_5='''CREATE TABLE if not exists Map_map(states varchar(255),
                                                     years int,
                                                     quarter int,
                                                     districts varchar(255),
                                                     trans_count bigint,
                                                     trans_amount bigint)'''
                                                   
cursor.execute(create_query_5)
mydb.commit()
insert_query_5= '''insert into Map_map(states,years,quarter,districts,trans_count,trans_amount)
                                                values(%s,%s,%s,%s,%s,%s)'''
data3=Map_map.values.tolist()
cursor.executemany(insert_query_5,data3)
mydb.commit()

create_query_6='''CREATE TABLE if not exists map_user(states varchar(255),
                                                      years int,
                                                      quarter int,
                                                      district_name varchar(255),
                                                      reg_user bigint,
                                                      app_opens bigint)'''
                                                   
cursor.execute(create_query_6)
mydb.commit()
insert_query_6= '''insert into map_user(states,years,quarter,district_name,reg_user,app_opens)
                                                values(%s,%s,%s,%s,%s,%s)'''
data4=map_user.values.tolist()
cursor.executemany(insert_query_6,data4)
mydb.commit()

create_query_7='''CREATE TABLE if not exists Top_insurance(states varchar(255),
                                                            years int,
                                                            quarter int,
                                                            district_name varchar(255),
                                                            Trans_count bigint,
                                                            trans_amount bigint)'''
                                                   
cursor.execute(create_query_7)
mydb.commit()
insert_query_7= '''insert into Top_insurance(states,years,quarter,district_name,Trans_count,trans_amount)
                                                values(%s,%s,%s,%s,%s,%s)'''
data5=Top_insurance.values.tolist()
cursor.executemany(insert_query_7,data5)
mydb.commit()

create_query_8='''CREATE TABLE if not exists Top_map(states varchar(255),
                                                            years int,
                                                            quarter int,
                                                            district_name varchar(255),
                                                            Trans_count bigint,
                                                            trans_amount bigint,
                                                            Pin_codes bigint)'''
                                                   
cursor.execute(create_query_8)
mydb.commit()
insert_query_8= '''insert into Top_map(states,years,quarter,district_name,Trans_count,trans_amount,Pin_codes)
                                                values(%s,%s,%s,%s,%s,%s,%s)'''
data6=Top_map.values.tolist()
cursor.executemany(insert_query_8,data6)
mydb.commit()

create_query_9='''CREATE TABLE if not exists Top_user(states varchar(255),
                                                        district_name varchar(255),
                                                        years int,
                                                        quarter int,
                                                        registered_users bigint)'''
                                                   
cursor.execute(create_query_9)
mydb.commit()
insert_query_9= '''insert into Top_user(states,district_name,years,quarter,registered_users)
                                                values(%s,%s,%s,%s,%s)'''
data7=Top_user.values.tolist()
cursor.executemany(insert_query_9,data7)
mydb.commit()
