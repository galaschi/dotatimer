var time = {sec: -120, timerStatus: 0}
var timer;

function pad ( val ) {
    if (val < 0) {
        val *= -1;
    }
    return val > 9 ? val : "0" + val;
}

function changeDisplayButton(id, display) {
    document.getElementById(id).style.display = display;
}

function initializeTimer() {
    timer = setInterval( function(){
        document.getElementById("seconds").innerHTML=pad(++time.sec%60);
        document.getElementById("minutes").innerHTML=pad(parseInt(time.sec/60,10));
        getMessage();
    }, 1000);
}

function resetTimer() {
    time.timerStatus = 0;
    time.sec = -120;
    document.getElementById("seconds").innerHTML='00';
    document.getElementById("minutes").innerHTML='00';
    timer = null;
}

function updateTimer(status){
    time.timerStatus = status;
    if (time.timerStatus == 1){
        initializeTimer();
    } else if (time.timerStatus == 2) {
        clearTimeout(timer);
    } else {
        clearTimeout(timer);
        resetTimer();
    }
}

function playTimer(){
    updateTimer(1);
    changeDisplayButton("play","none");
    changeDisplayButton("pause","inline");
    changeDisplayButton("stop","inline");
    changeDisplayButton("fast_backward","inline");
    changeDisplayButton("backward","inline");
    changeDisplayButton("forward","inline");
    changeDisplayButton("fast_forward","inline");
}

function pauseTimer(){
    updateTimer(2);
    changeDisplayButton("play","inline");
    changeDisplayButton("pause","none");
    changeDisplayButton("stop","inline");
}

function stopTimer(){
    updateTimer(3);
    changeDisplayButton("play","inline");
    changeDisplayButton("pause","none");
    changeDisplayButton("stop","none");
    changeDisplayButton("fast_backward","none");
    changeDisplayButton("backward","none");
    changeDisplayButton("forward","none");
    changeDisplayButton("fast_forward","none");
}

function getMessage(){
    for (var i = 0; i < rules["rules"].length; i++){
        if (time.sec == rules["rules"][i].time) {
        message = pad(parseInt(time.sec/60,10))+":"+pad(time.sec%60)+" -> "+rules["rules"][i].message;
        var oldmessage = document.getElementById("message").innerHTML;
        document.getElementById("message").innerHTML=message+'<br>'+oldmessage;
        }
    }
}

function fastBackwardTimer() {
    time.sec -= 10;
}

function backwardTimer() {
    time.sec -= 1;
}

function forwardTimer()  {
    time.sec += 1;
}

function fastForwardTimer() {
    time.sec += 10;
}

function roshanTime() {
    var rosh_kill_time = time.sec;
    var aegis_claim = rosh_kill_time + 300;
    var rosh_respawn_init = rosh_kill_time + 480;
    var rosh_respawn_end = rosh_kill_time + 660;

    rules.rules.push({"time": rosh_kill_time, "message": "Roshan has been Killed!"});
    rules.rules.push({"time": rosh_kill_time, "message": "Aegis will be claimed at: " + formatTime(aegis_claim)});
    rules.rules.push({"time": rosh_kill_time, "message": "Roshan will respawn between " + formatTime(rosh_respawn_init) + " and " + formatTime(rosh_respawn_end)});
    rules.rules.push({"time": aegis_claim , "message": "Aegis expired"});
    rules.rules.push({"time": rosh_respawn_init , "message": "Roshan could have respawned"});
    rules.rules.push({"time": rosh_respawn_end , "message": "Roshan certainly have respawned"});
}

function formatTime(time){
    var seconds = time%60;
    var minutes = (time - seconds)/60;

    if (seconds < 9){
        return minutes + ":0" + seconds;
    } else {
        return minutes + ":" + seconds;
    }
}

