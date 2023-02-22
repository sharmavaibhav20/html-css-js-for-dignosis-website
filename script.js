const form = document.querySelector('form');

form.addEventListener('submit', (event) => {
  event.preventDefault();
  
  const testType = form.elements['test-type'].value;
  const name = form.elements['name'].value;
  const email = form.elements['email'].value;
  const address = form.elements['address'].value;
  const phone = form.elements['phone'].value;

  fetch('/order-test', {
    method: 'POST',
    body: JSON.stringify({
      testType,
      name,
      email,
      address,
      phone
    }),
    headers: {
      'Content-Type': 'application/json'
    }
  })
  .then(response => response.json())
  .then(data => {
    // handle the response from the server
  });
});
