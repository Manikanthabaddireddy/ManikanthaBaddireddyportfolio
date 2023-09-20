# import all the nessasary modules
import streamlit as st
from PIL import Image
from pathlib import Path
from assets.configs import *
#path settings
from pathlib import Path


#file_path=r"C:\Users\manib\OneDrive\Desktop\ManikanthaBaddireddyportfolio\assets\Manikantha_AzureDataEnginner .pdf"
cur_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
resume_file = cur_dir /  "Manikantha_AzureDataEnginner .pdf"
css_file=cur_dir/ "styles" / "main.css"
# Read the PDF file
with open(resume_file, "rb") as pdf_file:
    pdf = pdf_file.read()
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()),unsafe_allow_html=True)

# write code heree
# st.set_page_config(page_title=PAGE_TITLE,page_icon=PAGE_ICON)
img=Image.open("Mani.png")
H,I=st.columns([2,1])
with H:
    st.header(NAME)
    st.write(POSITION)
    st.write(DESCRIPTION)
    st.download_button(
        label="📄 Download Resume",data=pdf,file_name=resume_file.name,mime="application/octet-stream"
    )
    st.write("📫",EMAIL)
with I:
    st.image(img,width=50)


# social media links
col=st.columns(len(SOCIAL_MEDIA))
for index,(platform,link) in enumerate(SOCIAL_MEDIA.items()):
    col[index].write(f"[{platform}]({link})")

# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qulifications")
st.write(''' 
- ✔️ 1+ Years expereince making quality data from raw data.
- ✔️ Maintained Data integrity while Data ingestion and transformation layers.
- ✔️ Strong hands on experience and knowledge in Python and SQL.
- ✔️ Good understanding of Data modeling and Dimensional Modeling.
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks.


''')

# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
 - 👩‍💻 Languages: Python(pandas,python-mysql-connector,streamlit), SQL
 - 📊 Data Visulization: PowerBi basics
 - 📚 Modeling: Data Modeling, Dimensional Modeling
 - 🗄️ Databases: MS SQL SERVER, CASSANDRA, MySQL
 - ⚙️ Tools: ❄️Snowflake,Spark,DataBricks
 - 🌨️ Cloud Providers: Azure,AWS
"""
)
# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
# --- JOB 1
st.write("🚧", "**Data Engineer @ Achyutas Soft **")
st.write("10/2022 - Present")
st.write(
    """
- ► Designed pipelines for data ingestion from on-premise to azure data lake.
- ► Used databricks for creating notebooks for data quality and data integrity.
- ► Team member responsible for archiving raw data.
- ► Resposable for ingesting data from azure data lake to snowflake by creating integrations,stages,pipes.
"""
)

