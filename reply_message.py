import random
from textblob import TextBlob


class ReplyMessage:

    def keyword_matching(self, input_text):
        # Define your keywords and associated responses
        keyword_responses = {
            "python": "I love Python too!",
            "data science": "Data science is a fascinating field.",
            "chatbot": "Chatbots are a great application of AI.",
            "gpt-3": "GPT-3 is a powerful language model."
            # Add more keywords and responses as needed
        }

        # Check if any keyword is present in the input text
        for keyword, response in keyword_responses.items():
            if keyword.lower() in input_text.lower():
                return response

        # If no keyword is found, return a default response
        # return "Interesting."

    def keyword_response(self, input_text):
        # Check for keyword match
        keyword_response = self.keyword_matching(input_text)
        if keyword_response:
            return keyword_response

    def plain_response(self, input_text):
        # Implement your logic to generate a meaningful response here
        # For now, let's create a simple list of responses
        possible_responses = [
            "That's interesting!",
            "Tell me more about that.",
            "I see what you mean.",
            "Interesting perspective!",
            "I'm not sure how to respond to that."
        ]

        # Select a random response from the list
        response = random.choice(possible_responses)

        return response

    def get_sentiment(self, text):
        analysis = TextBlob(text)

        # Check if sentiment analysis was successful
        if analysis.sentiment is not None:
            print(f"analysis: {analysis.sentiment.polarity}")
            return analysis.sentiment.polarity
        else:
            print("Sentiment analysis failed.")
            return 0  # or handle it according to your needs

    def sentiment_response(self, input_text):
        sentiment = self.get_sentiment(input_text)

        # Set a default value for response
        response = None

        if sentiment > 0.4:
            response = "That's great to hear!"
            return response
        elif sentiment < -0.4:
            response = "I'm sorry to hear that."
            return response

        # print(response)
        return response

    def generate_response(self, input_text):

        keyword_response = self.keyword_matching(input_text)
        if keyword_response is not None:
            print("From Keyword I am responding")
            print(keyword_response)
            return keyword_response

        sentiment_response = self.sentiment_response(input_text)
        if sentiment_response is not None:
            print("From Sentiment I am responding")
            print(sentiment_response)
            return sentiment_response

        return self.plain_response(input_text)


if __name__ == "__main__":
    # Example usage
    user_input = input("Enter some text: ")
    reply = ReplyMessage().generate_response(user_input)
    print("Coda:", reply)
