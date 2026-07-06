import os
os.environ["OTEL_SDK_DISABLED"] = "true"

import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from crewai import Agent, Task, Crew, LLM
import yaml

# ==============================
# CONFIGURATION
# ==============================
load_dotenv()

gemini_llm = LLM(
    model="gemini-2.5-flash",
    api_key=os.environ["GEMINI_API_KEY"],
    temperature=0.2
)


# ==============================
# PDF READER
# ==============================
def get_pdf_text(pdf_file):
    text = ""
    try:
        reader = PdfReader(pdf_file)
        for page in reader.pages:
            content = page.extract_text()
            if content:
                text += content
        return text
    except Exception as e:
        st.error(f"Erreur lecture PDF : {e}")
        return None

# ==============================
# STREAMLIT APP
# ==============================
def main():
    st.set_page_config(page_title="Analyseur Médical IA", layout="wide", page_icon="🩺")

    st.title("🩺 Analyseur Intelligent de Rapports Médicaux")
    st.markdown("---")

    # ==============================
    # SIDEBAR
    # ==============================
    with st.sidebar:
        st.header("📂 Téléchargement")
        uploaded_file = st.file_uploader("Choisissez un rapport PDF", type="pdf")

    if uploaded_file:
        report_text = get_pdf_text(uploaded_file)

        if report_text:
            st.success("✅ Rapport chargé avec succès")

            if st.button("🚀 Lancer l'Analyse"):

                try:
                    # ==============================
                    # Charger YAML
                    # ==============================
                    with open("config/agents.yaml", "r", encoding="utf-8") as f:
                        agents_config = yaml.safe_load(f)

                    with open("config/tasks.yaml", "r", encoding="utf-8") as f:
                        tasks_config = yaml.safe_load(f)

                    # ==============================
                    # Affichage des Agents actifs
                    # ==============================
                    st.markdown("## 👥 Agents Actifs")

                    for name, config in agents_config.items():
                        with st.expander(f"🔹 {name}", expanded=False):
                            st.write("**Rôle :**", config["role"])
                            st.write("**Objectif :**", config["goal"])

                    # ==============================
                    # Création Agents
                    # ==============================
                    medical_data_extractor = Agent(
                        **agents_config["medical_data_extractor"],
                        llm=gemini_llm
                    )

                    medical_diagnostic_agent = Agent(
                        **agents_config["medical_diagnostic_agent"],
                        llm=gemini_llm
                    )

                    # ==============================
                    # EXECUTION LIVE
                    # ==============================
                    with st.status("🧠 Analyse en cours...", expanded=True) as status:

                        # -------- Extraction --------
                        status.write("🤖 Agent Extracteur : Lecture et structuration...")

                        task1 = Task(
                            description=tasks_config["extraction_task"]["description"].format(
                                report_text=report_text
                            ),
                            expected_output=tasks_config["extraction_task"]["expected_output"],
                            agent=medical_data_extractor
                        )

                        crew1 = Crew(
                            agents=[medical_data_extractor],
                            tasks=[task1],
                            verbose=True
                        )

                        summary_result = crew1.kickoff()

                        status.write("✅ Extraction terminée")

                        # -------- Diagnostic --------
                        status.write("👨‍⚕️ Agent Diagnostiqueur : Analyse médicale...")

                        task2 = Task(
                            description=tasks_config["diagnostic_task"]["description"].format(
                                summary=summary_result.raw
                            ),
                            expected_output=tasks_config["diagnostic_task"]["expected_output"],
                            agent=medical_diagnostic_agent
                        )

                        crew2 = Crew(
                            agents=[medical_diagnostic_agent],
                            tasks=[task2],
                            verbose=True
                        )

                        final_diagnostic = crew2.kickoff()

                        status.write("✅ Diagnostic terminé")
                        status.update(label="🎉 Analyse complète", state="complete")

                    # ==============================
                    # AFFICHAGE RÉSULTATS
                    # ==============================
                    st.markdown("## 📊 Résultats de l'analyse")

                    col1, col2 = st.columns(2)

                    with col1:
                        st.subheader("📋 Données Extraites")
                        st.info(summary_result.raw)

                    with col2:
                        st.subheader("🩺 Diagnostic Final")
                        st.success(final_diagnostic.raw)

                except Exception as e:
                    st.error(f"❌ Erreur pendant l'analyse : {e}")

if __name__ == "__main__":
    main()