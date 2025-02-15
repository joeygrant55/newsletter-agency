from agency_swarm.tools import BaseTool
from pydantic import Field
import os
import requests
from dotenv import load_dotenv

load_dotenv()

class DistributionManagerTool(BaseTool):
    """
    Prepares newsletter content for BeeHiiv distribution. Formats content
    and provides instructions for manual posting.
    """
    
    content: str = Field(
        ..., 
        description="Final approved newsletter content to distribute"
    )
    
    def run(self):
        formatted_content = {
            "title": "Sports Tech & Performance Update",
            "body": f"<!DOCTYPE html>\n<html>\n<body>\n{self.content}\n</body>\n</html>",
            "subject_line": "Latest in Sports Performance Tech",
            "preview_text": "Cutting-edge developments in athlete development"
        }
        
        instructions = """
        To publish this newsletter in BeeHiiv:
        
        1. Log into BeeHiiv dashboard
        2. Click "Create Post"
        3. Title: {title}
        4. Copy and paste the HTML content below
        5. Set email subject: {subject_line}
        6. Set preview text: {preview_text}
        7. Review and schedule/publish
        
        --- HTML Content Below ---
        
        {body}
        """
        
        # For future API integration:
        # api_url = "https://api.beehiiv.com/v2/posts"
        # headers = {"Authorization": f"Bearer {os.getenv('BEEHIIV_API_KEY')}"}
        # response = requests.post(api_url, json=formatted_content, headers=headers)
        # return response.json()
        
        return instructions.format(**formatted_content)

if __name__ == "__main__":
    tool = DistributionManagerTool(content="""
        <h1>Breaking: New Recovery Tech</h1>
        <p>Researchers discover...</p>
        <ul>
            <li>Wearable muscle sensors</li>
            <li>AI-powered recovery algorithms</li>
        </ul>
    """)
    print(tool.run()) 