import streamlit as st
from pathlib import Path 
from PIL import Image
import streamlit.components.v1 as components

# Path settings
curr_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = curr_dir / 'styles' / 'styles\main.css'
resume_file = curr_dir / 'assets' / 'assets\Maxwell Ogunsanya - CV.pdf'
avi = curr_dir / 'images' / 'Images\pfp.png'


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Portfolio"
PAGE_ICON = ":robot:"
NAME = "Maxwell Ogunsanya"
DESCRIPTION = """
Computer Science Graduate, creating custom software solutions.
"""
EMAIL = "maxwellogunsanya@email.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/maxwellogunsanya/",
    "GitHub": "https://github.com/CassDabii",
}
PROJECTS = {
    "✔️ Design Document Maker - Makes use of NLP to aid in the generation of design documnets:": "https://cassadoc.streamlit.app/",
    "⌛ CassaLog - A trading journal that will use ML to give detailed insights into trading habits":"",
    "⌛ CassaBot - An alternate UI for the Open assistant AI":"",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
avi = Image.open(avi)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(avi, width=230)
with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")



# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python, SQL, Java
- 📊 Data Visulization: PowerBi, MS Excel, Plotly
- 📚 Modeling: Logistic regression, linear regression, decition trees
- 🗄️ Databases: Postgres, MongoDB, MySQL, NoSQL
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("👨‍💻", "**Founder | CassaCorp**")
st.write("11/2022 - Present")
st.write(
    """
- ► Created 3 successful software products within the first year of operations, resulting in an £1000 investment by effectively managing all aspects of software
development, from planning to deployment.
- ► Reduced project development time by 30% by implementing revised agile methodologies for individual projects, resulting in faster time-to-market and
increased customer satisfaction.
- ► Developed a strategic plan that resulted in a 50% increase in client base and led to the expansion of the company's services by leveraging networking and
marketing skills to establish new business relationships and promote the company's services.
"""
)

# --- JOB 2
st.write('\n')
st.write("🥡", "**Runner | THE RIVER CAFE**")
st.write("07/2021 - 01/2022")
st.write(
    """
- ► Achieved an average rating of 4.8 out of 5 stars on customer reviews by providing exceptional service to guests.
- ► Increased table turnover rate by 20% by implementing efficient table clearance and ordering processes, resulting in increased revenue for the restaurant.
- ► Trained and mentored new staff members, resulting in improved overall service quality and a more cohesive team environment which netted me employee
awards on two separate occasions.
"""
)

# --- JOB 3
st.write('\n')
st.write("💻", "**Junior Web Developer | Start Smart London**")
st.write("06/2019 - 03/2020")
st.write(
    """
- ► Increased website traffic by 50% and reduced bounce rate by 25% by implementing a comprehensive redesign that prioritized user experience and consistent
branding.
- ► Incorporated relevant resources and updated content regularly, resulting in a 40% increase in student engagement and a 90% satisfaction rate among
students and faculty.
- ► Developed and implemented a hands-on approach to learning HTML, CSS, and JavaScript, resulting in a 40% improvement in student performance and
positive feedback from supervisors.
"""
)


# --- Projects ---
st.write('\n')
st.subheader("Projects on the way")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")



st.subheader(" Contact Me")


contact_form = """
        <form action="https://formsubmit.co/maxwellogunsanya@gmail.com" method="POST">
            <input type="hidden" name="_captcha" value="false">
            <input type="text" name="name" placeholder="Your name" required>
            <input type="email" name="email" placeholder="Your email" required>
            <textarea name="message" placeholder="Your message here"></textarea>
            <button type="submit">Send</button>
        </form>
        """

st.markdown(contact_form, unsafe_allow_html=True)

# Use Local CSS File
def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("styles\contactme.css")
