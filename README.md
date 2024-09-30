
# Fake Social Media Detection

## Overview

This project is designed to identify fake social media accounts by analyzing various attributes such as follower count, following count, profile images, background images, the network of followers and followings, posting frequency, and types of posts. The detection model is implemented using the Random Forest algorithm and trained on a large dataset.

The project consists of two main components:

1. **Data Collection (Python):** Utilizes Tweepy library to gather details of user accounts from Twitter, including follower and following information, profile and background images, and post insights.

2. **Detection Model (Python):** Implements a Random Forest algorithm to train and predict fake social media accounts based on the collected data. The trained model is saved using Pickle.

3. **Web App (Node.js):** A graphical user interface is created using Node.js to showcase the detection results. The web app allows users to input a Twitter username and receive a prediction regarding the authenticity of the account.

![image](https://github.com/Sumitpathak721/Fake-Account-detection/assets/98797074/17392530-f022-4065-a052-2bab4ab59019)


## Prerequisites

- Python 3.x
- Node.js
- Tweepy library (`pip install tweepy`)
- Scikit-learn library (`pip install scikit-learn`)

## Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/<your-username>/Fake-Account-Detection.git
## Installation

1. **Install Python dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

2. **Install Node.js dependencies:**

    ```bash
    npm install
    ```

3. **Run the web app:**

    ```bash
    node index.js
    ```

    The web app will be accessible at [http://localhost:3000](http://localhost:3000) in your web browser.

## Usage

1. Run the data collection script to gather user details:

    ```bash
    python Checker.py
    ```

2. Train the detection model:

    ```bash
    python model.py
    ```

3. Open the web app and input a Twitter username to get the detection results.

## Contributer 

- Sujeet Sharma

