st.title("AI Video Generator")
api_key = st.text_input("Enter your Gemini API key", type="password")
prompt = st.text_area("Enter your prompt for video generation")
if st.button("Generate Video"):
if api_key and prompt:










  



  
os.environ["GEMINI_API_KEY"] = api_key
st.write(
"Generating video for prompt: '{0}' using API key provided.".format(
prompt
)
)
else:
st.warning("Please enter your API key and prompt.")
