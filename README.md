# Smart Light IoT Controller

**ENGR 491 / ENGR 492 – Engineering Capstone**  
**Regent University | 2025–2026**

**Team Members:**  
- Riley Pence  
- Alex O'Neal  
- Elijah Atkinson  

**Instructor:** Gregory M. Baumgardner  

---

## 🔍 Overview

This project is part of the Engineering Capstone sequence at Regent University. The goal is to design and implement an **Internet-connected smart light controller** that allows a homeowner to remotely manage a light bulb using an ESP32 microcontroller and a web-based interface.

The system is designed to be modular, secure, and reproducible, with both **hardware** and **software** components developed collaboratively by the team.

Key capabilities include:
- Remote **on/off** control  
- **Brightness dimming** via a TRIAC-based circuit  
- **Scheduled automation**  
- **User authentication and permissions**  
- **Power usage monitoring**  
- **Activity logging**  
- **Conflict handling** when multiple users issue commands  

---

## ⚙️ System Architecture

### Hardware
- ESP32-C6 (or similar ESP32 variant)  
- TRIAC-based AC dimmer circuit  
- AC-to-DC power regulation  
- Optional current / power sensor (e.g., ACS712)  

### Software
- Python/Django backend  
- Relational database (local development via Docker)  
- Web-based control interface  
- REST and/or MQTT communication between ESP32 and server  

---

## 🧱 Development Environment

This project uses a **containerized development workflow** to ensure all team members run the same environment.

- **VS Code Dev Container** for a consistent Linux development environment  
- **Docker Compose** for backend services and database  
- **Makefile** for standardized development commands  

No local Python or Django installation is required.

---

## 📘 Onboarding & Setup

All setup instructions and development workflows are maintained in a centralized onboarding document.

👉 **[Team Onboarding & Development Setup Guide]((https://docs.google.com/document/d/1S6X8KR8X2IKavoMGxNuK4bp7QqtarrereW7RVvmiM-k/edit?tab=t.0))**

Please follow the onboarding guide **before making any code changes**.

---

### 🗓️ Week-by-Week Execution Plan
👉 **[Capstone Week-by-Week Execution Plan](https://docs.google.com/document/d/1rj9rKCci_vYrwdZt3Hwqrge441vVNJ1GV4GpvJUPwgY/edit?usp=sharing)**

This document outlines:
- Weekly objectives and deliverables
- Task sequencing for hardware and software
- Team coordination and milestones
- Expected progress through the semester

This plan serves as the **primary schedule and accountability reference** for the team.

---
## 📁 Repository Structure

smartlight-iot-controller/
├── firmware/ # ESP32 firmware (PlatformIO)
├── server/ # Django backend
├── ops/ # Environment and operational configuration
├── .devcontainer/ # VS Code Dev Container configuration
├── docker-compose.yml # Local backend and database services
├── Makefile # Standardized team commands
├── README.md

