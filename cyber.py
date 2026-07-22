import streamlit as st
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

st.set_page_config(
    page_title="Cybersecurity AI",
    page_icon="🛡️"
)

st.markdown("""
<style>

/* Background */
.stApp{
    background-color: #000000;
}

/* Title */
h1{
    color:#00E676;
    text-align:center;
}

/* Buttons */
.stButton>button{
    background-color:#00C853;
    color:white;
    border:none;
    border-radius:10px;
    padding:10px 20px;
    font-size:16px;
}

.stButton>button:hover{
    background-color:#00E676;
}

/* Text Box */
.stTextArea textarea,
.stTextInput input{
    border:2px solid #00E676;
    border-radius:10px;
}

</style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown("## 🛡️ Cybersecurity AI")
    st.success("Welcome!")

    st.write("🔒 Network Security")
    st.write("🦠 Malware Detection")
    st.write("🎣 Phishing Awareness")
    st.write("🔑 Password Security")
    st.write("🌐 Web Security")
    st.write("☁ Cloud Security")
    st.write("💻 Ethical Hacking")
    st.write("🚨 Cyber Threats")

# Main Page
st.title("🛡️ Cybersecurity AI Assistant")



question = st.text_area("")

if st.button("Ask AI👨‍💻"):

    if not question.strip():
        st.warning("Please enter a question.")
        st.stop()

    llm = ChatGroq(
        model="llama-3.1-8b-instant",
        temperature=1
    )

    prompt = ChatPromptTemplate.from_template("""
You are a professional Cybersecurity Expert.

Your job is to answer ONLY cybersecurity-related questions.

Topics include:

- Cybersecurity Fundamentals
- Ethical Hacking
- Network Security
- Cryptography
- Firewalls
- Malware
- Ransomware
- Viruses
- Trojans
- Spyware
- Password Security
- Authentication
- Phishing
- Social Engineering
- Penetration Testing
- Cloud Security
- IoT Security
- Linux Security
- Windows Security
- Wi-Fi Security
- Digital Forensics
- Incident Response
- Vulnerability Assessment
- Cyber Laws
- Data Privacy
- Security Awareness

If the user asks anything outside cybersecurity, politely reply:

"Sorry, I only answer Cybersecurity-related questions."

Question:
{question}

Provide:

🔹 Simple Explanation

🔹 Step-by-Step Guidance

🔹 Best Practices

🔹 Common Mistakes

🔹 Precautions (if needed)
""")

    chain = prompt | llm

    with st.spinner("Analyzing... 🛡️"):
        response = chain.invoke(
            {
                "question": question
            }
        )

    st.success(response.content)