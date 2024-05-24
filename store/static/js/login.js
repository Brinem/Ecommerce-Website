document.addEventListener('DOMContentLoaded', function() {
  var loginForm = document.getElementById('login-form');

  loginForm.addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the form from submitting

    var email = document.getElementById('email').value;
    var password = document.getElementById('password').value;

    // Example: Basic validation
    if (email.trim() === '' || password.trim() === '') {
      alert('Please enter both email and password.');
      return;
    }

    // If validation passes, submit the form
    this.submit();
  });
});