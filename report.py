from google import genai

client = genai.Client(api_key="你的_GEMINI_API_KEY")

def generate_report(text):
    prompt = f"""
    You are an education data analyst.
    Summarize key strengths, weaknesses, and suggestions from these student feedbacks:

    {text}
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    return response.text