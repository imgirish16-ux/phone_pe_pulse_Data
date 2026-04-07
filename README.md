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

#####streamlit Part ###
import streamlit as st
from streamlit_option_menu import option_menu
import mysql.connector as sql
import pandas as pd
import plotly.express as px
import requests
import json

#sql connection
mydb=sql.connect(
    user="root",
    host="localhost",
    password="GirishGidda@2002",
    database="phone_pe_t_i",
    auth_plugin='mysql_native_password')


cursor=mydb.cursor()
#agre_insurance

cursor.execute("SELECT * FROM aggregated_insurance")
#data frames
import pandas as pd
table1=cursor.fetchall()

Aggregated_Insurance=pd.DataFrame(table1, columns=("States","Years","Quarter","trans_type","trans_amount","trans_count"))

#aggregated transc
cursor.execute("SELECT * FROM aggregated_transaction")

import pandas as pd
table2=cursor.fetchall()

Aggregated_Transaction=pd.DataFrame(table2, columns=("States","Years","Quarter","trans_count","trans_name","trans_amount"))

#Aggregated_User
cursor.execute("SELECT * FROM aggregated_user")

import pandas as pd
table3=cursor.fetchall()

Aggregated_User=pd.DataFrame(table3, columns=("States","Years","Quarter","trans_count","percentage","Brands"))


#Map_Insurance
cursor.execute("SELECT * FROM map_insurance")

import pandas as pd
table4=cursor.fetchall()

Map_Insurance=pd.DataFrame(table4, columns=("States","Years","Quarter","districts","trans_count","trans_amount"))


#Map_User
cursor.execute("SELECT * FROM map_user")

import pandas as pd
table5=cursor.fetchall()

Map_User=pd.DataFrame(table5, columns=("States","Years","Quarter","districts","reg_user","app_opens"))

#top insurance
cursor.execute("SELECT * FROM top_insurance")
table6 = cursor.fetchall()

Top_Insurance = pd.DataFrame(
    table6,
    columns=("States","Years","Quarter","district_name","trans_count","trans_amount")
)


#Top_Map
cursor.execute("SELECT * FROM top_map")

import pandas as pd
table7=cursor.fetchall()

Top_Map=pd.DataFrame(table7, columns=("States","Years","Quarter","district_name","trans_count","trans_amount","Pin_codes"))

#Top_User
cursor.execute("SELECT * FROM top_user")


import pandas as pd
table5=cursor.fetchall()

Top_User=pd.DataFrame(table5, columns=("States","district_name","Years","Quarter","reg_user"))


def Transaction_amount_count_Y(df,year):    
   tacy=df[df["Years"]==year]
   tacy.reset_index(drop=True,inplace=True)
   tacyg=tacy.groupby("States")[["trans_count","trans_amount"]].sum()
   tacyg.reset_index(inplace=True)
   x=tacyg['States']
   y=tacyg['trans_amount']

   col1,col2=st.columns(2)
   with col1:
        
        fig_amount=px.bar(tacyg,x,y,title=f"{year} Transaction amount",height=750,width=950)
        st.plotly_chart(fig_amount)
        x=tacyg["States"]
        y=tacyg["trans_count"]
   with col2:
        
        fig_count=px.bar(tacyg,x,y,title=f"{year} Transaction count",height=750,width=950)
        st.plotly_chart(fig_count)


   col1,col2=st.columns(2)
   with col1:
            
        url="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"
        response=requests.get(url)
        data1=json.loads(response.content)
        states_name=[]
        for feature in data1["features"]:    
            states_name.append(feature["properties"]["ST_NM"])
            states_name.sort()
        fig_india_1=px.choropleth(tacyg, geojson=data1,locations="States",featureidkey="properties.ST_NM",
                                                color="trans_amount",
                                                color_continuous_scale="Rainbow",
                                                range_color=(tacyg["trans_amount"].min(),tacyg["trans_amount"].max()),
                                                hover_name="States",title=f"{year}Transaction amount",fitbounds="locations",
                                                height=750,width=950)
        fig_india_1.update_geos(visible=False)
        st.plotly_chart(fig_india_1)
   with col2:
        fig_india_2=px.choropleth(tacyg, geojson=data1,locations="States",featureidkey="properties.ST_NM",
                                                color="trans_count",
                                                color_continuous_scale="Rainbow",
                                                range_color=(tacyg["trans_count"].min(),tacyg["trans_count"].max()),
                                                hover_name="States",title=f"{year}Transaction count",fitbounds="locations",
                                                height=750,width=950)
        fig_india_2.update_geos(visible=False)
        st.plotly_chart(fig_india_2)

   return tacy




