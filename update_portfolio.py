from pathlib import Path
import re

ROOT = Path(__file__).parent

# -----------------------------
# Common information
# -----------------------------
NAME = "Anointed Cos-Ibe"
EMAIL = "cosibeanointed23@gmail.com"
LOCATION = "Lagos, Nigeria"

LINKEDIN = "https://www.linkedin.com/in/anointed-cos-ibe"
GITHUB = "https://github.com/cos-ibe23"
PORTFOLIO = "https://acosibe.onrender.com"
MIRA = "https://miraessentials.onrender.com"
CI_PIPELINE = "https://github.com/cos-ibe23/docker-ci-pipeline"
CREDLY = "https://www.credly.com/badges/5d93a83b-6759-49db-b37b-9b6895bdb4a2/public_url"


# ============================================================
# INDEX.HTML
# ============================================================

index_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>{NAME} | Cloud Engineer & DevOps Engineer</title>

<meta name="description"
      content="Portfolio of {NAME}, Cloud Engineer and DevOps Engineer specializing in cloud infrastructure, automation, Terraform, Kubernetes, CI/CD and monitoring.">

<link rel="stylesheet" href="style.css">
<link href="https://cdn.jsdelivr.net/npm/remixicon/fonts/remixicon.css" rel="stylesheet">
</head>

<body>

<header>
  <a href="index.html" class="logo">{NAME}</a>

  <button class="menu-toggle" onclick="toggleMenu()" aria-label="Toggle navigation">
    <i class="ri-menu-line"></i>
  </button>

  <nav id="nav">
    <a href="index.html">Home</a>
    <a href="resume.html">Resume</a>
    <a href="projects.html">Projects</a>
    <a href="{LINKEDIN}" target="_blank" rel="noopener">LinkedIn</a>
  </nav>
</header>


<main>

<section class="hero fade-in">

  <div class="hero-content">

    <p class="eyebrow">
      CLOUD ENGINEERING · DEVOPS · INFRASTRUCTURE AUTOMATION
    </p>

    <h1>
      Cloud Engineer
      <span>/</span>
      DevOps Engineer
    </h1>

    <p class="hero-description">
      I build reliable cloud infrastructure, automate deployments,
      and create repeatable engineering workflows using modern
      cloud and DevOps technologies.
    </p>

    <div class="buttons">
      <a href="projects.html" class="btn">
        View Projects
      </a>

      <a href="resume.html" class="btn secondary">
        View Resume
      </a>
    </div>

  </div>

  <div class="image-container">
    <img src="images/My picc .jpg" alt="{NAME}">
  </div>

</section>


<section class="stats-section fade-in">

  <div class="stat-card">
    <strong>40%</strong>
    <span>Deployment Efficiency Improvement</span>
  </div>

  <div class="stat-card">
    <strong>60%</strong>
    <span>Infrastructure Setup Time Reduction</span>
  </div>

  <div class="stat-card">
    <strong>3x</strong>
    <span>GCP Certified</span>
  </div>

</section>


<section class="about section-container fade-in">

  <div class="section-heading">
    <p class="eyebrow">ABOUT ME</p>
    <h2>Building and automating cloud infrastructure.</h2>
  </div>

  <div class="about-content">

    <p>
      I'm {NAME}, a Cloud Engineer and DevOps Engineer with a background
      in Computer Science and hands-on experience working with cloud
      infrastructure, Linux systems, automation, CI/CD and containerized
      environments.
    </p>

    <p>
      My work focuses on making infrastructure more reliable,
      repeatable and efficient through Infrastructure as Code,
      configuration management, deployment automation and cloud-native
      technologies.
    </p>

    <div class="socials">

      <a href="{GITHUB}" target="_blank" rel="noopener">
        <i class="ri-github-fill"></i>
        GitHub
      </a>

      <a href="{LINKEDIN}" target="_blank" rel="noopener">
        <i class="ri-linkedin-box-fill"></i>
        LinkedIn
      </a>

      <a href="mailto:{EMAIL}">
        <i class="ri-mail-line"></i>
        Email
      </a>

    </div>

  </div>

</section>


