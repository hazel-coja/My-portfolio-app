import streamlit as st

st.set_page_config(page_title="My Multipage App", page_icon= "🌐", layout="wide")

st.title("🌐 Welcome to My Multipage App")
st.subheader("A Simple Multipage Portfolio")

st.markdown(""" ### 👋 Hello! I am Hazel Ann F. Coja
             A student learning streamlit and building interactive web apps.
            

         ### 🚀 What this Web App Showcases""")
col1, col2, col3 = st.columns(3)
with col1:
        st.markdown(""" 
                <div style="background-color:#1f77b4;
                    padding:20px;
                    text-align:center;
                    color:white;">
                    <h3>👤 About Me</h3>
                    <p>Learn more about my background, skills, and goals.</p>
                </div>
                    """, unsafe_allow_html=True)
        
with col2:
         st.markdown("""
                <div style=" background-color:#2ca02c;
                     padding:20px;
                     border-radius:15px;
                     text-align:center;
                     color:white;">
                     <h3>💻 Projects</h3>
                     <p>Explore the projects I have created using Python and Streamlit.</p>
                </div>""", unsafe_allow_html=True)
         
with col3:
        st.markdown(""" 
                <div style="
                          background-color:#ff7f0e;
                          padding:20px;
                          border-radius:15px;
                          color:white;">
                          <h3>📞 Contact</h3>
                          <p>Find ways to connect with me through social media.</p>
                </div>""", unsafe_allow_html=True)
         

st.divider()

st.subheader("✨ Features")
col1, col2, col3 = st.columns(3)

with col1: 
    st.info("📄 About Me")

with col2:
    st.success("💻 Projects")

with col3:
    st.warning("📞 Contact")


