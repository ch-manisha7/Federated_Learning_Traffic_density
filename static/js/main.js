function updateValue(name) {
    const slider = document.getElementById(name);
    const label = document.getElementById(name + '_val');
    const value = parseFloat(slider.value);
    
    // Format the value based on the range
    let formattedValue;
    if (value < 1) {
        formattedValue = value.toFixed(2);
    } else if (value < 10) {
        formattedValue = value.toFixed(2);
    } else {
        formattedValue = value.toFixed(2);
    }
    
    label.textContent = formattedValue;
}

// Initialize all values on page load
document.addEventListener('DOMContentLoaded', function() {
    const sliders = document.querySelectorAll('input[type="range"]');
    sliders.forEach(slider => {
        updateValue(slider.id);
    });
});