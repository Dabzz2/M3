# agents.py
from crewai import Agent, LLM
from textwrap import dedent
from langchain_openai import ChatOpenAI
from langchain_ollama import OllamaLLM
from langchain_community.llms import Ollama
from neo4j import GraphDatabase

# This is an example of how to define custom agents.
# You can define as many agents as you want.
# You can also define custom tasks in tasks.py
class CustomAgents:
    def __init__(self):
        self.OpenAIGPT35 = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)
        self.OpenAIGPT4 = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)
        self.Ollama = LLM(model="ollama/llama3.2", base_url="http://localhost:11434")  # Specify the provider here

        # Initialize Neo4j connection
        self.neo4j_driver = GraphDatabase.driver(
            "neo4j+s://0aa8f456.databases.neo4j.io",  # Update with your Neo4j URI
            auth=("neo4j", "3MsV_P37NaEw0GjM4PLLoV4nQt01irr_wo48HOpd0L4")  # Update with your Neo4j credentials
        )
    def agent_1_name(self):
        return Agent(
            role="Economist specializing in fiscal policy",
            backstory="Experienced economist with expertise in analyzing government spending and taxation policies.",
            goal="To discuss and analyze the impact of fiscal policy on the economy.",
            llm=self.Ollama,  # Using Ollama for diverse insights
        )

    def agent_2_name(self):
        return Agent(
            role="Financial analyst focusing on monetary policy",
            backstory="Specializes in understanding central bank actions and their impact on inflation and economic stability.",
            goal="To evaluate the effect of monetary policy decisions on the economy.",
            llm=self.Ollama,  # Using Ollama for consistency
        )
    
    def agent_3_name(self):
        return Agent(
        role="Trade analyst specializing in international trade policies",
        backstory="Expert in analyzing the effects of trade agreements and tariffs on global and domestic markets.",
        goal="To evaluate how current trade policies influence economic growth and international relations.",
        llm=self.Ollama,
    )

    def agent_4_name(self):
        return Agent(
            role="Data Scientist specializing in knowledge graphs",
            backstory="Expert in leveraging graph databases to uncover insights and answer complex queries.",
            goal="To utilize Neo4j for extracting and analyzing relationships within datasets.",
            llm=self.OpenAIGPT4,
            context_fn=self.get_graph_context
    )

    def get_graph_context(self, question):
        """Fetch context from Neo4j relevant to graph-based questions."""
        query = """
        MATCH (n)-[r]->(m)
        WHERE n.name CONTAINS $keyword OR m.name CONTAINS $keyword
        RETURN n.name AS source, type(r) AS relationship, m.name AS target
        """
        keyword = question.split()[0]  # Simplified keyword extraction
        results = self.query_neo4j(query, {"keyword": keyword})
        context = "\n".join([f"{r['source']} -[{r['relationship']}]-> {r['target']}" for r in results])
        return context

    def close(self):
        """Close the Neo4j connection."""
        self.neo4j_driver.close()