def Transaction_amount_count_Y_Q(df,quarter):

    tacy=df[df['Quarter']==quarter]
    tacy.reset_index(drop=True,inplace=True)
    tacyg=tacy.groupby("States")[["trans_count","trans_amount"]].sum().reset_index()
    tacyg.reset_index(inplace=True)
    x=tacyg['States']
    y=tacyg['trans_amount']

    col1,col2=st.columns(2)
    with col1:
        fig_amount=px.bar(tacyg,x,y,title=f"{tacy["Years"].unique()} Year {quarter} Quarter Transaction amount",height=650,width=600)
        st.plotly_chart(fig_amount)
        x=tacyg["States"]
        y=tacyg["trans_count"]

    with col2:
        fig_count=px.bar(tacyg,x,y,title=f"{tacy["Years"].unique()} Year {quarter} Quarter Transaction count",height=650,width=600)
        st.plotly_chart(fig_count)

    col1,col2=st.columns(2)
    with col1:
        url="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"

        response=requests.get(url)
        data1=json.loads(response.content)
        states_name=[]
        for feature in data1["features"]:
            states_name.append(feature["properties"]["ST_NM"])

        states_name.sort()

        fig_india_1=px.choropleth(tacyg, geojson=data1,locations="States",featureidkey="properties.ST_NM",
                                            color="trans_amount",
                                            color_continuous_scale="Rainbow",
                                            range_color=(tacyg["trans_amount"].min(),tacyg["trans_amount"].max()),
                                            hover_name="States",title=f"{tacy["Years"].unique()} Year {quarter} Quarter Transaction amount",fitbounds="locations",
                                            height=600,width=600)
        fig_india_1.update_geos(visible=False)
        st.plotly_chart(fig_india_1)

    with col2:
        fig_india_2=px.choropleth(tacyg, geojson=data1,locations="States",featureidkey="properties.ST_NM",
                                            color="trans_count",
                                            color_continuous_scale="Rainbow",
                                            range_color=(tacyg["trans_count"].min(),tacyg["trans_count"].max()),
                                            hover_name="States",title=f"{tacy["Years"].unique()} Year {quarter} Quarter Transaction amount",fitbounds="locations",
                                            height=600,width=600)
        fig_india_2.update_geos(visible=False)
        st.plotly_chart(fig_india_2)
        return tacy


def Agrre_Tran_type(df,state):

    tacy=df[df['States']==state]
    tacy.reset_index(drop=True,inplace=True)
    tacyg=tacy.groupby("trans_name")[["trans_count","trans_amount"]].sum()
    tacyg.reset_index(inplace=True)
    col1,col2=st.columns(2)
    with col1:
        fig_pie_1=px.pie(data_frame=tacyg,names="trans_name",values='trans_amount',
                        width=600,title=f"{state.upper()} TRANSACTION AMOUNT",hole=0.5)
        st.plotly_chart(fig_pie_1)

    with col2:
        fig_pie_2=px.pie(data_frame=tacyg,names="trans_name",values='trans_count',
                        width=600,title=f"{state.upper()} TRANSACTION COUNT",hole=0.5)
        st.plotly_chart(fig_pie_2)

#agregated_user
def Aggre_user_plot_1(df,year):
    aguy=df[df["Years"]==year]
    aguy.reset_index(drop=True,inplace=True)

    aguyg=pd.DataFrame(aguy.groupby("Brands")['trans_count'].sum())
    aguyg.reset_index(inplace=True)

    fig_bar_1=px.bar(aguyg,x="Brands" , y="trans_count",title=f"{year} BRANDS AND TRANS COUNT",
                    width=1000,color_discrete_sequence=px.colors.sequential.haline,hover_name="Brands")
    st.plotly_chart(fig_bar_1)
    return aguy

#aggre_user_analysis
def Aggre_user_plot_2(df,quarter):
    aguyq=df[df["Quarter"]==quarter]
    aguyq.reset_index(drop=True,inplace=True)
    aguyqg=pd.DataFrame(aguyq.groupby("Brands")["trans_count"].sum())
    aguyqg.reset_index(inplace=True)
    fig_bar_1=px.bar(aguyqg,x="Brands" , y="trans_count",title=f"{quarter} BRANDS AND TRANS COUNT",
                        width=1000,color_discrete_sequence=px.colors.sequential.haline,hover_name="Brands")
    st.plotly_chart(fig_bar_1)

    return aguyq

