HTF25-Team-151
Abstract

The HTF25-Team-151 project is designed to provide a robust backend application for data processing and API integration, leveraging the Hugging Face API for confidence and label class. The project separates sensitive API tokens from the codebase using environment variables (.env) and ensures a secure, modular structure for development and deployment.

It is ideal for developers and researchers looking to quickly integrate Hugging Face APIs or build ML-enabled backend services without exposing secret keys.

Features

Hugging Face API integration for confidence and label class.

Modular Python backend (Flask/FastAPI)

Secure storage of API keys using .env

Easy setup and deployment for local and production environments

Installation Instructions
1. Clone the repository
git clone https://github.com/SarvikaSomishetty/HTF25-Team-151.git
cd HTF25-Team-151

2. Create a virtual environment

It’s recommended to use a virtual environment to manage dependencies.

# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate

3. Install dependencies
pip install -r requirements.txt

4. Setup environment variables

Create a .env file in the project root:

HF_TOKEN=your_huggingface_api_token_here


Make sure .env is not committed to GitHub (.gitignore already includes .env).

Running the Project
1. Start the backend server
# Example for Flask
python main.py

2. Run in Streamlit
   python stramlit run app.py
The server should run on http://127.0.0.1:5000 (or specified port).

2. 
