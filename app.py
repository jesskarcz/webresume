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

- ► Successfully multitask in the management of diverse Mobility, Home Solutions and Health portfolios, meeting and exceeding expected deadlines.
- ► Development of large-scale automations, customer journeys, and ad-hoc campaigns using Adobe Campaign. This includes template coding (HTML, CSS, JS), data extraction (SAS), and audience segmentation.
- ► Build responsive mobile-first email templates for optimal customer experience across all devices, ensuring consistent rendering through QA testing.
- ► Optimized marketing campaign, increasing customer engagement by 20% through A/B testing and dynamic modules.
- ► Provide technical guidance to GTM and MarComm teams, promoting best practices. 
- ► Identify automation and journey opportunities to minimize churn and customer fatigue.
- ► Conduct comprehensive data analysis using SAS Studio and SQL, extracting actionable insights to enhance marketing strategies.
- ► Partner with GTM, Marketing, Data stakeholders to identify and address operational bottlenecks, streamline processes and to enhance customer experience.

"""
)

# --- Exp 2
st.write('\n')
st.subheader("Sr Digital Manager & E-Commerce Developer | JUANITA JO")
st.write("03/2016 to 06/2019")
st.write(
    """
- ► Managed the SDLC process for B2B and B2C E-Commerce platforms (Prestashop, Wordpress), including API integrations.
- ► Tested, troubleshooted, and fixed front-end and back-end production issues.
- ► Established benchmarks and implemented robust reporting mechanisms to enhance sales strategy and drive digital initiatives.
- ► Defined and monitored quarterly KPIs aligned with company strategic goals.
- ► Reviewed monthly conversion rates, leading strategic planning and execution of improvements to optimize performance.
- ► Led the end-to-end development of a B2B platform, defining user stories, roadmap, and priorities. 
- ► Conducted regular market research to identify actionable insights. Analyzed monthly conversion rates and led strategic planning to optimize platform performance.
- ► Headed the development and execution of email marketing strategies using Salesforce Marketing Cloud, integrated with the e-commerce platform and CRM (Zoho).
- ► Directed internal and external teams (UI/UX & graphic designers, advertising) to boost e-commerce and social presence, resulting in a 20% increase in brand awareness, engagement, and conversions during the first year.
 
"""
)

# --- Exp 3
st.write('\n')
st.subheader("Project Manager & Full-Stack Developer  | BRAINDW")
st.write("08/2014 to 03/2016")
st.write(
    """
- ► Headed meetings with commercial teams, designers, and developers to optimize e-commerce platform usability, performance, and go-to-market strategies.
- ► Applied Software Development Life Cycle (SDLC) process for the requirements for an effective e-commerce development.
- ► Debugged and troubleshooted code, resulting in a 15% reduction in production issues and increased customer satisfaction.
- ► Designed and developed responsive landing pages and e-commerce templates, ensuring optimal user experience across all devices and browsers. 
- ► Implemented new functionalities through scripts or API integrations. 
- ► Utilized HTML, CSS, PHP, .NET, and JavaScript for development. Worked with MySQL and SQL Server databases. Version control systems such as Tortoise SVP & GitHub.


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