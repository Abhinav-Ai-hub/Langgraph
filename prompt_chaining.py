
Imports
from langgraph.graph import StateGraph, START, END
from langchain_openai import ChatOpenAI
from typing import TypedDict
from dotenv import load_dotenv
Loading env variables
load_dotenv()
True
Define LLM
model = ChatOpenAI()
Define State
class BlogState(TypedDict):

    title: str
    outline: str
    content: str
Creating Nodes
def create_outline(state: BlogState) -> BlogState:

    # fetch title
    title = state['title']

    # call llm gen outline
    prompt = f'Generate a detailed outline for a blog on the topic - {title}'
    outline = model.invoke(prompt).content

    # update state
    state['outline'] = outline

    return state
def create_blog(state: BlogState) -> BlogState:

    title = state['title']
    outline = state['outline']

    prompt = f'Write a detailed blog on the title - {title} using the follwing outline \n {outline}'

    content = model.invoke(prompt).content

    state['content'] = content

    return state
Define and Compile Graph
graph = StateGraph(BlogState)

# nodes
graph.add_node('create_outline', create_outline)
graph.add_node('create_blog', create_blog)

# edges
graph.add_edge(START, 'create_outline')
graph.add_edge('create_outline', 'create_blog')
graph.add_edge('create_blog', END)

workflow = graph.compile()
Execute the Graph
intial_state = {'title': 'Rise of AI in India'}

final_state = workflow.invoke(intial_state)

print(final_state)
{'title': 'Rise of AI in India', 'outline': "I. Introduction\n    A. Brief overview of artificial intelligence (AI)\n    B. Explanation of the rise of AI in India \n    C. Thesis statement: The increasing adoption of AI in India is reshaping various industries and transforming the country's economic landscape.\n\nII. Current State of AI in India\n    A. Overview of AI ecosystem in India\n    B. Key players in the AI industry\n    C. Government initiatives to promote AI adoption \n    D. Challenges faced by the AI industry in India\n\nIII. Industries Impacted by AI in India\n    A. Healthcare\n        1. AI applications in healthcare \n        2. Benefits of AI in improving healthcare outcomes \n        3. Case studies of successful AI implementations in Indian healthcare sector\n\n    B. Manufacturing\n        1. AI use cases in manufacturing \n        2. Impact of AI on production efficiency and cost reduction \n        3. Examples of Indian manufacturing companies leveraging AI technology\n\n    C. Finance\n        1. AI applications in the financial sector \n        2. Role of AI in fraud detection and risk management \n        3. Case studies of Indian financial institutions using AI for competitive advantage\n\nIV. Future Trends in AI in India\n    A. Potential growth opportunities for AI in India \n    B. Emerging technologies shaping the future of AI \n    C. Predictions for the AI industry in India in the coming years \n\nV. Conclusion\n    A. Recap of key points discussed in the blog\n    B. Final thoughts on the rise of AI in India and its implications for the country's economy and society \n    C. Call to action for readers to stay informed and engaged with developments in the AI industry in India", 'content': "Artificial Intelligence (AI) has been making massive strides in India in recent years, revolutionizing various industries and shaping the country's economic landscape. From healthcare to finance to manufacturing, AI is being leveraged to drive innovation, improve efficiency, and enhance decision-making processes. In this blog, we will explore the rise of AI in India, its current state, industries impacted by AI, future trends, and the implications for the country's economy and society.\n\nThe Current State of AI in India:\nIndia's AI ecosystem has been experiencing rapid growth, with the emergence of various startups, research institutes, and technology giants focusing on AI research and development. Companies like Tata Consultancy Services (TCS), Infosys, Wipro, and startups such as Niki.ai, Niramai, and SigTuple are leading the way in the AI industry in India. The government has also been actively promoting AI adoption through initiatives like the National Strategy for Artificial Intelligence and the National AI Portal, which aim to foster collaboration between industry, academia, and the government.\n\nDespite these developments, the AI industry in India faces challenges such as a shortage of AI talent, lack of data privacy regulations, and concerns about bias and ethics in AI algorithms. Addressing these challenges is crucial to ensure the responsible and sustainable growth of the AI industry in India.\n\nIndustries Impacted by AI in India:\nAI is making significant inroads in various industries in India, transforming the way businesses operate and deliver services. In healthcare, AI is being used for early disease detection, personalized treatment plans, and medical image analysis. Companies like Practo, Portea Medical, and Mfine are leveraging AI to improve healthcare outcomes and patient care.\n\nIn manufacturing, AI is optimizing production processes, predictive maintenance, and quality control. Indian manufacturing companies like Mahindra & Mahindra, Tata Steel, and Hindustan Unilever are embracing AI technology to drive production efficiency and cost reduction.\n\nIn finance, AI is revolutionizing fraud detection, credit scoring, and risk management. Indian financial institutions like HDFC Bank, ICICI Bank, and SBI are using AI-powered chatbots, algorithms, and predictive analytics to enhance customer service and gain a competitive edge in the market.\n\nFuture Trends in AI in India:\nThe future of AI in India looks promising, with potential growth opportunities in areas like agriculture, education, and cybersecurity. Emerging technologies like edge computing, quantum computing, and natural language processing are expected to shape the future of AI in India. Predictions suggest that AI will continue to disrupt traditional industries, create new job opportunities, and drive economic growth in the country.\n\nConclusion:\nThe rise of AI in India is reshaping various industries and creating new possibilities for innovation and growth. As AI continues to advance, it is essential for businesses, policymakers, and society as a whole to stay informed and engaged with the developments in the AI industry in India. By embracing AI responsibly and ethically, India can harness the transformative power of AI to drive progress, economic prosperity, and societal well-being. Let us all stay vigilant and involved in the exciting journey of AI in India."}
print(final_state['outline'])
I. Introduction
    A. Brief overview of artificial intelligence (AI)
    B. Explanation of the rise of AI in India 
    C. Thesis statement: The increasing adoption of AI in India is reshaping various industries and transforming the country's economic landscape.

