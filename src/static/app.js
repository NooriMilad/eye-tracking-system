let socket = io.connect('http://' + document.domain + ':' + location.port);
let eyeX = 0;
let eyeY = 0;
let video;

function setup() {
    let canvas = createCanvas(800, 600);
    canvas.parent('canvas-container');
    background(255);

    // Zugriff auf die Kamera
    video = createCapture(VIDEO);
    video.size(800, 600);
    video.parent('video-container');  // Video in den video-container einfügen
    video.hide();

    socket.on('eye_data', function(data) {
        updateEyePosition(data.x, data.y);
    });
}

function draw() {
    background(255);
    image(video, 0, 0, width, height);  // Zeichne den Kamerastream auf das Canvas
    fill(0);
    ellipse(eyeX, eyeY, 50, 50);  // Zeichne den Punkt basierend auf Eye-Tracking-Daten
}

function updateEyePosition(x, y) {
    eyeX = x;
    eyeY = y;
}