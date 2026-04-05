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


from PIL import Image

#streamlit part
st.set_page_config(layout="wide")
st.title("Phone_PE data visualization")

with st.sidebar:
    select=option_menu("Main menu",["Home","Data","Top Charts"])

if select=="Home":
    col1, col2= st.columns(2)

    with col1:
        st.header("PHONEPE")
        st.subheader("INDIA'S BEST TRANSACTION APP")
        st.markdown("PhonePe is an Indian digital payments and financial technology company")
        st.write("FEATURES")
        st.write("Credit & Debit card linking")
        st.write("Bank Balance check")
        st.write("Money Storage")
        st.write("PIN Authorization")
        st.download_button("DOWNLOAD THE APP NOW","https://www.phonepe.com/app-download/")

    with col2:
        st.image(Image.open(r"C:\Users\GIRISH\Downloads\images.jpg"))
    
    
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


        
        

        
