# analytics.py

import streamlit.components.v1 as components

GA_ID = "G-07DKVV3XXM"

def load_ga():

    components.html(
        f"""
        <script async src="https://www.googletagmanager.com/gtag/js?id={GA_ID}"></script>

        <script>
          window.dataLayer = window.dataLayer || [];
          function gtag(){{dataLayer.push(arguments);}}

          gtag('js', new Date());

          gtag('config', '{GA_ID}');
        </script>
        """,
        height=0,
    )