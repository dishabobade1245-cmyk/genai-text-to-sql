import streamlit as st
import requests

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="QueryMind AI",
    page_icon="◈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------

st.markdown("""
<style>

    .stApp {
        background: #0b1020;
        color: #e8ecf7;
    }

    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    header {
        visibility: hidden;
    }

    section[data-testid="stSidebar"] {
        background: #11182b;
        border-right: 1px solid #202a44;
    }

    .main-title {
        font-size: 42px;
        font-weight: 700;
        margin-bottom: 5px;
        letter-spacing: -1px;
    }

    .subtitle {
        color: #8e9ab5;
        font-size: 17px;
        margin-bottom: 35px;
    }

    .hero {
        background: linear-gradient(135deg, #151f38, #10172b);
        border: 1px solid #263452;
        border-radius: 18px;
        padding: 28px;
        margin-bottom: 25px;
    }

    .hero-title {
        font-size: 22px;
        font-weight: 600;
        margin-bottom: 8px;
    }

    .hero-text {
        color: #9ca8c0;
        font-size: 15px;
    }

    .section-title {
        font-size: 18px;
        font-weight: 600;
        margin-top: 25px;
        margin-bottom: 10px;
    }

    .status {
        display: inline-block;
        padding: 6px 12px;
        border-radius: 20px;
        background: #123528;
        color: #5ee6a8;
        font-size: 13px;
        margin-bottom: 15px;
    }

    .example {
        background: #151e33;
        border: 1px solid #263452;
        border-radius: 10px;
        padding: 10px 12px;
        margin: 8px 0;
        color: #aab5ca;
        font-size: 13px;
    }

</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

with st.sidebar:

    st.markdown("## ◈ QueryMind AI")

    st.markdown(
        "<p style='color:#8e9ab5;'>Natural Language → SQL</p>",
        unsafe_allow_html=True
    )

    st.divider()

    st.markdown("### Database")

    st.markdown(
        """
        <div class="example">
        🟢 PostgreSQL<br>
        <span style="color:#7f8ba5;">Connected</span>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("### Try asking")

    examples = [
        "Show all completed orders",
        "List all customers",
        "Show products with price above 500",
        "How many orders are completed?"
    ]

    for example in examples:
        st.markdown(
            f"<div class='example'>{example}</div>",
            unsafe_allow_html=True
        )

    st.divider()

    st.caption("GenAI Text-to-SQL")
    st.caption("Powered by Gemini + PostgreSQL")

# --------------------------------------------------
# MAIN HEADER
# --------------------------------------------------

st.markdown(
    "<div class='main-title'>Ask your database anything.</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='subtitle'>Turn natural-language questions into safe SQL queries using AI.</div>",
    unsafe_allow_html=True
)

# --------------------------------------------------
# HERO
# --------------------------------------------------

st.markdown(
    """
    <div class="hero">
        <div class="hero-title">◈ AI Database Assistant</div>
        <div class="hero-text">
            Ask questions in plain English. QueryMind generates a PostgreSQL
            query, validates it, executes it safely, and displays the result.
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# --------------------------------------------------
# QUESTION INPUT
# --------------------------------------------------

question = st.text_area(
    "Your question",
    placeholder="Example: Show me all completed orders",
    height=110
)

run_query = st.button(
    "✦  Generate & Run Query",
    use_container_width=True
)

# --------------------------------------------------
# QUERY PROCESSING
# --------------------------------------------------

if run_query:

    if not question.strip():

        st.warning("Please enter a question.")

    else:

        with st.spinner("Understanding your question..."):

            try:

                response = requests.get(
                    "https://genai-text-to-sql.onrender.com/query",
                    params={"question": question},
                    timeout=120
                )

                result = response.json()

                if result.get("status") == "success":

                    st.markdown(
                        '<div class="status">● Query executed successfully</div>',
                        unsafe_allow_html=True
                    )

                    st.markdown(
                        '<div class="section-title">Generated SQL</div>',
                        unsafe_allow_html=True
                    )

                    st.code(
                        result["sql"],
                        language="sql"
                    )

                    st.markdown(
                        '<div class="section-title">Query Results</div>',
                        unsafe_allow_html=True
                    )

                    data = result["result"]

                    if data:

                        st.dataframe(
                            data,
                            use_container_width=True,
                            hide_index=True
                        )

                        st.caption(
                            f"{len(data)} row(s) returned"
                        )

                    else:

                        st.info("The query returned no results.")

                elif result.get("status") == "clarification_required":

                    st.warning(
                        result.get(
                            "message",
                            "Could you provide more details?"
                        )
                    )

                else:

                    st.error(
                        result.get(
                            "message",
                            "Something went wrong."
                        )
                    )

            except requests.exceptions.ConnectionError as error:

                st.error(
                    f"Could not connect to the FastAPI API. "
                    f"Please try again later.\n\nDetails: {error}"
                )

            except requests.exceptions.Timeout:

                st.error(
                    "The request took too long. "
                    "Please try again."
                )

            except Exception as error:

                st.error(f"Unexpected error: {error}")