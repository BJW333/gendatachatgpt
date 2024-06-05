import openai
import tqdm
import random

openai.api_key = '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'

def generate_text(prompt, engine="text-davinci-003", max_tokens=30, temperature=0.7):
    try:
        response = openai.Completion.create(
            engine=engine,
            prompt=prompt,
            max_tokens=max_tokens,
            temperature=temperature,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        return response.choices[0].text.strip()
    except Exception as e:
        print(f"Error in generate_text: {e}")
        return None

def main():
    num_lines = 50
    prompts = ["Create a short simple realistic user query for general mental health advice:",
               "Create a short simple user query that is a basic conversational apperication statement:",
               "Create a short simple user query that is a basic conversational greeting statement:",
               "Create a short simple user query that is a basic conversational ending statement:",
               "Create a short simple user query that is a basic conversational acknowledgment statement:"]    
    with open('/Users/blakeweiss/Desktop/generatedatachatgpt/inputs.txt', 'w') as inputs_file, open('/Users/blakeweiss/Desktop/generatedatachatgpt/outputs.txt', 'w') as outputs_file:
        for prompt in prompts:
            for _ in tqdm.tqdm(range(num_lines), desc="Generating Data"):
                #prompt = random.choice(prompts)
                user_input = generate_text(prompt, max_tokens=random.randint(20, 30))
                if user_input:
                    inputs_file.write(user_input + '\n')
                    ai_response = generate_text(user_input, max_tokens=random.randint(20, 30))
                    if ai_response:
                        outputs_file.write(ai_response + '\n')

if __name__ == "__main__":
    main()
