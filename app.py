import streamlit as st

# Title of the web app
st.title("Smart Resume Generator")

# Input fields for the user
name = st.text_input("Full Name")
email = st.text_input("Email Address")
phone = st.text_input("Phone Number")
linkedin = st.text_input("LinkedIn Profile")
github = st.text_input("GitHub Profile")
summary = st.text_area("Professional Summary")
skills = st.text_area("Skills (comma separated)")
experience = st.text_area("Work Experience")
education = st.text_area("Education")
certifications = st.text_area("Certifications")

# Generate Resume button
if st.button("Generate Resume"):
    if name and email and phone and summary and skills and experience and education:
        # Create a resume template
        resume = f"""
        ============================================
                            RESUME
        ============================================
        
        Name: {name}
        Email: {email}
        Phone: {phone}
        LinkedIn: {linkedin}
        GitHub: {github}
        
        ============================================
                        SUMMARY
        ============================================
        
        {summary}
        
        ============================================
                        SKILLS
        ============================================
        
        {skills}
        
        ============================================
                    WORK EXPERIENCE
        ============================================
        
        {experience}
        
        ============================================
                        EDUCATION
        ============================================
        
        {education}
        
        ============================================
                    CERTIFICATIONS
        ============================================
        
        {certifications}
        """
        
        # Display the generated resume
        st.text_area("Generated Resume", resume, height=500)
        
        # Option to download the resume as a text file
        st.download_button(
            label="Download Resume",
            data=resume,
            file_name=f"{name}_resume.txt",
            mime="text/plain"
        )
    else:
        st.error("Please fill in all the required fields.")