from typing import List
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=openai_api_key)

def get_answer(question:str, context_chunks:List[str]) -> str:
    """
    Answer a question using relavent context chunks.

    Args:
        question (str): The user's question.
        context_chunks (list[str]): Relevant text chunks retreieved from vector DB.

    Returns:
        str: The LLM-generated answer.
    """
    context_text= "\n\n".join(context_chunks)

    system_prompt = (
         "Aşağıda bir kullanıcının sorusu ve bu soruyla ilgili bazı belgelerden alınmış bağlam parçaları verilmiştir.\n"
         "Soruyu yalnızca bu bağlamlara dayanarak, açık ve doğru bir şekilde TÜRKÇE yanıtla.\n"
         "Belgeyi hazırlayanların isimleri genelde başlarda veya sonlarda bulunur ve birden fazla yazarı olabilir; bu tür bilgileri tanımaya özellikle dikkat et.\n"
         "Eğer bağlamda yeterli bilgi yoksa, varsayımda bulunma ve şu şekilde cevap ver: "
         "'Bu soruya mevcut belge içeriğine göre cevap veremem.'\n"
    )

    response= client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"Bağlam:\n{context_text}\n\nSoru: {question}"},
            
        ],
        temperature=0.3,
    )       
    
    return response.choices[0].message.content.strip()