<section class="skills-section section-container fade-in">

  <div class="section-heading">
    <p class="eyebrow">TECHNOLOGY</p>
    <h2>Tools I work with</h2>
  </div>

  <div class="skills-grid">

    <div class="skill-card">
      <i class="ri-cloud-line"></i>
      <h3>Cloud Platforms</h3>
      <p>AWS · Google Cloud · Azure</p>
    </div>

    <div class="skill-card">
      <i class="ri-terminal-box-line"></i>
      <h3>Linux & Scripting</h3>
      <p>Python · Bash · PowerShell · Shell · SQL · CLI</p>
    </div>

    <div class="skill-card">
      <i class="ri-code-box-line"></i>
      <h3>Infrastructure as Code</h3>
      <p>Terraform · Ansible · Pulumi · HCL</p>
    </div>

    <div class="skill-card">
      <i class="ri-box-3-line"></i>
      <h3>Containers</h3>
      <p>Docker · Kubernetes · Nomad · Helm</p>
    </div>

    <div class="skill-card">
      <i class="ri-git-branch-line"></i>
      <h3>DevOps</h3>
      <p>GitHub Actions · Jenkins · Git · GitHub</p>
    </div>

    <div class="skill-card">
      <i class="ri-line-chart-line"></i>
      <h3>Observability</h3>
      <p>Prometheus · Grafana · Loki · Alloy · Cloud Monitoring</p>
    </div>

  </div>

</section>


<section class="experience section-container fade-in">

  <div class="section-heading">
    <p class="eyebrow">EXPERIENCE</p>
    <h2>Cloud Engineering</h2>
  </div>

  <div class="experience-card">

    <div class="experience-header">
      <div>
        <h3>Cloud Engineer</h3>
        <p>Imbod · Lagos, Nigeria</p>
      </div>

      <span>July 2025 – Present</span>
    </div>

    <ul>

      <li>
        Configured and maintained Linux-based application servers
        on Google Compute Engine, ensuring secure and reliable deployments.
      </li>

      <li>
        Automated infrastructure provisioning and configuration management
        with Terraform and Ansible, increasing deployment efficiency by
        <strong>40%</strong>.
      </li>

      <li>
        Delivered cloud solutions with Terraform, minimizing infrastructure
        setup time by <strong>60%</strong> using reusable Terraform modules.
      </li>

      <li>
        Supported systems integration, networking and security configuration
        across cloud workloads.
      </li>

    </ul>

  </div>

</section>


<section class="featured-project section-container fade-in">

  <div class="section-heading">
    <p class="eyebrow">FEATURED PROJECT</p>
    <h2>Mira Essentials</h2>
  </div>

  <div class="project-feature">

    <div>

      <span class="project-label">
        FULL-STACK E-COMMERCE APPLICATION
      </span>

      <h3>Production-ready commerce platform</h3>

      <p>
        Built and deployed a production-ready e-commerce application
        with a React/Vite frontend and Node.js/Express backend.
      </p>

      <p>
        Implemented product variants, carts, checkout, customer order
        tracking, Paystack payments, bank-transfer confirmation workflows,
        and an admin dashboard.
      </p>

      <p>
        PostgreSQL and Prisma ORM power product, order, payment and
        customer data management.
      </p>

      <div class="tech-tags">
        <span>React</span>
        <span>Vite</span>
        <span>Node.js</span>
        <span>Express</span>
        <span>PostgreSQL</span>
        <span>Prisma</span>
        <span>Paystack</span>
      </div>

      <a href="{MIRA}" target="_blank" rel="noopener" class="btn">
        View Live Project →
      </a>

    </div>

  </div>

</section>


<section class="certification section-container fade-in">

  <div class="certification-card">

    <div>
      <p class="eyebrow">CERTIFICATION</p>

      <h2>Google Cloud Certified</h2>

      <p>
        Associate Cloud Engineer
      </p>
    </div>

    <a href="{CREDLY}" target="_blank" rel="noopener" class="btn">
      Verify Credential →
    </a>

  </div>

</section>

</main>


<footer>

  <div>
    <strong>{NAME}</strong>
    <p>Cloud Engineer · DevOps Engineer</p>
  </div>

  <div class="footer-links">

    <a href="{GITHUB}" target="_blank" rel="noopener">GitHub</a>

    <a href="{LINKEDIN}" target="_blank" rel="noopener">LinkedIn</a>

    <a href="mailto:{EMAIL}">Email</a>

  </div>

  <p class="copyright">
    © 2026 {NAME}
  </p>

</footer>


<script src="script.js"></script>

</body>
</html>
"""

(ROOT / "index.html").write_text(index_html, encoding="utf-8")


# ============================================================
# PROJECTS.HTML
# ============================================================

projects_html = f"""<!DOCTYPE html>
<html lang="en">
<head>

<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>Projects | {NAME}</title>

<meta name="description"
      content="Cloud, DevOps and software engineering projects by {NAME}.">

<link rel="stylesheet" href="style.css">
<link href="https://cdn.jsdelivr.net/npm/remixicon/fonts/remixicon.css" rel="stylesheet">

</head>

<body>

<header>

  <a href="index.html" class="logo">{NAME}</a>

  <button class="menu-toggle" onclick="toggleMenu()" aria-label="Toggle navigation">
    <i class="ri-menu-line"></i>
  </button>

  <nav id="nav">

    <a href="index.html">Home</a>

    <a href="resume.html">Resume</a>

    <a href="projects.html">Projects</a>

    <a href="{LINKEDIN}" target="_blank" rel="noopener">
      LinkedIn
    </a>

  </nav>

