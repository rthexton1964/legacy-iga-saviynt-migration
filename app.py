#!/usr/bin/env python3
"""
Legacy IGA to Saviynt Migration Platform
=======================================

Enterprise-grade migration platform supporting multiple legacy IGA systems:
- Oracle OIM (Oracle Identity Manager)
- One Identity Manager
- IBM Tivoli Identity Manager
- SailPoint IdentityIQ

Target Platform: Saviynt
"""

from flask import Flask, render_template, request, jsonify, redirect, url_for
import json
import os
from datetime import datetime, timedelta
import uuid

app = Flask(__name__)

# Migration platform configuration
SUPPORTED_LEGACY_SYSTEMS = {
    'oracle_oim': {
        'name': 'Oracle Identity Manager (OIM)',
        'version_support': ['11g', '12c'],
        'complexity': 'High',
        'typical_timeline': '12-18 weeks'
    },
    'one_identity': {
        'name': 'One Identity Manager',
        'version_support': ['8.x', '9.x'],
        'complexity': 'Medium',
        'typical_timeline': '8-12 weeks'
    },
    'ibm_tivoli': {
        'name': 'IBM Tivoli Identity Manager',
        'version_support': ['5.x', '6.x'],
        'complexity': 'High',
        'typical_timeline': '14-20 weeks'
    },
    'sailpoint_iiq': {
        'name': 'SailPoint IdentityIQ',
        'version_support': ['7.x', '8.x'],
        'complexity': 'Medium',
        'typical_timeline': '6-10 weeks'
    }
}

def get_current_dates():
    """Generate dynamic dates for migration timeline"""
    today = datetime.now()
    return {
        'discovery_start': today,
        'analysis_complete': today + timedelta(days=7),
        'migration_start': today + timedelta(days=14),
        'testing_phase': today + timedelta(days=35),
        'go_live': today + timedelta(days=49),
        'post_migration': today + timedelta(days=63)
    }

def add_template_globals():
    """Add global variables to template context"""
    app.jinja_env.globals['timedelta'] = timedelta

add_template_globals()

@app.route('/')
def index():
    """Main landing page"""
    dates = get_current_dates()
    return render_template('index.html', 
                         supported_systems=SUPPORTED_LEGACY_SYSTEMS,
                         dates=dates)

@app.route('/discovery')
def discovery():
    """Legacy system discovery and assessment"""
    # Prepare legacy systems data for the template
    legacy_systems = [
        {
            'id': 'oracle_oim',
            'name': 'Oracle Identity Manager (OIM)',
            'icon': 'fab fa-oracle',
            'color': 'danger',
            'complexity': 'High'
        },
        {
            'id': 'one_identity',
            'name': 'One Identity Manager',
            'icon': 'fas fa-id-card',
            'color': 'primary',
            'complexity': 'Medium'
        },
        {
            'id': 'ibm_tivoli',
            'name': 'IBM Tivoli Identity Manager',
            'icon': 'fab fa-ibm',
            'color': 'dark',
            'complexity': 'High'
        },
        {
            'id': 'sailpoint_iiq',
            'name': 'SailPoint IdentityIQ',
            'icon': 'fas fa-anchor',
            'color': 'info',
            'complexity': 'Medium'
        }
    ]
    
    return render_template('discovery.html', 
                         legacy_systems=legacy_systems,
                         supported_systems=SUPPORTED_LEGACY_SYSTEMS)

@app.route('/discovery/analyze', methods=['POST'])
def analyze_legacy_system():
    """Analyze selected legacy IGA system"""
    data = request.json
    legacy_system = data.get('legacy_system')
    
    if legacy_system not in SUPPORTED_LEGACY_SYSTEMS:
        return jsonify({'error': 'Unsupported legacy system'}), 400
    
    # Simulate discovery analysis
    analysis_results = {
        'system_info': SUPPORTED_LEGACY_SYSTEMS[legacy_system],
        'discovery_summary': {
            'identities_discovered': 125000 + (hash(legacy_system) % 75000),
            'roles_discovered': 2500 + (hash(legacy_system) % 1500),
            'policies_discovered': 850 + (hash(legacy_system) % 650),
            'applications_integrated': 65 + (hash(legacy_system) % 35),
            'workflows_identified': 120 + (hash(legacy_system) % 80)
        },
        'compatibility_assessment': {
            'identity_mapping': 95 if legacy_system == 'sailpoint_iiq' else 85 + (hash(legacy_system) % 10),
            'role_conversion': 90 if legacy_system == 'sailpoint_iiq' else 80 + (hash(legacy_system) % 15),
            'policy_migration': 88 if legacy_system == 'sailpoint_iiq' else 75 + (hash(legacy_system) % 15),
            'workflow_compatibility': 85 if legacy_system == 'sailpoint_iiq' else 70 + (hash(legacy_system) % 20)
        },
        'migration_complexity': {
            'data_volume': 'High' if legacy_system in ['oracle_oim', 'ibm_tivoli'] else 'Medium',
            'customizations': 'Extensive' if legacy_system == 'oracle_oim' else 'Moderate',
            'integrations': 'Complex' if legacy_system in ['oracle_oim', 'ibm_tivoli'] else 'Standard'
        },
        'timeline_estimate': get_current_dates()
    }
    
    return jsonify(analysis_results)

