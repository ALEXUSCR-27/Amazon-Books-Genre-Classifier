import gradio as gr
import joblib
import time

# For information on how to customize the ChatInterface, peruse the gradio docs: https://www.gradio.app/docs/chatinterface


model = joblib.load('models/svm_model.pkl')

vectorizer = joblib.load('models/vectorizer.pkl') 

def classify_genre(
    title,
    history
):
    title_processed = title.lower()  
    title_vectorized = vectorizer.transform([title_processed]) 
    prediction = model.predict(title_vectorized)
    time.sleep(1)
    return "The Genre predicted is: \n ➥ " + prediction[0] + "\n\nTell me about another title or description to predict.🫡"

chatbot = gr.Chatbot(value=[[None, "👋 Hi, I'm a book genre classifier.\n Tell me about a title or a description and I will predict the genre."]])
theme = gr.themes.Base().set(
    loader_color='*link_text_color_hover'
)
demo = gr.ChatInterface(
    classify_genre,
    title='Books Genre classifier',
    chatbot=chatbot,
    theme=theme,
)

if __name__ == "__main__":
    demo.launch()