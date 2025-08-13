import streamlit as st
import important_functions as ipn
import pandas as pd
import pickle as pk


st.title("Flight Price Prediction")


url = 'https://www.boeing.com/content/theboeingcompany/us/en/commercial/777x/by-design/_jcr_content/root/container_2091943792/hero_teaser.coreimg.jpeg/1702317983600/cover-image-blue-livery.jpeg'

st.image(url)
st.divider()

st.sidebar.title("Flights")
st.sidebar.image("https://media.istockphoto.com/id/1526986072/photo/airplane-flying-over-tropical-sea-at-sunset.jpg?s=612x612&w=0&k=20&c=Ccvg3BqlqsWTT0Mt0CvHlbwCuRjPAIWaCLMKSl3PCks=")

initial_city=st.sidebar.selectbox(
    "Origin",
    tuple(ipn.get_Available_City())
)


final_city=st.sidebar.selectbox(
    "Destination",
    tuple(ipn.get_Available_City())
)

st.sidebar.divider()
st.sidebar.write('Flight Timings')
col1, col2 = st.sidebar.columns(2)

with col1:
    t1 = st.sidebar.radio(
        "Time of Departure",
        ipn.get_Timing(),
        index=0
    )

with col2:
    t2 = st.sidebar.radio(
        "Time of Arrival",
        ipn.get_Timing(),
        index=1
    )
st.sidebar.divider()

number_of_Stops = st.sidebar.slider(
    "Number of Stops",
    0,3,1
)
st.sidebar.divider()

ticket_class=st.sidebar.selectbox(
    "Select Category",
    ("Economy","Business")
    
)

st.sidebar.divider()
st.sidebar.write("Flight Duration")
hour = st.sidebar.slider(
    "hour",
    0,32,1
)
minute=st.sidebar.slider(
    "minutes",
    0,60,1
)
st.sidebar.divider()

days=st.sidebar.slider(
    "Days Left before Departure",
    0,60,1
)
st.sidebar.divider()


time_elapsed = round(float(hour + (minute/6)/10),2)

# ["Delhi","Evening","three","Evening","Mumbai","Economy",23.8,39]
to_predict=[initial_city,t1,number_of_Stops,t2,final_city,ticket_class,time_elapsed,days]
column_data = ['Origin','Time of Departure','Number of Stops','Time of Arrival','Destination','Category','Flight Duration','Days left before Booking']

# st.write(to_predict)
my_dict = {}
for i in range(8):
    my_dict[column_data[i]] = to_predict[i]


    
st.dataframe(my_dict)


file_path = '''model.pkl'''

f=open(file_path,'rb')
chatGPT = pk.load(f)
data=ipn.final_y(to_predict)
result = round(chatGPT.predict([data])[0],1)



to_write=f"Estimated Ticket Cost: {result} Rs."
st.markdown(
    "<h3 style='font-size:50px;'>"+to_write+"</h3>", 
    unsafe_allow_html=True
)




