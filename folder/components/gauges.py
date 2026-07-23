import plotly.graph_objects as go
import streamlit as st

# ============================================================
# AI Aluminium Gauge
# ============================================================

def aluminium_gauge(value=238,
                    confidence=94,
                    title="AI Predicted Aluminium"):

    fig = go.Figure()

    fig.add_trace(

        go.Indicator(

            mode="gauge+number+delta",

            value=value,

            number={"suffix":" kg"},

            delta={"reference":250},

            title={
                "text":f"<b>{title}</b><br><span style='font-size:16px'>Confidence : {confidence}%</span>"
            },

            gauge={

                "axis":{"range":[0,400]},

                "bar":{"color":"deepskyblue"},

                "bgcolor":"white",

                "borderwidth":2,

                "bordercolor":"gray",

                "steps":[

                    {
                        "range":[0,180],
                        "color":"#16A34A"
                    },

                    {
                        "range":[180,260],
                        "color":"#FACC15"
                    },

                    {
                        "range":[260,400],
                        "color":"#DC2626"
                    }

                ],

                "threshold":{

                    "line":{
                        "color":"cyan",
                        "width":6
                    },

                    "thickness":0.8,

                    "value":value

                }

            }

        )

    )

    fig.update_layout(

        height=420,

        paper_bgcolor="#0B1220",

        plot_bgcolor="#0B1220",

        font=dict(

            color="white",

            size=18

        ),

        margin=dict(

            l=20,

            r=20,

            t=60,

            b=20

        )

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )