from agency_swarm.tools import BaseTool
from pydantic import Field
import os
import requests
from dotenv import load_dotenv

load_dotenv()

class ContentGeneratorTool(BaseTool):
    """
    Generates newsletter content using Anthropic's Claude API. Creates multiple variations
    and optimizes based on performance data.
    """
    
    research_brief: str = Field(
        ..., 
        description="Structured research brief from TrendAnalysisTool"
    )
    
    def run(self):
        url = "https://api.anthropic.com/v1/messages"
        api_key = os.getenv('ANTHROPIC_API_KEY')
        if not api_key:
            raise Exception("ANTHROPIC_API_KEY not found in environment variables")

        headers = {
            "x-api-key": api_key,
            "anthropic-version": "2023-06-01",
            "Content-Type": "application/json"
        }
        
        # Debug print
        print(f"Using Anthropic API Key: {api_key[:10]}...")
        
        prompt = f"""Generate newsletter content based on this research:
        {self.research_brief}
        
        Create engaging content focused on athlete development and performance:
        1. 3 attention-grabbing subject lines for coaches/athletes
        2. 2 content structures (technical breakdown & practical application)
        3. Main article (500 words) highlighting key innovations
        4. Specific action items for athletes/coaches
        
        Format the content for a professional sports audience."""
        
        payload = {
            "model": "claude-3-5-sonnet-20241022",
            "max_tokens": 2000,
            "messages": [{
                "role": "user",
                "content": prompt
            }],
            "temperature": 0.7
        }
        
        # Debug print
        print(f"Sending request to Anthropic API...")
        
        response = requests.post(url, json=payload, headers=headers)
        
        # Print raw response for debugging
        print(f"Response status: {response.status_code}")
        print(f"Response text: {response.text[:200]}...")  # First 200 chars
        
        if response.status_code != 200:
            raise Exception(f"API Error: {response.status_code} - {response.text}")
            
        response_json = response.json()
        if "content" not in response_json:
            raise Exception("Unexpected API response format")
        
        # Add engaging elements
        structured_content = f"""
        <div class="feature-story">
            <h2>🚨 {self.research_data.get('main_trend')}</h2>
            <p class="hook">{self._generate_attention_hook()}</p>
            
            <div class="case-study">
                <h3>Real-World Impact: {self.research_data.get('case_study_title')}</h3>
                <p>{self.research_data.get('case_study')}</p>
                <blockquote>"{self.research_data.get('expert_quote')}"<br>
                - {self.research_data.get('expert_source')}</blockquote>
            </div>
            
            <div class="tech-breakdown">
                <h3>Under the Hood: How It Works</h3>
                {self._format_technical_details()}
                <div class="infographic-prompt">
                    <!-- Add infographic suggestion for 2-3 key data points -->
                    <p>📊 Visualization Opportunity: {self.research_data.get('key_metric')} performance improvement</p>
                </div>
            </div>
            
            <div class="future-outlook">
                <h3>What's Next: 2025 and Beyond</h3>
                <ul>
                    {self._generate_predictions()}
                </ul>
            </div>
        </div>
        """
        return self._apply_newsletter_template(structured_content)

if __name__ == "__main__":
    tool = ContentGeneratorTool(research_brief="""
        Latest innovations in athlete performance tracking:
        - Wearable tech for real-time biomechanics
        - AI-powered training optimization
        - Recovery monitoring systems
        """)
    print(tool.run()) 