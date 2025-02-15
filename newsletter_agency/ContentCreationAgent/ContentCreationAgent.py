from agency_swarm import Agent

class ContentCreationAgent(Agent):
    def __init__(self):
        super().__init__(
            name="Content Creator",
            description="Creates engaging newsletter content from research",
            instructions="./instructions.md",
            tools_folder="./tools",
        ) 