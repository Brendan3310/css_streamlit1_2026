import streamlit as st

def main():
  
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
        
    # ... REST OF YOUR CODE ...
    
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

# This allows the file to be run directly for testing
if __name__ == "__main__":
    main()