</header>


<main class="content">

  <section class="page-hero">

    <p class="eyebrow">SELECTED WORK</p>

    <h1>Projects</h1>

    <p class="intro">
      A selection of projects demonstrating cloud engineering,
      DevOps automation and full-stack application development.
    </p>

  </section>


  <section class="projects-grid">


    <article class="project-card featured-project-card">

      <div class="project-icon">
        <i class="ri-shopping-bag-3-line"></i>
      </div>

      <div class="project-content">

        <span class="project-label">
          FULL-STACK APPLICATION
        </span>

        <h2>Mira Essentials</h2>

        <p>
          Production-ready e-commerce application built with
          React/Vite and Node.js/Express.
        </p>

        <ul>

          <li>
            Product variants, carts and checkout
          </li>

          <li>
            Customer order tracking
          </li>

          <li>
            Paystack payment integration
          </li>

          <li>
            Bank-transfer payment confirmation workflow
          </li>

          <li>
            Admin dashboard
          </li>

          <li>
            PostgreSQL + Prisma ORM
          </li>

        </ul>

        <div class="tech-tags">
          <span>React</span>
          <span>Vite</span>
          <span>Node.js</span>
          <span>Express</span>
          <span>PostgreSQL</span>
          <span>Prisma</span>
        </div>

        <a href="{MIRA}"
           target="_blank"
           rel="noopener"
           class="project-link">

          View Live Project
          <i class="ri-arrow-right-up-line"></i>

        </a>

      </div>

    </article>


    <article class="project-card">

      <div class="project-icon">
        <i class="ri-git-merge-line"></i>
      </div>

      <div class="project-content">

        <span class="project-label">
          CI/CD AUTOMATION
        </span>

        <h2>CI Pipeline Automation</h2>

        <p>
          Continuous integration pipeline using GitHub Actions
          to automate testing and deployment for a demo application.
        </p>

        <ul>

          <li>
            Integrated Git and GitHub for version control
          </li>

          <li>
            Automated CI workflow with GitHub Actions
          </li>

          <li>
            Automated application testing
          </li>

          <li>
            Automated deployment workflow
          </li>

        </ul>

        <div class="tech-tags">
          <span>Git</span>
          <span>GitHub</span>
          <span>GitHub Actions</span>
          <span>Docker</span>
          <span>CI/CD</span>
        </div>

        <a href="{CI_PIPELINE}"
           target="_blank"
           rel="noopener"
           class="project-link">

          View GitHub Repository
          <i class="ri-arrow-right-up-line"></i>

        </a>

      </div>

    </article>


  </section>


  <section class="impact-section">

    <div class="section-heading">
      <p class="eyebrow">ENGINEERING IMPACT</p>
      <h2>Automation with measurable results</h2>
    </div>

    <div class="metrics">

      <div class="metric">
        <strong>40%</strong>
        <span>Deployment efficiency improvement</span>
      </div>

      <div class="metric">
        <strong>60%</strong>
        <span>Infrastructure setup-time reduction</span>
      </div>

    </div>

  </section>


  <section class="pipeline-section">

    <div class="terminal-box">

      <div class="terminal-header">
        <span>devops@pipeline:~</span>
        <span>● ● ●</span>
      </div>

      <div id="terminal-output"></div>

    </div>

    <div class="pipeline">

      <div>Code</div>
      <span>→</span>

      <div>Build</div>
      <span>→</span>

      <div>Test</div>
      <span>→</span>

      <div>Deploy</div>

    </div>

  </section>


  <a href="index.html" class="btn secondary">
    ← Back Home
  </a>

</main>


<script src="script.js"></script>

</body>
</html>
"""

(ROOT / "projects.html").write_text(projects_html, encoding="utf-8")


# ============================================================
# RESUME.HTML
# ============================================================

resume_html = f"""<!DOCTYPE html>
<html lang="en">

<head>

<meta charset="UTF-8">

<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>Resume | {NAME}</title>

<link rel="stylesheet" href="style.css">

</head>

<body>

<header>

  <a href="index.html" class="logo">{NAME}</a>

  <nav class="desktop-nav">

    <a href="index.html">Home</a>
    <a href="projects.html">Projects</a>
    <a href="{LINKEDIN}" target="_blank" rel="noopener">LinkedIn</a>

  </nav>

</header>


