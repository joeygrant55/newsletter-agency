from agency_swarm import Agent

class DistributionAgent(Agent):
    def __init__(self):
        super().__init__(
            name="Distribution",
            description="Handles newsletter distribution and delivery",
            instructions="./instructions.md",
            tools_folder="./tools",
        ) 