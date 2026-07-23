from folder.login import login
import streamlit as st
st.set_page_config(
    page_title="Jindal Steel AI Aluminium Optimizer",
    page_icon="🏭",
    layout="wide",
    initial_sidebar_state="expanded"
)

if "logged_in" not in st.session_state:

    st.session_state.logged_in=False

if not st.session_state.logged_in:

    login()

    st.stop()
from streamlit_option_menu import option_menu
# CSS
with open("assets/style.css") as css:
    st.markdown(
        f"<style>{css.read()}</style>",
        unsafe_allow_html=True
    )

# Sidebar
with st.sidebar:

    st.image("assets/jspl_logo.png", width=200)

    selected = option_menu(

        menu_title="Navigation",

        options=[

            "Dashboard",

            "Prediction",

            "Recommendation",

            "Analytics",

            "Digital Twin(updating soon)",

            "Reports",
            "AI Explainability(updating soon)",
            "Management Dashboard",
            "Optimization Simulator(updating soon)"

        ],

        icons=[

            "speedometer2",

            "cpu",

            "robot",

            "graph-up",

            "diagram-3",

            "file-earmark",

            "search",
            
            "bar-chart",

            "sliders"

        ],

        default_index=0,

        menu_icon="list",

       styles={
         "container": {
             "padding": "0px",
             "background-color": "transparent"
         },

          "icon": {
             "color": "#00E5FF",
             "font-size": "18px"
        },

         "nav-link": {
           "font-size": "15px",
           "text-align": "left",
           "margin": "5px",
           "--hover-color": "#1C2B45"
         },

         "nav-link-selected": {
           "background": "linear-gradient(90deg,#00C8FF,#0095FF)",
           "color": "white"
         }
       }
    )


# Loadfolder

if selected=="Dashboard":

    from folder.dashboard import dashboard

    dashboard()

elif selected=="Prediction":

    from folder.prediction import prediction

    prediction()

elif selected=="Recommendation":

    from folder.recommendation import recommendation

    recommendation()

elif selected=="Analytics":

    from folder.analytics import analytics

    analytics()

elif selected=="Digital Twin":

    from folder.digital_twin_panel import digital_twin_panel

    digital_twin_panel(recommendation)
elif selected=="AI Explainability":

    from folder.ai_explainability import ai_explainability

    ai_explainability()
elif selected=="Management Dashboard":

    from folder.management_dashboard import management_dashboard

    management_dashboard()
elif selected=="Optimization Simulator":

    from folder.optimization_simulator import optimization_simulator

    optimization_simulator()
    
elif selected=="Reports":

    from folder.Reports import reports

    reports()