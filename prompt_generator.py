from langchain_core.prompts import PromptTemplate

template_prompt = '''
Please summarize the research paper titled "{paper_input}" in a {style_input} style with a {length_input} explanation. The summary should include the following details:  
1. Mathematical Details – Incorporate relevant mathematical equations from the paper and explain key mathematical concepts using simple, intuitive code snippets where applicable.  
2. Analogies – Use relatable analogies to simplify complex ideas and make the concepts easier to understand.  
If certain information is not available in the paper, respond with "Insufficient information available" instead of making assumptions. Ensure the summary is clear, accurate, and aligned with the specified style and length.
'''

template = PromptTemplate(template = template_prompt, input_variables = ['paper_input','style_input','length_input'])

template.save('template.json')