@app.route('/migration')
def migration():
    """Migration execution dashboard"""
    # Get the system information from URL parameters
    system_id = request.args.get('system', 'sailpoint_iiq')
    
    # Get system details
    legacy_systems = {
        'oracle_oim': {
            'name': 'Oracle Identity Manager (OIM)',
            'icon': 'fab fa-oracle',
            'color': 'danger',
            'version': '12.2.1.4.0',
            'complexity': 'High'
        },
        'one_identity': {
            'name': 'One Identity Manager',
            'icon': 'fas fa-id-card',
            'color': 'primary',
            'version': '9.2',
            'complexity': 'Medium'
        },
        'ibm_tivoli': {
            'name': 'IBM Tivoli Identity Manager',
            'icon': 'fab fa-ibm',
            'color': 'dark',
            'version': '7.0.2',
            'complexity': 'High'
        },
        'sailpoint_iiq': {
            'name': 'SailPoint IdentityIQ',
            'icon': 'fas fa-anchor',
            'color': 'info',
            'version': '8.4',
            'complexity': 'Medium'
        }
    }
    
    selected_system = legacy_systems.get(system_id, legacy_systems['sailpoint_iiq'])
    
    # Calculate timeline based on complexity
    start_date = datetime.now()
    if selected_system['complexity'] == 'High':
        weeks = 12  # High complexity systems
    else:
        weeks = 8   # Medium complexity systems
    
    end_date = start_date + timedelta(weeks=weeks)
    
    migration_info = {
        'source_system': selected_system,
        'target_system': {
            'name': 'Saviynt Enterprise Platform',
            'icon': 'fas fa-shield-alt',
            'color': 'success'
        },
        'timeline': {
            'start_date': start_date.strftime('%b %d, %Y'),
            'end_date': end_date.strftime('%b %d, %Y'),
            'duration': f'{weeks} weeks',
            'status': 'Ready to Start'
        }
    }
    
    return render_template('migration.html', 
                         migration_info=migration_info,
                         system=system_id)

@app.route('/migration/start', methods=['POST'])
def start_migration():
    """Start the migration process"""
    data = request.json
    legacy_system = data.get('legacy_system', 'sailpoint_iiq')
    
    migration_id = str(uuid.uuid4())
    
    # Migration phases
    phases = [
        {
            'name': 'Legacy System Analysis',
            'duration': 5,
            'status': 'completed',
            'progress': 100,
            'tasks': ['System inventory', 'Data extraction', 'Configuration analysis']
        },
        {
            'name': 'Identity Data Migration',
            'duration': 8,
            'status': 'completed',
            'progress': 100,
            'tasks': ['User account migration', 'Identity correlation', 'Attribute mapping']
        },
        {
            'name': 'Role & Entitlement Conversion',
            'duration': 12,
            'status': 'in_progress',
            'progress': 75,
            'tasks': ['Role transformation', 'Entitlement mapping', 'Access certification setup']
        },
        {
            'name': 'Workflow & Policy Migration',
            'duration': 10,
            'status': 'pending',
            'progress': 0,
            'tasks': ['Workflow conversion', 'Policy recreation', 'Approval chains setup']
        },
        {
            'name': 'Testing & Validation',
            'duration': 7,
            'status': 'pending',
            'progress': 0,
            'tasks': ['Integration testing', 'User acceptance testing', 'Performance validation']
        },
        {
            'name': 'Go-Live & Production',
            'duration': 3,
            'status': 'pending',
            'progress': 0,
            'tasks': ['Production deployment', 'User training', 'Support transition']
        }
    ]
    
    return jsonify({
        'migration_id': migration_id,
        'legacy_system': SUPPORTED_LEGACY_SYSTEMS.get(legacy_system, {}),
        'phases': phases,
        'overall_progress': 58,
        'estimated_completion': (datetime.now() + timedelta(days=28)).isoformat()
    })

