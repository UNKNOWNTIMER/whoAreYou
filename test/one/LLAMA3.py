from openai import OpenAI

def create_openai_client(api_key):
    return OpenAI(
        base_url="https://integrate.api.nvidia.com/v1",
        api_key = api_key
    )

def get_user_input():
    return input("TIMER: ")

def generate_response(client, context):
    try:
        completion = client.chat.completions.create(
            model="meta/llama3-70b-instruct",
            messages=context,
            temperature=0.5,
            top_p=1,
            max_tokens=1024,
            stream=True
        )

        response = ""
        for chunk in completion:
            if chunk.choices[0].delta.content is not None:
                response += chunk.choices[0].delta.content
        return response
    except Exception as e:
        print(f"Error generating response: {e}")
        return "Sorry, there was an error processing your request."

def chat_loop(client):
    context = []

    while True:
        user_input = get_user_input()
        
        if user_input.lower() == "end":
            print("Exiting the chat.")
            break

        context.append({"role": "user", "content": user_input})
        response = generate_response(client, context)
        context.append({"role": "assistant", "content": response})

        print(f"\nCOMPUTER: {response}\n")

def main():
    api_key = "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"  # Replace with your actual API key
    client = create_openai_client(api_key)
    chat_loop(client)

if __name__ == "__main__":
    main()