#Aggre analysis
#Aggre analysis
def aggre_user_plot_3(df,state):
    auyqs=df[df["States"]==state]
    auyqs.reset_index(drop=True,inplace=True)

    auyqs=auyqs.sort_values(by="trans_count",ascending=False)

    fig_line_1=px.line(auyqs,x="Brands",y="trans_count",hover_data="percentage",
                    title="Brand ,trans_count,percentage",width=1000,markers=True)
    st.plotly_chart(fig_line_1)


def map_insur_district_name(df, state):

    # filter correctly
    tacy = df[df['States'] == state].copy()
    tacy.reset_index(drop=True, inplace=True)

    # group by correct column name: districts
    tacyg = (
        tacy.groupby("districts")[["trans_count", "trans_amount"]]
        .sum()
        .reset_index()
    )

    # Transaction Count bar
    fig_bar_1 = px.bar(
        tacyg,
        x='trans_count',
        y='districts',
        orientation="h",
        title=f"{state} District and Transaction Count",
        color_discrete_sequence=px.colors.sequential.Reds_r
    )
    st.plotly_chart(fig_bar_1)

    # Transaction Amount bar
    fig_bar_2 = px.bar(
        tacyg,
        x='trans_amount',
        y='districts',
        orientation="h",
        title=f"{state} District and Transaction Amount",
        color_discrete_sequence=px.colors.sequential.Reds_r
    )
    st.plotly_chart(fig_bar_2)

def map_user_plot_1(df,year):
    muy=df[df['Years']==year]
    muy.reset_index(drop=True,inplace=True)
    muyg=muy.groupby("States")["reg_user",].sum()
    muyg.reset_index(inplace=True)
    fig_line_1=px.line(muyg,x="States",y=["reg_user"],
                    title=f"{year} REGSTRED USER App opens",width=1000,height=800,markers=True)
    st.plotly_chart(fig_line_1)
    return muy

#mapuser plot_2
def map_user_plot_2(df,quarter):
    muyq=df[df['Quarter']==quarter]
    muyq.reset_index(drop=True,inplace=True)
    muyqg=muyq.groupby("States")[["reg_user","app_opens"]].sum()
    muyqg.reset_index(inplace=True)
    fig_line_1=px.line(muyqg,x="States",y=["reg_user","app_opens"],
                    title=f"{quarter} REGSTRED USER App opens",width=1000,height=800,markers=True)
    st.plotly_chart(fig_line_1)

    return muyq

def map_user_plot_3(df,state):
    muyqs=df[df["States"]==state]
    muyqs.reset_index(drop=True,inplace=True)

    muyg = muyqs.groupby("districts",as_index=False)[["reg_user","app_opens"]].sum()
    muyg.reset_index(inplace=True)

    fig_user_bar_1=px.bar(muyg,x="reg_user",y="districts",orientation="h",
                        title="Registered user",height=800,
                        color_discrete_sequence=px.colors.sequential.Rainbow)
    st.plotly_chart(fig_user_bar_1)

    fig_user_bar_2=px.bar(muyg,x="app_opens",y="districts",orientation="h",
                        title="App opens",height=800,
                        color_discrete_sequence=px.colors.sequential.Reds_r)
    st.plotly_chart(fig_user_bar_2)


#top insurance
def top_insurance_district_plot(df, state):

    tacy = df[df["States"] == state].copy()
    tacy.reset_index(drop=True, inplace=True)

    tacyg = (
        tacy.groupby("district_name")[["trans_count", "trans_amount"]]
        .sum()
        .reset_index()
        .sort_values(by="trans_amount", ascending=False)
    )

    col1, col2 = st.columns(2)

    with col1:
        fig1 = px.bar(
            tacyg,
            x="trans_amount",
            y="district_name",
            orientation="h",
            title=f"{state} Top Insurance District - Amount",
            color_discrete_sequence=px.colors.sequential.Blues_r
        )
        st.plotly_chart(fig1)

    with col2:
        fig2 = px.bar(
            tacyg,
            x="trans_count",
            y="district_name",
            orientation="h",
            title=f"{state} Top Insurance District - Count",
            color_discrete_sequence=px.colors.sequential.Greens_r
        )
        st.plotly_chart(fig2)

#top transaction analysis

