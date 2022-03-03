#------------------------
#App for Boarding Pass
#------------------------
# Import modules

#from multiapp import MultiApp
import os
import json
from web3 import Web3
from pathlib import Path
from dotenv import load_dotenv
import streamlit as st
import base64

load_dotenv("./api.env")

# Define and connect a new Web3 provider
w3 = Web3(Web3.HTTPProvider(os.getenv("WEB3_PROVIDER_URI")))

# Contract Helper function
def show_pdf(file_path):
    with open(file_path,"rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
        pdf_display = f'<embed src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf">'
        st.markdown(pdf_display, unsafe_allow_html=True)

@st.cache(allow_output_mutation=True)
def load_contract():

    # Load the contract ABI
    with open(Path('./contracts/compiled/artwork_abi.json')) as f:
        artwork_abi = json.load(f)

    contract_address = os.getenv("SMART_CONTRACT_ADDRESS")

    # Load the contract
    contract = w3.eth.contract(
        address=contract_address,
        abi=artwork_abi
    )

    return contract

def app():
    contract = load_contract()
    
    # Register New Artwork
    
    st.title("Fly Token App")
    st.header("Use blockchain and avoid the lines!")
    accounts = w3.eth.accounts
    
    # Use a streamlit component to get the address of the artwork owner from the user
    address = st.selectbox("Select travelers blockchain account", options=accounts)
    
    # Use a streamlit component to get the artwork's URI
    artwork_uri = st.text_input("URI to the boarding pass token")
    image_file = st.file_uploader("Upload Image",type=['jpg','png','jpeg']) 
    if image_file is not None:
        artwork_uri = "./token/"+image_file.name
    if st.button("Register token"):
        
        # Use the contract to send a transaction to the registerArtwork function
        tx_hash = contract.functions.registerArtwork(
            address,
            artwork_uri
        ).transact({'from': address, 'gas': 1000000})
        receipt = w3.eth.waitForTransactionReceipt(tx_hash)
        # st.write("Transaction receipt mined:")
        # st.write(dict(receipt))
        st.write("Your token is registered!")
    
    st.markdown("---")
    
    ################################################################################
    # Display a Token
    ################################################################################
    st.markdown("## Collect your unique token")
    
    selected_address = st.selectbox("Select Account", options=accounts)
    
    tokens = contract.functions.balanceOf(selected_address).call()
    
    st.write(f"This address has {tokens} unique tokens")
    
    token_id = st.selectbox("Travelers Tokens", list(range(tokens)))
    
    st.markdown("---")
    
    
    
    if st.button("Display Token"):
    
        # Use the contract's `ownerOf` function to get the art token owner
        owner = contract.functions.ownerOf(token_id).call()
    
        st.write(f"The token is registered to account {owner}")
    
        # Use the contract's `tokenURI` function to get the art token's URI
        token_uri = contract.functions.tokenURI(token_id).call()
    
        # st.write(f"The tokenURI is {token_uri}")
        #st.image(token_uri, width=200)
        
        st.markdown("---")
        st.markdown("Have a great flight!")
        
        st.image("./boarding_pass/flyToken_pass.png")
        st.write(show_pdf("./boarding_pass/pass.pdf"))
        
        
        #st.markdown(link, unsafe_allow_html=True)
    
    
    
    
    st.markdown("---")
