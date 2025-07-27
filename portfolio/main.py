print("Shiv hi satya hai")

import streamlit as st

st.set_page_config(page_title="Rajsingh Sendhav | Portfolio", layout = "wide")

st.markdown("""
    <style>
            html, body , [  class*="css"]  
            { front-family: 'Segoe UI', Calibri, Lato,sans - serif; }
    </style> """, 
    unsafe_allow_html=True ) 

with st.container():
    st.markdown("<br><br>", unsafe_allow_html=True)  # Spacer

    st.markdown("<h1 style='text-align: center; font-size: 48px; color: #111;'>Rajsingh Sendhav</h1>", unsafe_allow_html=True)

    st.markdown("<h1 style='text-align: center; font-size: 35px; color: #111;'>Aspiring Data Analyst | Turning Raw Data into Business Intelligence </h1>", unsafe_allow_html=True)

    st.markdown("""
        <p style='text-align: center; font-size: 20px; color: #444; max-width: 800px; margin: auto;'>
            A passionate and job-ready Data Analyst who turns raw data into real business decisions.
            I specialize in cleaning messy datasets, uncovering insights, and building dashboards that help teams take action. With tools like Python, Power BI, and SQL, I focus on delivering clarity, not just charts.
                If it doesn't solve a real problem — I don’t build it.
        </p>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)


# Step 2: About Me Section
with st.container():
    st.markdown("<br><hr><br>", unsafe_allow_html=True)  # Section divider

    # 3 Feature Columns
    st.markdown("## 🦾 Skills")
    col1, col2, col3 , col4 = st.columns(4)

    with col1:
        st.markdown("""
            <div style='background-color: #ffffff; border: 1px solid #eee; border-radius: 12px; padding: 24px; text-align: center;'>
                <div style='font-size: 36px;'>📊</div>
                <h4 style='margin-top: 10px;'>Data Analysis</h4>
                <p style='color: #555; font-size: 18px;'>Skilled in transforming raw data into actionable insights through cleaning, exploration, and visualization.</p>
            </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
            <div style='background-color: #ffffff; border: 1px solid #eee; border-radius: 12px; padding: 24px; text-align: center;'>
                <div style='font-size: 36px;'>📈</div>
                <h4 style='margin-top: 10px;'>Dashboard Creation</h4>
                <p style='color: #555; font-size: 18px;'>Experienced in building clean, executive-level dashboards using Power BI for strategic decision-making.</p>
            </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
            <div style='background-color: #ffffff; border: 1px solid #eee; border-radius: 12px; padding: 24px; text-align: center;'>
                <div style='font-size: 36px;'>💡</div>
                <h4 style='margin-top: 10px;'>Business Insights</h4>
                <p style='color: #555; font-size: 18px;'>Focused on delivering insights that solve business problems and drive growth using real-world datasets effectively always.</p>
            </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown("""
            <div style="display: inline-block; width: 280px; background-color: #fff; border: 1px solid #eee; border-radius: 12px; padding: 24px; margin-right: 16px; text-align: center;">
                <div style='font-size: 36px;'>🗣</div>
                <h4>Data Storytelling</h4>
                <p style='font-size: 18px; color: #555;'>
                Strong presentation & communication skills.Use Power BI dashboards to explain insights drive decisions
                </p>
            </div>
        """, unsafe_allow_html=True)


with st.container(border=False):
    st.markdown("<br><hr><br>", unsafe_allow_html=True)
    st.markdown("## 📁 Projects")

    st.markdown("""
    <p style='font-size: 18px; text-align: justify;'>            
    These projects demonstrate my ability to clean, analyze, and visualize real-world datasets to drive business insights.<br>
    Each project is structured like a real case study — with a clear problem, step-by-step process, and impact-focused recommendations.
    </p>
    """, unsafe_allow_html=True)


# Title or preview section
st.markdown("<br>", unsafe_allow_html=True)

with st.container(border=False):
    st.markdown("""
    <div style='background-color: #f9f9f9; padding: 28px 32px; border-radius: 12px;'>
        <h4>📦 Amazon Product Strategy Analysis</h4>
        <p style='font-size: 18px; text-align: justify;'>        
        <strong>Tools:</strong> Python (pandas, TextBlob), Power BI, Excel<br>
        <strong>Link: </strong><a href='https://github.com/Rajsingh321/Amazon-Product-Review-Sentiment-Analysis' target='_blank'> GitHub</a></p>
        <ul style='line-height: 1.8;'>
            <li style='font-size: 17px; text-align: justify;'>    
            <strong>Analyzed</strong> 6,000+ products using sentiment scoring and correlation analysis to uncover promotional winners and risky products.<br>
            <strong>Built</strong> Power BI dashboards showing how reviews, ratings, and discounts impact product trust and sales outcomes.<br>
            <strong>Discovered</strong> that discounts had no impact on ratings; helped shift strategy to quality-first decisions based on customer sentiment.<br>
            </li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# Styled button 
st.markdown("""
<div style='text-align: left; margin-top: 12px;'>
    <a href='https://amazon-appuct-review-sentiment-analysis-2rutwv7qxyz9rldyczwlfu.streamlit.app/' target='_blank'>
        <button style='padding: 12px 24px; font-size: 16px; background-color: #2563eb; color: white; border: none; border-radius: 8px;'>
            🐱‍🏍 It's Live
        </button>
    </a>
</div>
""", unsafe_allow_html=True)
    
st.markdown("<br>", unsafe_allow_html=True)

# Flipkart Project Preview Card
with st.container(border=False):
    st.markdown("""
    <div style='background-color: #f6f6f6; padding: 20px 24px; border-radius: 12px;'>
        <h4>🛒 Flipkart Sales & Profitability Dashboard</h4>
        <p style='font-size: 18px; text-align: justify;'>
        <strong>Tools:</strong> Python (pandas), Power BI, Excel<br>
        <strong>Link: </strong><a href='https://github.com/Rajsingh321/Flipkart-Sales-Profitability-Analysis.git' target='_blank'> GitHub</a></p>
        <ul style='line-height: 1.8;'>
            <li style='font-size: 17px; text-align: justify;'>    
            <strong>Processed</strong> 38,000+ orders to detect revenue leaks, seasonal patterns, and pricing risks across Flipkart product lines.<br>
            <strong>Identified</strong> 20+ SKUs with margins below -270% and showed that Technology drives 47% of total profits.<br>
            <strong>Created</strong> an executive Power BI dashboard to help business teams cap discounts at 30% and optimize product/category strategies.<br>
            </li>
        </ul>
    </div>

    """, unsafe_allow_html=True)

# Button logic to reveal Flipkart full case study
st.markdown("""
<div style='text-align: left; margin-top: 12px;'>
    <a href='https://flipkart-sales-profitability-analysis-8zkmgspzcvdfevavhu4py8.streamlit.app/' target='_blank'>
        <button style='padding: 12px 24px; font-size: 16px; background-color: #2563eb; color: white; border: none; border-radius: 8px;'>
            🐱‍🏍 It's Live
        </button>
    </a>
</div>

    """, unsafe_allow_html=True)

with st.container(border=False):
    st.markdown("## 🧰 Tools & Technologies Used")
    st.markdown("""
<div style='background-color:#f9f9f9; padding: 20px 28px; border-radius: 12px;'>
  <ul style='font-size: 20px; color: #333; line-height: 1.8;'>
    <li style='font-size: 18px; text-align: justify;'>            
    <strong>Programming:</strong> Python (Pandas, NumPy)<br>
    <strong>Visualization:</strong> Power BI, Excel<br>
    <strong>Data Handling:</strong> CSV, Excel, Web Scraping<br>
    <strong>Soft Skills:</strong> Data Storytelling, Business Insight Thinking, Communication<br>
    </li>
  </ul>
</div>
""", unsafe_allow_html=True)
    
with st.container(border=False):
    st.markdown("## 📬 Contact & Links")
    st.markdown("""
           
<div style='background-color:#f9f9f9; padding: 24px 28px; border-radius: 12px;'>
  <p style='font-size:20px; color:#333;'>Feel free to connect or reach out for collaborations, projects, or opportunities.</p>

  <ul style='font-size: 16px; color: #444; line-height: 1.8;'>            
    <li style='font-size: 18px; text-align: justify;'>
    📧 <strong>Email:</strong> <a href="mailto:rajbgi377@gmail.com">rajbgi377@gmail.com</a><br>
    💼 <strong>LinkedIn:</strong> <a href="https://www.linkedin.com/in/rajsinghsendhav" target="_blank">linkedin.com/in/rajsinghsendhav</a><br>
    💻 <strong>GitHub:</strong> <a href="https://github.com/Rajsingh321" target="_blank">github.com/Rajsingh321</a><br>
    </li>           
  </ul>                
</div>
""", unsafe_allow_html=True)    
