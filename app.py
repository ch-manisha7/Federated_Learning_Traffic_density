from flask import Flask, render_template, request
import numpy as np
import pickle
from joblib import load

app = Flask(__name__)

# Try both pickle and joblib loaders
try:
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)
except Exception:
    model = load('model.pkl')

def get_traffic_description(prediction, features):
    """Generate detailed description based on prediction and input features"""
    
    # Extract key features
    hour = features[5]
    speed = features[6]
    is_peak = features[7]
    weather = features[2]
    congestion = features[11]
    energy_consumption = features[9]
    
    # Density levels
    if prediction < 0.15:
        density_level = "Very Low"
        emoji = "🟢"
        color_class = "very-low"
    elif prediction < 0.3:
        density_level = "Low"
        emoji = "🟢"
        color_class = "low"
    elif prediction < 0.5:
        density_level = "Moderate"
        emoji = "🟡"
        color_class = "moderate"
    elif prediction < 0.7:
        density_level = "High"
        emoji = "🟠"
        color_class = "high"
    else:
        density_level = "Very High"
        emoji = "🔴"
        color_class = "very-high"
    
    # Build description
    description = []
    
    # Time-based insights
    if 7 <= hour <= 9 or 17 <= hour <= 19:
        description.append("⏰ <strong>Peak Hour Period:</strong> Traffic is typically heavier during morning (7-9 AM) and evening (5-7 PM) rush hours.")
    elif 22 <= hour or hour <= 5:
        description.append("🌙 <strong>Off-Peak Hours:</strong> Late night/early morning typically sees minimal traffic.")
    else:
        description.append("☀️ <strong>Mid-Day Period:</strong> Moderate traffic expected during business hours.")
    
    # Speed analysis
    if speed < 30:
        description.append("🐌 <strong>Low Speed Detected:</strong> Average speed below 30 km/h indicates heavy congestion or stop-and-go traffic.")
    elif speed > 80:
        description.append("⚡ <strong>High Speed Flow:</strong> Average speed above 80 km/h suggests free-flowing traffic conditions.")
    else:
        description.append("🚗 <strong>Normal Speed:</strong> Average speed indicates typical urban traffic flow.")
    
    # Weather impact
    weather_conditions = ["Clear", "Rainy", "Foggy", "Snowy", "Stormy"]
    if int(weather) < len(weather_conditions):
        weather_name = weather_conditions[int(weather)]
        if weather > 1:
            description.append(f"🌧️ <strong>Weather Impact:</strong> {weather_name} conditions may be affecting traffic flow and visibility.")
    
    # Congestion analysis
    if congestion > 0.15:
        description.append("🚦 <strong>High Congestion:</strong> Significant congestion detected. Consider alternate routes.")
    elif congestion > 0.05:
        description.append("⚠️ <strong>Moderate Congestion:</strong> Some slowdowns expected in certain areas.")
    
    # Energy consumption insight
    if energy_consumption > 90:
        description.append("⚡ <strong>High Energy Usage:</strong> Vehicles consuming more energy, possibly due to frequent stops or heavy loads.")
    
    # Recommendations
    recommendations = []
    if prediction > 0.5:
        recommendations.append("🔄 Consider using alternate routes")
        recommendations.append("⏱️ Allow extra travel time")
        recommendations.append("🚇 Use public transportation if available")
    elif prediction > 0.3:
        recommendations.append("📱 Check real-time traffic updates")
        recommendations.append("🕐 Plan for possible delays")
    else:
        recommendations.append("✅ Good time to travel")
        recommendations.append("🚗 Smooth traffic flow expected")
    
    return {
        'density_level': density_level,
        'emoji': emoji,
        'color_class': color_class,
        'description': description,
        'recommendations': recommendations
    }

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        features = [
            float(request.form['City']),
            float(request.form['Vehicle Type']),
            float(request.form['Weather']),
            float(request.form['Economic Condition']),
            float(request.form['Day Of Week']),
            float(request.form['Hour Of Day']),
            float(request.form['Speed']),
            float(request.form['Is Peak Hour']),
            float(request.form['Random Event Occurred']),
            float(request.form['Energy Consumption']),
            float(request.form['Energy Efficiency']),
            float(request.form['Congestion Level']),
            float(request.form['Peak Traffic Factor']),
            float(request.form['Traffic Pressure']),
            float(request.form['FedAvg_pred'])
        ]

        prediction = model.predict([features])[0]
        traffic_info = get_traffic_description(prediction, features)
        
        return render_template('index.html', 
                             prediction=round(prediction, 4),
                             traffic_info=traffic_info)
    except Exception as e:
        return render_template('index.html', error=str(e))

if __name__ == '__main__':
    app.run(debug=True)