import streamlit as st
from ultralytics import YOLO
from PIL import Image
import numpy as np
import requests
from datetime import date

st.title("DeFekt.AI - Defect Detection and Classification")
st.subheader("An AI Built For Industrial Quality Assurance")

modelpath = "models/best.pt"
OLLAMA_URL = "http://localhost:11434/api/generate"
OLLAMA_MODEL = "llama3.2"

@st.cache_resource
def load_model():
    return YOLO(modelpath)

model = load_model()


def compute_severity(defects):
    if not defects:
        return "None"
    if len(defects) >= 3 or any(d["confidence"] > 90 for d in defects):
        return "High"
    if len(defects) == 2:
        return "Medium"
    return "Low"


def build_prompt(defects, severity):
    defect_lines = "\n".join(
        f"- {d['label']} ({d['confidence']}% confidence)" for d in defects
    )
    return f"""You are a quality assurance assistant for a steel manufacturing plant.
Given the detected surface defects below, write a concise professional inspection report.

Respond ONLY in this exact format, with no extra text before or after:

Summary:
<2-3 sentence summary of the defects found and their impact>

Recommended Action:
- <action 1>
- <action 2>
- <action 3>
- <action 4>

Detected Defects:
{defect_lines}

Severity (already determined, state exactly as given, do not change it): {severity}
"""


def generate_report(defects, severity):
    prompt = build_prompt(defects, severity)
    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": OLLAMA_MODEL,
                "prompt": prompt,
                "stream": False,
                "options": {"temperature": 0.3}
            },
            timeout=120
        )
        response.raise_for_status()
        return response.json()["response"].strip()
    except requests.exceptions.ConnectionError:
        return "⚠️ Could not connect to Ollama. Make sure `ollama serve` is running."
    except Exception as e:
        return f"⚠️ Error generating report: {e}"


def build_context(defects, severity):
    defect_lines = "\n".join(
        f"- {d['label']} ({d['confidence']}% confidence)" for d in defects
    )
    return f"""You are a quality assurance expert assistant for a steel manufacturing plant.
The following defects were detected in the current inspection:
{defect_lines}
Severity: {severity}

Answer the user's questions about these defects, their causes, risks, and recommended handling.
Keep answers concise and professional."""


def chat_with_llm(user_message, context, history):
    convo = context + "\n\n"
    for turn in history:
        convo += f"User: {turn['user']}\nAssistant: {turn['assistant']}\n"
    convo += f"User: {user_message}\nAssistant:"

    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": OLLAMA_MODEL,
                "prompt": convo,
                "stream": False,
                "options": {"temperature": 0.4}
            },
            timeout=120
        )
        response.raise_for_status()
        return response.json()["response"].strip()
    except requests.exceptions.ConnectionError:
        return "⚠️ Could not connect to Ollama."
    except Exception as e:
        return f"⚠️ Error: {e}"


file = st.file_uploader("Upload an image of the product", type=["jpg", "jpeg", "png", "webp"])

if file is not None:
    # reset chat history when a new file is uploaded
    if st.session_state.get("last_file_id") != file.file_id:
        st.session_state.chat_history = []
        st.session_state.last_file_id = file.file_id

    # Convert uploaded file into a PIL image, then to numpy array for YOLO
    image = Image.open(file).convert("RGB")
    image_array = np.array(image)

    with st.spinner("Detecting defects..."):
        results = model.predict(image_array, conf=0.4)

    r = results[0]
    boxes = r.boxes
    names = model.names

    # Build a clean list of detected defects
    defects = []
    for box in boxes:
        cls_id = int(box.cls[0])
        conf = float(box.conf[0])
        defects.append({
            "label": names[cls_id],
            "confidence": round(conf * 100, 1)
        })

    # Display original vs annotated image side by side
    col1, col2 = st.columns(2)
    with col1:
        st.image(image, caption="Original Image", use_container_width=True)
    with col2:
        annotated_img = r.plot()  # numpy array (BGR) with boxes drawn
        st.image(annotated_img, caption="Detected Defects", channels="BGR", use_container_width=True)

    # Display detected defects as text
    st.markdown("### Detected Defects")
    if defects:
        for d in defects:
            st.markdown(f"- **{d['label']}** ({d['confidence']}%)")
    else:
        st.success("No defects detected.")

    # ---------- INSPECTION REPORT (LLM) ----------
    if defects:
        st.markdown("---")
        st.markdown("## Inspection Report")
        st.markdown(f"**Inspection Date:** {date.today().strftime('%d %B %Y')}")

        severity = compute_severity(defects)

        with st.spinner("Generating inspection report..."):
            report_text = generate_report(defects, severity)
        st.markdown(report_text)

        severity_display = {
            "Low": st.success,
            "Medium": st.warning,
            "High": st.error
        }
        severity_display.get(severity, st.info)(f"Severity: {severity}")

        # ---------- CHATBOT ----------
        st.markdown("---")
        st.markdown("## Ask about this inspection")

        context = build_context(defects, severity)

        for turn in st.session_state.chat_history:
            with st.chat_message("user"):
                st.markdown(turn["user"])
            with st.chat_message("assistant"):
                st.markdown(turn["assistant"])

        user_input = st.chat_input("Ask a question about the detected defects...")
        if user_input:
            with st.chat_message("user"):
                st.markdown(user_input)
            with st.chat_message("assistant"):
                with st.spinner("Thinking..."):
                    answer = chat_with_llm(user_input, context, st.session_state.chat_history)
                st.markdown(answer)
            st.session_state.chat_history.append({"user": user_input, "assistant": answer})

else:
    st.info("Please upload an image to begin inspection.")