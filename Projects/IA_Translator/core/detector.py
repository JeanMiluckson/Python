import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import os

MODEL_PATH = "model/language_detector.pkl"


def treinar_modelo():
    textos = [
        "bom dia", "como vai você", "eu gosto de tecnologia",
        "bonjour", "comment allez-vous", "j'aime la technologie"
    ]
    idiomas = ["pt", "pt", "pt", "fr", "fr", "fr"]

    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(textos)

    model = LogisticRegression()
    model.fit(X, idiomas)

    os.makedirs("model", exist_ok=True)
    joblib.dump((vectorizer, model), MODEL_PATH)

    print("✅ Modelo treinado e salvo com sucesso!")


def detectar_idioma(texto):
    if not os.path.exists(MODEL_PATH):
        print("⚠️ Modelo não encontrado. Treinando agora...")
        treinar_modelo()

    vectorizer, model = joblib.load(MODEL_PATH)
    X = vectorizer.transform([texto])
    return model.predict(X)[0]