def top_transaction_district_plot(df, state):

    tacy = df[df["States"] == state].copy()
    tacy.reset_index(drop=True, inplace=True)

    tacyg = (
        tacy.groupby("district_name")[["trans_count", "trans_amount"]]
        .sum()
        .reset_index()
        .sort_values(by="trans_amount", ascending=False)
    )

    col1, col2 = st.columns(2)

    with col1:
        fig1 = px.bar(
            tacyg,
            x="trans_amount",
            y="district_name",
            orientation="h",
            title=f"{state} Top Transaction District - Amount",
            color_discrete_sequence=px.colors.sequential.Purples_r
        )
        st.plotly_chart(fig1)

    with col2:
        fig2 = px.bar(
            tacyg,
            x="trans_count",
            y="district_name",
            orientation="h",
            title=f"{state} Top Transaction District - Count",
            color_discrete_sequence=px.colors.sequential.Oranges_r
        )
        st.plotly_chart(fig2)

# top_user analysis

def top_user_district_plot(df, state):

    tacy = df[df["States"] == state].copy()
    tacy.reset_index(drop=True, inplace=True)

    tacyg = (
        tacy.groupby("district_name")["reg_user"]
        .sum()
        .reset_index()
        .sort_values(by="reg_user", ascending=False)
    )

    col1, col2 = st.columns(2)

    with col1:
        fig1 = px.bar(
            tacyg,
            x="reg_user",
            y="district_name",
            orientation="h",
            title=f"{state} Top User District - Registered Users",
            color_discrete_sequence=px.colors.sequential.Blues_r
        )
        st.plotly_chart(fig1)


#sql
def top_chart_transaction(table_name):
    import mysql.connector as sql
    mydb=sql.connect(
        user="root",
        host="localhost",
        password="GirishGidda@2002",
        database="phone_pe_t_i",
        auth_plugin='mysql_native_password')

    cursor=mydb.cursor()

    query_1=f'''select states,sum(trans_amount) as transaction_amount
                        from {table_name} group by states
                        order by transaction_amount desc
                        limit 10;'''

    cursor.execute(query_1)
    table_1=cursor.fetchall()
    mydb.commit()

    #plot_1
    df_1=pd.DataFrame(table_1,columns=("states","transaction_amount"))
    col1, col2 = st.columns(2)
    with col1:
        fig_amount=px.bar(df_1,x="states",y="transaction_amount",title=f"top 10 high Transction amount",
                        color_discrete_sequence=px.colors.sequential.Aggrnyl,height=650,width=650,hover_name="states",)
        st.plotly_chart(fig_amount)


    query_2=f'''select states,sum(trans_amount) as transaction_amount
                        from {table_name} group by states
                        order by transaction_amount asc
                        limit 10;'''

    cursor.execute(query_2)
    table_2=cursor.fetchall()
    mydb.commit()

    #plot_2
    df_2=pd.DataFrame(table_2,columns=("states","transaction_amount"))
    col1, col2 = st.columns(2)
    with col2:

        fig_amount=px.bar(df_2,x="states",y="transaction_amount",title=f"top 10 low Transction amount",
                        color_discrete_sequence=px.colors.sequential.Aggrnyl,height=650,width=650,hover_name="states",)
        st.plotly_chart(fig_amount)


    #plot_3

    query_3=f'''select states,avg(trans_amount) as transaction_amount
                from {table_name} group by states
                order by transaction_amount;'''
    cursor.execute(query_3)
    table_3=cursor.fetchall()
    mydb.commit()

    df_3=pd.DataFrame(table_3,columns=("states","transaction_amount"))

    fig_amount=px.bar(df_3,y="states",x="transaction_amount",title="avg Transction amount",orientation="h",
                    color_discrete_sequence=px.colors.sequential.Aggrnyl,height=650,width=650,hover_name="states")
    st.plotly_chart(fig_amount)


