import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Ramokgopa Kgotso | Data Analyst",
    page_icon="📊",
    layout="wide"
)

# Simple, clean CSS
st.markdown("""
<style>
    .contact-badge {
        display: inline-flex;
        align-items: center;
        background: white;
        padding: 10px 15px;
        border-radius: 8px;
        margin: 5px 10px 5px 0;
        border: 1px solid #e0e0e0;
        transition: 0.2s;
    }
    .contact-badge:hover {
        border-color: #4285F4;
        box-shadow: 0 2px 8px rgba(66, 133, 244, 0.1);
    }
    .icon {
        margin-right: 8px;
        font-size: 18px;
    }
</style>
""", unsafe_allow_html=True)

# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
    # Your original image
    st.image("./assets/github_pic.jpg", width=230)

with col2:
    st.title("Ramokgopa Kgotso", anchor=False)
    st.markdown("**📊 Aspiring Data Analyst**")
    st.write(
        "I help businesses make smarter decisions by uncovering insights hidden in their data."
    )
    


# --- EXPERIENCE & QUALIFICATIONS ---
st.write("\n")
st.subheader("💼 Experience & Qualifications", anchor=False)
st.write(
    """
    - 2 Years experience extracting actionable insights from data
    - Strong hands-on experience and knowledge in Python and Excel
    - Good understanding of statistical principles and their respective applications
    - Excellent team-player and displaying a strong sense of initiative on tasks
    """
)

# --- SKILLS ---
st.write("\n")
st.subheader("🛠️ Hard Skills", anchor=False)
st.write(
    """
    - Programming: Java, Python (Scikit-learn, Pandas), SQL, VBA
    - Data Visualization: PowerBi, MS Excel, Plotly
    - Modeling: Logistic regression, linear regression, decision trees
    - Databases: Postgres, MongoDB, MySQL
    
    
    """
)

# --- PERSONAL TOUCH ---
st.divider()
st.subheader("👋 About me")
st.write("""
When I'm not analyzing data, you can find me hiking, reading sci-fi novels, 
or trying out new coffee brewing methods. I believe good data tells a story, 
and I enjoy being the one to help tell it.
""")

# --- SIMPLE CONTACT SECTION ---
st.divider()
st.subheader("📬 Let's connect")

st.write("""
I'm always open to chatting about data, potential collaborations, or just connecting with fellow analysts.
""")

# Simple contact form
with st.form("simple_contact"):
    col1, col2 = st.columns(2)
    with col1:
        your_name = st.text_input("Your name")
    with col2:
        your_email = st.text_input("Your email")
    
    your_message = st.text_area("What's on your mind?", height=120)
    
    submitted = st.form_submit_button("Send message")
    
    if submitted:
        if your_name and your_email and your_message:
            st.success(f"Thanks {your_name}! I'll get back to you soon.")
        else:
            st.info("Please fill in all fields")

# --- ALTERNATIVE WAYS TO REACH OUT ---
st.write("**Or reach out directly:**")

# Simple contact methods
methods = [
    {"icon": "📧", "label": "Email", "link": "malito:ramokgopakgotso@gmail.com", "text": "ramokgopakgotso@gmail.com"},
    {"icon": "🐙", "label": "GitHub", "link": "https://github.com/Brendan3310", "text": "github.com/ramokgopa-kgotso"},
    {"icon": "💼", "label": "LinkedIn", "link": "https://www.linkedin.com/in/kgotsoramokgopa", "text": "linkedin.com/in/ramokgopa-kgotso"},
]

for method in methods:
    st.markdown(f"""
    <div style="margin: 10px 0;">
        <span class="icon">{method['icon']}</span>
        <strong>{method['label']}:</strong>
        <a href="{method['link']}" target="_blank" style="margin-left: 10px;">
            {method['text']}
        </a>
    </div>
    """, unsafe_allow_html=True)

# --- FOOTER ---
st.divider()
st.markdown("""
<div style="text-align: center; color: #666; padding: 20px 0;">
    <p>Made with ❤️ using Streamlit</p>
    <p style="font-size: 0.9em;">
        P.S. I usually respond within a day or two
    </p>
</div>
""", unsafe_allow_html=True)