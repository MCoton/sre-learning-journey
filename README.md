# SRE Learning Environment Setup Checklist

## Chunk 1: Foundation Accounts & Version Control
- [ ] Create a free account on GitHub.
- [ ] Create a new public repository on GitHub named `sre-learning-journey`.
- [ ] Enable GitHub Codespaces on your repository (Click `Code` -> `Codespaces` -> `Create codespace on main`).
- [ ] Verify your environment loads a full VS Code interface directly inside your web browser.

## Chunk 2: Lightweight Local Editor Setup (Optional)
- [ ] Install Visual Studio Code on your Mac / Windows PC (as a lightweight client; no local Python required).
- [ ] Install the GitHub Codespaces extension inside VS Code.
- [ ] Connect VS Code on your desktop directly to your remote cloud Codespace (`Cmd/Ctrl + Shift + P` -> `Codespaces: Connect to Codespace`).

## Chunk 3: Cloud Python & Project Structure (Inside Codespace)
- [ ] Open the terminal inside your Codespace and confirm Python version (`python3 --version`).
- [ ] Initialize your first Python virtual environment inside the container (`python3 -m venv venv`).
- [ ] Test package installation inside the container (`pip install requests fastapi uvicorn`).
- [ ] Practice saving your changes back to GitHub (`git add .` -> `git commit -m "setup codespace"` -> `git push`).

## Chunk 4: Learning Platform & Cloud Sandboxes
- [ ] Choose your primary interactive Python foundation track:
    - Boot.dev (Gamified interactive CLI & backend focus) OR
    - University of Helsinki Python Programming MOOC (Free, text-based VS Code exercises)
- [ ] Select a project/video resource for supplementary builds (e.g., 100 Days of Code by Angela Yu or Automate the Boring Stuff).
- [ ] Create a free account on KodeKloud (for browser-based Linux, Docker, and Kubernetes labs).
- [ ] Create an AWS Free Tier or Microsoft Azure Free Account for future cloud operations modules.

## Chunk 5: Habit Tracking & Daily Workflow
- [ ] Import this checklist into your task app (Notion, Todoist, Obsidian, or Trello).
- [ ] Schedule a recurring 45-minute calendar block labeled "SRE Study Session".
- [ ] Test the "Portability Factor": Open your Codespace from a second device (or browser window) and verify your setup loads identically.