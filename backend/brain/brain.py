from typing import Dict


class AIBrain:
    """
    Zentrale Orchestrierung aller KI-Agenten.
    """

    def __init__(self):
        self.agents = {}

    def register_agent(self, name: str, agent):
        self.agents[name] = agent

    def process(self, text: str) -> Dict:
        return {
            "input": text,
            "status": "received",
            "registered_agents": list(self.agents.keys())
        }

        