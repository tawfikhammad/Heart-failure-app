import joblib
import pandas as pd
import streamlit as st

model = joblib.load('rf.sav')

st.cache_data.clear()

st.set_page_config(page_title="Heart Failure Prediction",page_icon='🚨')

st.title(':red[Heart] Failure Prediction 🫀🏥')
st.image("heart_beating_0.gif",use_container_width =True)

sex_list_selection = ['Male','Female']
ChestPainType_list_selection = ['TA: Typical Angina','ATA: Atypical Angina','NAP: Non-Anginal Pain','ASY: Asymptomatic']
FastingBS_list_selection = ['Yes','No']
RestingECG_list_selection = ['Normal','ST','LVH']
ExerciseAngina_list_selection = ['Yes','No']
ST_Slope_list_selection = ['Up', 'Flat', 'Down']

with st.container(height=1400):
    col1 , col2 = st.columns(2)

    with col1:
        st.write("### Enter Your Age⏳")
        age = st.slider("Select Age:",0,100,35)

        st.write("### Select Your Gender ⚤")
        sex = st.radio("Select:",sex_list_selection)
        
        st.write("### Select Your Chest Pain Type")
        ChestPainType = st.radio("Select:",ChestPainType_list_selection)

        st.write("### Select Your Fasting Blood Sugar")
        st.caption("Yes: if FastingBS > 120 mg/dl")
        FastingBS = st.selectbox("Select:",FastingBS_list_selection,key=1)

        st.write("### Select Your Resting Electrocardiogram Results")
        st.caption("ST: having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV)")
        st.caption("LVH: showing probable or definite left ventricular hypertrophy by Estes criteria")
        RestingECG = st.radio("Select:",RestingECG_list_selection)

        st.write("### Enter Your Cholesterol")
        Cholesterol = st.slider("Select:",40,400,120)

    with col2:
         st.write("### Resting Blood Pressure🩸")
         RestingBP = st.slider("Select [mm Hg]:",40,400,120)

         st.write("### Oldpeak (ST Depression Induced by Exercise)🏃‍♂️")
         Oldpeak = st.slider("Select:",0,10,0)
         
         st.write("### Maximum Heart Rate Achieved⏱️")
         MaxHR = st.slider("Select [bpm]:",50,250,120)

         st.write("### Select Exercise Induced Angina")
         ExerciseAngina = st.selectbox("Select:",ExerciseAngina_list_selection)

         st.write("### Select Slope of the Peak Exercise ST segment")
         st.caption("Up is UpSloping")
         st.caption("Down is DownSloping")
         ST_Slope = st.selectbox("Select:",ST_Slope_list_selection)

st.divider()
st.title("Start Prediction")

b = st.button("Start")


sex_to_encode = ['Male','Female']
encode_sex = [1,0]
convert_sex = dict(zip(sex_to_encode, encode_sex))

ChestPainType_to_encode = ['TA: Typical Angina','ATA: Atypical Angina','NAP: Non-Anginal Pain','ASY: Asymptomatic']
encode_ChestPainType = [3,1,2,0]
convert_ChestPainType = dict(zip(ChestPainType_to_encode, encode_ChestPainType))

FastingBS_to_encode = ['Yes','No']
encode_FastingBS = [1,0]
convert_FastingBS = dict(zip(FastingBS_to_encode, encode_FastingBS))

RestingECG_to_encode = ['Normal','ST','LVH']
encode_RestingECG = [1,2,0]
convert_RestingECG = dict(zip(RestingECG_to_encode, encode_RestingECG))

ExerciseAngina_to_encode = ['Yes','No']
encode_ExerciseAngina = [1,0]
convert_ExerciseAngina = dict(zip(ExerciseAngina_to_encode,encode_ExerciseAngina))


ST_Slope_to_encode = ['Up', 'Flat', 'Down']
encode_ST_Slope = [2, 1, 0]
convert_ST_Slope = dict(zip(ST_Slope_to_encode,encode_ST_Slope))

											
try:
 df = pd.DataFrame({
          'Age':[age],
          'Sex':convert_sex[sex],
          'ChestPainType':convert_ChestPainType[ChestPainType],
          'RestingBP':[RestingBP],
          'Cholesterol':[Cholesterol],
          'FastingBS':convert_FastingBS[FastingBS],
          'RestingECG':convert_RestingECG[RestingECG],
          'MaxHR':[MaxHR],
          'ExerciseAngina':convert_ExerciseAngina[ExerciseAngina],
          'Oldpeak':[Oldpeak],
          'ST_Slope':convert_ST_Slope[ST_Slope]},index=[0])
except ValueError:
    st.error("Please ensure all numerical fields are correctly filled! ❌")

print(df)


def predict_heart_failure(df):
    prediction = model.predict(df)
    prediction_prob = model.predict_proba(df)  
    return prediction, prediction_prob
prediction,prediction_prob = predict_heart_failure(df)

no_patient = str((prediction_prob[0,0])*100)[:5] + '%'
patient = str((prediction_prob[0,1])*100)[:5] + '%'

if b:
 with st.sidebar:
    st.markdown(
    """
    <div style="text-align: center;">
        <h1>🚀 Prediction Is</h1>
    </div>
    """,
    unsafe_allow_html=True
    )
    with st.sidebar.container(height=400):
       co1 , co2 = st.columns(2)
       with co1:
          st.image('https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExbWU2eXR0aHo0bHd3NmFtbDRiZzZwOW80c21iazJ3bXdpY2tpbDZxaiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/1Bd7DmRvbhV5UPkoDw/giphy.gif'
                 ,use_container_width =True)
          st.write(f"# Prediction Probability: {patient}")
          st.subheader(":red[*Heart Patient*]")

       with co2:
            st.image('https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExd3d5aHB3eW1leDgxMG5wNG4zM3hhZXhpbm5mYWJtOWkzNWpoamZsMCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/yeUxljCJjH1rW/giphy.gif'
                     ,use_container_width =True)
            st.write(f"# Prediction Probability: {no_patient}")
            st.subheader(":green[*No Heart Patient*]")

          
             
    if prediction == 1:  
        st.markdown(
                      """
                 <div style="text-align: center;">
                 <h1>Expected He Is</h1>
                 </div>
                      """,
        unsafe_allow_html=True)
        st.markdown(
                          """
                <div style="text-align: center;">
                <h1 style="color: red;">Heart Patient</h1>
                </div>
                """,
                 unsafe_allow_html=True)
    else:
         st.markdown(
                      """
                 <div style="text-align: center;">
                 <h1>Expected He Is</h1>
                 </div>
                      """,
        unsafe_allow_html=True)
         st.markdown(
                          """
                <div style="text-align: center;">
                <h1 style="color: green;">Not Heart Patient</h1>
                </div>
                """,
                 unsafe_allow_html=True)