#trans_count
def top_chart_transaction_count(table_name):
    import mysql.connector as sql
    mydb=sql.connect(
        user="root",
        host="localhost",
        password="GirishGidda@2002",
        database="phone_pe_t_i",
        auth_plugin='mysql_native_password')

    cursor=mydb.cursor()

    query_1=f'''select states,sum(trans_count) as transaction_count
                        from {table_name} group by states
                        order by transaction_count desc
                        limit 10;'''

    cursor.execute(query_1)
    table_1=cursor.fetchall()
    mydb.commit()

    #plot_1
    df_1=pd.DataFrame(table_1,columns=("states","transaction_count"))
    col1, col2 = st.columns(2)
    with col1:

        fig_amount=px.bar(df_1,x="states",y="transaction_count",title="top 10 high Transction count",
                        color_discrete_sequence=px.colors.sequential.Aggrnyl,height=650,width=650,hover_name="states",)
        st.plotly_chart(fig_amount)


    query_2=f'''select states,sum(trans_count) as transaction_count
                        from {table_name} group by states
                        order by transaction_count asc
                        limit 10;'''

    cursor.execute(query_2)
    table_2=cursor.fetchall()
    mydb.commit()

    #plot_2
    df_2=pd.DataFrame(table_2,columns=("states","transaction_count"))
    col1, col2 = st.columns(2)
    with col2:

        fig_amount=px.bar(df_2,x="states",y="transaction_count",title="top 10 low Transction count",
                        color_discrete_sequence=px.colors.sequential.Aggrnyl,height=650,width=650,hover_name="states",)
        st.plotly_chart(fig_amount)


    #plot_3

    query_3=f'''select states,avg(trans_count) as transaction_count
                from {table_name} group by states
                order by transaction_count;'''
    cursor.execute(query_3)
    table_3=cursor.fetchall()
    mydb.commit()

    df_3=pd.DataFrame(table_3,columns=("states","transaction_count"))

    fig_amount=px.bar(df_3,y="states",x="transaction_count",title="avg Transction count",orientation="h",
                    color_discrete_sequence=px.colors.sequential.Aggrnyl,height=650,width=650,hover_name="states")
    st.plotly_chart(fig_amount)


def quarter_trans_amt(table_name):
    import mysql.connector as sql
    mydb=sql.connect(
        user="root",
        host="localhost",
        password="GirishGidda@2002",
        database="phone_pe_t_i",
        auth_plugin='mysql_native_password')

    cursor=mydb.cursor()

    query_4=f'''select years,quarter,sum(trans_amount) as transaction_amount
                from {table_name}
                group by years,quarter
                order by years,quarter;'''
    cursor.execute(query_4)
    table_4=cursor.fetchall()
    mydb.commit()

    table_4=pd.DataFrame(table_4,columns=("years","quarter","transaction_amount"))
    fig = px.line(table_4,
                x="years",
                y="transaction_amount",
                color="quarter",
                markers=True,
                title="Quarterly Transaction Trend")

    st.plotly_chart(fig)

def agg_pie(table_name):
    import mysql.connector as sql
    mydb=sql.connect(
        user="root",
        host="localhost",
        password="GirishGidda@2002",
        database="phone_pe_t_i",
        auth_plugin='mysql_native_password')

    cursor=mydb.cursor()
    query_5=f'''SELECT trans_type,
            SUM(trans_count) AS transaction_count,
            SUM(trans_amount) AS transaction_amount
    FROM {table_name}
    GROUP BY trans_type
    ORDER BY transaction_amount DESC;'''
    cursor.execute(query_5)
    table_5=cursor.fetchall()
    mydb.commit()
    table_5=pd.DataFrame(table_5,columns=("trans_type","transaction_count","transaction_amount"))

    fig_amount=px.pie(table_5,names="trans_type",values="transaction_amount",hole=0.5,title="Transaction Types Share")

    st.plotly_chart(fig_amount)

def pincodes(table_name):
    query_6=f'''select states,Pin_codes,sum(trans_amount) as transaction_amount
                from {table_name}
                group by Pin_codes,states
                order by transaction_amount desc
                limit 10;'''
    cursor.execute(query_6)
    table_6=cursor.fetchall()
    mydb.commit()
    table_6=pd.DataFrame(table_6,columns=("states","Pin_codes","transaction_amount"))
    fig_amount=px.bar(table_6,x="Pin_codes",y="states",title="Top 10 pincodes",orientation="h",
                                    color_discrete_sequence=px.colors.sequential.Aggrnyl,height=650,width=650,color="transaction_amount")

    st.plotly_chart(fig_amount)




def performance_user(table_name):
    query_7='''select states,district_name,
                sum(reg_user) as reg_user,
                sum(app_opens) as app_opens
            from map_user
            group by states,district_name
            order by reg_user desc
            limit 20;'''
    cursor.execute(query_7)
    table_7=cursor.fetchall()
    mydb.commit()

    table_7=pd.DataFrame(table_7,columns=("states","district_name","reg_user","app_opens"))
    fig_amount_1=px.bar(table_7,x="states",y="district_name",title="Top 10 user ",orientation="h",hover_name="reg_user",
                                    color_discrete_sequence=px.colors.sequential.Aggrnyl,height=650,width=650,color="app_opens")

    st.plotly_chart(fig_amount_1)

    query_8='''select states,district_name,
                sum(reg_user) as reg_user,
                sum(app_opens) as app_opens
            from map_user
            group by states,district_name
            order by reg_user asc
            limit 20;'''
    cursor.execute(query_8)
    table_8=cursor.fetchall()
    mydb.commit()

    table_8=pd.DataFrame(table_8,columns=("states","district_name","reg_user","app_opens"))
    fig_amount_2=px.bar(table_8,x="states",y="district_name",title="low performing user",orientation="h",hover_name="reg_user",
                                    color_discrete_sequence=px.colors.sequential.Aggrnyl,height=650,width=650,color="app_opens")

    st.plotly_chart(fig_amount_2)
    
