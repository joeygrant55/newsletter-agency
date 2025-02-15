from agency_swarm import Agent

class CEOAgent(Agent):
    def __init__(self):
        super().__init__(
            name="CEO",
            description="Responsible for overseeing newsletter production and final approval",
            instructions="./instructions.md",
            tools_folder="./tools",
        ) 