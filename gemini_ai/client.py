import google.generativeai as genai
import os
from dotenv import load_dotenv

# Carrega a chave do arquivo .env
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Configura a API
genai.configure(api_key=api_key)

def generate_car_description(model, brand, year):
    """
    Gera uma descrição de venda para um carro usando IA.
    """
    try:
        # 1. Definimos a configuração de geração aqui
        config = genai.types.GenerationConfig(
            max_output_tokens=1000,
            temperature=0.7  # Opcional: Define a criatividade (0.0 a 1.0)
        )

        # Instancia o modelo
        # Nota: O nome oficial costuma ser 'gemini-1.5-flash', mas mantive o seu caso esteja usando um alias
        model_ai = genai.GenerativeModel('gemini-flash-latest') 
        
        prompt = f"""
        Escreva um anúncio de venda curto, atraente e persuasivo para um carro.
        Carro: {brand} {model}
        Ano: {year}
        Destaque que é uma ótima oportunidade. use especificacoes tecnicas e pra que érecomendado
        Máximo de 3 linhas.
        """
        
        # 2. Passamos o generation_config na chamada
        response = model_ai.generate_content(prompt, generation_config=config)
        return response.text

    except Exception as e:
        return f"Erro ao gerar descrição: {e}"