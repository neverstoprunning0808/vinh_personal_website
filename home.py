import streamlit as st
import base64

# ── Portfolio section ──────────────────────────────────────────────────────────

def portfolio():
    st.write("##")
    st.subheader("🗂️ Portfolio")
    st.write("A collection of ML & AI projects grouped by domain.")
    st.write("---")

    groups = {
        "🔍 AI Assistants & RAG": [
            {
                "title": "Multi-Document RAG Assistant",
                "description": (
                    "Built a Retrieval-Augmented Generation (RAG) chatbot supporting pdf, docx, and txt document ingestion with"
                    "semantic vector search and conversational QA."
                ),
                "stack": ["Python", "LangChain", "ChromaDB", "HuggingFace", "Streamlit"],
                "demo": "https://vinh-nguyen-rag-chatbot.streamlit.app/",
                "code": "https://github.com/neverstoprunning0808/rag-chatbot",
            },
            {
                "title": "LLM Tool-Calling Weather Assistant",
                "description": (
                    "Built an LLM-powered weather assistant with tool-calling capabilities using Groq API, Geopy geocoding, and"
                    " Open-Meteo APIs, deployed through an interactive Streamlit interface."
                ),
                "stack": ["Python", "GroqAPI", "Geopy", "Open-Meteo", "Streamlit"],
                "demo": "https://vinh-nguyen-the-weather-forecast-assistant.streamlit.app/",
                "code": "https://github.com/neverstoprunning0808/llm-tool-call-weather-app",
            },
        ],
        "🤖 LLM & Fine-Tuning": [
            {
                "title": "Restaurant Review Classification",
                "description": (
                    "Fine-tuned DistilBERT for 5-class sentiment classification on the Yelp Review Full "
                    "dataset using Hugging Face Transformers and the Trainer API."
                ),
                "stack": ["Python", "PyTorch", "HF Transformers", "DVC", "Gradio"],
                "demo": "https://vinh0808-restaurant-review-rating-prediction.hf.space/",
                "code": "https://github.com/neverstoprunning0808/llm-multiclass-finetuning",
            },
            {
                "title": "Grade School Math Reasoning App",
                "description": (
                    "Fine-tuned small LLMs on GSM8K using LoRA-based supervised fine-tuning. "
                    "Evaluated Direct Answer SFT, few-shot Chain-of-Thought prompting, and CoT SFT "
                    "reasoning strategies."
                ),
                "stack": ["Python", "PyTorch", "HF Transformers", "LoRA", "PEFT", "DVC", "Gradio"],
                "demo": "https://vinh0808-grade-school-math-solver.hf.space/",
                "code": "https://github.com/neverstoprunning0808/llm-math-reasoning-finetuned",
            },
            {
                "title": "Quantization & LoRA Techniques",
                "description": (
                    "Built from-scratch implementations of FP16/BF16 half-precision training, 4-bit "
                    "quantization, and LoRA adapters for parameter-efficient LLM fine-tuning techniques."
                ),
                "stack": ["Python", "PyTorch", "LoRA", "Quantization", "Low Precision"],
                "demo": None,
                "code": "https://github.com/neverstoprunning0808/lora-qlora-quantization-from-scratch",
            },
        ],
        "👁️ Computer Vision": [
            {
                "title": "Scene Text Recognition Pipeline",
                "description": (
                    "Built a two-stage Scene Text Recognition pipeline by fine-tuning YOLOv11 for text detection and training a "
                    "custom CRNN with CTC loss for text recognition on the ICDAR 2013 dataset."
                ),
                "stack": ["Python", "PyTorch", "ultralytics", "YOLOv11", "OpenCV", "DVC"],
                "demo": None,
                "code": "https://github.com/neverstoprunning0808/Finetune-YOLOv11-Custom-CRNN-STR",
            },
                                    {
                "title": "Brain Tumor Segmentation",
                "description": (
                    "A UNET model with a ResNet-34 encoder trained on multi-modal MRI scans to automatically segment brain tumors,"
                    " achieving an IoU score of 0.65 on the validation set."
                ),
                "stack": ["Python", "PyTorch", "UNET", "ResNet", "IoU", "Segmentation"],
                "demo": None,
                "code": "https://github.com/neverstoprunning0808/brain-tumor-segmentation-unet-resnet34",
            },
                        {
                "title": "Self-Supervised Contrastive Learning",
                "description": (
                    "Built a ResNet-18–based contrastive learning model for chest X-ray pneumonia classification, "
                    "achieving 81.25% accuracy with limited labeled data."
                ),
                "stack": ["Python", "PyTorch", "ResNet", "Self-supervised", "Contrastive Learning"],
                "demo": None,
                "code": "https://github.com/neverstoprunning0808/self-supervised-contrastive-learning-for-pneumonia-detection",
            }
        ],
        "⚙️ MLOps & Cloud": [
            {
                "title": "MLOps Pipeline System",
                "description": (
                    "Built an end-to-end reproducible ML pipeline using Hydra, DVC, MLflow, Poetry, " 
                    "and Docker for experiment tracking, configuration management, and workflow orchestration."
                ),
                "stack": ["Python", "Pytorch", "DVC", "Mlflow", "Poetry", "Docker"],
                "demo": None,
                "code": "https://github.com/neverstoprunning0808/dvc-hydra-mlflow-ml-pipeline",
            },
            {
                "title": "CI/CD Pipeline with GitHub Actions",
                "description": (
                    "A 'Hello World' CI/CD pipeline using GitHub Actions, Docker, and pytest to automate testing and containerization of a Python app."
                ),
                "stack": ["Python", "GitHub Actions", "Docker", "Pytest", "Flask"],
                "demo": None,
                "code": "https://github.com/neverstoprunning0808/ci_cd_101",
            },

            {
                "title": "Blog Web",
                "description": (
                    "Built a full-stack blog platform using FastAPI, PostgreSQL, Alembic, JWT authentication, and Jinja templating."
                ),
                "stack": ["Python", "FastAPI", "Alembic", "Postgresql", "JWT", "Jinja"],
                "demo": None,
                "code": "https://github.com/neverstoprunning0808/fastapi-jinja-postgresql-jwt-web-app",
            },
        ],
    }

    for group_name, projects in groups.items():
        st.markdown(f"### {group_name}")

        cols = st.columns(2)
        for i, proj in enumerate(projects):
            with cols[i % 2]:
                with st.container(border=True):
                    st.markdown(f"**{proj['title']}**")
                    st.write(
                        f"<div style='min-height: 130px'>{proj['description']}</div>",
                        unsafe_allow_html=True
                    )

                    # Tech-stack badges
                    badges = " ".join(f"`{tag}`" for tag in proj["stack"])
                    st.markdown(badges)

                    # Demo / Code links
                    link_parts = []
                    if proj.get("demo"):
                        link_parts.append(f"[🚀 Demo]({proj['demo']})")
                    if proj.get("code"):
                        link_parts.append(f"[💻 Code]({proj['code']})")
                    if link_parts:
                        st.markdown("  |  ".join(link_parts))

        st.write("")  # spacing between groups


