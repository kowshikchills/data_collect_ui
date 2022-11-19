import pandas as pd
import numpy as np
import streamlit as st
import re
from streamlit_option_menu import option_menu
from os.path import exists

with st.sidebar:
    selected_menu = option_menu(
        menu_title="UPSC Tagging",  
        options=["Home", "file"],  
        icons=["house", "envelope"],  
        menu_icon="cast", 
        default_index=0,  
    )
path_file = 'data/state_file.csv'

if selected_menu == 'Home':
    st.header('UPSC Sentence Tagging Tool')
    from os.path import exists
    
    df_data = pd.read_pickle('data/data_tagging.pkl')
    if not exists(path_file):
        df = pd.DataFrame()
        df['TrainId'] = []
        df['Label'] = []
        df.to_csv(path_file, index=None)

    df = pd.read_csv(path_file)
    if len(df) == 0:
        i = 0
    else:
        i = len(df)

    if len(df) > 2:
        col1, col2, col3 = st.columns(3)
        CLS = col1.button('Correct Last Sentence')
        if CLS:
            df_ = df[:-1]
            df_.to_csv(path_file, index=None)
            st.experimental_rerun()

    heading = df_data['headings'].values[i]
    tags = df_data['tags'][i]
    tags_ = [x for x in tags if re.match("^[A-Za-z_-]*$", x)]
    tags_str = ', '.join(tags_)
    st.write('Sentence',)
    st.success(heading, icon = '📄')
    st.warning(tags_str, icon='🎙')

    labels = ['Environment','History','Culture','Geography','International Relations/Issues',
    'Polity','Governance','Health','Society','Economy','Science&Technology','Defence','Agriculture']

    st.subheader('Select Relevant Topic',)
    col1,_, col2, = st.columns(3)
    Environment = col1.button('Environment')
    History = col2.button('History')
    col1,_, col2, = st.columns(3)
    Culture = col1.button('Culture')
    Geography = col2.button('Geography')
    col1,_, col2, = st.columns([0.4,0.1,0.25])
    Ir = col1.button('International Relations/Issues')
    Governance = col2.button('Governance')
    col1,_, col2, = st.columns(3)
    Health = col1.button('Health')
    Society = col2.button('Society')
    col1,_, col2, = st.columns(3)
    Economy = col1.button('Economy')
    polity = col2.button('polity')
    col1,_, col2, = st.columns(3)
    ST = col1.button('Science&Technology')
    Defence = col2.button('Defence')
    col1,_, col2, = st.columns(3)
    Agriculture = col1.button('Agriculture')
    noa = col2.button('None')

    col1, col2, col3, col4, col5  = st.columns(5)
    skip = col3.button('skip')
    

    label = None
    if Environment:
        label = 'Environment'
    elif History:
        label = 'History'
    elif Culture:
        label = 'Culture'
    elif Geography:
        label = 'Geography'
    elif Ir:
        label = 'International Relations/Issues'
    elif Governance:
        label = 'Governance'
    elif Health:
        label = 'Health'
    elif Society:
        label = 'Society'
    elif Economy:
        label = 'Economy'
    elif ST:
        label = 'Science&Technology'
    elif Defence:
        label = 'Defence'
    elif Agriculture:
        label = 'Agriculture'
    elif polity:
        label = 'Polity'
    elif skip:
        label = 'skip'
    elif noa:
        label = 'None_of_above'

    if label != None:
        df_add = pd.DataFrame([[i, label]], columns=['TrainId','Label'])
        df = pd.concat([df,df_add])
        df.to_csv(path_file, index=None)
        st.experimental_rerun()

if selected_menu == 'file':
    if exists(path_file):
        df = pd.read_csv(path_file)
        df
        def convert_df(df):
            return df.to_csv().encode('utf-8')

        csv = convert_df(df)

        st.download_button(
            label="Download data as CSV",
            data=csv,
            file_name='labels.csv',
            mime='text/csv',
)


