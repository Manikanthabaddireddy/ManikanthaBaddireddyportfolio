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
st.set_page_config(page_title=PAGE_TITLE,page_icon=PAGE_ICON)
with open(resume_file, "rb") as pdf_file:
    pdf = pdf_file.read()
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()),unsafe_allow_html=True)

# write code heree

img=Image.open("dp_mani.png")
I,H=st.columns(2,gap="small")
with H:
    st.header(NAME)
    st.write(POSITION)
    st.write(DESCRIPTION)
    st.download_button(
        label="📄 Download Resume",data=pdf,file_name=resume_file.name,mime="application/octet-stream"
    )
    st.write("📫",EMAIL)
with I:
    st.image(img,width=250)


# social media links added
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
# -- PERSONAL PROJECTS ----
st.write("\n")
st.subheader("PERSONAL 🧍 PROJECTS")
st.write("---")
# --- Porject 1 for web scraping
st.write("Web Scraping with python")
st.write(
    """
- ► Used bs4 and request modules to scrap the data for quotes, it includes attributes like quote,author,bio of author and date of birth and location 
- ► By using this data I have created a guessing game , i will display the quote and player need to tell the author name given four chances and also given hints
"""
)
st.write("<b>Technologies used</b>: Python, request,bs4",unsafe_allow_html=True)

st.write(f"git hub link ({Python})")
# --- project 2 for etl ---
st.write("\n")
st.write("End to End Azure ETL Project")
st.write("""
 - ► Ingesting pipeline for   on-premise ms sql server  data to azure data lake stage layer then to raw layer using azure data factor
 used optimization techniques.
 - ► Spark script for  raw data cleansing then pushed to bronze layer.
 - ► Validations on bronze layer then pushed to silver layer.
 - ► Derived columns and partition the data based on end user requirements then pushed to business layer.
 - ► designed start schema for  dimensional modeling in snowflake.
 - ► Ingesting pipeline from business layer to snowflake data warehouse.
""")
st.write("<b>Technologies used</b>: ADF, pyspark on databricks,azure data lake,snowflake,start schema,dimensional "
         "modeling", unsafe_allow_html=True)

# -- project 3 s3 to snowflake ----
st.write("\n")
st.write("Migrating project from on-premise Mysql to snowflake")
st.write("""
 - ► Reading mysql data in databricks using jdbc, to s3 for staging purposes.After reading the stage data and performing 
     type checks and validation then pushed to the snowflake
 - ► Before that Created integrations for s3 bucket,stage, snowpipe for automating the process through SQS service
 - ► Whenever the data written to s3 then SQS sends the alert then snowpipe runs and copy the data from s3 bucket into 
     snowflake tables
 - ► Created dynamic tables for snowflake tables to build dashboards

""")
st.write("<b><h3>Technologies used</h3></b>: MYSQL, pyspark on databricks,Snowflake,"
         "stages,storage integrations,Snowpipe,Dynamic tables", unsafe_allow_html=True)