import plotly.express as px
import json, requests

def phonepe_3d_map(df):

    st.subheader("PhonePe Pulse 3D karnataka Map")

    # Geojson
    url = "https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"
    geojson = json.loads(requests.get(url).content)

    # Aggregate
    data = df.groupby("States")[["trans_amount"]].sum().reset_index()

    fig = px.choropleth_mapbox(
        data,
        geojson=geojson,
        locations="States",
        featureidkey="properties.ST_NM",
        color="trans_amount",
        color_continuous_scale="Turbo",
        mapbox_style="carto-darkmatter",   # dark style like Pulse
        zoom=3.8,
        center={"lat": 22.5, "lon": 80},
        opacity=0.85,
        height=800
    )

    # 🔥 This creates 3D effect
    fig.update_layout(
        mapbox=dict(
            pitch=55,      # tilt
            bearing=-20    # angle
        ),
        margin={"r":0,"t":40,"l":0,"b":0}
    )

    st.plotly_chart(fig, use_container_width=True)


from PIL import Image

#streamlit part
st.set_page_config(layout="wide")
st.title("Phone_PE data visualization")

with st.sidebar:
    select=option_menu("Main menu",["Home","Data","Top Charts"])

if select=="Home":
    if select == "Home":

        st.title("📊 PhonePe Pulse Data Visualization Dashboard")

        phonepe_3d_map(Aggregated_Transaction)

        st.markdown("""
        This dashboard recreates the PhonePe Pulse experience using real transaction data.
        Explore state-wise performance using the interactive India heatmap below.
        """)


    
    
