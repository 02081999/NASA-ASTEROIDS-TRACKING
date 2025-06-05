#Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
#.\env\Scripts\Activate.ps1

import streamlit as st
import pandas as pd
import pymysql
from datetime import date

#connecting to the Mysql database 

connection= pymysql.connect( host="localhost",user="root",password="Ishu@0208",database="nasa_neo_project")
cursor=connection.cursor()

#importing menu options
from streamlit_option_menu import option_menu

with st.sidebar:
    st.markdown("""
      <h1 style='text-align: center;'>▶ASTEROID APPROACHES◀</h1>
    """,unsafe_allow_html=True)

    selected = option_menu("Main Menu", ['Home','Filter criteria', 'Queries'], 
        icons=['house','paperclip', 'gear'], menu_icon="cast", default_index=1)
#home page info   
if selected == "Home":    
    #background image setting
    st.markdown("""
    <style>
    .stApp {
        background-image: url("https://images.unsplash.com/photo-1503264116251-35a269479413");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
        }    
    </style>
    """,unsafe_allow_html=True)
    #home page title
    st.markdown("""
            <h1 style='background-color:white;text-align:center;'>NASA NEAR EARTH OBJECT(NEO) TRACKING AND INSIGHTS USING PUBLIC API</h1>"
    """,unsafe_allow_html=True)
    #divsion info
    st.markdown("""
     <div style="
        background-color: rgba(0, 0, 0, 0.5);
        border: 5px solid;
        width: 100%;
        padding: 80px;
        margin: auto;
        margin-top: 1px;
        border-radius: 10px;
        color: white;
        text-align:left;
        box-shadow: 0px 4px 12px rgba(0, 255, 170, 0.5);
    ">        
        <h5> 
        NASA’s Near-Earth Object (NEO) tracking system plays a critical role in monitoring asteroids and comets that come close to Earth's orbit.
        Through its efforts, NASA aims to assess the potential risks posed by these objects and provide early warnings in case any pose a threat to our planet.
        One of the most powerful tools for public access to this data is the NASA NEO Web Service (NeoWs)—a freely available RESTful API that enables developers, researchers, and enthusiasts to explore and analyze information on NEOs in real time. 
        </h5>
        <h5>    
        NASA’s open data initiative and provides detailed information on thousands of NEOs.
        These include their names, estimated sizes, orbital parameters, velocity, closest approach distances, and whether they are classified as potentially hazardous. 
        The data originates from multiple observational programs and is continually updated as new NEOs are discovered or existing ones are reanalyzed.
        </h5>
        <h5>
        The API is structured into several endpoints to serve different data needs.
        For example, allows users to retrieve a list of NEOs that are expected to pass near Earth within a given date range.
        This is particularly useful for those who want to analyze daily or weekly activity. 
        </h5>
        <h5>
        A particularly useful feature of the NeoWs API is the inclusion of estimated diameters and miss distances, both expressed in multiple units (meters, kilometers, lunar distances, astronomical units, etc.).
        This flexibility helps developers create visualizations and interfaces that are easy for both experts and the general public to understand. 
        The API also flags whether a NEO is considered potentially hazardous, which is determined based on its size and how closely it approaches Earth.
        </h5>
        <h5>
        Developers can use this data to build applications for public education, academic research, or even real-time tracking dashboards.
        For example, one could create a Streamlit web app that visualizes NEOs approaching Earth in the next 7 days, plotting their trajectories, sizes, and closest approach distances. 
        Others might use the API data to perform statistical analyses of how many hazardous objects have been detected over time or to model the frequency of close approaches by object size.
        The public API makes this effort transparent and encourages collaborative innovation.
        </h5>        
     </div>
     """,
     unsafe_allow_html=True)             

