from fastapi import FastAPI, UploadFile, Form
from pathlib import Path
import subprocess

app = FastAPI()

@app.post("/upload/")
async def upload_video(file: UploadFile = None, temp_file_path: str = Form(...)):
   
    temp_dir = Path("temp/")
    temp_dir.mkdir(parents=True, exist_ok=True)

    # Gradioから送信された一時的なパスをprint
    print(f"Temporary path from Gradio: {temp_file_path}")
    uploaded_filepath=temp_file_path
    print(f"Tuploaded_filepath: {uploaded_filepath}")

    filepath = Path(file.filename) # /fuga/../fuga/hoge.mp4
    filename = filepath.name # hoge.mp4
    base_filename= filepath.stem # hoge

    print(f"filepath: {filepath}")
    print(f"filename: {filename}")
    print(f"base_filename: {base_filename}")
    print(f"temp_dir: {temp_dir}")

    
    v_path = temp_dir / filename

    print(f"v_path: {v_path}")

    # with open(v_path, 'wb') as dest_file:
    #     dest_file.write(await file.read())

    # バイナリデータを読み込んで新しい場所に書き込む
    with open(uploaded_filepath, 'rb') as src_file:
        with open(v_path, 'wb') as dest_file:
            dest_file.write(src_file.read())
    
    # ffmpegで音声を分離
    a_filename= base_filename + ".wav"
    a_path = temp_dir / a_filename
    subprocess.run(["ffmpeg", "-i", v_path, "-map", "a", a_path, "-y"])
    return {"audio_path": a_path}
