import streamlit as st
import base64
from pathlib import Path

# ------------------------------------------------------------
# PERSONALIZE THESE VALUES BEFORE PUBLISHING
# ------------------------------------------------------------
NAME = "ATHMAKUR KARUNAKAR REDDY "
ROLE = "Aspiring Data Analyst"
TAGLINE = "I turn raw data into clear insights and useful decisions."
EMAIL = "athmakurkarunakarreddy@gmail.com"
PHONE = "+91 9676021954"
LOCATION = "Bengaluru, India"
LINKEDIN_URL = "https://www.linkedin.com/in/athmakurkarunakarreddy "
GITHUB_URL = "https://github.com/Karunakarreddyy"
ASSETS = Path(__file__).parent / "assets"
RESUME_FILE = ASSETS / "resume.pdf"

st.set_page_config(
    page_title=f"{NAME} | Portfolio",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Manrope:wght@400;500;600;700;800&display=swap');

:root {
  --bg: #07110f;
  --panel: #0d1b17;
  --panel2: #10231d;
  --green: #43d6a0;
  --green2: #a4f0d2;
  --text: #f1f7f4;
  --muted: #a3b7ae;
  --line: rgba(183, 220, 202, .14);
}
html { scroll-behavior: smooth; scroll-padding-top: 90px; }
.stApp {
  background: var(--bg);
  color: var(--text);
  font-family: 'DM Sans', sans-serif;
}
[data-testid="stSidebar"], [data-testid="collapsedControl"] {display:none;}
header[data-testid="stHeader"] {background:rgba(7,17,15,.92);}
.block-container {max-width:1180px; padding:1rem 2rem 3rem;}
h1,h2,h3 {font-family:'Manrope',sans-serif !important; letter-spacing:-.035em;}
p, li {line-height:1.8;}
a {color:var(--green2) !important; text-decoration:none !important;}
a:hover {color:var(--green) !important;}
.nav {
 display:flex; justify-content:space-between; align-items:center; gap:18px;
 flex-wrap:wrap; padding:17px 0 22px; border-bottom:1px solid var(--line);
 margin-bottom:30px;
}
.logo {font:800 19px 'Manrope',sans-serif; color:var(--text);}
.logo span {color:var(--green);}
.navlinks {display:flex; gap:19px; flex-wrap:wrap; font-size:13px; font-weight:600;}
.navlinks a {color:#c4d4cd !important;}
.hero {
 background:radial-gradient(ellipse at 80% 20%, rgba(39,160,113,.22), transparent 40%),
 linear-gradient(135deg,#0d211a,#091310 70%);
 border:1px solid rgba(105,220,169,.18); border-radius:26px;
 padding:clamp(28px,5vw,64px); margin-bottom:64px; overflow:hidden;
}
.kicker {color:var(--green) !important; font-size:12px; font-weight:800; letter-spacing:2.5px; text-transform:uppercase;}
.hero h1 {font-size:clamp(38px,6vw,70px); line-height:1.08; color:#f4faf7; margin:15px 0;}
.hero h1 span {color:var(--green);}
.hero p {max-width:680px; color:#bfd0c8; font-size:16px;}
.pill {display:inline-block; padding:7px 11px; border:1px solid var(--line); border-radius:99px; color:#c9ded4; font-size:12px; margin:4px 5px 0 0;}
.section {padding:16px 0 35px; margin-bottom:16px;}
.section-kicker {color:var(--green); font-size:11px; letter-spacing:2.5px; font-weight:800;}
.section-title {font-size:clamp(27px,4vw,38px); font-weight:800; margin:5px 0 8px;}
.section-sub {color:var(--muted); max-width:720px;}
.card {
 background:linear-gradient(150deg,rgba(18,39,31,.95),rgba(11,25,20,.95));
 border:1px solid var(--line); border-radius:17px; padding:23px;
 margin:7px 0 15px; height:100%;
}
.card h3 {font-size:19px; color:#f2faf6; margin:7px 0;}
.card p,.card li {color:#b8c9c1; font-size:14px;}
.card .small {font-size:11px; color:var(--green); font-weight:800; letter-spacing:1.5px; text-transform:uppercase;}
.tag {display:inline-block; background:#17382b; color:#b5f4d9; padding:5px 9px; margin:3px 3px 3px 0; border-radius:7px; font-size:11px;}
.metric {background:#0c1b16; border:1px solid var(--line); padding:17px; border-radius:14px;}
.metric strong {display:block; color:var(--green); font-size:18px;}
.metric span {color:var(--muted); font-size:12px;}
.timeline {border-left:2px solid #285642; padding:0 0 12px 20px; margin:18px 0;}
.timeline h3 {font-size:17px; margin:0 0 3px;}
.timeline p {color:var(--muted); margin:0; font-size:14px;}
.cta {background:linear-gradient(120deg,#103a2a,#0d211a); border:1px solid rgba(67,214,160,.25); border-radius:20px; padding:28px;}
.cta h2 {font-size:29px;}
.footer {border-top:1px solid var(--line); margin-top:45px; padding:25px 0; color:#8da49a; font-size:12px; text-align:center;}
/* Keep Streamlit controls readable against the dark portfolio theme. */
div.stButton > button,
div.stDownloadButton > button,
div.stLinkButton > a {
  border-radius:10px !important;
  font-weight:700 !important;
  min-height:42px;
  background:#10231d !important;
  color:#eaf7f0 !important;
  border:1px solid #3a6250 !important;
}
div.stButton > button:hover,
div.stDownloadButton > button:hover,
div.stLinkButton > a:hover {
  background:#17382b !important;
  color:#ffffff !important;
  border-color:#43d6a0 !important;
}
div.stButton > button[kind="primary"] {
  background:var(--green) !important;
  color:#07110f !important;
  border:0 !important;
}
hr {border-color:var(--line) !important;}
@media(max-width:700px) {
 .block-container {padding: .6rem 1rem 2rem;}
 .navlinks {gap:12px;}
 .hero {padding:27px 22px; border-radius:19px;}
}
</style>
""", unsafe_allow_html=True)

# Single-page top navigation
st.markdown("""
<div class="nav">
  <div class="logo">KR<span>.</span> <span style="color:#dceae3;font-weight:600">Portfolio</span></div>
  <div class="navlinks">
    <a href="#about">About</a><a href="#skills">Skills</a>
    <a href="#projects">Projects</a><a href="#education">Education</a>
    <a href="#certifications">Certificates</a><a href="#contact">Contact</a>
  </div>
</div>
""", unsafe_allow_html=True)


# Hero with professional profile photo
hero_left, hero_right = st.columns([1.35, 1], gap="large")

with hero_left:
    st.markdown(f"""
    <div id="home" class="hero">
      <div class="kicker">DATA ANALYTICS · BUSINESS INTELLIGENCE</div>
      <h1>Hi, I'm<br><span>{NAME.strip()}.</span></h1>
      <h3 style="color:#d8e8df;font-size:clamp(19px,2.5vw,25px);font-weight:600">{ROLE}</h3>
      <p>{TAGLINE} I work with Python, SQL, Power BI and data visualization to explore datasets, communicate findings, and support data-informed decisions.</p>
      <div style="margin-top:22px">
        <a href="#projects" style="display:inline-block;background:#43d6a0;color:#07110f!important;padding:12px 18px;border-radius:9px;font-weight:800;margin:0 8px 8px 0">Explore My Work ↘</a>
        <a href="#contact" style="display:inline-block;border:1px solid #507261;color:#effaf4!important;padding:11px 18px;border-radius:9px;font-weight:700">Get In Touch ↗</a>
      </div>
      <div style="margin-top:22px">
        <span class="pill">Python</span>
        <span class="pill">SQL / MySQL</span>
        <span class="pill">Power BI</span>
        <span class="pill">Excel</span>
      </div>
    </div>
    """, unsafe_allow_html=True)

with hero_right:
    st.markdown("""
    <div style="
        background:linear-gradient(145deg,#153b2d,#0b1712);
        border:1px solid rgba(67,214,160,0.4);
        border-radius:24px;
        padding:14px;
        margin:35px auto 0;
        max-width:440px;
        box-shadow:0 18px 50px rgba(0,0,0,0.35);
    ">
        <div style="
            color:#43d6a0;
            font-size:11px;
            font-weight:800;
            letter-spacing:2px;
            text-align:center;
            padding:8px 0 14px;
        ">PROFESSIONAL PROFILE</div>
    """, unsafe_allow_html=True)

    st.image(
        str(ASSETS / "profile.jpg"),
        use_container_width=True,
    )

    st.markdown("""
        <div style="
            text-align:center;
            padding:17px 8px 10px;
            color:#f1f7f4;
            font-size:17px;
            font-weight:800;
        ">ATHMAKUR KARUNAKAR REDDY</div>
        <div style="
            text-align:center;
            color:#a4f0d2;
            font-size:13px;
            padding-bottom:12px;
        ">Aspiring Data Analyst</div>
    </div>
    """, unsafe_allow_html=True)

# Profile metrics - no invented client counts or testimonials
m1, m2, m3 = st.columns(3)
for col, title, desc in [
    (m1, "Analytics", "Cleaning · Analysis · Insights"),
    (m2, "Visualization", "Power BI · Dashboards"),
    (m3, "Programming", "Python · SQL"),
]:
    with col:
        st.markdown(f'<div class="metric"><strong>{title}</strong><span>{desc}</span></div>', unsafe_allow_html=True)

# About
st.markdown("""
<div id="about" class="section">
  <div class="section-kicker">01 / ABOUT ME</div>
  <div class="section-title">Curious about data. Focused on useful outcomes.</div>
  <div class="section-sub">A short introduction to my background, interests, and the work I want to do.</div>
</div>
""", unsafe_allow_html=True)
a1, a2 = st.columns([1.3, 1])
with a1:
    st.markdown("""
    I am an MCA graduate with an interest in **Data Analytics and Business Intelligence**.
    My project work has involved preparing datasets, exploring patterns, creating analytical
    measures, and presenting results through dashboards and applications.

    I am currently building my practical experience through training and projects, and looking
    for opportunities where I can learn, collaborate, and contribute to data-driven decisions.
    """)
with a2:
    st.markdown("""
    <div class="card">
      <div class="small">PROFILE SNAPSHOT</div>
      <h3>What I bring</h3>
      <p>• Analytical thinking and structured problem solving</p>
      <p>• Interest in data quality and clear visual storytelling</p>
      <p>• Willingness to learn tools and business context</p>
      <p>• Project-based practice in analytics and machine learning</p>
    </div>
    """, unsafe_allow_html=True)

# Skills
st.markdown("""
<div id="skills" class="section">
  <div class="section-kicker">02 / SKILLS & EXPERIENCE</div>
  <div class="section-title">Tools I use to explore data</div>
  <div class="section-sub">Skill groups instead of arbitrary percentage bars, so the portfolio stays honest and easy to update.</div>
</div>
""", unsafe_allow_html=True)
skill_cols = st.columns(2)
skill_data = [
    ("Data Analysis", ["Data Cleaning", "Data Transformation", "Exploratory Analysis", "Data Quality"]),
    ("BI & Visualization", ["Power BI", "Power Query", "DAX Measures", "Dashboard Design"]),
    ("Programming & Data", ["Python", "MySQL", "Pandas (if applicable)", "SQL Queries"]),
    ("Professional", ["Problem Solving", "Communication", "Attention to Detail", "Continuous Learning"]),
]
for i, (heading, tags) in enumerate(skill_data):
    with skill_cols[i % 2]:
        tag_html = "".join('<span class="tag">' + x + '</span>' for x in tags)
        st.markdown(
            f'<div class="card"><div class="small">SKILL GROUP</div>'
            f'<h3>{heading}</h3>{tag_html}</div>',
            unsafe_allow_html=True
        )

st.markdown('<div class="section-title" style="font-size:24px;margin-top:15px">Experience & learning</div>', unsafe_allow_html=True)
st.markdown("""
<div class="timeline">
  <h3>Internship / Training — QSpiders</h3>
  <p>Currently undergoing training at QSpiders and i have worked on Quick Commerce Sales & Zepto Sales Dashboard projects using power BI to analyse sales data and create insightful visualizations.</p>
</div>
""", unsafe_allow_html=True)

# Projects
st.markdown("""
<div id="projects" class="section">
  <div class="section-kicker">03 / SELECTED PROJECTS</div>
  <div class="section-title">Work that puts data to use</div>
  <div class="section-sub">Two project summaries to start with. Add verified repository, demo, and dashboard links when available.</div>
</div>
""", unsafe_allow_html=True)
p1, p2 = st.columns(2)
with p1:
    st.markdown("""
    <div class="card">
      <div class="small">POWER BI · BUSINESS ANALYTICS</div>
      <h3>Quick-Commerce Sales & Business Analytics</h3>
      <p>Explored customer, product, order, transaction, rating, and delivery data to build a more useful view of business performance.</p>
      <p><b>Work areas</b></p>
      <ul>
        <li>Cleaned and transformed source data</li>
        <li>Built a data model and analytical measures</li>
        <li>Designed interactive views for sales, customers, and delivery patterns</li>
      </ul>
      <span class="tag">Power BI</span><span class="tag">Power Query</span><span class="tag">DAX</span>
    </div>
    """, unsafe_allow_html=True)
    st.caption("Project repository/dashboard URL: https://github.com/Karunakarreddyy/quick-commerce-power-BI-dashboard ")
with p2:
    st.markdown("""
    <div class="card">
      <div class="small">PYTHON · MACHINE LEARNING</div>
      <h3>Air Pollution & Respiratory Health</h3>
      <p>Project exploring relationships between environmental pollution and respiratory-health risk using machine-learning methods.</p>
      <p><b>Work areas</b></p>
      <ul>
        <li>Prepared data for modelling and evaluation</li>
        <li>Explored classification and forecasting approaches</li>
        <li>Developed a Flask-based interface for predictions</li>
      </ul>
      <span class="tag">Python</span><span class="tag">Machine Learning</span><span class="tag">Flask</span>
    </div>
    """, unsafe_allow_html=True)
    st.caption("Project repository/demo URL: https://drive.google.com/file/d/1FS0iEK1rrgB5eGL0MzFOni34LNUSl7uF/view?usp=drive_link")

# Education
st.markdown("""
<div id="education" class="section">
  <div class="section-kicker">04 / EDUCATION</div>
  <div class="section-title">Academic background</div>
</div>
""", unsafe_allow_html=True)

education = [
    ("Master of Computer Applications (MCA)", "Mohan Babu University", "2024–2026", "7.66"),
    ("B.Sc. Computer Science", "Sree Vidyanikethan Degree College", "2021–2024", "7.00"),
    ("Intermediate — M.P.C", "Sri Chaitanya Junior College", "2019–2021", "9.25"),
    ("10th", "Vaagdevi High School", "2019", "9.7"),
]

for degree, institution, period, cgpa in education:
    st.markdown(
        f"""
        <div class="timeline">
            <h3>{degree}</h3>
            <p>{institution} · {period}</p>
            <p><strong>CGPA: {cgpa}</strong></p>
        </div>
        """,
        unsafe_allow_html=True
    )


# Certifications
st.markdown("""
<div id="certifications" class="section">
  <div class="section-kicker">05 / CERTIFICATIONS</div>
  <div class="section-title">Courses, credentials & milestones</div>
""", unsafe_allow_html=True)
certs = [
    ("Data Analytics Job Simulation", "Deloitte — Forage", "https://drive.google.com/file/d/1_tX4JNvEtDz-iTYBDXiPYtoLWTFftbAl/view?usp=sharing"),
    ("Web Development with HTML, CSS and JavaScript", "Apexplanet", "https://drive.google.com/file/d/1Xco0WU9hfhCvKMqtIBbF8HYxDugQIOy3/view?usp=drive_link"),
    ("International Conference on Recent Challenges in Engineering and Technology", "ICRCET-2026", "https://drive.google.com/file/d/14ddgwbD-FHWXfeOUKj3TrZ0dt1-tCAVl/view?usp=drive_link"),
    ("Python Foundation Certification", "Infosys Springboard — 2026", "https://drive.google.com/file/d/1Hjnnyd0TTIsP4UMCbxkbQN8MfE3oFmDJ/view?usp=drive_link"),
    ("QSpiders Offer Letter", "Internship / Training", "https://drive.google.com/file/d/17Z7-gXxiCIeo-rPn4spTx0LEyQShHqkw/view?usp=drive_link"),
]
cert_cols = st.columns(2)
for i, (title, issuer, cert_url) in enumerate(certs):
    with cert_cols[i % 2]:
        st.markdown(f'<div class="card"><div class="small">CERTIFICATE / CREDENTIAL</div><h3>✳ {title}</h3><p>{issuer}</p></div>', unsafe_allow_html=True)
        st.link_button("View Certificate ↗", cert_url, use_container_width=True)


# Resume and Contact
st.markdown("""
<div class="section-header">
    <h2>Resume & Contact</h2>
    <p>Let's connect and explore opportunities to work together.</p>
</div>
""", unsafe_allow_html=True)

c1, c2 = st.columns([1, 1])

# Contact Information
with c1:
    st.markdown(f"""
    <div class="card">
        <h3>📬 Contact Information</h3>
        <p><strong>Email:</strong>
        <a href="mailto:{EMAIL}">{EMAIL}</a></p>
        <p><strong>Phone:</strong>
        <a href="tel:{PHONE}">{PHONE}</a></p>
        <p><strong>Location:</strong> {LOCATION}</p>
    </div>
    """, unsafe_allow_html=True)

# Resume and Social Links
with c2:
    st.markdown("""
    <div class="card">
        <h3>📄 My Resume</h3>
        <p>View or download my resume to learn more about my
        skills, projects, and experience.</p>
    </div>
    """, unsafe_allow_html=True)

    if RESUME_FILE.is_file():
        resume_bytes = RESUME_FILE.read_bytes()

        r_view, r_download = st.columns(2)

        with r_view:
            if st.button(
                "👁️ View Resume",
                use_container_width=True
            ):
                st.session_state["show_resume_preview"] = not (
                    st.session_state.get("show_resume_preview", False)
                )

        with r_download:
            st.download_button(
                label="⬇️ Download PDF",
                data=resume_bytes,
                file_name="Karunakar_Reddy_Resume.pdf",
                mime="application/pdf",
                use_container_width=True
            )

        if st.session_state.get("show_resume_preview", False):
            st.markdown("### Resume Preview")

            pdf_base64 = base64.b64encode(
                resume_bytes
            ).decode("utf-8")

            pdf_html = f"""
            <iframe
                src="data:application/pdf;base64,{pdf_base64}"
                width="100%"
                height="760"
                style="border: none; border-radius: 8px;"
                type="application/pdf">
            </iframe>
            """

            st.components.v1.html(
                pdf_html,
                height=780,
                scrolling=True
            )
    else:
        st.error(
            "Resume PDF not found. Please place your resume at "
            "assets/resume.pdf inside your portfolio folder."
        )

    st.link_button(
        "🔗 LinkedIn Profile",
        LINKEDIN_URL,
        use_container_width=True
    )

    st.link_button(
        "💻 GitHub Profile",
        GITHUB_URL,
        use_container_width=True
    )

# Footer
st.markdown("""
<div style="text-align:center; padding:25px 0 10px 0;">
    <p>Made with ❤️ using Python and Streamlit</p>
    <p>© 2026 Karunakar Reddy. All rights reserved.</p>
</div>
""", unsafe_allow_html=True)

