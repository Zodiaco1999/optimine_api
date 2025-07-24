import requests

OPENROUTER_API_KEY = "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"
MODEL = "deepseek/deepseek-r1-0528:free"
API_URL = "https://openrouter.ai/api/v1/chat/completions"

HEADERS = {
    "Authorization": f"Bearer {OPENROUTER_API_KEY}",
    "Content-Type": "application/json",
    "X-Title": "IA-Retroexcavadora"
}

def answer_question(text: str) -> dict:
    prompt_sistema = (
        "Eres un experto técnico en maquinaria pesada, especializado en retroexcavadoras y palas hidráulicas. "
        "Responde cualquier pregunta relacionada con estos equipos, incluyendo sus componentes, partes, repuestos, funcionamiento, mantenimiento, fallas, operación, marcas o modelos. "
        "Si la pregunta trata sobre otra maquinaria no relacionada, responde: 'Lo siento, solo puedo responder sobre retroexcavadoras y palas hidráulicas.'"
    )

    body = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": prompt_sistema},
            {"role": "user", "content": text}
        ],
        "max_tokens": 1024,
        "temperature": 0.2
    }

    try:
        response = requests.post(API_URL, headers=HEADERS, json=body)
        response.raise_for_status()
        content = response.json()["choices"][0]["message"]["content"]
        return {"response": content}
    except Exception as e:
        return {"error": str(e)}
