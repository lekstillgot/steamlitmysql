import pymysql
import streamlit as st
import connectmysql as conn
st.title('MySQL Person CRUD App')

# create connection
# อ่านข้อมูลฟังก์ชั่นจาก database
connection = conn.connectdb()
cursor = connection.cursor()


def read_persons():
    cursor.execute("Select * from person")
    persons = cursor.fetchall()
    return persons

# function เพิ่มข้อมูล


def create_person(fullname, email, age):
    try:
        cursor.execute(
            "insert into person (fullname, email, age) values (%s,%s,%s)", (fullname, email, age))
        connection.commit()
        st.success('เพิ่มข้อมูลเรียบร้อยแล้ว')
        # st.experimental_set_query_params(menu='Read')
        st.markdown("Click [here](?Menu=Read) to view the list of persons. ")
        st.markdown("""
                    <a href ="?Menu=Read" target="_self">Click here</a> to view the list of persons
                    """, unsafe_allow_html=True)

    except pymysql.Error:
        connection.rollback()
        st.error(f'Error created person :{pymysql.Error}')


def update_person(id, fullname, email, age):
    try:
        cursor.execute(
            "update  person set fullname=%s, email=%s, age=%s", (
                fullname, email, age)
        )

        connection.commit()
        st.success('เพิ่มข้อมูลเรียบร้อยแล้ว')
        # st.experimental_set_query_params(menu='Read')
        st.markdown("Click [here](?Menu=Read) to view the list of persons. ")
        st.markdown("""
                    <a href ="?Menu=Read" target="_self">Click here</a> to view the list of persons
                    """, unsafe_allow_html=True)

    except pymysql.Error:
        connection.rollback()
        st.error(f'Error created person :{pymysql.Error}')


# main menu
menu = st.sidebar.radio("Menu", ["Read", "Create", "Update", "Delete"])

# menu read
if menu == "Read":
    st.subheader("Read Persons")
    persons = read_persons()
    # check persons is not empty
    if persons:
        # create table data show data persons
        table_data = [["ID", "Fullname", "Email", "age", "Edit"]]
        for person in persons:
            edit_link = f"[Edit person{'id'}]"
            delete_link = f"[Delete person{'id'}]"
            edit_button = st.button(f"Edit{person}{'id'}")
            row = [person['id'], person['fullname'],
                   person['email'], person['age'], 'edit_button']
            table_data.append(row)
        st.table(table_data)
    else:
        st.info('ไม่พบข้อมูล')


# Menu Create
elif menu == "Create":
    st.subheader("Create Persons")
    fullname = st.text_input("fullname")
    email = st.text_input("email")
    age = st.number_input("Age", 0, 100, 0)

    # button create
    if st.button("Create"):
        if fullname and email and age:
            create_person(fullname, email, age)
        else:
            st.warning("กรุณาป้อนข้อมูลให้ครบ")

elif menu == "Update":
    st.subheader("Update Persons")
    id = st.number_input("ID,min_value=1")
    fullname = st.text_input("fullname")
    email = st.text_input("email")
    age = st.number_input("Age", min_value=1, max_value=100)

    # button create
    if st.button("Update"):
        update_person(fullname, email, age)


def delete_person(id):
    try:
        cursor.execute(
            "delete  person where id=%s", (id))

        connection.commit()
        st.success('ลบข้อมูลเรียบร้อยแล้ว')
        # st.experimental_set_query_params(menu='Read')
        st.markdown("Click [here](?Menu=Read) to view the list of persons. ")
        st.markdown("""
                    <a href ="?Menu=Read" target="_self">Click here</a> to view the list of persons
                    """, unsafe_allow_html=True)

    except pymysql.Error:
        connection.rollback()
        st.error(f'Error created person :{pymysql.Error}')
