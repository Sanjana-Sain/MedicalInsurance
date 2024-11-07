
# In[12]:


import streamlit as st


# In[13]:


import pickle as pkl


# In[14]:


model = pkl.load(open('insurance_charges.p', 'rb'))


# In[17]:


st.title('MEDICAL INSURANCE COST PREDICTOR')


# In[19]:


age = st.number_input('Age', min_value=1, max_value=100)
sex = st.number_input('Sex (Male-0, Female-1)', min_value=0, max_value=1)
bmi = st.number_input('BMI', min_value=10, max_value=50)
children = st.number_input('Children', min_value=0, max_value=5)
smoker = st.number_input('Smoker (No-0, Yes-1)', min_value=0, max_value=1)
region_northeast = st.number_input('Region : Northeast', min_value=0, max_value=1)
region_northwest = st.number_input('Region : Northwest', min_value=0, max_value=1)
region_southeast = st.number_input('Region : Southeast', min_value=0, max_value=1)
region_southwest = st.number_input('Region : Southwest', min_value=0, max_value=1)
output=""
if st.button("Predict"):
    result = model.predict([[age, sex, bmi, children, smoker, region_northeast, region_northwest, region_southeast, region_southwest]])
    st.success('The output of the above is {}'.format(result))


# In[ ]:




