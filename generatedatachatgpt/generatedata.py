import openai
import tqdm

# Set your OpenAI API key here
openai.api_key = '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'
print("example of what the command should look like")
print("Write a simple realistic user query:")
print("Write a simple realistic user query for a mental health chatbot but the query can only be one line long:")
print("Write a simple realistic user query for a mental health chatbot but the query can only be one line long also the response can only be one line:")

commandinput = input("write a query for chatgpt to generate data off of:")

def generate_text(prompt, tokens=50):
    response = openai.Completion.create(
      engine="text-davinci-003",  # You can change the engine as needed
      prompt=prompt,
      max_tokens=20  # Adjust the number of tokens (words) as needed
    )
    return response.choices[0].text.strip()

def main():
    num_lines = 500  # Set the number of lines you want to generate

    with open('/Users/blakeweiss/Desktop/generatedatachatgpt/inputs.txt', 'w') as inputs_file, open('/Users/blakeweiss/Desktop/generatedatachatgpt/outputs.txt', 'w') as outputs_file:
        for _ in tqdm.tqdm(range(num_lines), desc="Generating Lines"):
            # Generate a user input
            user_input = generate_text(commandinput)
            inputs_file.write(user_input + '\n')

            # Generate an AI response to the user input
            ai_response = generate_text(user_input)
            outputs_file.write(ai_response + '\n')

if __name__ == "__main__":
    main()
