import streamlit as st
from openai import OpenAI 
from datetime import datetime,date
import base64
import time
import API




veri=st.session_state
def main():
 
  if "step" not in veri:
       veri.step=0
  if veri.step==0:
     st.title("Welcome to our page")
     st.subheader("Form ")
     min=date(1900,1,1)
     max=date.today()
     liste=[]
     with st.form(key="simple_form"):
      ask=st.text_input("Please enter your name")
      ask4=st.selectbox("select your gender", ["Male","Female", "Other"])
      ask2=st.date_input("Enter your born",max_value=max, min_value=min)
      button=st.form_submit_button("Submit")
      liste.append({"Name":ask, "Gender":ask4, "Born":ask2, })
      if button and ask:
          veri.step=1
          veri.name=ask
          veri.date=ask2
          veri.gender=ask4
          time.sleep(1)
          st.rerun()
     
  elif veri.step==1:
       st.title("Healtcare AI")
       st.subheader("This Aı mission is to give best advice for your request" \
                   "\n All the rights belongs to Efe Karakaş")
       s=st.chat_input("Whats your ilness and how is your situtation present")
       if s:
        agent = OpenAI(api_key=API.apı())
        response1=agent.images.generate(model="gpt-image-2.5-flare", prompt=f"can you make a image about the users response which is {s} and not show what they write just make good picture",)
        bs64type=response1.data[0].b64_json
        image=base64.b64decode(bs64type)
        response=agent.responses.create(model="gpt-6-astra",input=s)
       
        veri.image=image
        veri.chat=response.output_text
       if "chat" in veri:
         st.image(veri.image)
         time.sleep(0.5)
         st.write("Advice:",veri.chat)
         a=st.feedback("stars")
         if a is not None:
          st.markdown(f"Thanks for your response {veri.name}")
          veri.step=2
          st.rerun()
          
  elif veri.step==2:
    prompt="This website aims to detect best solution for users with **OpenAI**(gpt-6-astra)**\nAlso if you wanted to feedback about the website you can write below\n Or you can call +90(531) 661 24 16"
    st.write(prompt)
    with st.form(key="feedback_form"):
       feedback=st.text_area("Feedback")
       button=st.form_submit_button("Submit")
       if button and feedback:
           st.success("Filled")
           st.write("Thanks for your response")
           time.sleep(2)
           veri.step=3
           st.rerun()
  elif veri.step==3:
    st.title("Let's play game")
    st.subheader("Guess your birthdate")
    agent2=OpenAI(api_key=API.apı())
    ask5=st.chat_input("write your favorite number between 1-100 and tell your favorite animal ")
    if ask5:
     response2=agent2.responses.create(model="gpt-6-astra", input=f"users information: {ask5} and user name is {veri.name} and guess their birthdate (day/month/year)")
     veri.guess=response2.output_text
    if "guess" in veri:
      st.write(veri.guess)
      b=st.radio("İs it correct?",["Yes", "No"], index=None)
      if b=="Yes":
        st.success("True Claim")
        st.write("Wonderful")
      elif b=="No":
        st.error("False Claim")
        st.write("Maybe next time")

if True :
   main()
