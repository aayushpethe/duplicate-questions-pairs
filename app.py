import streamlit as st
import helper
import pickle

model = pickle.load(open('model.pkl','rb'))

st.header('Duplicate Question Pairs')

q1 = st.text_input('Enter question 1')
q2 = st.text_input('Enter question 2')

if st.button('Find'):
    query = helper.query_point_creator(q1,q2)
    result = model.predict(query)[0]

    st.write("Prediction:", result)
    st.write("Feature shape:", query.shape)
    st.write("Feature shape:", query.shape)

    if result:
        st.header('Duplicate')
    else:
        st.header('Not Duplicate')

#run in app.py terminal:-
#python -m pip install streamlit
#python -m streamlit run app.py

# if error of bs4 then:- python -m pip install beautifulsoup4
# if error of distance then:- python -m pip install distance
# if error of fuzzywuzzy then:- python -m pip install fuzzywuzzy
# if error of sklearn then:- python -m pip install scikit-learn
# if error of sklearn then:- python -m pip install nlkt -> python -m streamlit run app.py



# then go to heroku