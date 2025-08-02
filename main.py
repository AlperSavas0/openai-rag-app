from app.loader import load_pdf_text, chunk_text
from app.retriever import create_faiss_index, get_similar_chunks
from app.llm import get_answer
from pathlib import Path

# PDF dosyasının yolu
example_pdf_path = "data/example.pdf"

# PDF dosyasının varlığını kontrol et
if not Path(example_pdf_path).exists():
    print(f"PDF bulunamadı: {example_pdf_path}")
    exit()

# 1. PDF'ten metni oku
print("PDF okunuyor...")
raw_text = load_pdf_text(example_pdf_path)

# 2. Metni parçalara ayır
chunks = chunk_text(raw_text)
print(f"{len(chunks)} adet parça oluşturuldu.")

# 3. Embedding oluştur ve FAISS vektör veritabanına kaydet
print("Embedding oluşturuluyor ve FAISS'e kaydediliyor...")
create_faiss_index(chunks)

# 4. Kullanıcıdan bir örnek soru
question = "Bu belgenin amacı nedir?"

# 5. En benzer metin parçalarını getir
print(f"Soru: {question}")
similar_chunks = get_similar_chunks(question)

# 6. LLM'e bu parçalarla soruyu sor ve yanıt al
answer = get_answer(question, similar_chunks)

# 7. Cevabı yazdır
print("\nYanıt:")
print(answer)