# ── Main page ──────────────────────────────────────────────────────────────────

def home():
    st.set_page_config(
        page_title="Vinh Nguyen's Portfolio",
        page_icon="🐱",
    )

    with open("styles/main.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    with open("assets/profile_pic.jpg", "rb") as img_file:
        img = "data:image/jpeg;base64," + base64.b64encode(img_file.read()).decode()

    with open("assets/Vinh_Nguyen_Resume_May26.pdf", "rb") as pdf_file:
        pdf_bytes = pdf_file.read()

    # Top title
    st.write(f"""<div class="title">G'day! I'm <strong>Vinh Nguyen</strong>👋</div>""", unsafe_allow_html=True)

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
    """, unsafe_allow_html=True)

    # Subtitle
    st.write(f"""<div class="subtitle" style="text-align: center;">Machine Learning & AI Engineer</div>""", unsafe_allow_html=True)

    # Social Icons
    social_icons = {
        "LinkedIn": ["https://www.linkedin.com/in/vinh-nguyen-huynh-quang/", "https://cdn-icons-png.flaticon.com/512/174/174857.png"],
        "GitHub":   ["https://github.com/neverstoprunning0808", "https://img.icons8.com/ios-filled/50/ffffff/github.png"],
    }
    social_icons_html = [
        f"<a href='{social_icons[p][0]}' target='_blank' style='margin-right: 10px;'>"
        f"<img class='social-icon' src='{social_icons[p][1]}' alt='{p}'></a>"
        for p in social_icons
    ]
    st.write(f"""
    <div style="display: flex; justify-content: center; margin-bottom: 20px;">
        {''.join(social_icons_html)}
    </div>""", unsafe_allow_html=True)

    st.write("####")

    # About Me
    st.subheader("🙋‍♂️ About Me")
    st.write("""
    - 🧑‍💻 I am a **ML and AI enthusiast**, a recent graduate from the Master of Science in AI program at UT Austin.
    - ❤️ I am passionate about **Machine Learning, LLM, Computer Vision**, and more!
    - 🏈 I can't wait to have my first footy kick in 🇦🇺! Same to football and rugby touch.
    - 📫 Contact me: vinh.nguyenhuynhquang@utexas.edu
    - 📍 Current location: Melbourne 🇦🇺
    - 🪪 Work Permit: full work rights in 🇦🇺 until 2030.
    """)

    st.write("##")

    # Download CV
    st.download_button(
        label="📄 Download my CV",
        data=pdf_bytes,
        file_name="Resume_Vinh_Nguyen.pdf",
        mime="application/pdf",
    )

    # ── Portfolio section ──────────────────────────────────────────────────────
    portfolio()


if __name__ == "__main__":
    home()
