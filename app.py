import streamlit as st
import requests
import streamlit.components.v1 as components
from streamlit_lottie import st_lottie
from PIL import Image
from pathlib import Path



# --- SETTINGS --- #
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "style.css"
resume_file = current_dir / "assets" / "Resume_Jesica_Karczewski.docx"
profile_pic = current_dir / "assets" / "jkprofile-pic.png"


# --- GENERAL SETTINGS --- #
PAGE_TITLE = "Jesica Karczewski | Digital Resume"
PAGE_ICON = "👩🏻‍💻"
NAME = "Jesica Karczewski"
DESCRIPTION = """
Sr Performance Analyst & Full Stack Developer"""
EMAIL = "jesicakarcz@gmail.com"
LINKS = {
    "Email ": "mailto:jesicakarcz@gmail.com",
    "LinkedIn": "https://linkedin.com/in/jesicakarczewski",
    "GitHub": "https://github.com/jesskarcz",
}

PROJECTS = {
    "🔗 Spotify Dashboard - Most Streamed Songs 2023": "https://www.datascienceportfol.io/jesKarcz/projects/0",
    "🔗 For Cooking Blog - Wordpress website": "https://for.cooking",
    "🔗 TO-DO List - React.js Web App": "https://todo-list-n.vercel.app/",
 
}
 

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

 

# --- LOAD CSS, PDF & PROFIL PIC --- #
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)
st.markdown('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">', unsafe_allow_html=True)

# Lottier animation
lottie_coding = "https://lottie.host/11e64c3b-2b74-460a-8472-22c882b948b2/345vdrNStY.json"
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# --- HERO SECTION --- 3
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    #st.write("📫", EMAIL)
    # --- LINKS --- #
    st.write('\n')
    cols = st.columns(len(LINKS))
    for index, (platform, link) in enumerate(LINKS.items()):
        if platform == "LinkedIn":
            icon_class = "fab fa-linkedin"
        elif platform == "GitHub":
            icon_class = "fab fa-github"
        else:
            icon_class = "fa fa-envelope"
        cols[index].write(f'<a href="{link}" target="_blank"><i class="{icon_class}"></i> {platform}</a>', unsafe_allow_html=True)
     


# --- SKILLS --- #
left_column, right_column = st.columns(2)    
with left_column:
    st.write('\n')
    st.header("Hard Skills")
    st.write(
        """
    - 👩🏻‍💻 Programming: Python (Streamlit, Pandas), SQL.
    - 📊 Data Visulization: PowerBi, Tableau, SAS Studio, MS Excel, Plotly, Jupyter.
    - 🗄️ Databases: SAS, MySQL, BigQuery.
    - 🖥️ Full-stack Technologies: HTML, CSS, JavaScript, PHP, React, SQLite, MySQL. Node.js.
    """
    )  
      
with right_column:
    st_lottie(lottie_coding, height=290, width=420, key="coding")    


# --- SKILL SUMMARY --- #
st.header("Skill Summary")
st.write(
    """
- ✔️ +8 years of experience as Full-Stack Developer.
- ✔️ Software Development Life Cycle (SDLC) process.
- ✔️ Skilled in extracting actionable insights from data.
- ✔️ Strong hands on experience and knowledge in Python and SQL.
- ✔️ Excellent team-player and strong sense of initiative on tasks.
- ✔️ Detail-oriented and problem solving.
"""
)   



# --- WORK HISTORY --- #
st.write('\n')
st.header("Work Experience")
st.write("---")


# --- Exp 1
st.write('\n')
st.subheader("Sr Performance Analyst | TELUS")
st.write("06/2019 to present")
st.write(
    """
- ► Manage larger deployments, automations, and Ad-hocs, including template coding (HTML, CSS, JS), data integration (SAS), Adobe Campaign workflow setup, and segmentation configuration (Queries).
- ► Develop mobile-friendly email templates for optimized customer experiences across all devices, ensuring consistency through QA rendering.
- ► Collaborate with stakeholders to identify and address operational bottlenecks, and streamline processes. 
- ► Work with technical teams and campaign stakeholders on software development, improvements, internal tools, and implementation issues.
- ► Provide technical expertise to establish and implement intake processes for EM/SMS campaigns, ensuring compliance with internal policies, regulatory requirements (including CASL), and industry best practices.
- ► Develop clear guidelines and checklists for campaign submissions, set timelines and requirements, covering key elements like content, targeting, approvals, and scheduling. 
- ► Ad-hoc analysis for marketing campaigns to generate insights, improve resources allocation and make recommendations.
- ► Collaborate with cross-functional teams (GTM, Marketing, Data, Devs) to optimize campaign execution and enhance customer experience.
- ► Detect automation opportunities, manage developers' workload, and provide guidance to implement process improvements and best practices.
- ► Utilize Tableau & Domo for data visualization and analysis, and conduct comprehensive data analysis.

"""
)

# --- Exp 2
st.write('\n')
st.subheader("Sr Digital Manager & E-Commerce Developer | JUANITA JO")
st.write("03/2016 to 06/2019")
st.write(
    """
- ► SDLC for B2B and B2C E-Commerce platforms (Prestashop, Wordpress). API integrations.
- ► Test, troubleshoot, and fix front-end and back-end software production issues.
- ► Established benchmarks and implemented robust reporting mechanisms to enhance sales strategy and drive digital initiatives.
- ► Defined and monitored quarterly KPIs aligning with company strategic goals, ensuring measurable performance across business units and conducted recurring market research, employing data analysis and segmentation techniques to identify and prioritize actionable insights.
- ► Reviewed monthly conversion rates, leading strategic planning and execution of improvements to optimize performance.
- ► Led the implementation end-to-end and development of the B2B e-commerce platform project, defining user stories, roadmap, and priorities.
- ► Oversaw all aspects of technical projects and IT initiatives, ensuring timely deliverables within budget and meeting KPIs.
- ► Collaborated with internal and external stakeholders to enhance e-commerce and social presence, contributing to a 20% increase in brand awareness and annual sales during the first year.

"""
)

# --- Exp 3
st.write('\n')
st.subheader("Project Manager & Full-Stack Developer  | BRAINDW")
st.write("08/2014 to 03/2016")
st.write(
    """
- ► Managed and planned the requirements for e-commerce development, with a strategic vision based on user stories.
- ► Cross-functional meetings with developments teams (commercial, designers & developers) for improvements such as usability, performance and commercial strategies.
- ► Software Development Life Cycle (SDLC) process. 
- ► Debugged and troubleshot code, resulting in a 15% reduction in production issues, increasing customer satisfaction.
- ► Added new functionalities (scripts or APIs implementations). 
- ► Used different programming languages: HTML, CSS, PHP, .NET and JavaScript and worked with database systems: MySQL and SQL Server. Version control systems such as Tortoise SVP & GitHub.

"""
)

# --- Projects  --- #
st.write('\n')
st.header("Projects")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")

# --- Education  --- #
st.write('\n')
st.header("Education & Certifications")
st.write("---")
st.write("⦿ Athabasca University, Bachelor of Science, Major in Computing and Information Systems. Expected Graduation Date: May 2026") 
st.write("⦿ Colegio Universitario IES, Graphic Design | 2016-2017, Argentina")
st.write("⦿ Coderhouse, Front End Developer Certificate | 2015, Argentina")
st.write("⦿ Coursera, SQL for Data Science | 2023")
st.write("⦿ Six Sigma Global Institute, Certified Product Owner Scrum Professional (CPOSP) | 2023")