elif select=="Data":

    tab1,tab2,tab3=st.tabs(["Aggregated Analysis","Map Analysis","Top Analysis"])

    with tab1:
        method=st.radio("select the method",["Insurance Analysis","Transaction Analysis","User Analysis"])
    
        if method=="Insurance Analysis":
            col1,col2=st.columns(2)
            with col1:

                years=st.slider("select the Year",Aggregated_Insurance["Years"].min(),Aggregated_Insurance["Years"].max(),Aggregated_Insurance["Years"].min())
            tac_YS=Transaction_amount_count_Y(Aggregated_Insurance,years)


            col1,col2=st.columns(2)
            with col1:

                quarters=st.slider("select the Year",tac_YS["Quarter"].min(),Aggregated_Insurance["Quarter"].max(),tac_YS["Quarter"].min())

            Transaction_amount_count_Y_Q(tac_YS,quarters)

        elif method=="Transaction Analysis" :
            col1,col2=st.columns(2)
            with col1:

                years=st.slider("select the Year",Aggregated_Transaction["Years"].min(),Aggregated_Transaction["Years"].max(),Aggregated_Transaction["Years"].min())
            Aggre_trans_tac_YS=Transaction_amount_count_Y(Aggregated_Transaction,years)

            col1,col2=st.columns(2)
            with col1:
                states=st.selectbox("select the states",Aggre_trans_tac_YS['States'].unique())

            Agrre_Tran_type(Aggre_trans_tac_YS,states)

            col1,col2=st.columns(2)
            with col1:

                quarters=st.slider("select the quarter",Aggre_trans_tac_YS["Quarter"].min(),Aggre_trans_tac_YS["Quarter"].max(),Aggre_trans_tac_YS["Quarter"].min())

            Aggre_tran_tac_Y_Q=Transaction_amount_count_Y_Q(Aggre_trans_tac_YS,quarters)

            col1,col2=st.columns(2)
            with col1:
                states=st.selectbox("select the states_TY",Aggre_tran_tac_Y_Q['States'].unique())

            Agrre_Tran_type(Aggre_tran_tac_Y_Q,states)


        elif method=="User Analysis":
            col1,col2=st.columns(2)
            with col1:

                years=st.slider("select the Year",Aggregated_User["Years"].min(),Aggregated_User["Years"].max(),Aggregated_User["Years"].min())
            aggre_user_Y=Aggre_user_plot_1(Aggregated_User,years)

            col1,col2=st.columns(2)
            with col1:

                quarters=st.slider("select the quarter",aggre_user_Y["Quarter"].min(),aggre_user_Y["Quarter"].max(),aggre_user_Y["Quarter"].min())

            aggre_user_Y_Q=Aggre_user_plot_2(aggre_user_Y,quarters)

            col1,col2=st.columns(2)
            with col1:
                states=st.selectbox("select the states",aggre_user_Y_Q['States'].unique())

                aggre_user_plot_3(aggre_user_Y_Q,states)


    
    with tab2 :
        method2=st.radio("select the method",["Map Insurance Analysis","Map Transaction Analysis","Map User Analysis"])

        if method2=="Map Insurance Analysis" :
            col1,col2=st.columns(2)
            with col1:
                years = st.slider("select the Year_insur",Map_Insurance["Years"].min(),Map_Insurance["Years"].max(),Map_Insurance["Years"].min())
            map_inusurance_YS = Map_Insurance[Map_Insurance["Years"] == years]
            col1,col2=st.columns(2)
            with col1:
                states = st.selectbox("select the states__mi",map_inusurance_YS['States'].unique())

            map_insur_district_name(map_inusurance_YS, states)

            col1,col2=st.columns(2)
            with col1:

                quarters=st.slider("select the quarter",map_inusurance_YS["Quarter"].min(),map_inusurance_YS["Quarter"].max(),map_inusurance_YS["Quarter"].min())

            map_inusurance_Y_Q=Transaction_amount_count_Y_Q(map_inusurance_YS,quarters)

            col1,col2=st.columns(2)
            with col1:
                states=st.selectbox("select the states_TY",map_inusurance_Y_Q['States'].unique())

            map_insur_district_name(map_inusurance_Y_Q,states)

            
            

        elif method2=="Map Transaction Analysis":

            col1,col2=st.columns(2)
            with col1:
                years = st.slider(
                    "Select the Year",
                    Map_Insurance["Years"].min(),
                    Map_Insurance["Years"].max(),
                    Map_Insurance["Years"].min()
                )

            map_transaction_YS = Map_Insurance[Map_Insurance["Years"] == years]

            col1,col2=st.columns(2)
            with col1:
                states = st.selectbox("Select State", map_transaction_YS['States'].unique())

            map_insur_district_name(map_transaction_YS, states)

            col1,col2=st.columns(2)
            with col1:
                quarters = st.slider(
                    "Select Quarter",
                    map_transaction_YS["Quarter"].min(),
                    map_transaction_YS["Quarter"].max(),
                    map_transaction_YS["Quarter"].min()
                )

            map_transaction_Y_Q = map_transaction_YS[map_transaction_YS["Quarter"] == quarters]

            col1,col2=st.columns(2)
            with col1:
                states = st.selectbox("Select State (Quarter)", map_transaction_Y_Q['States'].unique())

            map_insur_district_name(map_transaction_Y_Q, states)

            
        elif method2=="Map User Analysis":

            col1,col2=st.columns(2)
            with col1:
                years = st.slider(
                    "Select the Year",
                    Map_User["Years"].min(),
                    Map_User["Years"].max(),
                    Map_User["Years"].min()
                )

            map_user_YS = Map_User[Map_User["Years"] == years]

            col1,col2=st.columns(2)
            with col1:
                quarters = st.slider(
                    "Select Quarter",
                    map_user_YS["Quarter"].min(),
                    map_user_YS["Quarter"].max(),
                    map_user_YS["Quarter"].min()
                )

            map_user_Y_Q = map_user_YS[map_user_YS["Quarter"] == quarters]

            col1,col2=st.columns(2)
            with col1:
                states = st.selectbox("Select State", map_user_Y_Q['States'].unique())

            map_user_plot_3(map_user_Y_Q, states)

    with tab3:
        method3=st.radio("select the method",["Top Insurance Analysis","Top Transaction Analysis","Top User Analysis"])

        if method3=="Top Insurance Analysis":
            col1,col2=st.columns(2)
            with col1:
                
                cursor.execute("""
                SELECT States, district_name, Years, Quarter, 
                    trans_count ,
                    trans_amount 
                FROM Map_Insurance
                """)

                map_insura_tac = pd.DataFrame(cursor.fetchall(), columns=cursor.column_names)

                # create year filtered dataframe
                map_insura_tac_Y = Transaction_amount_count_Y(map_insura_tac, years)
                min_year = int(map_insura_tac_Y["Years"].min())
                max_year = int(map_insura_tac_Y["Years"].max())

                if min_year == max_year:
                    years = st.selectbox(
                        "Select the Year_mi",
                        [min_year],
                        key="map_insur_year"
                    )
                else:
                    years = st.slider(
                        "Select the Year",
                        min_year,
                        max_year,
                        min_year,
                        key="map_insur_year"
                    )

            map_insura_tac_Y = map_insura_tac_Y[map_insura_tac_Y["Years"] == years]

            top_year_df = Top_Insurance[Top_Insurance["Years"] == years]

            col1, col2 = st.columns(2)
            with col1:
                states = st.selectbox(
                    "Select State",
                    top_year_df["States"].unique()
                )

            top_insurance_district_plot(top_year_df, states)

            col1, col2 = st.columns(2)
            with col1:
                quarters = st.slider(
                    "Select Quarter_ti",
                    top_year_df["Quarter"].min(),
                    top_year_df["Quarter"].max(),
                    top_year_df["Quarter"].min()
                )

            top_quarter_df = top_year_df[top_year_df["Quarter"] == quarters]

            col1, col2 = st.columns(2)
            with col1:
                states_q = st.selectbox(
                    "Select State (Quarter)",
                    top_quarter_df["States"].unique()
                )

            top_insurance_district_plot(top_quarter_df, states_q)

            
        elif method3=="Top Transaction Analysis":
            col1, col2 = st.columns(2)
            with col1:
                years = st.slider(
                    "Select Year",
                    Top_Map["Years"].min(),
                    Top_Map["Years"].max(),
                    Top_Map["Years"].min()
                )

            top_year_df = Top_Map[Top_Map["Years"] == years]

            col1, col2 = st.columns(2)
            with col1:
                states = st.selectbox(
                    "Select State",
                    top_year_df["States"].unique()
                )

            top_transaction_district_plot(top_year_df, states)

            col1, col2 = st.columns(2)
            with col1:
                quarters = st.slider(
                    "Select Quarter",
                    top_year_df["Quarter"].min(),
                    top_year_df["Quarter"].max(),
                    top_year_df["Quarter"].min()
                )

            top_quarter_df = top_year_df[top_year_df["Quarter"] == quarters]

            col1, col2 = st.columns(2)
            with col1:
                states_q = st.selectbox(
                    "Select State (Quarter)",
                    top_quarter_df["States"].unique()
                )

            top_transaction_district_plot(top_quarter_df, states_q)
        elif method3=="Top User Analysis":
            col1, col2 = st.columns(2)
            with col1:
                years = st.slider(
                    "Select Year",
                    Top_User["Years"].min(),
                    Top_User["Years"].max(),
                    Top_User["Years"].min()
                )

            top_year_df = Top_User[Top_User["Years"] == years]

            col1, col2 = st.columns(2)
            with col1:
                states = st.selectbox(
                    "Select State_yu",
                    top_year_df["States"].unique()
                )

            top_user_district_plot(top_year_df, states)

            col1, col2 = st.columns(2)
            with col1:
                quarters = st.slider(
                    "Select Quarter_qua",
                    top_year_df["Quarter"].min(),
                    top_year_df["Quarter"].max(),
                    top_year_df["Quarter"].min()
                )

            top_quarter_df = top_year_df[top_year_df["Quarter"] == quarters]

            col1, col2 = st.columns(2)
            with col1:
                states_q = st.selectbox(
                    "Select State (Quarter)",
                    top_quarter_df["States"].unique()
                )

            top_user_district_plot(top_quarter_df, states_q)

