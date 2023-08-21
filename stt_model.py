from faster_whisper import WhisperModel

model_size = "large-v2"

# モデルの初期化と設定
# Run on GPU with FP16
# model = WhisperModel(model_size, device="cuda", compute_type="float16")

# or run on GPU with INT8
# model = WhisperModel(model_size, device="cuda", compute_type="int8_float16")
# or run on CPU with INT8
model = WhisperModel(model_size, device="cpu", compute_type="int8")

def speech_to_text(audio_path):
    segments, info = model.transcribe(audio_path, beam_size=5)
    
    # 検出された言語とその確率を表示するための情報
    language_info = "Detected language '%s' with probability %f\n" % (info.language, info.language_probability)

    # 各セグメントから取得したテキストを結合
    transcriptions = ["[%.2fs -> %.2fs] %s" % (segment.start, segment.end, segment.text) for segment in segments]
    transcription_text = "\n".join(transcriptions)
    
    # 最終的なトランスクリプトを返す
    return language_info + transcription_text
