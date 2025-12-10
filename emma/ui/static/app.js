const statusEl = document.getElementById("status");
const consoleEl = document.getElementById("console");
const micButton = document.getElementById("micButton");
const inputEl = document.getElementById("commandInput");

window.addEventListener("online", () => statusEl.innerText = "Online");
window.addEventListener("offline", () => statusEl.innerText = "Offline");

// Send command
async function sendCommand(text) {
    consoleEl.innerHTML += `<div>> ${text}</div>`;

    let r = await fetch("/process", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({text})
    });

    let data = await r.json();
    consoleEl.innerHTML += `<div style='color:#00b4d8'>${data.response}</div>`;
}

// Keyboard enter
inputEl.addEventListener("keypress", e => {
    if (e.key === "Enter") sendCommand(inputEl.value);
});

// Voice input
micButton.addEventListener("click", () => {
    let rec = new webkitSpeechRecognition();
    rec.lang = "en-US";
    rec.onresult = e => {
        let text = e.results[0][0].transcript;
        inputEl.value = text;
        sendCommand(text);
    };
    rec.start();
});
