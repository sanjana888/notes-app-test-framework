import random
import string


class MCPUtils:

    @staticmethod
    def generate_note_title():

        random_text = ''.join(
            random.choices(string.ascii_uppercase, k=5)
        )

        return f"MCP_Note_{random_text}"

    @staticmethod
    def generate_note_description():

        descriptions = [
            "Generated using MCP utility",
            "AI assisted test data",
            "Dynamic automation data",
            "Smart generated content"
        ]

        return random.choice(descriptions)

    @staticmethod
    def suggest_locator():

        return {
            "primary_locator": "//button[text()='Save']",
            "fallback_locator": "//button[contains(text(),'Save')]"
        }

    @staticmethod
    def analyze_failure(error_message):

        if "NoSuchElementException" in error_message:
            return "Locator issue detected"

        if "TimeoutException" in error_message:
            return "Application loading issue"

        return "General automation failure"
