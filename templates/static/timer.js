let time = 60;
let timer = setInterval(() => {
    document.getElementById("time").innerText = time;
    time--;
    if (time < 0) {
        clearInterval(timer);
        document.getElementById("quizForm").submit();
    }
}, 1000);