<main class="resume-page">

  <section class="resume-header">

    <p class="eyebrow">
      CLOUD ENGINEER · DEVOPS ENGINEER
    </p>

    <h1>{NAME}</h1>

    <p>
      {LOCATION} · {EMAIL}
    </p>

    <div class="resume-links">

      <a href="{LINKEDIN}" target="_blank" rel="noopener">
        LinkedIn
      </a>

      <a href="{GITHUB}" target="_blank" rel="noopener">
        GitHub
      </a>

      <a href="{PORTFOLIO}" target="_blank" rel="noopener">
        Portfolio
      </a>

      <a href="resume-ats.html">
        ATS Resume
      </a>

    </div>

    <a href="resume.pdf" download class="btn">
      Download PDF
    </a>

  </section>


  <section class="resume-section">

    <h2>Professional Profile</h2>

    <p>
      Cloud Engineer and DevOps Engineer with experience building,
      automating and maintaining cloud infrastructure. Experienced
      with Linux systems, Infrastructure as Code, configuration
      management, containerization, CI/CD, monitoring and cloud
      platforms including AWS, Google Cloud Platform and Azure.
    </p>

    <p>
      Google Cloud Certified Associate Cloud Engineer with hands-on
      experience using Terraform, Ansible, Docker, Kubernetes,
      GitHub Actions and modern observability tools.
    </p>

  </section>


  <section class="resume-section">

    <h2>Technical Skills</h2>

    <div class="resume-skills">

      <div>
        <h3>Linux & Scripting</h3>
        <p>Python, Bash, HCL, PowerShell, Shell, JSON, YAML, SQL, CLI</p>
      </div>

      <div>
        <h3>Cloud Platforms</h3>
        <p>AWS, Google Cloud Platform (GCP), Azure</p>
      </div>

      <div>
        <h3>Containerization</h3>
        <p>Docker, Kubernetes, Nomad, Helm</p>
      </div>

      <div>
        <h3>Monitoring & Logging</h3>
        <p>Cloud Monitoring, Prometheus, Grafana, Loki, Alloy</p>
      </div>

      <div>
        <h3>DevOps Tools</h3>
        <p>Jenkins, GitHub Actions, Terraform, Ansible, Pulumi, GitHub</p>
      </div>

    </div>

  </section>


  <section class="resume-section">

    <h2>Experience</h2>

    <div class="resume-entry">

      <div class="resume-entry-header">

        <div>
          <h3>Cloud Engineer</h3>
          <strong>Imbod</strong>
        </div>

        <div>
          <strong>July 2025 – Present</strong>
          <span>{LOCATION}</span>
        </div>

      </div>

      <ul>

        <li>
          Configured and maintained Linux-based application servers
          on Google Compute Engine, ensuring secure and reliable deployments.
        </li>

        <li>
          Automated infrastructure provisioning and configuration
          management with Terraform and Ansible, increasing deployment
          efficiency by <strong>40%</strong>.
        </li>

        <li>
          Delivered cloud solutions with Terraform, minimizing setup
          time by <strong>60%</strong> using reusable Terraform modules.
        </li>

        <li>
          Supported systems integration, networking and security
          configuration across cloud workloads.
        </li>

      </ul>

    </div>

  </section>


  <section class="resume-section">

    <h2>Projects</h2>

    <div class="resume-entry">

      <h3>Mira Essentials — Full-Stack E-commerce Application</h3>

      <ul>

        <li>
          Built and deployed a production-ready e-commerce website
          using React/Vite and Node.js/Express.
        </li>

        <li>
          Implemented product variants, carts, checkout, customer
          order tracking, Paystack payments and bank-transfer
          payment confirmation.
        </li>

        <li>
          Built an admin dashboard for application management.
        </li>

        <li>
          Integrated PostgreSQL with Prisma ORM for product, order,
          payment and customer data management.
        </li>

      </ul>

      <a href="{MIRA}" target="_blank" rel="noopener">
        View Project →
      </a>

    </div>


    <div class="resume-entry">

      <h3>CI Pipeline Automation</h3>

      <ul>

        <li>
          Integrated Git and GitHub for streamlined collaboration
          and code tracking.
        </li>

        <li>
          Built and configured a continuous integration pipeline
          using GitHub Actions.
        </li>

        <li>
          Automated testing and deployment for a demo application.
        </li>

      </ul>

      <a href="{CI_PIPELINE}" target="_blank" rel="noopener">
        View Repository →
      </a>

    </div>

  </section>


  <section class="resume-section">

    <h2>Education</h2>

    <div class="resume-entry">

      <h3>Gregory University Uturu</h3>

      <p>
        B.Sc. Computer Science
      </p>

      <p>
        Abia, Nigeria
      </p>

    </div>

  </section>


  <section class="resume-section">

    <h2>Certifications</h2>

    <div class="resume-entry">

      <h3>Google Cloud Certified Associate Cloud Engineer</h3>

      <a href="{CREDLY}"
         target="_blank"
         rel="noopener">

        Verify Credential →

      </a>

    </div>

    <div class="resume-entry">

      <h3>Kubernetes Certification</h3>

      <p>
        Kubernetes certified.
      </p>

    </div>

    <div class="resume-entry">

      <h3>Google Cloud Certification</h3>

      <p>
        3x GCP certified.
      </p>

    </div>

  </section>


  <section class="resume-cta">

    <h2>Let's connect.</h2>

    <p>
      Interested in cloud engineering, DevOps and infrastructure automation?
    </p>

    <a href="{LINKEDIN}"
       target="_blank"
       rel="noopener"
       class="btn">

      Connect on LinkedIn

    </a>

  </section>

