# # project 3 password strenght meter

# import re
# import streamlit as st 

# #page styling 
# st.set_page_config(page_title = "Password Strength Checker", page_icon= "🔑🌘", layout = "centered")

# # Custom css
# st.markdown("""
# <style>
#     .main {text-align: center;} 
#     .stTextInput {width: 60% !important; margin: auto; }
#     .stButton button {width: 50%; background-color #4caf50; color: white; font-size:18px;}
#     .stButton button:hover { background: #45a049;} 
# </Style> 
# """, unsafe_allow_html=True)

# #page title and descripton 
# st.title("🔏🔐Password Strength Generator")
# st.write("Enter your password below to check its security level. 🔎")

# #Function to check password strength
# def check_password_strength(Password) :
#     score= 0
#     feedback = []

#     if len(Password) >=8:
#         score +=1 #increased score by 1
#     else:
#         feedback.append("❌Password should be **atleast 8 character long**.")

#     if re.search(r"[A-Z]", Password) and re.search(r"[a-z]", Password): 
#         score += 1
#     else:
#         feedback.append("❌Password should include **both upper case (A-Z) and lower case (a-z) letters**.")    

#     if re.search(r"\d", Password): 
#         score += 1
#     else:
#         feedback.append("❌Password should include **atleast one number**.")     

#     # special character
#     if re.search(r"[!@#$%^&*]", Password):
#         score +=1
#     else:
#         feedback.append("❌ Include **at least one special character (!@#$%^&*)**.")


#         #display password strength results
#         if score ==4 :
#             st.success("✅ **Strong Password** Your password is secure.")
#         elif score ==3 :
#             st.info("⚠ ** Modeerat Password** -consider improving add security by adding more feature") 
#         else:
#             st.error("❌ **Week Passord ** - Follow the suggestion below to strength it. ") 

#          #feedback
#     if feedback:
#         with st.expander ("🔎**Improve Your Password**"):
#           for item in feedback:
#                 st.write(item)
# Password = st.text_input("Enter your Password ", type= "password", help= "Ensure your password is strong🔐")   
# #Button working
# if st.button("Check Strength"):
#  if Password:
#     check_password_strength(Password)
# else:
#     st.warning("⚠Please enter a password first!")   #show warning if password empty


import re
import streamlit as st 

# Page styling 
st.set_page_config(page_title="Password Strength Checker", page_icon="🔑🌘", layout="centered")


st.markdown("""
    <style>
        /* Background color for the entire app */
        [data-testid="stAppViewContainer"] {
            background-color: rgb(179, 201, 180); /* Light green background */
        }
        
        /* Centering elements */
        .main {text-align: center;} 

        /* Text input box styling */
        .stTextInput {
            width: 60% !important;
            margin: auto; 
        }

        /* Button styling */
        .stButton button {
            width: 50%; 
            background-color:rgb(60, 116, 62); 
            color: white; 
            font-size: 18px;
        }
        .stButton button:hover {
            background: #45a049;
        }
    </style>
""", unsafe_allow_html=True)

# Page title and description 
st.title("🔐 Password Strength Checker")
st.write("Enter your password below to check its security level. 🔎")

# Function to check password strength
def check_password_strength(Password):
    score = 0
    feedback = []

    if len(Password) >= 8:
        score += 1  # Increase score by 1
    else:
        feedback.append("❌ Password should be **at least 8 characters long**.")

    if re.search(r"[A-Z]", Password) and re.search(r"[a-z]", Password): 
        score += 1
    else:
        feedback.append("❌ Password should include **both uppercase (A-Z) and lowercase (a-z) letters**.")    

    if re.search(r"\d", Password): 
        score += 1
    else:
        feedback.append("❌ Password should include **at least one number**.")     

    # Special character
    if re.search(r"[!@#$%^&*]", Password):
        score += 1
    else:
        feedback.append("❌ Include **at least one special character (!@#$%^&*)**.")

    # Display password strength results (Fixing Indentation)
    if score == 4:
        st.success("✅ **Strong Password** - Your password is secure.")
    elif score == 3:
        st.info("⚠ **Moderate Password** - Consider improving security by adding more features.") 
    else:
        st.error("❌ **Weak Password** - Follow the suggestions below to strengthen it.") 

    # Feedback
    if feedback:
        with st.expander("🔎 **Improve Your Password**"):
            for item in feedback:
                st.write(item)

# Input Field
Password = st.text_input("Enter your Password", type="password", help="Ensure your password is strong 🔐")   

# Button Working
if st.button("Check Strength"):
    if Password:
        check_password_strength(Password)
    else:
        st.warning("⚠ Please enter a password first!")  # Show warning if password is empty

                     

