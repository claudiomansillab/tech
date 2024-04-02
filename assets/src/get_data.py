import cv2
import librosa
import numpy as np
from pdf2image import convert_from_path
import os

def extraer_frames_de_video(ruta_video, saltos=30):
    video = cv2.VideoCapture(ruta_video)
    contador = 0
    frames = []
    while video.isOpened():
        ret, frame = video.read()
        if not ret:
            break
        if contador % saltos == 0:
            frames.append(frame)
        contador += 1
    video.release()
    return frames


def extraer_caracteristicas_audio(ruta_audio):
    y, sr = librosa.load(ruta_audio)

    mfcc = librosa.feature.mfcc(y=y, sr=sr)
    return mfcc

def extraer_imagenes_de_pdf_con_pdf2image(pdf_path):
    
    imagenes = convert_from_path(pdf_path)
    
    for i, imagen in enumerate(imagenes):
        img_path = f"pagina_{i+1}.jpg"
        imagen.save(img_path, 'JPEG')
        print(f"Saved image: {img_path}")


def main(pdf_path: str, video_path: str, audio_path: str):

    # Extract pdf images

    

    return


if __name__ == "__main__":
    pdf_path = os.path.join("data", "pdf")
    video_path = os.path.join("data", "videos")
    audio_path = os.path.join("data", "audio")
    main(pdf_path = pdf_path, video_path = video_path, audio_path = audio_path)

