import streamlit as st
import plotly.express as px


def process_analysis(df):

    st.markdown(

        '<div class="section-title">⚙ Process Behaviour Analysis</div>',

        unsafe_allow_html=True

    )

    left,right = st.columns(2)

    # =======================================================
    # TEMPERATURE
    # =======================================================

    with left:

        fig = px.scatter(

            df,

            x="LIFTING TEMP_LRF",

            y="Total_Al_LRF_kg",

            color="GRADE",
            

        )

        fig.update_layout(

            template="plotly_dark",

            title="Temperature vs Aluminium",

            paper_bgcolor="rgba(0,0,0,0)",

            plot_bgcolor="rgba(0,0,0,0)",

            height=500

        )

        st.plotly_chart(

            fig,

            use_container_width=True

        )

    # =======================================================
    # OXYGEN
    # =======================================================

    with right:

        if "OXYGEN" in df.columns:

            fig = px.scatter(

                df,

                x="OXYGEN",

                y="Total_Al_LRF_kg",

                trendline="ols",

                color="GRADE"

            )

            fig.update_layout(

                template="plotly_dark",

                title="Dissolved Oxygen vs Aluminium",

                paper_bgcolor="rgba(0,0,0,0)",

                plot_bgcolor="rgba(0,0,0,0)",

                height=500

            )

            st.plotly_chart(

                fig,

                use_container_width=True

            )

        else:

            st.info(

                "Dissolved Oxygen data will automatically appear after plant validation."

            )