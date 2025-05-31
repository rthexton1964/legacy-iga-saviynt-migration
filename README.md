# Legacy IGA to Saviynt Migration Platform

A comprehensive web-based platform for migrating from legacy Identity Governance & Administration (IGA) systems to Saviynt's modern identity platform.

## 🚀 Live Demo

**Live Application**: https://legacy-iga-saviynt-migration-516cf9d451dc.herokuapp.com/

## 📋 Overview

This platform provides a complete migration solution for organizations looking to modernize their identity governance infrastructure by migrating from legacy IGA systems to Saviynt's comprehensive identity platform.

### Supported Legacy Systems
- **SailPoint IdentityIQ** - Comprehensive identity governance platform
- **Oracle Identity Manager (OIM)** - Enterprise identity management solution  
- **IBM Tivoli Identity Manager** - Legacy identity and access management
- **CA Identity Manager** - Broadcom's identity governance solution
- **NetIQ Identity Manager** - Micro Focus identity management platform

## ✨ Key Features

### 🔍 **Discovery & Assessment**
- Automated system discovery and inventory
- Risk and complexity assessment
- Migration readiness evaluation
- Detailed system profiling

### 🔄 **Migration Planning & Execution**
- Interactive 1-minute demo migration simulation
- Real-time progress tracking with pause/resume functionality
- Dynamic migration timeline with milestones
- Live activity feed and status updates
- Issues & alerts monitoring

### 📊 **Analytics & Reporting**
- System-specific migration analytics
- Progress tracking and timeline visualization
- Migration speed and performance metrics
- Comprehensive migration reports
- Cost savings calculations

### 🛡️ **Compliance & Security**
- SOX, GDPR, and HIPAA compliance tracking
- Security assessment and validation
- Risk mitigation strategies
- Regulatory compliance reporting

## 🏗️ Architecture

### Backend
- **Flask** - Python web framework
- **Jinja2** - Template engine with custom globals
- **Gunicorn** - WSGI HTTP Server

### Frontend
- **Bootstrap 5** - Responsive UI framework
- **FontAwesome** - Icon library
- **JavaScript** - Interactive functionality
- **Real-time updates** - Dynamic content management

### Deployment
- **Heroku** - Cloud platform deployment
- **Git** - Version control
- **Python 3.9.18** - Runtime environment

## 🚀 Quick Start

### Prerequisites
- Python 3.9+
- pip package manager
- Git

### Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/rthexton1964/legacy-iga-saviynt-migration.git
   cd legacy-iga-saviynt-migration
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python app.py
   ```

4. **Access the application**
   - Open your browser to `http://localhost:5007`

### Heroku Deployment

The application is configured for Heroku deployment with:
- `Procfile` - Gunicorn web server configuration
- `requirements.txt` - Python dependencies
- `runtime.txt` - Python version specification

## 🎯 Demo Workflow

1. **Discovery Page** - Select your legacy IGA system
2. **Migration Page** - Run the 1-minute interactive demo migration
3. **Analytics Page** - View system-specific progress and metrics
4. **Reports Page** - Access detailed migration documentation
5. **Compliance Page** - Review compliance scores and assessments

## 📁 Project Structure

```
webapp/
├── app.py                 # Flask application and routes
├── templates/             # Jinja2 HTML templates
│   ├── discovery.html     # Legacy system discovery
│   ├── migration.html     # Migration execution interface
│   ├── analytics.html     # Migration analytics dashboard
│   ├── reports.html       # Migration reports and documentation
│   ├── compliance.html    # Compliance tracking and assessment
│   └── index.html         # Landing page
├── static/               # Static assets (CSS, JS, images)
├── requirements.txt      # Python dependencies
├── Procfile             # Heroku deployment configuration
├── runtime.txt          # Python runtime version
└── README.md           # Project documentation
```

## 🔧 Configuration

### Environment Variables
- `PORT` - Application port (default: 5007)
- `FLASK_ENV` - Environment setting (development/production)

### Template Globals
- `timedelta` - Added to Jinja2 globals for date calculations

## 🌟 Features in Detail

### Migration Simulation
- **Real-time Progress**: Dynamic progress bars and status updates
- **Interactive Timeline**: Milestone tracking with completion states
- **Activity Feed**: Live migration event logging
- **Issues & Alerts**: Risk identification and resolution tracking

### System-Specific Data
- **Dynamic Content**: Content adapts based on selected legacy system
- **Complexity Scoring**: High/Medium complexity assessments
- **Progress Calculations**: System-specific migration metrics
- **Navigation Context**: Maintains system selection across all pages

## 🚨 Known Issues

- CSS lint warnings related to Jinja2 template syntax (non-blocking)
- Migration simulation is demonstration-only (not actual data migration)

## 🤝 Contributing

This project was developed as part of the Rex-AI-Palooza innovation initiative focused on revolutionizing cybersecurity service delivery.

## 📄 License

This project is part of the Rex-AI-Palooza innovation hub.

## 🔗 Related Projects

- **Rex-AI-Palooza Dashboard**: https://rex-ai-palooza-01aca72cba5f.herokuapp.com/
- **Security Incident Demo**: https://security-incident-demo-app-4beeaf592b30.herokuapp.com/
- **Splunk Migration Tools**: Multiple migration platform solutions

---

**Built with ❤️ for the Rex-AI-Palooza Innovation Hub**