@app.route('/compliance')
def compliance():
    """Compliance monitoring and assessment"""
    # Get the system information from URL parameters
    system_id = request.args.get('system', 'sailpoint_iiq')
    
    # Get system details
    legacy_systems = {
        'oracle_oim': {
            'name': 'Oracle Identity Manager (OIM)',
            'icon': 'fab fa-oracle',
            'color': 'danger',
            'complexity': 'High'
        },
        'one_identity': {
            'name': 'One Identity Manager',
            'icon': 'fas fa-id-card',
            'color': 'primary',
            'complexity': 'Medium'
        },
        'ibm_tivoli': {
            'name': 'IBM Tivoli Identity Manager',
            'icon': 'fab fa-ibm',
            'color': 'dark',
            'complexity': 'High'
        },
        'sailpoint_iiq': {
            'name': 'SailPoint IdentityIQ',
            'icon': 'fas fa-anchor',
            'color': 'info',
            'complexity': 'Medium'
        }
    }
    
    selected_system = legacy_systems.get(system_id, legacy_systems['sailpoint_iiq'])
    dates = get_current_dates()
    
    compliance_data = {
        'source_system': selected_system,
        'compliance_scores': {
            'sox_compliance': 95 if selected_system['complexity'] == 'Medium' else 88,
            'gdpr_compliance': 92,
            'hipaa_compliance': 89,
            'overall_score': 92
        }
    }
    
    return render_template('compliance.html', 
                         dates=dates, 
                         compliance_data=compliance_data,
                         system=system_id)

@app.route('/analytics')
def analytics():
    """Migration analytics and insights"""
    # Get the system information from URL parameters
    system_id = request.args.get('system', 'sailpoint_iiq')
    
    # Get system details
    legacy_systems = {
        'oracle_oim': {
            'name': 'Oracle Identity Manager (OIM)',
            'icon': 'fab fa-oracle',
            'color': 'danger',
            'complexity': 'High'
        },
        'one_identity': {
            'name': 'One Identity Manager',
            'icon': 'fas fa-id-card',
            'color': 'primary',
            'complexity': 'Medium'
        },
        'ibm_tivoli': {
            'name': 'IBM Tivoli Identity Manager',
            'icon': 'fab fa-ibm',
            'color': 'dark',
            'complexity': 'High'
        },
        'sailpoint_iiq': {
            'name': 'SailPoint IdentityIQ',
            'icon': 'fas fa-anchor',
            'color': 'info',
            'complexity': 'Medium'
        }
    }
    
    selected_system = legacy_systems.get(system_id, legacy_systems['sailpoint_iiq'])
    dates = get_current_dates()
    
    # Generate analytics data based on system complexity
    if selected_system['complexity'] == 'High':
        identities_total = 15000
        progress = 35
    else:
        identities_total = 12000
        progress = 42
    
    analytics_data = {
        'source_system': selected_system,
        'overall_progress': progress,
        'identities_migrated': int(identities_total * (progress / 100)),
        'identities_total': identities_total,
        'compliance_score': 92,
        'migration_speed': 250,
        'roles_migrated': int(2341 * (progress / 100)),
        'policies_migrated': int(127 * (progress / 100))
    }
    
    return render_template('analytics.html', 
                         dates=dates, 
                         analytics=analytics_data,
                         system=system_id)

