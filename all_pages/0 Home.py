import streamlit as st
from common_config import set_localization, footer_and_language

_ = set_localization(st.session_state.language)
footer_and_language(st.session_state.language)


def home_page():
    st.image("static/streamlit_banner_v4.png")
    st.markdown(
        '<span id="welcome" style="font-weight: 800; text-align: center; display: inline-block; width: 100%;"><span style="display: inline-block;">'
        + _("Welcome to")
        + ':blue-background[WinterPixelGames]&nbsp;!</span><span style="display: inline-block;">'
        + _(
            "A website which provides useful Tools & Statistics of games made by [Winterpixel Games](https://www.winterpixel.com/)"
        )
        + "</span></span>",
        unsafe_allow_html=True,
    )
    st.html(
        """
   <style>
       #welcome a {
           text-decoration: none;
       }
       .row-widget.stButton {
           display: flex;
           justify-content: center;
       }
       div[data-testid="column"] {
           display: inline-block !important;
       }
       div[data-testid="stHorizontalBlock"] div button {
           border: none;
           background: transparent;
           padding: 2vh;
           margin: 8px;
       }
       div[data-testid="stHorizontalBlock"] div button:hover {
           border: none !important;
           box-shadow: 0 0 0px transparent !important;
       }
       div[data-testid="stHorizontalBlock"] div button:active {
           background: transparent;
       }
       div[data-testid="stHorizontalBlock"] div button p:hover:before {
           box-shadow: 0 0 30px #158fd8;
       }
       @media screen and (min-width: 1100px) and (orientation: landscape) {
           #welcome {
               padding-top: 4rem !important;
               font-size: 2vw !important;
           }
           div[data-testid="stHorizontalBlock"] {
               padding-top: 4rem !important;
           }
           div[data-testid="stHorizontalBlock"] > div:nth-child(1) button:after {
               content: '"""
        + _("Rocket Bot Royale")
        + """' !important;
           }
           div[data-testid="stHorizontalBlock"] > div:nth-child(2) button:after {
               content: '"""
        + _("Goober Dash")
        + """' !important;
           }
           div[data-testid="stHorizontalBlock"] > div:nth-child(3) button:after {
               content: '"""
        + _("Goober Royale")
        + """' !important;
           }
           div[data-testid="stHorizontalBlock"] > div:nth-child(4) button:after {
               content: '"""
        + _("Goober Shot")
        + """' !important;
           }
           div[data-testid="stHorizontalBlock"] > div:nth-child(5) button:after {
               content: '"""
        + _("Moonrock Miners")
        + """' !important;
           }
       }
       div[data-testid="stHorizontalBlock"] div button:after {
           visibility: hidden;
       }
       div[data-testid="stHorizontalBlock"] div button:hover:after {
           visibility: visible;
           position: relative;
           top: 15rem;
           font-family: 'Baloo 2';
           font-weight: 700;
           font-size: 2rem;
       }
       div[data-testid="stHorizontalBlock"] div button p:before {
           border: 5px solid #0196ee;
           max-width: 25vw;
           border-radius: 2.8rem;
           background-size: 100%;
           display: flex;
           justify-content: center;
           overflow: hidden;
           content: "";
           position: absolute;
           width: 80%;
           bottom: auto;
           left: 50%;
           top: 10%;
           transform: translateX(-50%) scale(0.9);
           aspect-ratio: 1/1;
       }
       div[data-testid="stHorizontalBlock"] > div:nth-child(1) button p::before {
           background-image: url("./app/static/RocketBotRoyale/rocket_bot_royale_favicon.png");
       }
       div[data-testid="stHorizontalBlock"] > div:nth-child(2) button p::before {
           background-image: url("./app/static/GooberDash/goober_dash_favicon.png");
       }
       div[data-testid="stHorizontalBlock"] > div:nth-child(3) button p::before {
           background-image: url("./app/static/GooberRoyale/goober_royale_favicon.png");
       }
       div[data-testid="stHorizontalBlock"] > div:nth-child(4) button p::before {
           background-image: url("./app/static/GooberShot/goober_shot_favicon.png");
       }
       div[data-testid="stHorizontalBlock"] > div:nth-child(5) button p::before {
           background-image: url("./app/static/MoonrockMiners/moonrock_miners_favicon.png");
       }
   </style>
   """
    )

    col1, col2, col3, col4, col5 = st.columns(5)
    if col1.button("​", key="RBR"):
        st.switch_page("all_pages/1 Rocket Bot Royale.py")

    if col2.button("​", key="GD"):
        st.switch_page("all_pages/2 Goober Dash.py")

    if col3.button("​", key="GR"):
        st.switch_page("all_pages/3 Goober Royale.py")

    if col4.button("​", key="GS"):
        st.switch_page("all_pages/4 Goober Shot.py")

    if col5.button("​", key="MM"):
        st.switch_page("all_pages/5 Moonrock Miners.py")


pg = st.navigation(
    {
        "": [
            st.Page(home_page, title=_("Home"), default=True, url_path=""),
            st.Page(
                "all_pages/1 Rocket Bot Royale.py",
                title=_("Rocket Bot Royale"),
                url_path="Rocket_Bot_Royale",
            ),
            st.Page(
                "all_pages/2 Goober Dash.py",
                title=_("Goober Dash"),
                url_path="Goober_Dash",
            ),
            st.Page(
                "all_pages/3 Goober Royale.py",
                title=_("Goober Royale"),
                url_path="Goober_Royale",
            ),
            st.Page(
                "all_pages/4 Goober Shot.py",
                title=_("Goober Shot"),
                url_path="Goober_Shot",
            ),
            st.Page(
                "all_pages/5 Moonrock Miners.py",
                title=_("Moonrock Miners"),
                url_path="Moonrock_Miners",
            ),
            st.Page(
                "all_pages/6 About.py",
                title=_("About"),
                url_path="About",
            ),
            st.Page(
                "all_pages/7 Useful Links.py",
                title=_("Useful Links"),
                url_path="Userful_Links",
            ),
        ],
    }
)


try:
    pg.run()
except Exception as e:
    print(e)
