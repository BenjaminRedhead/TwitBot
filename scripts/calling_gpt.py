import openai
class AI_prompt:
    """
    ChatGPT Proompter
    """
    def __init__(self) -> None:
        openai.api_key = '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'

    def write_rap_battle(self, person1, person2) -> str:
        """
        Returns a rap battle between person1 and person1
        """
        messages = [{"role": "system", "content": 
                      "You are a rap battle writer."},
                     {"role": "user", "content":
                      f"Write me a rap battle between {person1} and {person2}"}
              ]
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
        reply = chat.choices[0].message.content
        return reply
        