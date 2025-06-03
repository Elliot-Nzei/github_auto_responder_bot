document.addEventListener("DOMContentLoaded", () => {
  fetch("/api/stats")
    .then(res => res.json())
    .then(data => {
      document.getElementById("issues-handled").textContent = data.issues_handled;
      document.getElementById("labels-applied").textContent = data.labels_applied;
    });

  fetch("/api/logs")
    .then(res => res.text())
    .then(log => {
      document.getElementById("log-output").textContent = log;
    });
});