import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.environ.get("GOOGLE_AISTUDIO_KEY"))

# Set up the model
generation_config = {
    "temperature": 0.4,
    "top_p": 1,
    "top_k": 32,
    "max_output_tokens": 4096,
}

# safety settings
safety_settings = [
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE",
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE",
    },
]

model = genai.GenerativeModel(
    model_name="gemini-pro-vision",
    generation_config=generation_config,
    safety_settings=safety_settings,
)


def write_caption(image_data, mime_type):
    """
    Writes an instagram caption using the multi-modal model - Google Gemini Pro Vision.
    """
    prompt_parts = [
        "Generate a short captivating and inspiring Instagram post in one paragraph that resonates with users and encourages them to take positive action. The post should include a compelling message, relevant hashtags to maximize its viral potential and impact in Markdown text format.\n",
        {"mime_type": mime_type, "data": image_data},
        "\n",
    ]

    response = model.generate_content(prompt_parts)

    return response.text
