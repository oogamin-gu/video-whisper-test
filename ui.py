import gradio as gr
import requests
from stt_model import speech_to_text

def save_video_ui(uploaded_file):
    # Gradioの一時ファイルのパスを取得
    temp_file_path = uploaded_file.name

    response = requests.post(
        "http://localhost:8000/upload",
        files={"file": uploaded_file},
        data={"temp_file_path": temp_file_path}  # 一時的なパスをデータとして追加
    )
    audio_path = response.json()["audio_path"]
    transcription = speech_to_text(audio_path)

    return transcription

iface = gr.Interface(
    fn=save_video_ui,
    inputs=gr.File(label="Upload a Video"),
    outputs="text"
)

if __name__ == "__main__":
    iface.launch()
