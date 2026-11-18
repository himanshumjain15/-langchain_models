from langchain_core.prompts import PromptTemplate
template = PromptTemplate(
    template= """
Summarize the research paper titled "{paper_input}" using these guidelines:
Explanation Style: {style_input}
Explanation Length: {length_input}
1. Mathematical Details:
   - Include key mathematical equations from the paper if available.
   - Break down the mathematical concepts with simple, intuitive code examples where helpful.
2. Analogies:
   - Include everyday analogies to clarify complex topics.
If any requested detail is missing from the paper, state "Insufficient information available" rather than making assumptions.
Make sure the summary is clear, accurate, and matches the chosen style and length.
""",
input_variables= ["paper_input","style_input","length_input"],
validate_template= True ## to double check if everything is right 
)

template.save("template.json")

## Advantages of prompt template
# Validation
# Reusealbility
# Langchain Ecosystem