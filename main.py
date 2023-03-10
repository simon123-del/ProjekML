import streamlit as st 
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split 

st.write("""
    ## Prediksi Peluang Penerimaan Program S2
""")

st.image('./image2.jpg')

st.write( """
    ### Keterangan Data Yang Digunakan
    1. GRE Score: Merupakan Score Test Untuk Masuk Program S2 (0 - 340) Bersifat Continous
    2. TOEFL Score: Score Kemampuan TOEFL (0 - 120) Bersifat Continous
    3. University Rating: Rating Universitas (0 - 5) Bersifat Ordinal
    4. Kekuatan Surat Rekomendasi (0 - 5) Bersifat Ordinal
    5. GPA Sewaktu Undergraduate (0 - 10) Bersifat Continous
    6. Pengalaman Riset (0 : tidak ada, 1 : ada) Bersifat Nominal
    
    7. Peluang Diterima (0 - 1) Merupakan Dependent Variable

""")

st.write("""
    ### Overview Data Sarjana
""")

myData = pd.read_csv('data.csv')

st.dataframe(myData)

st.write("""
    ### Deskripsi Data
""")

st.dataframe(myData.describe())

# Preproccessing Data

st.write("""
    ### Dilakukan Preprocessing Data dimana Fitur dan Labelnya akan Dipisah
""")

# Memisahkan Label Dan Fitur 
X = myData.iloc[:, 1:-1].values
y = myData.iloc[:, -1].values



st.write("### Input Data X",X)
st.write("### Label Data y",y)


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=69)



from sklearn.preprocessing import StandardScaler 

ss_train_test = StandardScaler()


X_train_ss_scaled = ss_train_test.fit_transform(X_train)
X_test_ss_scaled = ss_train_test.transform(X_test)

from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

l_regressor_ss = LinearRegression()
l_regressor_ss.fit(X_train_ss_scaled, y_train)
y_pred_l_reg_ss = l_regressor_ss.predict(X_test_ss_scaled)

st.write("Dengan Menggunakan Multiple Linear Regression Diperoleh Skor Untuk Data Test")
st.write(r2_score(y_test, y_pred_l_reg_ss))


st.write("# Silakan Masukkan Skor Test Anda")


form = st.form(key='my-form')
inputGRE = form.number_input("Masukan GRE Score: ", 0)
inputTOEFL = form.number_input("Masukan TOEFL Score: ", 0)
inputUnivRating = form.number_input("Masukan Rating Univ: ", 0)
inputSOP = form.number_input("Masukan Kekuatan SOP: ", 0)
inputLOR = form.number_input("Masukan Kekuatan LOR: ", 0)
inputCGPA = form.number_input("Masukan CGPA: ", 0)
inputResearch = form.number_input("Pengalaman Researc, 1 Jika Pernah Riset, 0 Jika Tidak", 0)
submit = form.form_submit_button('Submit')

completeData = np.array([inputGRE, inputTOEFL, inputUnivRating, 
                        inputSOP, inputLOR, inputCGPA, inputResearch]).reshape(1, -1)
scaledData = ss_train_test.transform(completeData)


st.write('Tekan Submit Untuk Melihat Prediksi Peluang S2 Anda')

if submit:
    prediction = l_regressor_ss.predict(scaledData)
    if prediction > 1 :
        result = 1
    elif prediction < 0 :
        result = 0
    else :
        result = prediction[0]
    st.write(result*100, "Percent")


st.write("")
st.write("# ABOUT US")
st.write("Website Ini Untuk Memenuhi Project Matakuliah Machine Learning")
st.write( """
    ### Anggota Kelompok
    1. Lady Gabriella - 2055301065
    2. Adinda Nola - 2055301001
    3. Daffa Naufal - 2055301027

""")



