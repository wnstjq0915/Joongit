import streamlit as st
from datetime import datetime

menu = [' 메뉴1', '메뉴2', '메뉴3']

def menus():
    choice = st.sidebar.selectbox('메뉴', menu)

    if choice == menu[0]:
        st.subheader('메뉴1')

    elif choice == menu[1]:
        st.subheader('메뉴2')

    elif choice == menu[2]:
        st.subheader('메뉴3')
        user_input = st.text_input('문자를 입력해주세요.')
        if user_input == 'hello':
            return 'hi'
    
    elif len(menu) >= 4 and choice == menu[3]:
        st.subheader('메뉴4')


def main():
    st.title('앱 대시보드')

    if menus() == 'hi':
        menus() # 두번째 셀렉트박스가 열릴 때 키 값이 달라서 에러.
    

if __name__ == '__main__':
    main()