#queries menu
elif selected == 'Queries':  
   
    st.markdown(
    """
    <h1 style='text-align: center;'>NEAR-EARTH OBJECT DATA EXPLORER⌕</h1>
    """,
    unsafe_allow_html=True)

    #queries list
    options = st.selectbox("QUERIES LIST",["1. Count how many times each asteroid has approached Earth",
                                      "2. Average velocity of each asteroid over multiple approaches""",
                                      "3. List top 10 fastest asteroids",
                                      "4. Find potentially hazardous asteroids that have approached Earth more than 3 times",
                                      "5. Find the month with the most asteroid approaches",
                                      "6. Get the asteroid with the fastest ever approach speed",
                                      "7. Sort asteroids by maximum estimated diameter (descending)",
                                      "8. An asteroid whose closest approach is getting nearer over time(Hint: Use ORDER BY close_approach_date and look at miss_distance).",
                                      "9. Display the name of each asteroid along with the date and miss distance of its closest approach to Earth.",
                                      "10. List names of asteroids that approached Earth with velocity > 50,000 km/h",
                                      "11. Count how many approaches happened per month",
                                      "12. Find asteroid with the highest brightness (lowest magnitude value)",
                                      "13. Get number of hazardous vs non-hazardous asteroids",
                                      "14. Find asteroids that passed closer than the Moon (lesser than 1 LD), along with their close approach date and distance.",
                                      "15. Find asteroids that came within 0.05 AU(astronomical distance)",
                                      "16. Display all the details of asteroids",
                                      "17. Display all the details of close_approach",                                                      
                                      "18. Details of asteroids which approached on 2025-01-04",
                                      "19. List name of the non hazardous_asteroid along with their absolute_magnitude_h",
                                      "20. Name asteroids and their velocity by sorting lunar distance which is greater between 61 and 99",
                                      "21. List asteroids approached date when asteroids is hazardous",
                                      "22. Count how many approaches happened per day",
                                      "23. Display the date which has highest approached count",
                                      "24. List asteriods which approaches between'2024-05-13' and '2024-08-03",
                                      ],placeholder='Pick an Option..',index=None)     
    
    
    if options== "1. Count how many times each asteroid has approached Earth":
         st.markdown("""
        <h3>🛒QUERY: Count how many times each asteroid has approached Earth</h3>
        """,
        unsafe_allow_html=True)
         st.markdown("""
        <h5>╰┈➤The results will be:</h5>
        """,
        unsafe_allow_html=True)
         
         cursor.execute("""
              select neo_reference_id, count(*) as approach_count from close_approach where orbiting_body='Earth' group by neo_reference_id        
        """)

         result = cursor.fetchall()
         columns = [desc[0] for desc in cursor.description]
         data = pd.DataFrame(result, columns=columns)
         st.dataframe(data)

    elif options== "2. Average velocity of each asteroid over multiple approaches":
         st.markdown("""
        <h3>🛒QUERY: Average velocity of each asteroid over multiple approaches</h3>
        """,
        unsafe_allow_html=True)
         st.markdown("""
        <h5>╰┈➤The results will be:</h5>
        """,
        unsafe_allow_html=True)
         cursor.execute("""
              select neo_reference_id, avg(relative_velocity_kmph) as average_velocity from close_approach group by neo_reference_id
        """)
         result = cursor.fetchall()
         columns = [desc[0] for desc in cursor.description]
         data = pd.DataFrame(result, columns=columns)
         st.dataframe(data)

    elif options== "3. List top 10 fastest asteroids":

        st.markdown("""
        <h3>🛒QUERY: List top 10 fastest asteroids</h3>
        """,
        unsafe_allow_html=True)
        st.markdown("""
        <h5>╰┈➤The results will be:</h5>
        """,
        unsafe_allow_html=True)

        cursor.execute("""
              select distinct a.id,a.name,c.relative_velocity_kmph from close_approach as c join asteroids as a on c.neo_reference_id = a.id where c.orbiting_body = 'Earth' order by c.relative_velocity_kmph desc limit 10
        """)
        result = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        data = pd.DataFrame(result, columns=columns)
        st.dataframe(data)   

    elif options== "4. Find potentially hazardous asteroids that have approached Earth more than 3 times":

        st.markdown("""
        <h3>🛒QUERY: Find potentially hazardous asteroids that have approached Earth more than 3 times</h3>
        """,
        unsafe_allow_html=True)
        st.markdown("""
        <h5>╰┈➤The results will be:</h5>
        """,
        unsafe_allow_html=True)

        cursor.execute("""
              select a.id,a.name from asteroids as a join close_approach as c on a.id = c.neo_reference_id where a.is_potentially_hazardous_asteroid = true and c.orbiting_body = 'Earth' group by a.id, a.name having COUNT(c.neo_reference_id) > 3 
        """)
        result = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        data = pd.DataFrame(result, columns=columns)
        st.dataframe(data) 

    elif options== "5. Find the month with the most asteroid approaches":

        st.markdown("""
        <h3>🛒QUERY: Find the month with the most asteroid approaches</h3>
        """,
        unsafe_allow_html=True)
        st.markdown("""
        <h5>╰┈➤The results will be:</h5>
        """,
        unsafe_allow_html=True)

        cursor.execute("""
               select MONTHNAME(close_approach_date) as asteroid_approach_month,count(*) as total_approaches from close_approach group by MONTHNAME(close_approach_date) order by total_approaches desc limit 1
        """)
        result = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        data = pd.DataFrame(result, columns=columns)
        st.dataframe(data) 

    elif options== "6. Get the asteroid with the fastest ever approach speed":

        st.markdown("""
        <h3>🛒QUERY: Get the asteroid with the fastest ever approach speed</h3>
        """,
        unsafe_allow_html=True)
        st.markdown("""
        <h5>╰┈➤The results will be:</h5>
        """,
        unsafe_allow_html=True)

        cursor.execute("""
               select a.id,a.name,c.relative_velocity_kmph from asteroids as a join close_approach as c on c.neo_reference_id = a.id  order by c.relative_velocity_kmph desc limit 1
        """)
        result = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        data = pd.DataFrame(result, columns=columns)
        st.dataframe(data) 

    elif options== "7. Sort asteroids by maximum estimated diameter (descending)":
        
        st.markdown("""
        <h3>🛒QUERY: Sort asteroids by maximum estimated diameter (descending)</h3>
        """,
        unsafe_allow_html=True)
        st.markdown("""
        <h5>╰┈➤The results will be:</h5>
        """,
        unsafe_allow_html=True)
    
        cursor.execute("""
               select id,name,estimated_diameter_max_km from asteroids order by estimated_diameter_max_km DESC
        """)
        result = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        data = pd.DataFrame(result, columns=columns)
        st.dataframe(data) 

    elif options== "8. An asteroid whose closest approach is getting nearer over time(Hint: Use ORDER BY close_approach_date and look at miss_distance).":
        
        st.markdown("""
        <h3>🛒QUERY: An asteroid whose closest approach is getting nearer over time(Hint: Use ORDER BY close_approach_date and look at miss_distance).</h3>
        """,
        unsafe_allow_html=True)
        st.markdown("""
        <h5>╰┈➤The results will be:</h5>
        """,
        unsafe_allow_html=True)

        cursor.execute("""
              select a.id,a.name,c.miss_distance_km from  close_approach as c join asteroids as a on c.neo_reference_id = a.id  order by close_approach_date,miss_distance_km desc limit 10
        """)
        result = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        data = pd.DataFrame(result, columns=columns)
        st.dataframe(data) 

    elif options== "9. Display the name of each asteroid along with the date and miss distance of its closest approach to Earth.":
        
        st.markdown("""
        <h3>🛒QUERY: Display the name of each asteroid along with the date and miss distance of its closest approach to Earth.</h3>
        """,
        unsafe_allow_html=True)
        st.markdown("""
        <h5>╰┈➤The results will be:</h5>
        """,
        unsafe_allow_html=True)

        cursor.execute("""
               select c.neo_reference_id,a.name,c.miss_distance_km,c.close_approach_date from close_approach as c join asteroids as a on c.neo_reference_id = a.id order by close_approach_date,miss_distance_km desc limit 1
        """)
        result = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        data = pd.DataFrame(result, columns=columns)
        st.dataframe(data) 

    elif options== "10. List names of asteroids that approached Earth with velocity > 50,000 km/h":
        
        st.markdown("""
        <h3>🛒QUERY: List names of asteroids that approached Earth with velocity > 50,000 km/h</h3>
        """,
        unsafe_allow_html=True)
        st.markdown("""
        <h5>╰┈➤The results will be:</h5>
        """,
        unsafe_allow_html=True)

        cursor.execute("""
               select distinct a.name, c.relative_velocity_kmph from close_approach as c join asteroids as a on c.neo_reference_id = a.id where c.relative_velocity_kmph > 50000 order by  c.relative_velocity_kmph asc
        """)
        result = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        data = pd.DataFrame(result, columns=columns)
        st.dataframe(data) 

    elif options== "11. Count how many approaches happened per month":
        
        st.markdown("""List
        <h3>🛒QUERY:  Count how many approaches happened per month</h3>
        """,
        unsafe_allow_html=True)
        st.markdown("""
        <h5>╰┈➤The results will be:</h5>
        """,
        unsafe_allow_html=True)

        cursor.execute("""
               select MONTHNAME(close_approach_date) as approach_month,COUNT(*) AS total_approaches from close_approach group by MONTH(close_approach_date), MONTHNAME(close_approach_date) order by approach_month
        """)
        result = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        data = pd.DataFrame(result, columns=columns)
        st.dataframe(data) 

    elif options== "12. Find asteroid with the highest brightness (lowest magnitude value)":
        
        st.markdown("""List
        <h3>🛒QUERY:  Find asteroid with the highest brightness (lowest magnitude value)</h3>
        """,
        unsafe_allow_html=True)
        st.markdown("""
        <h5>╰┈➤The results will be:</h5>
        """,
        unsafe_allow_html=True)

        cursor.execute("""
               select id,name,absolute_magnitude_h from asteroids order by absolute_magnitude_h ASC limit 1
        """)
        result = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        data = pd.DataFrame(result, columns=columns)
        st.dataframe(data) 

    elif options== "13. Get number of hazardous vs non-hazardous asteroids":
        
        st.markdown("""List
        <h3>🛒QUERY:  Get number of hazardous vs non-hazardous asteroids</h3>
        """,
        unsafe_allow_html=True)
        st.markdown("""
        <h5>╰┈➤The results will be:</h5>
        """,
        unsafe_allow_html=True)

        cursor.execute("""
               select is_potentially_hazardous_asteroid as hazardous,COUNT(*) AS total from asteroids group by is_potentially_hazardous_asteroid
        """)
        result = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        data = pd.DataFrame(result, columns=columns)
        st.dataframe(data) 

    elif options== "14. Find asteroids that passed closer than the Moon (lesser than 1 LD), along with their close approach date and distance.":
        
        st.markdown("""
        <h3>🛒QUERY:  Find asteroids that passed closer than the Moon (lesser than 1 LD), along with their close approach date and distance.</h3>
        """,
        unsafe_allow_html=True)
        st.markdown("""
        <h5>╰┈➤The results will be:</h5>
        """,
        unsafe_allow_html=True)

        cursor.execute("""
               select distinct a.name,c.close_approach_date,c.miss_distance_lunar from close_approach as c join asteroids as a on c.neo_reference_id = a.id where c.miss_distance_lunar < 1  order by c.miss_distance_lunar ASC
        """)
        result = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        data = pd.DataFrame(result, columns=columns)
        st.dataframe(data) 

    
    elif options== "15. Find asteroids that came within 0.05 AU(astronomical distance)":
        
        st.markdown("""
        <h3>🛒QUERY: Find asteroids that came within 0.05 AU(astronomical distance)</h3>
        """,
        unsafe_allow_html=True)
        st.markdown("""
        <h5>╰┈➤The results will be:</h5>
        """,
        unsafe_allow_html=True)


        cursor.execute("""
              select distinct a.name,c.close_approach_date,c.astronomical as miss_distance_au from close_approach as c join asteroids as a on c.neo_reference_id = a.id where c.astronomical < 0.05 order by c.astronomical ASC 
        """)
        result = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        data = pd.DataFrame(result, columns=columns)
        st.dataframe(data)


    elif options== "16. Display all the details of asteroids":
        
        st.markdown("""
        <h3>🛒QUERY: Display all the details of asteroids</h3>
        """,
        unsafe_allow_html=True)
        st.markdown("""
        <h5>╰┈➤The results will be:</h5>
        """,
        unsafe_allow_html=True)

        cursor.execute("""
               select * from asteroids
        """)
        result = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        data = pd.DataFrame(result, columns=columns)
        st.dataframe(data)


    elif options== "17. Display all the details of close_approach":
        
        st.markdown("""
        <h3>🛒QUERY:  Display all the details of close_approach</h3>
        """,
        unsafe_allow_html=True)
        st.markdown("""
        <h5>╰┈➤The results will be:</h5>
        """,
        unsafe_allow_html=True)

        cursor.execute("""
               select * from close_approach
        """)
        result = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        data = pd.DataFrame(result, columns=columns)
        st.dataframe(data) 

    elif options== "18. Details of asteroids which approached on 2025-01-04":
        
        st.markdown("""
        <h3>🛒QUERY:  Details of asteroids which approached on 2025-01-04</h3>
        """,
        unsafe_allow_html=True)
        st.markdown("""
        <h5>╰┈➤The results will be:</h5>
        """,
        unsafe_allow_html=True)

        cursor.execute("""
               select * from close_approach where close_approach_date='2025-01-04'                
        """)
        result = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        data = pd.DataFrame(result, columns=columns)
        st.dataframe(data) 

    elif options== "19. List name of the non hazardous_asteroid along with their absolute_magnitude_h":
        
        st.markdown("""
        <h3>🛒QUERY:  List name of the non hazardous_asteroid along with their absolute_magnitude_h</h3>
        """,
        unsafe_allow_html=True)
        st.markdown("""
        <h5>╰┈➤The results will be:</h5>
        """,
        unsafe_allow_html=True)

        cursor.execute("""
               select name,absolute_magnitude_h from asteroids where is_potentially_hazardous_asteroid= false
        """)
        result = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        data = pd.DataFrame(result, columns=columns)
        st.dataframe(data) 

    elif options== "20. Name asteroids and their velocity by sorting lunar distance which is greater between 61 and 99":
        
        st.markdown("""
        <h3>🛒QUERY:  Name asteroids and their velocity by sorting lunar distance which is greater between 61 and 99</h3>
        """,
        unsafe_allow_html=True)
        st.markdown("""
        <h5>╰┈➤The results will be:</h5>
        """,
        unsafe_allow_html=True)

        cursor.execute("""
               select distinct a.name,c.relative_velocity_kmph,c.miss_distance_lunar from close_approach as c join asteroids as a on c.neo_reference_id=a.id where miss_distance_lunar  between 61 and 99 order by miss_distance_lunar asc
        """)
        result = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        data = pd.DataFrame(result, columns=columns)
        st.dataframe(data) 

    elif options== "21. List asteroids approached date when asteroids is hazardous":
        
        st.markdown("""
        <h3>🛒QUERY:  List asteroids approached date when asteroids is hazardous</h3>
        """,
        unsafe_allow_html=True)
        st.markdown("""
        <h5>╰┈➤The results will be:</h5>
        """,
        unsafe_allow_html=True)

        cursor.execute("""
               select distinct a.name,c.close_approach_date from asteroids as a join close_approach as c on a.id=c.neo_reference_id where is_potentially_hazardous_asteroid=true
        """)
        result = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        data = pd.DataFrame(result, columns=columns)
        st.dataframe(data) 

    elif options== "22. Count how many approaches happened per day":
        
        st.markdown("""
        <h3>🛒QUERY:  Count how many approaches happened per day</h3>
        """,
        unsafe_allow_html=True)
        st.markdown("""
        <h5>╰┈➤The results will be:</h5>
        """,
        unsafe_allow_html=True)

        cursor.execute("""
               select close_approach_date,COUNT(*) as approach_count from close_approach group by close_approach_date order by close_approach_date
        """)
        result = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        data = pd.DataFrame(result, columns=columns)
        st.dataframe(data) 

    elif options== "23. Display the date which has highest approached count":
        
        st.markdown("""
        <h3>🛒QUERY:  Display the date which has highest approached count</h3>
        """,
        unsafe_allow_html=True)
        st.markdown("""
        <h5>╰┈➤The results will be:</h5>
        """,
        unsafe_allow_html=True)

        cursor.execute("""
               select close_approach_date,COUNT(*) as approach_count from close_approach group by close_approach_date order by approach_count desc limit 1
        """)
        result = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        data = pd.DataFrame(result, columns=columns)
        st.dataframe(data) 

    elif options== "24. List asteriods which approaches between'2024-05-13' and '2024-08-03":
        
        st.markdown("""
        <h3>🛒QUERY:  List asteriods which approaches between'2024-05-13' and '2024-08-03</h3>
        """,
        unsafe_allow_html=True)
        st.markdown("""
        <h5>╰┈➤The results will be:</h5>
        """,
        unsafe_allow_html=True)

        cursor.execute("""
               select distinct a.id,a.name,c.relative_velocity_kmph,c.close_approach_date from close_approach as c join asteroids as a on c.neo_reference_id=a.id where c.close_approach_date between '2024-05-13' and '2024-08-03' order by c.close_approach_date asc
        """)
        result = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        data = pd.DataFrame(result, columns=columns)
        st.dataframe(data)      