elif select=="Top Charts":
    question=st.selectbox("select the question",["1. Decoding Transaction Dynamics on PhonePe Scenario",

                                                    "2. Transaction Analysis Across States and Districts Scenario",

                                                    "3. User Registration Analysis",

                                                    "4. User Engagement and Growth Strategy",

                                                    "5. Transaction Analysis for Market Expansion",


                                                ])
    if question== "1. Decoding Transaction Dynamics on PhonePe Scenario":
        st.subheader ("transaction amount & count")
        top_chart_transaction("aggregated_insurance")
        top_chart_transaction_count("aggregated_insurance")
        quarter_trans_amt("aggregated_insurance")
        agg_pie("aggregated_transaction")
    
    if question== "2. Transaction Analysis Across States and Districts Scenario":
        st.subheader ("transaction amount & count")
        top_chart_transaction("aggregated_insurance")
        top_chart_transaction_count("aggregated_insurance")
        pincodes("top_map")

    if question=="3. User Registration Analysis":
        performance_user("map_user")

    if question=="4. User Engagement and Growth Strategy":
        agg_pie("aggregated_transaction")
        quarter_trans_amt("aggregated_insurance")

    if question=="5. Transaction Analysis for Market Expansion":
        top_chart_transaction("aggregated_insurance")


        
        

        