</main>


</body>
</html>
"""

(ROOT / "resume.html").write_text(resume_html, encoding="utf-8")


# ============================================================
# ATS RESUME
# ============================================================

resume_ats = f"""<!DOCTYPE html>

<html lang="en">

<head>

<meta charset="UTF-8">

<title>{NAME} - ATS Resume</title>

<style>

body {{
    font-family: Arial, sans-serif;
    line-height: 1.6;
    margin: 40px auto;
    max-width: 900px;
    color: #111;
}}

h1 {{
    margin-bottom: 5px;
}}

h2 {{
    border-bottom: 1px solid #ccc;
    padding-bottom: 5px;
    margin-top: 30px;
}}

h3 {{
    margin-bottom: 5px;
}}

a {{
    color: #111;
}}

</style>

</head>

<body>

<h1>{NAME}</h1>

<p>
Cloud Engineer | DevOps Engineer
</p>

<p>
Email: {EMAIL}<br>
Location: {LOCATION}<br>
LinkedIn: {LINKEDIN}<br>
GitHub: {GITHUB}<br>
Portfolio: {PORTFOLIO}
</p>


<h2>Professional Profile</h2>

<p>
Cloud Engineer and DevOps Engineer with hands-on experience in
cloud infrastructure, Linux systems, Infrastructure as Code,
configuration management, CI/CD, containerization, monitoring
and cloud-native technologies.
</p>


<h2>Skills</h2>

<ul>

<li>
<strong>Linux & Scripting:</strong>
Python, Bash, HCL, PowerShell, Shell, JSON, YAML, SQL, CLI
</li>

<li>
<strong>Cloud Platforms:</strong>
AWS, Google Cloud Platform (GCP), Azure
</li>

<li>
<strong>Containerization:</strong>
Docker, Kubernetes, Nomad, Helm
</li>

<li>
<strong>Monitoring & Logging:</strong>
Cloud Monitoring, Prometheus, Grafana, Loki, Alloy
</li>

<li>
<strong>DevOps Tools:</strong>
Jenkins, GitHub Actions, Terraform, Ansible, Pulumi, GitHub
</li>

</ul>


<h2>Experience</h2>

<h3>Cloud Engineer — Imbod</h3>

<p>
Lagos, Nigeria | July 2025 – Present
</p>

<ul>

<li>
Configured and maintained Linux-based application servers
on Google Compute Engine, ensuring secure and reliable deployments.
</li>

<li>
Automated infrastructure provisioning and configuration management
with Terraform and Ansible, increasing deployment efficiency by 40%.
</li>

<li>
Delivered cloud solutions with Terraform, minimizing setup time
by 60% using reusable Terraform modules.
</li>

<li>
Supported systems integration, networking and security configuration
across cloud workloads.
</li>

</ul>


<h2>Projects</h2>

<h3>Mira Essentials — Full-Stack E-commerce Application</h3>

<ul>

<li>
Built and deployed a production-ready e-commerce website using
React/Vite frontend and Node.js/Express backend.
</li>

<li>
Implemented product variants, carts, checkout, customer order
tracking, Paystack payments, bank-transfer payment confirmation
workflow and an admin dashboard.
</li>

<li>
Integrated PostgreSQL with Prisma ORM for product, order, payment
and customer data management.
</li>

<li>
Live project: {MIRA}
</li>

</ul>


<h3>CI Pipeline Automation</h3>

<ul>

<li>
Integrated Git and GitHub for streamlined collaboration and code tracking.
</li>

<li>
Built and configured a continuous integration pipeline using
GitHub Actions to automate testing and deployment for a demo application.
</li>

<li>
Repository: {CI_PIPELINE}
</li>

</ul>


<h2>Education</h2>

<p>
<strong>Gregory University Uturu</strong><br>
B.Sc. Computer Science<br>
Abia, Nigeria
</p>


<h2>Certifications</h2>

<ul>

<li>
Google Cloud Certified Associate Cloud Engineer —
{CREDLY}
</li>

<li>
3x GCP certified
</li>

<li>
Kubernetes certified
</li>

</ul>

</body>
</html>
"""

(ROOT / "resume-ats.html").write_text(resume_ats, encoding="utf-8")


# ============================================================
# STYLE.CSS
# ============================================================

css = r"""
/* =========================================================
   BASE
   ========================================================= */

