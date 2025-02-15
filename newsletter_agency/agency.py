from agency_swarm import Agency
from CEOAgent.CEOAgent import CEOAgent
from ResearchAgent.ResearchAgent import ResearchAgent
from ContentCreationAgent.ContentCreationAgent import ContentCreationAgent
from DistributionAgent.DistributionAgent import DistributionAgent

ceo = CEOAgent()
research_agent = ResearchAgent()
content_agent = ContentCreationAgent()
distribution_agent = DistributionAgent()

agency = Agency(
    agency_chart=[
        ceo,
        [ceo, research_agent],
        [ceo, content_agent],
        [ceo, distribution_agent],
        [research_agent, content_agent],
        [content_agent, distribution_agent],
    ],
    shared_instructions="./agency_manifesto.md"
)

if __name__ == "__main__":
    agency.run_demo() 