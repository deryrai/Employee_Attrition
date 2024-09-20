import streamlit as st
import pandas as pd
import numpy as np
import pickle

## load model
with open('best_pipeline_model.pkl', 'rb') as file1:
    best_model = pickle.load(file1)

def run():
  with st.form('form_employee'):
      #Employee
      Employee_id = st.number_input('Employee ID',value=0)
      #age
      age = st.number_input('Age',value=19, min_value= 19)
      #gender
      gender = st.selectbox('Gender',('Male','Female'))
      #Years at company
      years = st.number_input('Years at Company', value = 0)
      #Job Role
      job_role = st.selectbox('Job Role',('Technology','Healthcare','Education','Media','Finance'))
      #income
      Monthly_income =st.number_input('Monthly Income',value=0)
      #work life
      Work_Life_Balance = st.selectbox('Work-Life Balance',('Poor', 'Good', 'Fair', 'Excellent'))
      #job satisfaction
      job_satifasction = st.selectbox('Job Satisfaction',('Low', 'Medium', 'High', 'Very High'))
      #Performance Rating
      Performance_Rating = st.selectbox('Performance Rating',('Low', 'Below Average', 'Average', 'High'))
      #promosi
      Number_of_Promotions = st.number_input('Number_of_Promotions',value=0)
      #overtime
      overtime = st.selectbox('Overtime',('Yes','No'))
      #jarak
      distance = st.number_input('Distance from Home',value=0)
      #education level
      pendidikan = st.selectbox('Education Level',('High School', 'Associate Degree', 'Bachelor’s Degree', 'Master’s Degree', 'PhD'))
      #status pernikahan
      marital_status = st.selectbox('Marital Status',('Single','Marriage'))
      #tanggungan
      dependents = st.number_input('Number of Dependents',value=0)
      #job level
      job_level = st.selectbox('Job Level',('Entry', 'Mid', 'Senior'))
      #company size
      company_size = st.selectbox('Company Size',('Small','Medium','Large'))
      #company tenure
      company_ten = st.number_input('Company Tenure',value= 0)
      #remote
      remote_work = st.selectbox('Remote Work',('Yes','No'))
      #Leadership
      leadership_opp = st.selectbox('Leadership Opportunities',('Yes','No'))
      #innovation
      Innovation_Opp = st.selectbox('Innovation Opportunities',('Yes','No'))
      #company rep
      company_rep = st.selectbox('Company Reputation',('Poor', 'Good', 'Fair','Excellent'))
      #employee
      employee_rec = st.selectbox('Employee Recognition',( 'Low','Medium', 'High', 'Very High'))
      #attrition
      Attrition = st.number_input('Attrition',value=0 , min_value=0, max_value=1)

      #submit predict
      submitted = st.form_submit_button('Predict')


  data_inf={
          'Employee ID' :Employee_id,
          'Age' :age,
          'Gender' :gender,
          'Years at Company':years,
          'Job Role' :job_role,
          'Monthly Income' :Monthly_income,
          'Work-Life Balance' :Work_Life_Balance,
          'Job Satisfaction' :job_satifasction,
          'Performance Rating' :Performance_Rating,
          'Number of Promotions' :Number_of_Promotions,
          'Overtime' : overtime,
          'Distance from Home' :distance,
          'Education Level' : pendidikan,
          'Marital Status'  : marital_status,
          'Number of Dependents' :dependents,
          'Job Level' :job_level,
          'Company Size' :company_size,
          'Company Tenure' : company_ten,
          'Remote Work' : remote_work,
          'Leadership Opportunities': leadership_opp,
          'Innovation Opportunities' :Innovation_Opp,
          'Company Reputation' :company_rep,
          'Employee Recognition' :employee_rec,
          'Attrition' :Attrition
  }


  # Konversi dictionary menjadi DataFrame
  df_data = pd.DataFrame([data_inf])
  st.dataframe(df_data)
  if submitted :
      # Jalankan model untuk prediksi
      y_pred = best_model.predict(df_data)
      y_pred_labels = ['stayed' if y == 0 else 'left' for y in y_pred]
      st.write('## Attrition:',str(str(y_pred_labels)))

__name__ == '__main__'
run()