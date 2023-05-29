import streamlit as st
from datetime import datetime

def main():
    st.title('앱 대시보드')

    menu = [' 메뉴1', '메뉴2', '메뉴3']
    choice = st.sidebar.selectbox('메뉴', menu)

    if choice == menu[0]:
        st.subheader('메뉴1')

    elif choice == menu[1]:
        st.subheader('메뉴2')

    elif choice == menu[2]:
        st.subheader('메뉴3')


if __name__ == '__main__':
    main()