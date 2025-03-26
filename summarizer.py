# import libraries
import validators,streamlit as st
from langchain_community.document_loaders import YoutubeLoader, UnstructuredURLLoader
from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain.chains.summarize import load_summarize_chain
import pytube
pytube.innertube._default_clients['ANDROID'] = pytube.innertube._default_clients['WEB']

#page cofig
st.set_page_config(page_title='Langchain: summarize text from Youtube or Website')
st.title('Summarize Text from Youtube or Website')

#take groq api key and url for summarization
groq_api_key=st.sidebar.text_input('Enter groq api key',type='password')

llm=ChatGroq(model='Gemma2-9b-It',api_key=groq_api_key)

prompt_template='''
Please provde a summary of following content in 300 words {text}'''

prompt=PromptTemplate(
    input_variable=['text'],
    template=prompt_template
)

generic_url=st.text_input('URL',label_visibility='collapsed')

if st.button('Summarize'):
    if not groq_api_key.strip():
        st.error('Please provide groq api key')
    elif not generic_url.strip():
        st.error('Please provide Youtube or website url')
    elif not validators.url(generic_url):
        st.error('Please provide valid youtube or website url')
    else:
        with st.spinner('waiting....'):
            if 'youtube.com' in generic_url:
                loader=YoutubeLoader.from_youtube_url(youtube_url=generic_url,add_video_info=True)
            else:
                loader=UnstructuredURLLoader(urls=[generic_url],ssl_verify=False)
            docs=loader.load()
            chain=load_summarize_chain(llm=llm,chain_type='stuff',prompt=prompt,verbose=True)
            summary=chain.run(docs)
            st.success(summary)



        