import ollama

# Definir el modelo y la consulta
response = ollama.chat(model='deepseek-r1:1.5b', messages=[{'role': 'user', 'content': '¿Qué es DeepSeek?'}])

# Imprimir la respuesta del modelo
print(response['message']['content'])
