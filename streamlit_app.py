import streamlit as st
from streamlit.components.v1 import html

# Define a function to load and run JavaScript code


# Create a button to request location
if st.button("Get My Location"):
    
    
    # Run the JavaScript code
    def run_js_code(js_code):
        html(js_code)
    js_code = """

    <script>
    if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(showPosition);
    } else { 
    document.getElementById("demo").innerHTML =
    "Geolocation is not supported by this browser.";
    }

    function showPosition(position) {
    alert('posiosion geted')
    document.getElementById("demo").innerHTML =
    'Latitude: ' + position.coords.latitude + '<br>' +
    'Longitude: ' + position.coords.longitude;
    }
    </script>
          """
    
    st.markdown(js_code, unsafe_allow_html=True)   
