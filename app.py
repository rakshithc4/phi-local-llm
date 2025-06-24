import subprocess
from duckduckgo_search import DDGS

def load_facts(file_path='facts.txt'):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return ""

def build_prompt(question, facts):
    return f"{facts}\n\nQuestion: {question}\nAnswer:"

def ask_phi(prompt):
    result = subprocess.run(["ollama", "run", "phi"], input=prompt.encode(), capture_output=True)
    return result.stdout.decode()

def looks_uncertain(response):
    cues = ["I don't know", "not sure", "fictitious", "can't answer", "not real"]
    return any(cue in response.lower() for cue in cues)

def web_search(query):
    with DDGS() as ddgs:
        results = ddgs.text(query)
        for r in results:
            return r["body"]
    return "No result found."

def chat():
    facts = load_facts()
    print("Ask anything (type 'exit' to quit):")
    while True:
        question = input("You: ")
        if question.lower() in ["exit", "quit"]:
            break
        prompt = build_prompt(question, facts)
        answer = ask_phi(prompt).strip()
        if looks_uncertain(answer):
            print("(Using web search...)")
            print("Agent:", web_search(question))
        else:
            print("Phi:", answer)

if __name__ == "__main__":
    chat()
