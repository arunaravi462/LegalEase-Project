import streamlit as st
from datetime import date

st.set_page_config(page_title="LegalEase", page_icon="⚖️", layout="wide")

st.title("⚖️ LegalEase")
st.subheader("AI-Powered Legal Document Generator")
st.write("Create a simple legal document draft by entering the required details.")

with st.sidebar:
    st.header("Document Settings")
    doc_type = st.selectbox(
        "Choose document type",
        ["Rental Agreement", "Leave & License Agreement", "Employment Agreement", "Non-Disclosure Agreement", "General Legal Notice"]
    )
    language = st.selectbox("Language", ["English"])
    st.caption("Project by Aruna")

st.markdown("### Enter Details")
col1, col2 = st.columns(2)

with col1:
    party_one = st.text_input("First Party Name")
    party_two = st.text_input("Second Party Name")
    address = st.text_area("Address")
    purpose = st.text_area("Purpose / Agreement Details")

with col2:
    start_date = st.date_input("Start Date", value=date.today())
    end_date = st.date_input("End Date")
    amount = st.text_input("Amount / Consideration")
    extra = st.text_area("Additional Terms")

def generate_document():
    title = doc_type.upper()
    return f"""{title}

Date: {start_date.strftime("%d-%m-%Y")}

This document is prepared between:

First Party: {party_one or "[First Party Name]"}
Second Party: {party_two or "[Second Party Name]"}

Address:
{address or "[Address]"}

Purpose / Details:
{purpose or "[Purpose or agreement details]"}

Validity:
From {start_date.strftime("%d-%m-%Y")} to {end_date.strftime("%d-%m-%Y")}.

Amount / Consideration:
{amount or "[Amount]"}

Additional Terms:
{extra or "[Additional terms]"}

DECLARATION
Both parties acknowledge that the information entered above is intended to form a draft document for review.

IMPORTANT NOTICE
This application generates a general draft for educational and demonstration purposes. It is not legal advice and should be reviewed by a qualified legal professional before use.
"""

if st.button("Generate Document", type="primary"):
    if not party_one or not party_two:
        st.warning("Please enter both party names.")
    else:
        st.session_state["document"] = generate_document()

if "document" in st.session_state:
    st.markdown("### Document Preview")
    st.text_area("Generated Draft", st.session_state["document"], height=430)

    st.download_button(
        "Download TXT",
        data=st.session_state["document"],
        file_name="legal_document_draft.txt",
        mime="text/plain"
    )
