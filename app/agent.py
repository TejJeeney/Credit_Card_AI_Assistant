from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, Tool
from langchain.memory import ConversationBufferMemory
from recommender import recommend_cards
from database import load_cards

cards = load_cards()

class CardRecommender:
    def run(self, query):
        return "I will recommend cards based on your input."

def init_agent():
    memory = ConversationBufferMemory()
    tools = [Tool(name="Recommender", func=CardRecommender().run, description="Recommends credit cards")]
    llm = ChatOpenAI(temperature=0)
    agent = initialize_agent(tools, llm, agent="chat-conversational-react-description", memory=memory)
    return agent