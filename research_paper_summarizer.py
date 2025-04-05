from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate, load_prompt
import streamlit as st

load_dotenv()

model = ChatOpenAI(model = 'gpt-4')

st.header('Research Paper Summarization Tool')

paper_input = st.selectbox('Select Research Paper',["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis","NeRF: Representing Scenes as Neural Radiance Fields for View Synthesis","UNet: Convolutional Networks for Biomedical Image Segmentation","VGGNet: Very Deep Convolutional Networks for Large-Scale Image Recognition","AlexNet: ImageNet Classification with Deep Convolutional Neural Networks","MusicLM: Generating Music from Text"])

style_input = st.selectbox("Select Style",["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"])

length_input = st.selectbox("Select Length",["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"])

template = load_prompt('template.json')

if st.button('Summarize'):
    chain = template | model
    result = chain.invoke({
        'paper_input': paper_input,
        'style_input' : style_input,
        'length_input': length_input
    })
    st.write(result.content)