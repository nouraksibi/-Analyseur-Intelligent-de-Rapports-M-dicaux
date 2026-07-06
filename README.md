Le Medical Report Analyzer est un système intelligent basé sur une architecture multi-agents capable d’analyser automatiquement un rapport médical au format PDF et de générer un diagnostic probable.

Le projet repose sur l’utilisation de CrewAI et d’un modèle de langage Gemini, afin de simuler une collaboration entre plusieurs agents spécialisés.

 Ce système est un outil d’aide à la décision médicale et ne remplace en aucun cas un avis médical professionnel.

*  Fonctionnalités principales
1) Extraction automatique du texte depuis un PDF médical
2) Architecture multi-agents avec CrewAI
3) Analyse intelligente avec Gemini LLM
4) Génération de : 
    Diagnostic probable
    Niveau de risque
    Recommandations médicales
5) Interface web interactive avec Streamlit
6) Traitement séquentiel des agents


*Créer un environnement virtuel : 
      python -m venv venv 
Activation :
  Windows :
     venv\Scripts\activate
  Linux / Mac :
    source venv/bin/activate

*Installer les dépendances : 

pip install streamlit
pip install pyyaml
pip install python-dotenv
pip install PyPDF2
pip install crewai
pip install "crewai[google-genai]"
pip install google-generativeai

*Lancer l’application :
streamlit run main.py
