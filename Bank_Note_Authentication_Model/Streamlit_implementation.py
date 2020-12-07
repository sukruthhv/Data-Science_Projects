#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import pickle
import streamlit as st


# In[1]:


#!pip install streamlit


# In[5]:


pickle_file=open('Bank_Note_Auth_Model_class.pkl','rb')

classifier = pickle.load(pickle_file)

def predict_note(variance,skewness,curtosis,entropy):
    
    """ Let's authenticate the Bank Notes using this prediction Model
    
    ---
    parameters:
    - name: variance
      in: query
      type: number
      required: true
      
    - name: skewness
      in: query
      type: number
      required: true
      
    - name: curtosis
      in: query
      type: number
      required: true
      
    - name: entropy
      in: query
      type: number
      required: true
    
    responses:
        200:
            description: The output values
    """
    
    #variance = request.args.get('variance')
    #skewness = request.args.get('skewness')
    #curtosis = request.args.get('curtosis')
    #entropy = request.args.get('entropy')
    
    prediction=classifier.predict([[variance,skewness,curtosis,entropy]])
    #return "The predicted value is : " + str(prediction)
    return prediction

def main():
    st.title("Bank Note Authentication model")
    
    html_decorator = """
    <div style=background-color:blue; padding:10px">
    <h2 style="color:white;text-align:center;"> Streamlit Bank Authentication Model </h2>
    </div>
    """

    st.markdown(html_decorator,unsafe_allow_html=True)
    variance=st.text_input("Variance","Type Here")
    skewness=st.text_input("skewness","Type Here")
    curtosis=st.text_input("curtosis","Type Here")
    entropy=st.text_input("entropy","Type Here")
    
    result =""
    if st.button("Predict"):
        result=predict_note(variance,skewness,curtosis,entropy)
    
   # if result == 0 :
   #     st.success('The note is void!!!')
   # else:
   #     st.success('The note is VALID!!!')
    st.success('The output is {0}'.format(result))

    if st.button("About"):
        st.text("This is the Bank AUthentication Model!!!")
        
    
if __name__ == "__main__":
    main()


# ### Since the above implementation was in swagger, we can use the following url to open the swagger UI in browser : http://127.0.0.1:5000/apidocs/ 
# 

# In[3]:


#!pip install flasgger


# In[11]:


#!pip freeze > requirements.txt


# In[3]:


#get_ipython().system('streamlit run Streamlit_implementation.ipynb')


# In[ ]:




