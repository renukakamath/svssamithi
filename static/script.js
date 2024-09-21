

function speak(text) {
  var synth = window.speechSynthesis;
  var utterance = new SpeechSynthesisUtterance(text);
  synth.speak(utterance);
}

document.getElementById('username').addEventListener('focus', function() {
  speak('Enter your username');
});

document.getElementById('password').addEventListener('focus', function() {
  speak('Enter your password');
});

document.getElementById('firstname').addEventListener('focus', function() {
  speak('Enter your first name');
});

document.getElementById('email').addEventListener('focus', function() {
  speak('Enter your email');
});

document.getElementById('phoneno').addEventListener('focus', function() {
  speak('Enter your phone number');
});

document.getElementById('Confirmpassword').addEventListener('focus', function() {
  speak('Enter your Confirm password');
});

document.addEventListener("contextmenu",(event)=>{
  event.preventDefault();
  })