:root {
  --bg: #ffffff;
  --surface: #f8fafc;
  --surface-2: #f1f5f9;
  --text: #0f172a;
  --muted: #64748b;
  --border: #e2e8f0;
  --accent: #0284c7;
  --accent-dark: #0369a1;
  --terminal: #0f172a;
  --radius: 18px;
  --shadow: 0 12px 35px rgba(15, 23, 42, 0.08);
}

* {
  box-sizing: border-box;
}

html {
  scroll-behavior: smooth;
}

body {
  margin: 0;
  font-family: "Segoe UI", Inter, Arial, sans-serif;
  background: var(--bg);
  color: var(--text);
  line-height: 1.7;
}

a {
  color: inherit;
}

img {
  max-width: 100%;
}

button {
  font: inherit;
}


/* =========================================================
   NAVIGATION
   ========================================================= */

header {
  position: sticky;
  top: 0;
  z-index: 100;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 18px 6%;
  background: rgba(255, 255, 255, 0.94);
  border-bottom: 1px solid var(--border);
  backdrop-filter: blur(12px);
}

.logo {
  color: var(--text);
  text-decoration: none;
  font-size: 19px;
  font-weight: 800;
}

nav {
  display: flex;
  align-items: center;
  gap: 28px;
}

nav a {
  color: var(--muted);
  text-decoration: none;
  font-size: 14px;
  font-weight: 600;
  transition: 0.2s ease;
}

nav a:hover {
  color: var(--accent);
}

.menu-toggle {
  display: none;
  border: 0;
  background: transparent;
  color: var(--text);
  cursor: pointer;
  font-size: 24px;
}


/* =========================================================
   TYPOGRAPHY
   ========================================================= */

h1,
h2,
h3,
p {
  margin-top: 0;
}

h1 {
  font-size: clamp(42px, 7vw, 78px);
  line-height: 1.03;
  letter-spacing: -3px;
  margin-bottom: 24px;
}

h2 {
  font-size: clamp(30px, 4vw, 48px);
  line-height: 1.15;
  letter-spacing: -1.5px;
}

h3 {
  line-height: 1.25;
}

.eyebrow {
  margin-bottom: 12px;
  color: var(--accent);
  font-size: 12px;
  font-weight: 800;
  letter-spacing: 2px;
}

.section-heading {
  margin-bottom: 35px;
}


/* =========================================================
   HERO
   ========================================================= */

.hero {
  min-height: 78vh;
  max-width: 1250px;
  margin: auto;
  padding: 90px 6%;
  display: grid;
  grid-template-columns: 1.5fr 0.8fr;
  gap: 70px;
  align-items: center;
}

.hero h1 span {
  color: var(--accent);
}

.hero-description {
  max-width: 700px;
  color: var(--muted);
  font-size: 19px;
}

.buttons {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-top: 30px;
}

.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 12px 21px;
  border-radius: 10px;
  background: var(--accent);
  color: #ffffff;
  text-decoration: none;
  font-weight: 700;
  transition: 0.2s ease;
}

.btn:hover {
  background: var(--accent-dark);
  transform: translateY(-2px);
}

.btn.secondary {
  background: #ffffff;
  color: var(--text);
  border: 1px solid var(--border);
}

.btn.secondary:hover {
  border-color: var(--accent);
  color: var(--accent);
}

.image-container {
  display: flex;
  justify-content: center;
}

.image-container img {
  width: min(330px, 100%);
  aspect-ratio: 1;
  object-fit: cover;
  border-radius: 28px;
  border: 1px solid var(--border);
  box-shadow: var(--shadow);
}


/* =========================================================
   SECTIONS
   ========================================================= */

.section-container {
  max-width: 1150px;
  margin: auto;
  padding: 100px 6%;
}

.about {
  display: grid;
  grid-template-columns: 0.8fr 1.2fr;
  gap: 80px;
  border-top: 1px solid var(--border);
}

.about-content {
  color: var(--muted);
  font-size: 17px;
}

.socials {
  display: flex;
  flex-wrap: wrap;
  gap: 15px;
  margin-top: 30px;
}

.socials a {
  display: inline-flex;
  gap: 8px;
  align-items: center;
  text-decoration: none;
  color: var(--text);
  font-weight: 700;
}

.socials a:hover {
  color: var(--accent);
}


/* =========================================================
   STATS
   ========================================================= */

.stats-section {
  max-width: 1150px;
  margin: 0 auto;
  padding: 0 6% 60px;
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 18px;
}

.stat-card {
  padding: 28px;
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: var(--radius);
}

.stat-card strong {
  display: block;
  margin-bottom: 6px;
  color: var(--accent);
  font-size: 38px;
}