@app.route('/reports')
def reports():
    """Reports and documentation"""
    # Get the system information from URL parameters
    system_id = request.args.get('system', 'sailpoint_iiq')
    
    # Get system details
    legacy_systems = {
        'oracle_oim': {
            'name': 'Oracle Identity Manager (OIM)',
            'icon': 'fab fa-oracle',
            'color': 'danger',
            'complexity': 'High'
        },
        'one_identity': {
            'name': 'One Identity Manager',
            'icon': 'fas fa-id-card',
            'color': 'primary',
            'complexity': 'Medium'
        },
        'ibm_tivoli': {
            'name': 'IBM Tivoli Identity Manager',
            'icon': 'fab fa-ibm',
            'color': 'dark',
            'complexity': 'High'
        },
        'sailpoint_iiq': {
            'name': 'SailPoint IdentityIQ',
            'icon': 'fas fa-anchor',
            'color': 'info',
            'complexity': 'Medium'
        }
    }
    
    selected_system = legacy_systems.get(system_id, legacy_systems['sailpoint_iiq'])
    
    # Calculate system-specific values like in analytics
    complexity_factors = {'High': 0.65, 'Medium': 0.8, 'Low': 0.95}
    progress = int(35 + (complexity_factors.get(selected_system['complexity'], 0.8) * 15))
    identities_total = 12847
    
    report_data = {
        'source_system': selected_system,
        'progress': progress,
        'identities_migrated': int(identities_total * (progress / 100)),
        'compliance_score': 92,
        'cost_savings': 450.5,
        'migration_summary': {
            'identities_discovered': identities_total,
            'roles_discovered': 2341,
            'policies_discovered': 127,
            'applications_discovered': 47
        }
    }
    
    available_reports = [
        {
            'title': f'{selected_system["name"]} Discovery Report',
            'description': f'Comprehensive analysis of {selected_system["name"]} system configuration, users, roles, and policies.',
            'type': 'discovery',
            'icon': 'fas fa-search',
            'last_generated': datetime.now().strftime('%Y-%m-%d %H:%M')
        },
        {
            'title': 'Compatibility Assessment',
            'description': f'Technical compatibility analysis between {selected_system["name"]} and Saviynt platform.',
            'type': 'compatibility',
            'icon': 'fas fa-check-circle',
            'last_generated': datetime.now().strftime('%Y-%m-%d %H:%M')
        },
        {
            'title': 'Migration Roadmap',
            'description': 'Detailed migration timeline, phases, and resource requirements.',
            'type': 'roadmap',
            'icon': 'fas fa-route',
            'last_generated': datetime.now().strftime('%Y-%m-%d %H:%M')
        },
        {
            'title': 'Risk Assessment',
            'description': 'Security and compliance risk analysis for the migration process.',
            'type': 'risk',
            'icon': 'fas fa-shield-alt',
            'last_generated': datetime.now().strftime('%Y-%m-%d %H:%M')
        },
        {
            'title': 'Cost-Benefit Analysis',
            'description': 'Financial impact assessment and ROI projections for the migration.',
            'type': 'financial',
            'icon': 'fas fa-chart-line',
            'last_generated': datetime.now().strftime('%Y-%m-%d %H:%M')
        },
        {
            'title': 'User Training Plan',
            'description': 'Comprehensive training strategy and materials for end users.',
            'type': 'training',
            'icon': 'fas fa-graduation-cap',
            'last_generated': datetime.now().strftime('%Y-%m-%d %H:%M')
        }
    ]
    
    return render_template('reports.html', 
                         report_data=report_data,
                         available_reports=available_reports,
                         system=system_id)

@app.route('/compliance/assessment', methods=['POST'])
def compliance_assessment():
    """Generate compliance assessment report"""
    data = request.json
    legacy_system = data.get('legacy_system', 'sailpoint_iiq')
    
    assessment = {
        'regulatory_compliance': {
            'sox_compliance': 95,
            'gdpr_compliance': 90,
            'hipaa_compliance': 88,
            'pci_dss_compliance': 92
        },
        'security_posture': {
            'identity_governance': 94,
            'access_controls': 91,
            'audit_trail': 96,
            'segregation_of_duties': 89
        },
        'risk_factors': [
            {'category': 'Data Migration', 'risk_level': 'Medium', 'mitigation': 'Comprehensive testing'},
            {'category': 'System Integration', 'risk_level': 'Low', 'mitigation': 'API validation'},
            {'category': 'User Adoption', 'risk_level': 'Medium', 'mitigation': 'Training program'},
            {'category': 'Compliance Gap', 'risk_level': 'Low', 'mitigation': 'Policy updates'}
        ],
        'remediation_plan': {
            'immediate_actions': 5,
            'short_term_actions': 12,
            'long_term_actions': 8
        }
    }
    
    return jsonify(assessment)

@app.route('/reports/generate', methods=['POST'])
def generate_report():
    """Generate migration report"""
    data = request.json
    report_type = data.get('report_type', 'comprehensive')
    
    report = {
        'report_id': str(uuid.uuid4()),
        'generated_at': datetime.now().isoformat(),
        'report_type': report_type,
        'executive_summary': {
            'migration_status': 'In Progress',
            'completion_percentage': 58,
            'systems_migrated': 3,
            'identities_processed': 125000,
            'compliance_score': 92
        }
    }
    
    return jsonify(report)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5007)
