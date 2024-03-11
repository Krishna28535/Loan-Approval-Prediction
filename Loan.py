import streamlit as st
st.title('Loan Approval Prediction')
st.header('Enter Your Details')

gender=st.selectbox('Gender',('','Male','Female'))
if gender=='Male':
    gender=1
elif gender=='Female':
    gender=0

married=st.selectbox('Married or Not',('','Yes','No'))
if married=='Yes':
    married=1
elif married=='No':
    married=0

graduate=st.selectbox('Graduate or Not',('','Yes','No'))
if graduate=='Yes':
    graduate=0
elif graduate=='No':
    graduate=1


employed=st.selectbox('Self Employed or Not',('','Yes','No'))
if employed=='Yes':
    employed=1
elif employed=='No':
    employed=0


applicant_income=st.text_input('Write Applicant Income')


coapplicant_income=st.text_input('Write Coapplicant Income')


loanamount=st.text_input('Write Loan Amount')



loan_amount_term=365

area=st.selectbox('Property location',('','Rural','Urban','Semi Urban'))
if area=='Rural':
    area=0
elif area=='Urban':
    area=2
elif area=='Semi Urban':
    area=1


depend=st.selectbox('Number of family members depends on you ',('',0,1,2,'More than 2'))
if depend=='More than 2':
    depend=3

credit_history=st.selectbox('Credit History',('','Yes','No'))
if credit_history=='Yes':
    credit_history=1
elif credit_history=='No':
    credit_history=0


import pickle
load_model=pickle.load(open('LoanApprovalPrediction.sav', 'rb'))


if st.button('Check'):
    a=load_model.predict([[gender,married,graduate,employed,applicant_income,coapplicant_income,loanamount,loan_amount_term,area,depend,credit_history]])
    if a==0:
        st.header('Hat Gareeb Sala!')
    else:
        st.write('Ameer Baap Ki Aulaad')