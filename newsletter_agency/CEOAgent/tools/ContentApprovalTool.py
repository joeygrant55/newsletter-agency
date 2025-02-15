from agency_swarm.tools import BaseTool
from pydantic import Field

class ContentApprovalTool(BaseTool):
    """
    Manages user approval process for newsletter content and strategy decisions.
    Facilitates human-in-the-loop validation at critical workflow stages.
    """
    
    approval_prompt: str = Field(
        ..., 
        description="Specific item requiring user approval (e.g., topic list, draft content)"
    )
    
    def run(self):
        return f"USER APPROVAL REQUIRED:\n{self.approval_prompt}\n\nRespond with 'APPROVED' or provide feedback."

if __name__ == "__main__":
    tool = ContentApprovalTool(approval_prompt="Sample approval request")
    print(tool.run()) 