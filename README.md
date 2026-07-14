# Federated Learning Traffic Density Predictor

A web application that predicts urban traffic density using a model trained via **Federated Learning (FedAvg)**, deployed through a Flask interface for real-time, interpretable predictions.

## Overview

This project takes real-world traffic signals — location, weather, time of day, speed, congestion level, and energy metrics — and predicts a traffic density score. Rather than just returning a raw number, the app translates the prediction into a human-readable severity level (Very Low → Very High), explains *why* (peak hour, weather impact, low speed, high congestion), and offers actionable travel recommendations.

The underlying model was trained using a **federated learning (FedAvg)** approach across distributed data partitions, with **differential privacy** for data protection and **LIME-based explainability (XAI)** to keep predictions interpretable — critical for a domain like traffic forecasting where users need to trust and act on the output.

## Features

- 🚦 **Real-time density prediction** from 15 traffic and environmental features
- 🎯 **Severity classification** (Very Low, Low, Moderate, High, Very High) with intuitive color coding
- 🌦️ **Contextual insights** — flags peak-hour periods, weather impact, low-speed congestion, and high energy consumption
- 📱 **Actionable recommendations** — suggests alternate routes, real-time traffic checks, or confirms smooth travel conditions
- 🖥️ **Simple web UI** built with Flask, HTML/CSS, and JavaScript

## Tech Stack

- **Backend:** Python, Flask
- **Model:** Federated Learning (FedAvg), scikit-learn/PyTorch (serialized via pickle/joblib)
- **Frontend:** HTML, CSS, JavaScript
- **Deployment:** Procfile included for platform deployment (e.g. Heroku-style hosting)

## Input Features

| Feature | Description |
|---|---|
| City, Vehicle Type, Weather | Contextual/environmental inputs |
| Economic Condition, Day of Week, Hour of Day | Temporal and socioeconomic signals |
| Speed, Is Peak Hour | Traffic flow indicators |
| Random Event Occurred | Anomaly/incident flag |
| Energy Consumption, Energy Efficiency | Vehicle energy metrics |
| Congestion Level, Peak Traffic Factor, Traffic Pressure | Derived congestion signals |
| FedAvg_pred | Prediction signal from the federated model ensemble |

## How It Works

1. User submits current traffic conditions through the web form.
2. The Flask backend loads the trained model (`model.pkl`) and generates a density prediction.
3. The app interprets the prediction — flagging peak hours, weather effects, congestion, and energy usage — to generate a plain-language explanation.
4. Recommendations are surfaced based on the predicted severity level.

## Setup

```bash
pip install -r requirements.txt
python app.py
```

Visit `http://localhost:5000` in your browser.

## Project Motivation

Centralized traffic prediction models require pooling sensitive location data from all sources. This project explores a **federated learning approach**, where models are trained across distributed nodes without centralizing raw data — improving privacy while maintaining strong predictive performance, and pairing it with explainability tools so predictions remain transparent and trustworthy.