.stat-card span {
  color: var(--muted);
}


/* =========================================================
   SKILLS
   ========================================================= */

.skills-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 18px;
}

.skill-card {
  padding: 26px;
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  transition: 0.2s ease;
}

.skill-card:hover,
.project-card:hover,
.experience-card:hover {
  transform: translateY(-4px);
  box-shadow: var(--shadow);
}

.skill-card i {
  color: var(--accent);
  font-size: 27px;
}

.skill-card h3 {
  margin: 14px 0 7px;
}

.skill-card p {
  color: var(--muted);
  margin-bottom: 0;
}


/* =========================================================
   EXPERIENCE
   ========================================================= */

.experience {
  border-top: 1px solid var(--border);
}

.experience-card {
  padding: 35px;
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  transition: 0.2s ease;
}

.experience-header {
  display: flex;
  justify-content: space-between;
  gap: 30px;
  margin-bottom: 20px;
}

.experience-header p,
.experience-header span {
  color: var(--muted);
}

.experience-card li {
  margin-bottom: 12px;
}


/* =========================================================
   PROJECTS
   ========================================================= */

.project-feature {
  padding: 45px;
  border: 1px solid var(--border);
  border-radius: 24px;
  background: var(--surface);
  box-shadow: var(--shadow);
}

.project-label {
  color: var(--accent);
  font-size: 11px;
  font-weight: 800;
  letter-spacing: 1.5px;
}

.project-feature h3 {
  font-size: 32px;
  margin: 15px 0;
}

.project-feature p {
  max-width: 850px;
  color: var(--muted);
}

.tech-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin: 25px 0;
}

.tech-tags span {
  padding: 6px 10px;
  background: #ffffff;
  border: 1px solid var(--border);
  border-radius: 999px;
  color: var(--muted);
  font-size: 12px;
  font-weight: 700;
}


/* =========================================================
   PROJECT PAGE
   ========================================================= */

.content {
  max-width: 1150px;
  margin: auto;
  padding: 80px 6%;
}

.page-hero {
  margin-bottom: 60px;
}

.intro {
  max-width: 720px;
  color: var(--muted);
  font-size: 18px;
}

.projects-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 24px;
}

.project-card {
  display: flex;
  gap: 25px;
  padding: 32px;
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 22px;
  transition: 0.2s ease;
}

.featured-project-card {
  grid-column: span 2;
}

.project-icon {
  flex: 0 0 50px;
  height: 50px;
  display: grid;
  place-items: center;
  border-radius: 13px;
  background: #e0f2fe;
  color: var(--accent);
  font-size: 25px;
}

.project-content {
  flex: 1;
}

.project-content h2 {
  margin: 8px 0 12px;
  font-size: 30px;
}

.project-content p,
.project-content li {
  color: var(--muted);
}

.project-content li {
  margin-bottom: 7px;
}

.project-link {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  margin-top: 15px;
  color: var(--accent);
  text-decoration: none;
  font-weight: 800;
}


/* =========================================================
   METRICS
   ========================================================= */

.impact-section {
  padding: 100px 0 60px;
}

.metrics {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 18px;
}

.metric {
  padding: 32px;
  border: 1px solid var(--border);
  border-radius: var(--radius);
  background: var(--surface);
}

.metric strong {
  display: block;
  color: var(--accent);
  font-size: 42px;
}

.metric span {
  color: var(--muted);
}


/* =========================================================
   TERMINAL / PIPELINE
   ========================================================= */

.pipeline-section {
  padding: 30px 0 70px;
}

.terminal-box {
  overflow: hidden;
  border-radius: 15px;
  background: var(--terminal);
  color: #d1fae5;
  box-shadow: var(--shadow);
}

.terminal-header {
  display: flex;
  justify-content: space-between;
  padding: 13px 17px;
  color: #94a3b8;
  border-bottom: 1px solid #334155;
  font-family: monospace;
}

#terminal-output {
  min-height: 150px;
  padding: 20px;
  font-family: monospace;
  font-size: 13px;
}

.pipeline {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-wrap: wrap;
  gap: 12px;
  margin-top: 25px;
}

.pipeline div {
  padding: 10px 16px;
  border: 1px solid var(--border);
  border-radius: 9px;
  background: var(--surface);
  font-weight: 700;
}


/* =========================================================
   CERTIFICATION
   ========================================================= */

.certification-card {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 30px;
  padding: 35px;
  border: 1px solid var(--border);
  border-radius: var(--radius);
  background: var(--surface);
}


/* =========================================================
   FOOTER
   ========================================================= */

footer {
  padding: 45px 6%;
  border-top: 1px solid var(--border);
  display: flex;
  justify-content: space-between;
  gap: 30px;
  flex-wrap: wrap;
}

footer p {
  color: var(--muted);
}