#filter criteria 
elif selected == "Filter criteria":
     
    st.markdown("""
    <h1 style='text-align: center;'>NASA NEAR EARTH OBJECT(NEO) TRACKING DASHBOARD</h1>
    """,
    unsafe_allow_html=True)

    st.markdown("""
    <h3>FILTER RANGE:</h3>
    """,
    unsafe_allow_html=True)    

    #set columns with space
    col1, space1,col2, space2, col3 = st.columns([0.4, 0.1, 0.4, 0.1,0.4])
    #first column
    with col1:
        #magnitude
        magnitude_min = st.slider("Min Magnitude", 13.81, 32.61, (13.81, 32.61))

        #diameter
        diameter_min = st.slider("Min Estimated Diameter (km)", 0.0, 4.59785, (0.0, 4.59785))
        diameter_max = st.slider("Max Estimated Diameter (km)", 0.0, 10.2811, (0.0, 10.2811))

    #second column
    with col2:
        #velocity
        velocity = st.slider("Relative Velocity (km/h)", 1418.22, 173072.0,(1418.22, 173072.0))

        #astronomical
        astronomical = st.slider("Astronomical Unit", 0.0, 0.492289, (0.0,0.492289))

        #harzardous
        hazardous = st.selectbox("Hazardous", ["0", "1"])
        #third column

    from datetime import datetime

    with col3:
        #date
        start_date = st.date_input("Start Date", datetime(2024, 1, 1))
        end_date = st.date_input("End Date", datetime(2025, 4, 13))

        #filter button
        button = st.button("Apply Filters")

    data="""
         select
            a.id,a.name,a.absolute_magnitude_h,a.estimated_diameter_min_km,a.estimated_diameter_max_km,a.is_potentially_hazardous_asteroid,
             c.close_approach_date,c.relative_velocity_kmph,c.astronomical,c.miss_distance_km,c.miss_distance_lunar,c.orbiting_body
             FROM
               asteroids as a join close_approach as c on a.id = c.neo_reference_id
               WHERE    
               a.absolute_magnitude_h between %s AND %s
               AND a.estimated_diameter_min_km between %s AND %s
               AND a.estimated_diameter_max_km between %s AND %s
               AND c.relative_velocity_kmph between %s AND %s
               AND c.close_approach_date between %s AND %s    
               AND a.is_potentially_hazardous_asteroid = %s
        """
    values = [

        magnitude_min[0], magnitude_min[1],
        diameter_min[0], diameter_min[1],
        diameter_max[0], diameter_max[1],
        velocity[0], velocity[1],
        start_date, end_date,
        hazardous
]
    
    #query execution
    if button:
        cursor.execute(data,values)
        result = cursor.fetchall()

        #get columns names      
        columns = [desc[0] for desc in cursor.description]
      
        #convert to dataframe  
        data = pd.DataFrame(result, columns=columns)

        #show results 
        st.subheader("🔗Filtered Asteroids:")
        st.dataframe(data) 
