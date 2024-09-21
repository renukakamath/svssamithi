
   var audioTracks = [
    '/static/audio/WhatsApp Audio 2024-07-21 at 20.25.50_76c75877.mp3',
    '/static/audio/WhatsApp Audio 2024-07-21 at 20.31.50_29dc0f7c.mp3',
    '/static/audio/WhatsApp Audio 2024-07-22 at 00.42.18_60d368ba.mp3',
    '/static/audio/WhatsApp Audio 2024-07-22 at 22.33.36_8297aefd.waptt'
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