II. Current State of AI in India
    A. Overview of AI ecosystem in India
    B. Key players in the AI industry
    C. Government initiatives to promote AI adoption 
    D. Challenges faced by the AI industry in India

III. Industries Impacted by AI in India
    A. Healthcare
        1. AI applications in healthcare 
        2. Benefits of AI in improving healthcare outcomes 
        3. Case studies of successful AI implementations in Indian healthcare sector

    B. Manufacturing
        1. AI use cases in manufacturing 
        2. Impact of AI on production efficiency and cost reduction 
        3. Examples of Indian manufacturing companies leveraging AI technology

    C. Finance
        1. AI applications in the financial sector 
        2. Role of AI in fraud detection and risk management 
        3. Case studies of Indian financial institutions using AI for competitive advantage

IV. Future Trends in AI in India
    A. Potential growth opportunities for AI in India 
    B. Emerging technologies shaping the future of AI 
    C. Predictions for the AI industry in India in the coming years 

V. Conclusion
    A. Recap of key points discussed in the blog
    B. Final thoughts on the rise of AI in India and its implications for the country's economy and society 
    C. Call to action for readers to stay informed and engaged with developments in the AI industry in India
print(final_state['content'])
Artificial Intelligence (AI) has been making massive strides in India in recent years, revolutionizing various industries and shaping the country's economic landscape. From healthcare to finance to manufacturing, AI is being leveraged to drive innovation, improve efficiency, and enhance decision-making processes. In this blog, we will explore the rise of AI in India, its current state, industries impacted by AI, future trends, and the implications for the country's economy and society.

The Current State of AI in India:
India's AI ecosystem has been experiencing rapid growth, with the emergence of various startups, research institutes, and technology giants focusing on AI research and development. Companies like Tata Consultancy Services (TCS), Infosys, Wipro, and startups such as Niki.ai, Niramai, and SigTuple are leading the way in the AI industry in India. The government has also been actively promoting AI adoption through initiatives like the National Strategy for Artificial Intelligence and the National AI Portal, which aim to foster collaboration between industry, academia, and the government.

Despite these developments, the AI industry in India faces challenges such as a shortage of AI talent, lack of data privacy regulations, and concerns about bias and ethics in AI algorithms. Addressing these challenges is crucial to ensure the responsible and sustainable growth of the AI industry in India.

Industries Impacted by AI in India:
AI is making significant inroads in various industries in India, transforming the way businesses operate and deliver services. In healthcare, AI is being used for early disease detection, personalized treatment plans, and medical image analysis. Companies like Practo, Portea Medical, and Mfine are leveraging AI to improve healthcare outcomes and patient care.

In manufacturing, AI is optimizing production processes, predictive maintenance, and quality control. Indian manufacturing companies like Mahindra & Mahindra, Tata Steel, and Hindustan Unilever are embracing AI technology to drive production efficiency and cost reduction.

In finance, AI is revolutionizing fraud detection, credit scoring, and risk management. Indian financial institutions like HDFC Bank, ICICI Bank, and SBI are using AI-powered chatbots, algorithms, and predictive analytics to enhance customer service and gain a competitive edge in the market.

Future Trends in AI in India:
The future of AI in India looks promising, with potential growth opportunities in areas like agriculture, education, and cybersecurity. Emerging technologies like edge computing, quantum computing, and natural language processing are expected to shape the future of AI in India. Predictions suggest that AI will continue to disrupt traditional industries, create new job opportunities, and drive economic growth in the country.

Conclusion:
The rise of AI in India is reshaping various industries and creating new possibilities for innovation and growth. As AI continues to advance, it is essential for businesses, policymakers, and society as a whole to stay informed and engaged with the developments in the AI industry in India. By embracing AI responsibly and ethically, India can harness the transformative power of AI to drive progress, economic prosperity, and societal well-being. Let us all stay vigilant and involved in the exciting journey of AI in India.
Visualize Graph (Optional)
from IPython.display import Image
Image(workflow.get_graph().draw_mermaid_png())

 