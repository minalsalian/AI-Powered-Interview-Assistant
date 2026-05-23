import streamlit as st
from groq import Groq
import PyPDF2
import os
from groq import Groq


# =========================================================
# PAGE CONFIG
# =========================================================
st.set_page_config(
    page_title="AI Career Assistant",
    page_icon="🤖",
    layout="wide"
)

# =========================================================
# PREMIUM CSS
# =========================================================
st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}

body {
    background-color: #0F172A;
}

.main {
    background-color: #0F172A;
    color: white;
}

.block-container {
    margin-top: 12px;
    padding-top: 1rem;
    padding-bottom: 2rem;
    max-width: 1300px;
}


/* ============================= */
/* METRIC CARDS */
/* ============================= */

.metric-card {
    background: rgba(17,24,39,0.92);
    border-radius: 22px;
    padding: 1.5rem;
    height: 150px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    border: 1px solid rgba(255,255,255,0.06);
    box-shadow: 0 4px 25px rgba(0,0,0,0.25);
    transition: 0.3s;
    margin-top: 20px;
}
            
.metric-card:hover {
    transform: translateY(-4px);
}

.metric-title {

    color: #D1D5DB;
    font-size: 18px;
    margin-bottom: 14px;
    font-weight: 500;
    line-height: 1.5;
}

.metric-value {
    color: white;
    font-size: 52px;
    font-weight: 700;
}

/* ============================= */
/* BUTTONS */
/* ============================= */

.stButton > button {
    width: 100%;
    height: 3.2em;

    border-radius: 14px;

    background: linear-gradient(
        90deg,
        #6366F1,
        #8B5CF6
    );

    color: white;
    font-weight: 600;
    font-size: 16px;

    border: none;

    transition: 0.3s;
}

.stButton > button:hover {
    transform: scale(1.02);
    box-shadow: 0 0 18px rgba(99,102,241,0.55);
}

/* ============================= */
/* SIDEBAR */
/* ============================= */

[data-testid="stSidebar"] {
    background: linear-gradient(
        to bottom,
        #020617,
        #111827
    );
}

.sidebar-title {
    margin-top: -40px;
    color: white;
    font-size: 40px;
    font-weight: 600;
    line-height: 1.0;
    margin-bottom: 1rem;
}

/* ============================= */
/* TABS */
/* ============================= */

.stTabs [data-baseweb="tab-list"] {
    gap: 10px;
}

.stTabs [data-baseweb="tab"] {

    background-color: #111827;

    border-radius: 12px;

    padding: 12px 18px;

    color: white;

    font-weight: 500;
}

.stTabs [aria-selected="true"] {

    background: linear-gradient(
        90deg,
        #6366F1,
        #8B5CF6
    ) !important;
}

/* ============================= */
/* INPUT BOXES */
/* ============================= */

textarea, input {
    border-radius: 14px !important;
}

/* ============================= */
/* FILE UPLOADER */
/* ============================= */

[data-testid="stFileUploader"] {

    background: rgba(17,24,39,0.85);

    padding: 1rem;

    border-radius: 18px;

    border: 1px solid rgba(255,255,255,0.08);
}

/* ============================= */
/* EXPANDER */
/* ============================= */

div[data-testid="stExpander"] {

    border-radius: 16px !important;

    background: rgba(17,24,39,0.75);

    border: 1px solid rgba(255,255,255,0.08);
}

/* ============================= */
/* ALERTS */
/* ============================= */

