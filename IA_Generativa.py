from transformers import pipeline

model_name = "pierreguillou/bert-base-cased-squad-v1.1-portuguese"

# Cria pipeline de QA
qa_pipeline = pipeline(
  "question-answering",
  model=model_name,
  tokenizer=model_name
)

contexto = """
O Brasil é um país da América do Sul.
Capital: Brasília
Moeda: Real
Receita de bolo simples: 2 xícaras de farinha, 3 ovos, 1 xícara de leite
"""

def responder(pergunta):
  try:
    resultado = qa_pipeline(question=pergunta, context=contexto)
    return resultado['answer']
  except Exception as e:
    return f"Erro ao responder: {str(e)}"

# Testes
print(responder("Qual é a capital do Brasil?"))
print(responder("Qual é a moeda do Brasil?"))
print(responder("Qual é a receita de bolo simples?"))