import streamlit as st
from PIL import Image
import shutil

# initialize icon
img = Image.open('data/icon.png')
st.set_page_config(
    page_title="FLD Labeling Tool",
    page_icon=img,
    layout="wide",
    initial_sidebar_state="expanded"
)

# turn off some deprecation messages
st.set_option('deprecation.showfileUploaderEncoding', False)
st.set_option('deprecation.showPyplotGlobalUse', False)

# markdown css code to customize the web layout
with open("style.css") as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# initialization
if 'user' not in st.session_state:
    st.session_state.user = 'Anonymous'

if 'user_login' not in st.session_state:
    st.session_state.user_login=False

# side bar
st.sidebar.subheader('Welcome '+st.session_state.user)

if 'active_page' not in st.session_state:
    st.session_state['active_page'] = 'Ingestion'
    try:
        shutil.rmtree("temp")
    except:
        pass

with st.sidebar as sidebar:
    cols_icons=st.columns([3,5])
    st.session_state.active_page='Help' if cols_icons[0].button('💡 Help',key='help_button') \
                                        else st.session_state.active_page
    st.session_state.active_page='Contact' if cols_icons[1].button('📞 Contact Us',key='contact_button') \
                                        else st.session_state.active_page
    with sidebar.expander('New Tab'):
        st.session_state.active_page='Ingestion' if st.button('🕹 Ingestion',key='ingestion_button') \
                                        else st.session_state.active_page
        st.session_state.active_page='Optimizing' if st.button('🎯 Optimizing', key='optimizing_page') \
                                        else st.session_state.active_page
# cols=st.sidebar.columns(2)
# cols[1].image("data/icon.png",width=100)
# hide_img_fs='''
# '''
# st.markdown(hide_img_fs, unsafe_allow_html=True)

# authentication

# main
if __name__=="__main__":
    if st.session_state.user_login==False:
        st.title("Welcome to web app.")
        st.header("Please insert your email:")
        cols= st.columns([2,5])
        st.session_state.user=cols[0].text_input("Email:")
        cols[1].text('         ')
        cols[1].header('@novelis.com')
        user_login=st.button("OK")
        if user_login:
            st.session_state.user_login=True
            st.session_state.user=st.session_state.user.split('@',1)[0]
            st.experimental_rerun()
    else:
        if st.session_state.active_page=='Help':
            st.write('in help page')
        elif st.session_state.active_page=='Contact':
            st.write('in contact page')
        elif st.session_state.active_page=='Ingestion':
            st.write('in ingestion page')
        elif st.session_state.active_page == 'Optimizing':
            st.write('in Optimizing page')
        else:
            st.info('🛠 Under construction!')