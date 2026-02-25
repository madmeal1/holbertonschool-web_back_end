# Personal Data – Filtered Logger

## Description

Ce projet a pour objectif de protéger les **données personnelles sensibles (PII – Personally Identifiable Information)** lors de l’utilisation des logs en Python.

Il met en place un système de **journalisation sécurisée** permettant de masquer automatiquement les champs sensibles avant leur affichage ou leur stockage.

---

## Resources

Read or watch:

- [What Is PII, non-PII, and Personal Data?](https://piwik.pro/blog/what-is-pii-personal-data/)
- [Python `logging` documentation](https://docs.python.org/3/library/logging.html)
- [`bcrypt` package](https://github.com/pyca/bcrypt/)
- [Logging to Files, Setting Levels, and Formatting](https://www.youtube.com/watch?v=-ARI4Cz-awo)

---

## Learning Objectives

À la fin de ce projet, vous serez capable d’expliquer :

- Ce qu’est une **PII (Personally Identifiable Information)**
- Des exemples de données personnelles sensibles
- Comment implémenter un **log filter** pour masquer les champs sensibles
- Comment **chiffrer un mot de passe** et vérifier sa validité
- Comment s’authentifier à une base de données via des **variables d’environnement**
- Comment utiliser le module `logging` de Python de manière sécurisée

---

## Requirements

- Ubuntu 20.04 LTS
- Python 3.9
- Tous les fichiers doivent :
  - se terminer par une nouvelle ligne
  - commencer par `#!/usr/bin/env python3`
  - être exécutables
  - respecter le style **pycodestyle (version 2.5)**
- Un fichier `README.md` est obligatoire à la racine du projet
- La longueur des fichiers sera testée avec `wc`
- Tous les modules, classes et fonctions doivent avoir une **documentation claire**
- Toutes les fonctions doivent être **annotées avec des types**

---

## Project Structure

```text
personal_data/
│
├── README.md
├── filtered_logger.py
└── main.py
