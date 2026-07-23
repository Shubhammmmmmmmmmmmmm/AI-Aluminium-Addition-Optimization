import streamlit as st
import base64
import time
from datetime import datetime


# ============================================================
# IMAGE TO BASE64
# ============================================================

def get_base64(path):

    with open(path, "rb") as f:

        return base64.b64encode(f.read()).decode()


# ============================================================
# LOGIN PAGE
# ============================================================

def login():

    background = get_base64(
        "assets/login_background.png"
    )

    now = datetime.now().strftime(
        "%d %b %Y | %I:%M:%S %p"
    )

    st.markdown(
        f"""
<style>

/* -------------------------------------------------- */
/* Hide Streamlit */
/* -------------------------------------------------- */

#MainMenu {{
visibility:hidden;
}}

header {{
visibility:hidden;
}}

footer {{
visibility:hidden;
}}

[data-testid="stSidebar"] {{
display:none;
}}


/* -------------------------------------------------- */
/* Background */
/* -------------------------------------------------- */

.stApp {{

background:
linear-gradient(
rgba(5,12,25,.55),
rgba(5,12,25,.55)
),

url("data:image/png;base64,{background}");

background-size:cover;
background-position:center;
background-repeat:no-repeat;
background-attachment:fixed;

}}


/* -------------------------------------------------- */
/* Overlay */
/* -------------------------------------------------- */

.overlay {{

position:fixed;

top:0;
left:0;
right:0;
bottom:0;

background:rgba(0,0,0,.18);

z-index:-1;

}}


/* -------------------------------------------------- */
/* Clock */
/* -------------------------------------------------- */

.clock {{

position:fixed;

top:22px;

right:22px;

padding:18px;

min-width:220px;

background:rgba(10,20,40,.82);

border-radius:18px;

border:1px solid #00E5FF;

color:white;

text-align:center;

font-family:'Segoe UI',sans-serif;

box-shadow:
0 0 15px rgba(0,229,255,.25),
0 0 35px rgba(0,229,255,.10),
0 10px 25px rgba(0,0,0,.45);

animation:float 3s ease-in-out infinite;

}}


/* -------------------------------------------------- */
/* Glass Card */
/* -------------------------------------------------- */

.login-card {{

background:rgba(8,18,35,.72);

padding:38px;

border-radius:24px;

border:1px solid rgba(0,255,255,.30);

backdrop-filter:blur(14px);

box-shadow:

0px 12px 35px rgba(0,0,0,.45);

animation:fadeUp 1s;

}}


/* -------------------------------------------------- */
/* Title */
/* -------------------------------------------------- */

.title {{

text-align:center;

font-size:44px;

font-weight:700;

color:white;

font-family:'Segoe UI';

margin-bottom:5px;

}}


.subtitle {{

text-align:center;

font-size:20px;

font-weight:400;

color:#5CE1E6;

letter-spacing:1px;

margin-bottom:28px;

}}


/* -------------------------------------------------- */
/* Animation */
/* -------------------------------------------------- */

@keyframes fadeUp {{

from {{

opacity:0;

transform:translateY(30px);

}}

to {{

opacity:1;

transform:translateY(0);

}}

}}

@keyframes float {{

0% {{

transform:translateY(0px);

}}

50% {{

transform:translateY(-5px);

}}

100% {{

transform:translateY(0px);

}}

}}

</style>


<div class="overlay"></div>

<div class="clock">

🕒<br>

<b>{now}</b>

<br><br>

🟢 SYSTEM ONLINE

</div>

""",
       unsafe_allow_html=True
    )

    left, center, right = st.columns([1.2, 1.8, 1.2])

    with center:

        container = st.container()

    with container:

        st.markdown(
            """
<div class="title">
🏭 JINDAL STEEL
</div>
""",
            unsafe_allow_html=True
        )
         

        # ============================================================
        # LOGIN INPUTS
        # ============================================================

        username = st.text_input(
            "👤 Username",
            placeholder="Enter your username"
        )

        password = st.text_input(
            "🔒 Password",
            type="password",
            placeholder="Enter your password"
        )

        remember = st.checkbox("Remember Me")

        st.write("")

        login_btn = st.button(

            "🚀 LOGIN TO AI SYSTEM",

            width="stretch",

            type="primary"

        )

        # ============================================================
        # LOGIN LOGIC
        # ============================================================

        if login_btn:

            progress = st.progress(0)

            status = st.empty()

            for i in range(101):

                progress.progress(i)

                if i < 30:

                    status.info("🔍 Verifying User...")

                elif i < 60:

                    status.info("🤖 Loading AI Model...")

                elif i < 90:

                    status.info("🏭 Connecting to Plant Database...")

                time.sleep(0.01)

            if username == "admin" and password == "IS0290":
                 status.empty()
                 st.session_state.logged_in = True
                 status.success("✅ Login Successful")

                 time.sleep(0.3)

                 st.rerun()

            else:
                 status.empty()
                 status.error("❌ Invalid Username or Password")

        st.markdown(

            "</div>",

            unsafe_allow_html=True

        )

        st.write("")
        st.markdown("<br><br>", unsafe_allow_html=True)

    # ============================================================
    # FOOTER STATUS CARDS
    # ============================================================

    st.markdown(
        """
<style>

.status-card{

background:rgba(10,20,40,.80);

border-radius:18px;

padding:18px;

text-align:center;

border:1px solid rgba(0,229,255,.45);

transition:all .35s ease;

box-shadow:
0 0 12px rgba(0,229,255,.18),
0 0 24px rgba(0,229,255,.08),
0 8px 20px rgba(0,0,0,.35);

}

.status-card:hover{

transform:translateY(-6px) scale(1.03);

border:1px solid #00E5FF;

box-shadow:
0 0 20px rgba(0,229,255,.45),
0 0 45px rgba(0,229,255,.20),
0 16px 35px rgba(0,0,0,.40);

}

.status-title{

font-size:18px;

font-weight:700;

font-family:'Segoe UI',sans-serif;

color:white;

margin-bottom:10px;

}

.status-value{

font-size:15px;

font-weight:600;

font-family:'Segoe UI',sans-serif;

}

.footer-note{

text-align:center;

margin-top:25px;

font-size:13px;

color:#D1D5DB;

letter-spacing:.5px;

}

</style>
""",
        unsafe_allow_html=True
    )

    c1, c2, c3, c4 = st.columns(4)

    cards = [

        ("🧠 AI ENGINE",
         "● ONLINE",
         "#22C55E"),

        ("🤖 AI MODEL",
         "Extra Trees | R² = 0.77",
         "#38BDF8"),

        ("🏭 PLANT",
         "● CONNECTED",
         "#FACC15"),

        ("📈 VERSION",
         "v2.0",
         "#FB923C")

    ]

    columns = [c1, c2, c3, c4]

    for col, (title, value, color) in zip(columns, cards):

        with col:

            st.markdown(

                f"""
<div class="status-card">

<div class="status-title">

{title}

</div>

<div
class="status-value"
style="color:{color};">

{value}

</div>

</div>
""",

                unsafe_allow_html=True

            )

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(
        """
<div class="footer-note">

JINDAL STEEL • RAIGARH • SMS-III

<br>

AI Based Aluminium Addition Optimization System

</div>
""",
        unsafe_allow_html=True
    )

