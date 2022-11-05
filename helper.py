import streamlit as st
from st_aggrid import AgGrid
from st_aggrid.shared import GridUpdateMode
from st_aggrid.grid_options_builder import GridOptionsBuilder

def show_dataset(df_type,df,grid_type='normal'):
    st.write(str(len(df)),'records found')

    gob = GridOptionsBuilder.from_dataframe(df)
    if grid_type=='selection':
        gob.configure_selection(selection_mode='single',use_checkbox=True)
    gridOptions=gob.build()
    data = AgGrid(
        df,
        gridOptions=gridOptions,
        enable_enterprise_modules=True,
        allow_unsafe_jscode=True,
        update_mode=GridUpdateMode.SELECTION_CHANGED
    )

    return data