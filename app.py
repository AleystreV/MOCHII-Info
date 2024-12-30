import streamlit as st

st.title("MOCHII BALL by The Purposeful Mochii")
st.markdown("Delivering quality CS education to underserved communities through an AI-powered learning app for kids that interprets and executes handwritten code.")
st.video("https://youtu.be/48Ema22zQTo")

tab1, tab2, tab3, tab4, tab5 = st.tabs(["Overview", "Mission/Vision", "Demo", "Contact", "Credits"])

with tab1:
    with st.container(border=True):
        st.header("The Problem")
        st.markdown("The demand for coding skills is on the rise - growing 50% faster than the overall job market. Many Filipino students, however, are unequipped to handle the digital transformation, especially since computer science is not part of our basic education curriculum.")
        st.image("assets/problem-statement.png", caption = "Based on a 2021 report by the Philippine Department of Education, the ratio of computers to learners is as low as 1:19 for public elementary schoolers, and only an average of 67% of public schools have access to the Internet.")
        st.markdown("Considering the additional cost of purchasing, maintaining, and powering computers, it is difficult to imagine how the country might bridge the digital divide for the nearly 24 million Filipino students enrolled in public schools, and maintain its position as one of the world's top outsourcing destinations for BPO and technology.")

    with st.container(border=True):
        st.header("The Solution")
        st.markdown("With MOCHII BALL, schools can deliver quality computer science education - without the need for costly computer equipment or an Internet connection - in three simple steps:")
        st.image("assets/solution.png", caption = "First, students write their code on provided workbooks. Then, teachers take a picture of handwritten code. Finally, students see their code in action on the computer screen.")
        st.markdown("With this, any teacher with a single computer or laptop can successfully teach a computer science class in nearly the same manner as in a lab fully equipped with an Internet connection and a 1:1 student-to-computer ratio.")

    with st.container(border=True):
        st.header("The MOCHII Series")
        st.subheader("MOCHII BALL (Basic Algorithm Learning Language)")
        st.markdown("- Ideal for Gr. 4-6\n- Students solve fun puzzles based on Code.org's Curriculum C\n- Aims to build logical thinking skills and interest in computer science\n- Currently in pilot phase")
        st.subheader("MOCHII PACK (Paper App Creators' Kit)")
        st.markdown("- Ideal for high school and project-based learning\n- Students design their own mobile apps to solve problems in their communities\n- Aims to get kids thinking about applying technology towards social innovation\n- Currently in prototype phase")
        
    with st.container(border=True):
        st.markdown("Click through the other tabs to learn more!")

with tab2:
    with st.container(border=True):
        col1, col2 = st.columns([0.33, 0.66])
        with col1:
            st.image("assets/mission-vision.png")
        with col2:
            st.header("The MOCHII Mission")
            st.markdown("Making quality computer science education accessible to all Filipino youth.")
            st.header("The MOCHII Vision")
            st.markdown("A future generation of digitally empowered citizens with the skills and mindset to harness technology for social innovation.")
    with st.container(border=True):
        st.header("The MOCHII Timeline")
        st.subheader("2024")
        st.markdown("- Prototype of MOCHII BALL completed\n- MOCHII BALL pilot in progress")
        st.subheader("2025")
        st.markdown("- Prototype of MOCHII PACK for high school students completed\n- MOCHII BALL pilot in progress")
        st.subheader("2030")
        st.markdown("- CS education integrated in the Philippine basic education curriculum, using MOCHII educational kits to bridge the digital divide")
        st.subheader("2035")
        st.markdown("- MOCHII K-12 curriculum completed")
        st.subheader("2040")
        st.markdown("- Digitally skilled graduates\n- Increase in Computer Science graduates\n- Improved PISA scores\n- A generation of skilled social innovators")
        st.markdown('''
            <style>
            [data-testid="stMarkdownContainer"] ul{
                list-style-position: inside;
            }
            </style>
        ''', unsafe_allow_html=True)

with tab3:
    st.video("assets/demo.mp4", loop=True, autoplay=True)
    st.caption("A screen recording of MOCHII BALL in action.")
    
with tab4:
    st.markdown("Learn more and/or reach out through my Facebook page:")
    st.link_button("The Purposeful Mochii - Mobilizing Children to Harness Information for Innovation", "https://www.facebook.com/purposefulmochii")

with tab5:
    st.subheader("Graphics")
    st.markdown("Graphics created using assets from Canva.")
    st.subheader("Research")
    st.markdown("- https://www.deped.gov.ph/wp-content/uploads/2022/04/DepEd-Databits-Functional-Computers-and-Internet-Connectivity-4.pdf")
    st.markdown("- https://burning-glass.com/research/coding-skills/")
    st.markdown("- https://www.philstar.com/headlines/2023/08/16/2288980/over-28-million-students-expected-school-year")
