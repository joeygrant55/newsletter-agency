from agency_swarm import Agent

class ResearchAgent(Agent):
    def __init__(self):
        super().__init__(
            name="Research",
            description="Researches and analyzes sports tech trends",
            instructions="./instructions.md",
            tools_folder="./tools",
        ) 