.stAlert {
    border-radius: 14px;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# GROQ API
# =========================================================
client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

# =========================================================
# SIDEBAR
# =========================================================
st.sidebar.markdown("""
<div class="sidebar-title">
🤖 AI Career Assistant
</div>
""", unsafe_allow_html=True)

st.sidebar.markdown("""
### 🚀 Features

 Resume Analysis  
 ATS Resume Score  
 Interview Questions  
 Skill Assessment  
 Resume vs Job Match  
 AI Mock Interview  
 STAR Answer Generator  
 Career Roadmap  
 Resume Rewrite Assistant  
""")

st.sidebar.info(
    "Upload your resume and explore AI-powered career preparation."
)


# =========================================================
# METRIC CARDS
# =========================================================
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-title">ATS Optimization</div>
        <div class="metric-value">95%</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-title">AI Powered</div>
        <div class="metric-value">LLM</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-title">Career Guidance</div>
        <div class="metric-value">24/7</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-title">Interview Ready</div>
        <div class="metric-value">AI</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# =========================================================
# FILE UPLOAD
# =========================================================
uploaded_file = st.file_uploader(
    "📄 Upload Resume (PDF)",
    type="pdf"
)

resume_text = ""

# =========================================================
# PDF EXTRACTION
# =========================================================
if uploaded_file is not None:

    pdf_reader = PyPDF2.PdfReader(uploaded_file)

    for page in pdf_reader.pages:

        text = page.extract_text()

        if text:
            resume_text += text

    st.success("✅ Resume Uploaded Successfully!")

    # =====================================================
    # RESUME PREVIEW
    # =====================================================
    with st.expander("📄 Resume Preview"):

        st.write(resume_text[:4000])

    # =====================================================
    # TABS
    # =====================================================
    tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9 = st.tabs([
        "📌 Resume Analysis",
        "🎯 Interview Questions",
        "📝 Skill Assessment",
        "📊 ATS Score",
        "🚀 Job Match",
        "🎤 Mock Interview",
        "⭐ STAR Answer",
        "🛣️ Career Roadmap",
        "✍️ Resume Rewrite"
    ])

    # =====================================================
    # TAB 1
    # =====================================================
    with tab1:

        st.subheader("📌 AI Resume Analysis")

        if st.button("Generate Resume Analysis"):

            prompt = f"""
            Analyze this resume and provide:

            - Professional Summary
            - Key Skills
            - Strengths
            - Weaknesses
            - Suggested Improvements
            - Suggested Job Roles

            Resume:
            {resume_text[:1500]}
            """

            with st.spinner("🤖 Analyzing Resume..."):

                response = client.chat.completions.create(
                    model="llama-3.1-8b-instant",
                    max_tokens=500,
                    messages=[
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ]
                )

                st.write(
                    response.choices[0].message.content
                )

    # =====================================================
    # TAB 2
    # =====================================================
    with tab2:

        st.subheader("🎯 AI Interview Questions")

        difficulty = st.selectbox(
            "Select Difficulty",
            ["Beginner", "Intermediate", "Advanced"]
        )

        if st.button("Generate Interview Questions"):

            prompt = f"""
            Generate:
            - Technical Questions
            - HR Questions
            - Project-Based Questions

            Difficulty:
            {difficulty}

            Resume:
            {resume_text[:1500]}
            """

            with st.spinner("🤖 Generating Questions..."):

                response = client.chat.completions.create(
                    model="llama-3.1-8b-instant",
                    max_tokens=500,
                    messages=[
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ]
                )

                st.write(
                    response.choices[0].message.content
                )

    # =====================================================
    # TAB 3
    # =====================================================
    with tab3:

        st.subheader("📝 AI Skill Assessment")

        if st.button("Generate Skill Assessment"):

            prompt = f"""
            Generate:
            - 5 Technical MCQs
            - 3 Aptitude Questions
            - 2 Logical Questions

            Resume:
            {resume_text[:1500]}
            """

            with st.spinner("🤖 Generating Assessment..."):

                response = client.chat.completions.create(
                    model="llama-3.1-8b-instant",
                    max_tokens=500,
                    messages=[
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ]
                )

                st.write(
                    response.choices[0].message.content
                )

    # =====================================================
    # TAB 4
    # =====================================================
    with tab4:

        st.subheader("📊 ATS Resume Score")

        if st.button("Generate ATS Score"):

            prompt = f"""
            Analyze ATS compatibility.

            Include:
            - ATS Score out of 100
            - Missing Keywords
            - Improvement Suggestions
            - Formatting Tips

            Resume:
            {resume_text[:1500]}
            """

            with st.spinner("🤖 Calculating ATS Score..."):

                response = client.chat.completions.create(
                    model="llama-3.1-8b-instant",
                    max_tokens=500,
                    messages=[
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ]
                )

                st.write(
                    response.choices[0].message.content
                )

    # =====================================================
    # TAB 5
    # =====================================================
    with tab5:

        st.subheader("🚀 Resume vs Job Match")

        job_description = st.text_area(
            "Paste Job Description"
        )

        if st.button("Analyze Job Match"):

            prompt = f"""
            Compare this resume with the job description.

            Provide:
            - Match Percentage
            - Matching Skills
            - Missing Skills
            - ATS Improvements
            - Suggestions

            Resume:
            {resume_text[:1500]}

            Job Description:
            {job_description}
            """

            with st.spinner("🤖 Analyzing Match..."):

                response = client.chat.completions.create(
                    model="llama-3.1-8b-instant",
                    max_tokens=600,
                    messages=[
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ]
                )

                st.write(
                    response.choices[0].message.content
                )

    # =====================================================
    # TAB 6
    # =====================================================
    with tab6:

        st.subheader("🎤 AI Mock Interview")

        interview_question = st.text_input(
            "Enter Interview Question"
        )

        user_answer = st.text_area(
            "Type Your Answer"
        )

        if st.button("Evaluate Answer"):

            prompt = f"""
            Evaluate this interview answer.

            Provide:
            - Strengths
            - Weaknesses
            - Improvements
            - Confidence Score
            - Better Sample Answer

            Question:
            {interview_question}

            Answer:
            {user_answer}
            """

            with st.spinner("🤖 Evaluating Answer..."):

                response = client.chat.completions.create(
                    model="llama-3.1-8b-instant",
                    max_tokens=500,
                    messages=[
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ]
                )

                st.write(
                    response.choices[0].message.content
                )

    # =====================================================
    # TAB 7
    # =====================================================
    with tab7:

        st.subheader("⭐ STAR Answer Generator")

        normal_answer = st.text_area(
            "Enter Interview Answer"
        )

        if st.button("Convert to STAR Format"):

            prompt = f"""
            Convert this answer into STAR format.

            Include:
            - Situation
            - Task
            - Action
            - Result

            Answer:
            {normal_answer}
            """

            with st.spinner("🤖 Generating STAR Answer..."):

                response = client.chat.completions.create(
                    model="llama-3.1-8b-instant",
                    max_tokens=500,
                    messages=[
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ]
                )

                st.write(
                    response.choices[0].message.content
                )

    # =====================================================
    # TAB 8
    # =====================================================
    with tab8:

        st.subheader("🛣️ AI Career Roadmap")

        target_role = st.selectbox(
            "Select Career Goal",
            [
                "AI Engineer",
                "Data Scientist",
                "Backend Developer",
                "Java Developer",
                "Full Stack Developer",
                "ML Engineer"
            ]
        )

        if st.button("Generate Career Roadmap"):

            prompt = f"""
            Generate roadmap for:

            {target_role}

            Include:
            - Skills
            - Technologies
            - Certifications
            - Project Ideas
            - Learning Plan

            Resume:
            {resume_text[:1500]}
            """

            with st.spinner("🤖 Generating Roadmap..."):

                response = client.chat.completions.create(
                    model="llama-3.1-8b-instant",
                    max_tokens=700,
                    messages=[
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ]
                )

                st.write(
                    response.choices[0].message.content
                )

    # =====================================================
    # TAB 9
    # =====================================================
    with tab9:

        st.subheader("✍️ AI Resume Rewrite Assistant")

        rewrite_input = st.text_area(
            "Paste Resume Content"
        )

        rewrite_style = st.selectbox(
            "Rewrite Style",
            [
                "Professional",
                "ATS Optimized",
                "Technical",
                "Concise",
                "Recruiter Friendly"
            ]
        )

        if st.button("Rewrite Resume"):

            prompt = f"""
            Rewrite this resume content.

            Style:
            {rewrite_style}

            Make it:
            - Professional
            - ATS Friendly
            - Strong
            - Concise

            Content:
            {rewrite_input}
            """

            with st.spinner("🤖 Rewriting Resume..."):

                response = client.chat.completions.create(
                    model="llama-3.1-8b-instant",
                    max_tokens=700,
                    messages=[
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ]
                )

                st.write(
                    response.choices[0].message.content
                )

else:

    st.warning("⚠️ Please upload a resume PDF to continue.")