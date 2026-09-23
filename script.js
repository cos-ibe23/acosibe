
function toggleMenu() {
  const nav = document.getElementById("nav");

  if (!nav) return;

  nav.classList.toggle("open");
}


/*
 * Close mobile navigation after selecting a link.
 */
document.querySelectorAll("#nav a").forEach((link) => {
  link.addEventListener("click", () => {
    const nav = document.getElementById("nav");

    if (nav) {
      nav.classList.remove("open");
    }
  });
});


/*
 * CI/CD terminal animation.
 */
const logs = [
  "$ git push origin main",
  "→ GitHub Actions workflow triggered",
  "→ Installing dependencies...",
  "→ Running tests...",
  "→ Building application...",
  "→ Deployment workflow completed",
  "✓ Pipeline completed successfully"
];

let logIndex = 0;

function runTerminal() {

  const output = document.getElementById("terminal-output");

  if (!output) return;

  setInterval(() => {

    if (logIndex < logs.length) {

      output.innerHTML += `${logs[logIndex]}<br>`;

      output.scrollTop = output.scrollHeight;

      logIndex++;

    } else {

      output.innerHTML = "";

      logIndex = 0;

    }

  }, 1000);
}

runTerminal();
