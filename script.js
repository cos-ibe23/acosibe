function toggleMenu() {
  const nav = document.getElementById("nav");
  nav.style.display = nav.style.display === "flex" ? "none" : "flex";
}
// Toggle menu
function toggleMenu() {
  const nav = document.getElementById("nav");
  nav.style.display = nav.style.display === "flex" ? "none" : "flex";
}

// Fetch GitHub repos
async function loadProjects() {
  const container = document.getElementById("projects-container");

  if (!container) return;

  const response = await fetch("https://api.github.com/users/cos-ibe23/repos");
  const repos = await response.json();

  repos.slice(0, 6).forEach(repo => {
    const card = document.createElement("div");
    card.className = "card glass";

    card.innerHTML = `
      <i class="ri-github-fill icon"></i>
      <h3>${repo.name}</h3>
      <p>${repo.description || "DevOps project"}</p>
      <a href="${repo.html_url}" target="_blank">View Project</a>
    `;

    container.appendChild(card);
  });
}

loadProjects();

const logs = [
  "Initializing CI pipeline...",
  "Cloning repository...",
  "Running tests...",
  "Building container...",
  "Pushing image...",
  "Deploying to cluster...",
  "✔ Deployment successful"
];

let index = 0;

function runTerminal() {
  const output = document.getElementById("terminal-output");
  if (!output) return;

  setInterval(() => {
    if (index < logs.length) {
      output.innerHTML += logs[index] + "<br>";
      output.scrollTop = output.scrollHeight;
      index++;
    } else {
      output.innerHTML = "";
      index = 0;
    }
  }, 1200);
}

runTerminal();