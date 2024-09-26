
   var audioTracks = [
    '/static/audio/audio1.mp3',
    '/static/audio/audio2.mp3',
    '/static/audio/audio3.mp3',

];

var audio = new Audio();

function playRandomTrack() {

    var randomTrack = audioTracks[Math.floor(Math.random() * audioTracks.length)];
    
   
    console.log('Playing track:', randomTrack);

 
    audio.src = randomTrack;

   
    audio.addEventListener('canplaythrough', function() {
        audio.play().catch(function(error) {
            console.error('Playback prevented:', error);
        });
    });

    audio.addEventListener('error', function(e) {
        console.error('Error playing audio track:', e);
    });


    audio.addEventListener('ended', function() {
        playRandomTrack();
    });

 
    audio.load();
}


window.onload = function() {
    playRandomTrack();
};

document.addEventListener("contextmenu",(event)=>{
    event.preventDefault();
    })