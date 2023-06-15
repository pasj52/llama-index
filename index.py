import os, streamlit as st

# Uncomment to specify your OpenAI API key here (local testing only, not in production!), or add corresponding environment variable (recommended)
# os.environ['OPENAI_API_KEY']= ""

from llama_index import VectorStoreIndex, SimpleDirectoryReader

# Define a simple Streamlit app
st.title("Ask the DECTRIS digital assistant!")
query = st.text_input("What would you like to ask about our detectors?", "")

# If the 'Submit' button is clicked
if st.button("Submit"):
    if not query.strip():
        st.error(f"Please provide the search query.")
    else:
        try:
            # Configure prompt parameters and initialise helper
            max_input_size = 4096
            num_output = 256
            max_chunk_overlap = 20
                
            # Load documents from the 'data' directory
            documents = SimpleDirectoryReader('data_development').load_data()
            index = VectorStoreIndex.from_documents(documents) 
            query_engine = index.as_query_engine()
            response = query_engine.query(query).response
            st.success(response)
        except Exception as e:
            st.error(f"An error occurred: {e}")