.footer-links {
  display: flex;
  gap: 20px;
}

.footer-links a {
  color: var(--muted);
  text-decoration: none;
}

.footer-links a:hover {
  color: var(--accent);
}

.copyright {
  width: 100%;
  font-size: 13px;
}


/* =========================================================
   RESUME
   ========================================================= */

.resume-page {
  max-width: 950px;
  margin: auto;
  padding: 80px 6%;
}

.resume-header {
  padding-bottom: 45px;
  border-bottom: 1px solid var(--border);
}

.resume-header h1 {
  margin-bottom: 10px;
}

.resume-header > p {
  color: var(--muted);
}

.resume-links {
  display: flex;
  flex-wrap: wrap;
  gap: 18px;
  margin: 25px 0;
}

.resume-links a {
  color: var(--accent);
  text-decoration: none;
  font-weight: 700;
}

.resume-section {
  padding: 45px 0;
  border-bottom: 1px solid var(--border);
}

.resume-section h2 {
  font-size: 28px;
  margin-bottom: 25px;
}

.resume-section p,
.resume-section li {
  color: var(--muted);
}

.resume-skills {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 18px;
}

.resume-skills > div {
  padding: 20px;
  border: 1px solid var(--border);
  border-radius: 14px;
  background: var(--surface);
}

.resume-skills h3 {
  margin-bottom: 8px;
}

.resume-entry {
  margin-bottom: 35px;
}

.resume-entry-header {
  display: flex;
  justify-content: space-between;
  gap: 30px;
}

.resume-entry-header span {
  display: block;
  color: var(--muted);
}

.resume-entry a {
  color: var(--accent);
  text-decoration: none;
  font-weight: 700;
}

.resume-cta {
  margin-top: 50px;
  padding: 40px;
  text-align: center;
  border-radius: var(--radius);
  background: var(--surface);
}


/* =========================================================
   ANIMATION
   ========================================================= */

.fade-in {
  animation: fadeIn 0.6s ease both;
}

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(10px);
  }

  to {
    opacity: 1;
    transform: translateY(0);
  }
}


/* =========================================================
   MOBILE
   ========================================================= */

@media (max-width: 800px) {

  .menu-toggle {
    display: block;
  }

  nav {
    position: absolute;
    top: 70px;
    right: 6%;
    display: none;
    flex-direction: column;
    align-items: stretch;
    min-width: 210px;
    padding: 10px;
    background: #ffffff;
    border: 1px solid var(--border);
    border-radius: 12px;
    box-shadow: var(--shadow);
  }

  nav.open {
    display: flex;
  }

  nav a {
    padding: 10px;
  }

  .hero {
    grid-template-columns: 1fr;
    padding-top: 65px;
  }

  .image-container {
    order: -1;
  }

  .image-container img {
    width: 220px;
  }

  .about {
    grid-template-columns: 1fr;
    gap: 25px;
  }

  .skills-grid,
  .stats-section {
    grid-template-columns: 1fr;
  }

  .projects-grid {
    grid-template-columns: 1fr;
  }

  .featured-project-card {
    grid-column: span 1;
  }

  .metrics {
    grid-template-columns: 1fr;
  }

  .experience-header,
  .certification-card,
  .resume-entry-header {
    flex-direction: column;
  }

  .resume-skills {
    grid-template-columns: 1fr;
  }

  h1 {
    letter-spacing: -2px;
  }

}

@media (max-width: 500px) {

  .project-card {
    flex-direction: column;
  }

  .project-feature {
    padding: 28px;
  }

  .hero {
    padding-left: 5%;
    padding-right: 5%;
  }

}
"""

(ROOT / "style.css").write_text(css, encoding="utf-8")


# ============================================================
# SCRIPT.JS
# ============================================================

script_js = r"""
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
"""

(ROOT / "script.js").write_text(script_js, encoding="utf-8")


print()
print("============================================")
print(" Portfolio successfully rebranded")
print("============================================")
print()
print("Updated:")
print("  ✓ index.html")
print("  ✓ projects.html")
print("  ✓ resume.html")
print("  ✓ resume-ats.html")
print("  ✓ style.css")
print("  ✓ script.js")
print()
print("Removed project content:")
print("  ✓ Cloud Deployment")
print("  ✓ Facial Recognition Attendance System")
print()
print("Added:")
print("  ✓ Mira Essentials")
print("  ✓ CI Pipeline Automation")
print("  ✓ White background")
print("  ✓ Cloud / DevOps positioning")
print("  ✓ Correct LinkedIn")
print("  ✓ GitHub links")
print("  ✓ Live project links")
print("  ✓ Certification link")
print("  ✓ 40% / 60% metrics")
print("  ✓ Clean responsive CSS")
print("  ✓ Updated ATS resume")
print()