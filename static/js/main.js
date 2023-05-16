function sendText() {
    const inputText = document.getElementById('input-text').value; // Get the text from the input box
  
    // Make an HTTP POST request to the server
    fetch('/process-text', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ text: inputText })
    })
    .then(response => response.json())
    .then(data => {
      // Handle the response from the server, if needed
      console.log(data);
    })
    .catch(error => {
      // Handle any errors that occur during the request
      console.error('Error:', error);
    });
  }
  