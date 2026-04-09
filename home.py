import streamlit as st
import base64

def home():
    # st.write("hello")

    # Page configs (tab title, favicon)
    st.set_page_config(
        page_title="Vinh Nguyen's Portfolio",
        page_icon="🍕",
    )

    # CSS styles file
    with open("styles/main.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    # Profile image file
    with open("assets/profile_pic.jpg", "rb") as img_file:
        img = "data:image/jpeg;base64," + base64.b64encode(img_file.read()).decode()

    # PDF CV file
    with open("assets/Resume_Vinh_Nguyen_Jul.pdf", "rb") as pdf_file:
        pdf_bytes = pdf_file.read()

    # Top title
    st.write(f"""<div class="title">Hi! My name is <strong>Vinh Nguyen</strong>👋</div>""", unsafe_allow_html=True)

    # Profile image
    st.write(f"""
    <div class="container">
        <div class="box">
            <div class="spin-container">
                <div class="shape">
                    <div class="bd">
                        <img src="{img}" alt="Vinh Nguyen">
                    </div>
                </div>
            </div>
        </div>
    </div>
    """, 
    unsafe_allow_html=True)

    #     # Alternative image (static and rounded) uncomment it if you prefer this one
    # st.write(f"""
    # <div style="display: flex; justify-content: center;">
    #    <img src="{img}" alt="Enric Domingo" width="300" height="300" style="border-radius: 50%; object-fit: cover; margin-top: 40px; margin-bottom: 40px;">
    # </div>
    # """, unsafe_allow_html=True)

    # Subtitle
    st.write(f"""<div class="subtitle" style="text-align: center;">Machine Learning Engineer</div>""", unsafe_allow_html=True)

    # Social Icons
    social_icons = {
        # Platform: [URL, Icon]
        # "Kaggle": ["https://www.kaggle.com/edomingo", "https://www.kaggle.com/static/images/site-logo.svg"],
        "LinkedIn": ["https://www.linkedin.com/in/vinh-nguyen-huynh-quang/", "https://cdn-icons-png.flaticon.com/512/174/174857.png"],
        "GitHub": ["https://github.com/neverstoprunning0808", "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original.svg"],
    }

    social_icons_html = [f"<a href='{social_icons[platform][0]}' target='_blank' style='margin-right: 10px;'><img class='social-icon' src='{social_icons[platform][1]}'' alt='{platform}''></a>" for platform in social_icons]

    st.write(f"""
    <div style="display: flex; justify-content: center; margin-bottom: 20px;">
        {''.join(social_icons_html)}
    </div>""", 
    unsafe_allow_html=True)

    st.write("####")
    # About me section
    st.subheader("About Me")
    st.write("""
    - 🧑‍💻 I am a **ML and AI enthusiast** - a fresh graduate from the Master of Science in AI program at UT Austin.  

    - ❤️ I am passionate about **Machine Learning/Deep Learning, MLOps, Data, Software Engineering, Computer Vision, Bioinformatics, UAVs, Optimization, Automation**, and more!
        
    - 🏋️‍♂️ Also practicing sports like AFL 🏈 and football ⚽
    
    - 📫 How to reach me: vinh.nguyenhuynhquang@utexas.edu
    
    - 📍 Melbourne 🇦🇺
             
    """)

    st.write("##")
    # Download CV button

    st.download_button(
        label="📄 Download my CV",
        data=pdf_bytes,
        file_name="Resume_Vinh_Nguyen.pdf",
        mime="application/pdf",
    )

    st.write("##")

if __name__ == "__main__":
    home()