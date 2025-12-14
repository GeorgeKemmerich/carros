import google.generativeai as genai
import os
from dotenv import load_dotenv

# 1. Carrega o arquivo .env
load_dotenv()

chave = os.getenv('GEMINI_API_KEY')

print(f"--- TESTANDO CHAVE ---")
if not chave:
    print("ERRO: Não encontrei a GEMINI_API_KEY no arquivo .env")
else:
    print(f"Chave lida (início): {chave[:5]}...")
    
    # 2. Configura o Gemini
    genai.configure(api_key=chave)

    print("\n--- MODELOS DISPONÍVEIS NA SUA CONTA ---")
    try:
        # 3. Lista tudo que sua chave permite acessar
        for m in genai.list_models():
            if 'generateContent' in m.supported_generation_methods:
                # O .name geralmente vem como "models/gemini-pro"
                print(f"NOME PARA USAR: {m.name}")
    except Exception as e:
        print(f"DEU ERRO AO CONECTAR: {e}")

print("\n----------------------------------------")