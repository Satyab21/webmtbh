function submitForm() {
    var formElement = document.getElementById('ml_form');
    
    var data = new FormData(formElement);
    fetch('/', {
          method: 'POST',
          body: data,
        })
        .then(response => response.text())
        .then(data => {
          document.getElementById("ml_response").innerHTML = data;
        })
        .catch(error => {
          console.error(error);
        });
}

