import ollama

model = "rubberduck"
prompt = "Study guide: "

with open(r"C:\Users\aisha\rubberDucky\backend\studyguide.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        prompt += line

prompt += "\nStudent: "

prompt += "Alkanes are long carbon chains. Organic compounds are mostly oxygen"

client = ollama.Client()
response = client.generate(model=model, prompt=prompt)

print(response.response)