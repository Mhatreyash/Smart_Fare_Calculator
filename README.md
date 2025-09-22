# Smart Fare Calculator

This project provides a "Smart Fare Calculator" to estimate the cost of a taxi or rickshaw ride based on various factors like distance, time, and surge pricing. It comes with two user-friendly interfaces:

1.  **A web-based application** built with Streamlit, featuring interactive inputs and a visual breakdown of the fare.
2.  **A command-line interface (CLI)** built with Rich for a clean, table-based output directly in your terminal.

## Features

-   **Comprehensive Fare Logic**: Calculates fares considering base fare, per-kilometer cost, per-minute cost, and surge multipliers.
-   **Minimum Fare Enforcement**: Ensures the calculated fare never drops below a specified minimum.
-   **Rounding**: The final fare is rounded to the nearest ₹0.50 for convenience.
-   **Interactive Web UI**: The Streamlit app provides an easy-to-use form and visual feedback.
-   **Fare Breakdown Visualization**: The web app displays a pie chart showing the distribution of fare components (base fare, distance charge, etc.).
-   **Elegant CLI**: The command-line version presents the fare breakdown in a beautifully formatted table.

## Project Structure

```
.
├── app.py             # The Streamlit web application
├── main.py            # The command-line interface application
├── requirements.txt   # Python dependencies for the project
├── .gitignore         # Files and directories to be ignored by Git
└── README.md          # This file
```

## Setup and Installation

Follow these steps to get the project running on your local machine.

**1. Clone the Repository**

```sh
git clone <your-repository-url>
cd <your-repository-directory>
```

**2. Create and Activate a Virtual Environment**

It is highly recommended to use a virtual environment to manage project dependencies.

-   **For macOS/Linux:**
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```
-   **For Windows:**
    ```sh
    python -m venv venv
    .\venv\Scripts\activate
    ```

**3. Install Dependencies**

Install all the necessary libraries from the `requirements.txt` file.

```sh
pip install -r requirements.txt
```

## How to Run the Applications

You can run either the web application or the command-line version.

### 1. Running the Streamlit Web App

To start the web-based calculator, run the following command in your terminal:

```sh
streamlit run app.py
```

Your web browser will automatically open with the application running.

### 2. Running the Command-Line App

To use the CLI version, run the `main.py` script:

```sh
python main.py
```

The script will prompt you to enter the fare details directly in the terminal and will output the fare breakdown in a table.
