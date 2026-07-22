# 🧬 Research Impact Advisor

A Flask-based Bioinformatics Research Workflow Management System that helps researchers manage bioinformatics workflows, monitor software and reference database updates, analyze the impact of updates on research projects, and generate scientific reports.

---

# 📖 Overview

Modern bioinformatics research relies on multiple software tools, pipelines, and reference databases that are continuously updated. Researchers often struggle to determine whether these updates affect previously completed analyses.

Research Impact Advisor is a centralized decision-support platform that helps researchers organize their bioinformatics workflows and identify projects that may require reanalysis due to software or database updates.

---

# ✨ Version 1 Features

## 📁 Project Management

- Create and manage research projects
- Store researcher information
- Track organism details
- Maintain project status

---

## 🔬 Pipeline Management

- Create bioinformatics pipelines
- Assign pipelines to projects
- Store pipeline versions
- Add pipeline descriptions

---

## ⚙️ Tool Management

- Add bioinformatics tools
- Store tool versions
- Record tool purpose
- Link tools with pipelines

---

## 🗄️ Reference Database Management

- Manage reference databases
- Store database versions
- Record release dates
- Associate databases with pipelines

---

## 🌍 Latest Version Repository

Maintain the latest available versions of commonly used bioinformatics software, including:

- FastQC
- BWA
- SAMtools
- bcftools
- GATK
- Other bioinformatics software

---

## 🔄 Update Checker

Compare software and database versions used in research projects against the latest available versions.

---

## 📊 Impact Analysis

Automatically analyzes project impact by calculating:

- Total updates found
- High-impact updates
- Medium-impact updates
- Low-impact updates
- Research priority

---

## 💡 Recommendation Engine

Provides intelligent recommendations such as:

- Immediate Reanalysis
- Review Required
- Continue Monitoring

---

## 📜 Analysis History

- Store previous analyses
- Maintain project history
- Review historical impact assessments

---

## 📄 Report Generation

Generate downloadable scientific reports summarizing:

- Project details
- Detected updates
- Impact assessment
- Recommendations

---

# 🏗️ System Architecture

```
Research Project
        │
        ▼
Pipeline
        │
 ┌──────┴────────┐
 │               │
 ▼               ▼
Tools     Reference Databases
        │
        ▼
Latest Version Repository
        │
        ▼
Update Checker
        │
        ▼
Impact Engine
        │
        ▼
Recommendation Engine
        │
        ▼
Analysis History
        │
        ▼
Scientific Report
```

---

# 🛠️ Technologies Used

### Backend

- Python
- Flask
- SQLAlchemy

### Database

- SQLite

### Frontend

- HTML5
- Bootstrap 5
- Jinja2

### Version Control

- Git
- GitHub

---

# 📂 Project Structure

```
Research-Impact-Advisor
│
├── app
│   ├── models
│   ├── routes
│   ├── services
│   ├── reports
│   ├── templates
│   ├── static
│   └── app.py
│
├── data
├── docs
├── tests
├── instance
├── README.md
├── VERSION.md
└── LICENSE
```

---

# 🚀 Installation

## Clone the repository

```bash
git clone https://github.com/keerthanasri-bioinformatics/Research-Impact-Advisor.git
```

## Move into the project

```bash
cd Research-Impact-Advisor
```

## Install dependencies

```bash
pip install flask flask_sqlalchemy
```

## Run the application

```bash
cd app
python app.py
```

The application will start at:

```
http://127.0.0.1:5000
```

---

# 🚧 Current Status

This repository contains **Version 1.0**, a working prototype demonstrating:

- Research project management
- Pipeline management
- Tool management
- Reference database management
- Latest software version repository
- Update checking
- Research impact analysis
- Recommendation engine
- Analysis history
- Report generation

---

# 🎯 Future Roadmap (Version 2)

The next version will introduce advanced automation and researcher-friendly features, including:

- ✅ Automatic monitoring of official software releases (GitHub & official websites)
- ✅ Automatic reference database monitoring
- ✅ Email notifications
- ✅ Dashboard notifications
- ✅ Pipeline configuration file upload
- ✅ Automatic workflow import
- ✅ Sample-level impact analysis
- ✅ Automated reanalysis recommendations
- ✅ Research prioritization engine
- ✅ PDF & Excel report export
- ✅ Multi-user authentication
- ✅ Cloud deployment
- ✅ Real-time update monitoring

---

# 🎓 Academic Purpose

This project was developed as a bioinformatics software engineering project to demonstrate workflow version tracking, update monitoring, and research impact assessment for genomic research.

---

# 👩‍💻 Author

**Keerthana Sri**

B.E. Bioinformatics Student

GitHub

https://github.com/keerthanasri-bioinformatics

---

# 📜 License

This project is licensed under the **MIT License**.

---

# ⭐ If you found this project useful

Please consider giving this repository a ⭐ on GitHub.