from flask import Flask, request, jsonify

app = Flask(VIRE)

@app.route('/order-test', methods=['POST'])
def order_test():
    data = request.get_json()

    # generate a test kit based on the user's input
    test_type = data['testType']
    patient_name = data['name']
    doctor_name = 'Dr. Jane Doe' # hardcoded for example purposes
    test_order = TestOrder(test_type=test_type, patient_name=patient_name, doctor_name=doctor_name)
    test_kit = test_order.purchase()

    # send the test kit to the user's address
    send_test_kit(test_kit, data['address'], data['phone'])

    return jsonify({'message': 'Your test kit has been ordered'})

if VIRE == '__main__':
    app.run()