# README Evaluator - Snowy

A tool to evaluate GitHub README files against custom standards, created during the Companies House Hackathon by **Team Snowy**.

## Table of Contents
1. [Team](#team)
2. [Project Overview](#project-overview)
3. [Directory Structure](#directory-structure)
4. [Setup](#setup)
5. [Usage](#usage)
6. [Implementation Notes](#implementation-notes)

## Team

- Charlie Boundy
- John Williams
- Lisa Taylor
- Thomas Ferns

*Created for the Companies House Hackathon*

## Project Overview

The README Evaluator is a web application that allows users to paste in the content of a GitHub README file and evaluate it against a set of standards. The app provides feedback on met and unmet criteria, along with suggestions for improvement.

Our original idea was to clone all repositories from the Companies House organization and run metrics across them to gather data on documentation quality. However, due to rate limiting during the hackathon's limited timeframe, we pivoted to this simpler yet effective solution.

## Directory Structure

```
README-Evaluator-Snowy/
│
├── app.py                 # Main Flask application
├── .env.example           # Example environment variables
├── requirements.txt       # Python dependencies
├── bin/
│   └── llama_model.bin    # LLaMA model file (not included)
└── templates/
    └── index.html         # Frontend HTML template
```

## Setup

1. Ensure you have Python 3.9.6 installed..

2. Create and activate a virtual environment:
   ```
   python3.9 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Copy the `.env.example` file to `.env` and adjust the settings as needed:
   ```
   cp .env.example .env
   ```

5. Place your LLaMA model file in the `bin/` directory or specify a custom path in the `.env` file.

## Usage

1. Start the Flask application:
   ```
   python app.py
   ```

2. Open a web browser and navigate to `http://localhost:5000`. (or the port it specifies)

3. Paste your README content into the left text area.

4. (Optional) Modify the README standards in the right text area.

5. Click "Get Feedback" to evaluate the README.

## Implementation Notes

- This was created in a short period of time, and is not guaranteed to work out of the box for you if you run it.
- The application uses the LLaMA model by default. Ensure you have a compatible model file.
- Alternative models (Claude, GPT-4) are stubbed out in the code but not implemented. You can extend these functions if privacy concerns are not an issue.
- The frontend is built using GOV.UK Design System for a clean, accessible interface.
- The application is currently set up for local development and testing. Additional configuration would be needed for production deployment.
