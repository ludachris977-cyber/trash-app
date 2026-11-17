from flask import Flask, render_template, request

app = Flask(__name__)

# Temporary list to store pickup requests
pickup_requests = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/book', methods=['POST'])
def book_pickup():
    name = request.form.get('name')
    phone = request.form.get('phone')
    latitude = request.form.get('lat')
    longitude = request.form.get('lng')
    
    # Save the order details
    order = {
        "name": name,
        "phone": phone,
        "lat": latitude,
        "lng": longitude,
        "fee": "20.00 Cedis",
        "status": "Pending"
    }
    
    pickup_requests.append(order)
    return f"Success! Booking received for {name}. Fee: 20 Cedis. Our workers have your location."

@app.route('/worker-dashboard')
def worker_dashboard():
    return render_template('worker_dashboard.html')
@app.route('/sw.js')
def service_worker():
    return app.send_static_file('sw.js')
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)