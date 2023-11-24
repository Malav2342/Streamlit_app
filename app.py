import streamlit as st
from PIL import Image
import pandas as pd
import altair as alt


st.snow()
st.title("Malav Joshi")

#elevator Pitch. Your branding
st.subheader("One day there won't be any FEMALE LEADERS, just leaders")


col1, col2= st.columns([3,1])
with col1:
    st. subheader("About Me") 
    st.text("Passionate about the power data to drive insights and\ninnovation, I bring a wealth of Money")
with col2:
    image = Image.open('photo.jpeg')
    st.image(image,width = 250)  

#sidebar w/ Download
st.sidebar.caption('Wish to connect?')
st.sidebar.write('joshimalav0@gmail.com')
#rb means converting pdf file to raw binary format
pdf_file = open('MCVV.pdf', 'rb')
st.sidebar.download_button('Download Resume',pdf_file,file_name='MCVV.pdf',mime='pdf')


#creats tabs
tab_skills,tab_exp,tab_pro,tab_cont,tab_pic = st.tabs(['Skills','Experiene','Projects','Contact Me',"Take a picture"])

#Experience
with tab_exp:
    st.subheader("Relevant Experience")
    experience_table = pd.DataFrame ({
        "Job Title" : ["Member Technical Staff","Software Engineer"],
        "Company" : ["Company A","Company B"],
        "Job Description" : ["Handing Business requirment and client meeting","Implementation and UAT Testing"]
    })
    
    experience_table = experience_table.set_index('Job Title')
    st.table(experience_table)

#projects
with tab_pro:
    st.subheader("Projects")
    titanic_data = pd.read_csv('titanic.csv')
    interval = alt.selection_interval()
    bar_chart = alt.Chart(titanic_data).mark_bar().encode(
        x = 'sum(Survived):Q',
        y = 'Pclass:N',
        color = 'Pclass:N',
    ).properties(
        width = 300
    )
    scatter_plot = alt.Chart(titanic_data).mark_point().encode(
        x = 'Age:Q',
        y = 'Fare:Q',
        color = alt.condition(interval, 'Sex', alt.value('lightgray')),
    ).properties(
        width = 500,
        height = 400
    ).add_selection(
        interval
    ).interactive()
    # Define a selection to filter the scatter plot based on the selected passenger 
    selection = alt.selection_single(fields=['Pclass'], empty = 'none')
    bar_chart = bar_chart.add_selection(selection)
    scatter_plot = scatter_plot.transform_filter(selection)
    #put any jupiter chart in streamlit just add st.altair_chart()
    st.altair_chart(bar_chart | scatter_plot)

#SKILL section - in the form of a bar chqrt
with tab_skills:
    skill_data = pd.DataFrame(
        {
            "Skills Level":[90,60,60,40,75],
            "Skills":["Python","Tableau","Mysql","Rstudio","PowerBI"]
        })
    Skill_data = skill_data.set_index('Skills')
    with st.container():
        st.subheader("Skills")
        st.bar_chart(Skill_data)
    with st.expander("See More Skills"):  
        st.write("I have lots of more skills to such as")

#streamlit form
with tab_cont:
    form = st.form('my_form')
    fullname = form.text_input(label='Enter your Full Name', value='')
    age = st.slider("Select your age")
    gender = st.radio("Select your gender",('Male','Female','Other'))
    message = form.text_area(label="Your message", value='', height=100)
    terms = st.checkbox("Accept terms and condition")     
    submit = form.form_submit_button(label='Submit')          
    #Handle form submission
    if submit:
        if terms:
                st.success('Form completed: Thankyou for visiting')
        else:
            st.error('Please accept the terms and condition')
    st.write("Name",fullname,"Age: ",age,"Gender: ",gender,"Message: ",message)

    #add a map
    # create a data frame with latitude and longitude columns
    data = {
        'Location': ['Kitchener', 'Waterloo', 'Guelph', 'Cambridge'],
        'LAT': [43.451639, 43.464258, 43.5467, 43.3616],
        'LON': [-80.492533, -80.520410, -80.2482, -80.3144]
        }
    df = pd.DataFrame(data)
    st.map(df)


#camera
with tab_pic:
    picture = st.camera_input("Take a picture with me")
    if picture:
        st.image(picture)


#tabs
