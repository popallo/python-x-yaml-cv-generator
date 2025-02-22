from flask import Flask, render_template, abort, send_file, request
import yaml
import base64
import os
from config.settings import *
from weasyprint import HTML
from io import BytesIO

app = Flask(__name__)

def load_yaml_data(yaml_file):
    """Charge les données depuis un fichier YAML"""
    try:
        with open(yaml_file, 'r', encoding='utf-8') as file:
            return yaml.safe_load(file)
    except Exception as e:
        app.logger.error(f"Erreur lors de la lecture du YAML: {str(e)}")
        return None

def get_base64_photo(photo_path):
    """Convertit une photo en base64"""
    try:
        with open(photo_path, 'rb') as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')
    except FileNotFoundError:
        app.logger.error("Photo non trouvée")
        return None
    except PermissionError:
        app.logger.error("Permission refusée pour accéder à la photo")
        return None
    except Exception as e:
        app.logger.error(f"Erreur lors de la lecture de la photo: {str(e)}")
        return None

def get_available_cvs():
    """Liste tous les CVs disponibles"""
    cvs = {}
    
    # Ajouter les CVs personnalisés
    for file in os.listdir(CV_DIR):
        if file.endswith('.yaml'):
            cv_id = os.path.splitext(file)[0]
            cvs[cv_id] = f'CV - {cv_id}'
    
    return cvs

def get_cv_path(cv_id):
    """Récupère le chemin du fichier CV"""
    # Normalize the path to handle both Windows and Linux
    cv_path = os.path.normpath(os.path.join(CV_DIR, f'{cv_id}.yaml'))
    if os.path.exists(cv_path):
        return cv_path
    return None

def get_photo_path(cv_id):
    """Récupère le chemin de la photo"""
    # Chercher dans plusieurs extensions
    for ext in ['.jpg', '.jpeg', '.png']:
        photo_path = os.path.normpath(os.path.join(PHOTOS_DIR, f'{cv_id}{ext}'))
        if os.path.exists(photo_path):
            return photo_path
    return None  # Added explicit return None

@app.route('/')
def index():
    """Page d'accueil avec liste des CVs"""
    cvs = get_available_cvs()
    return render_template('index.html', cvs=cvs)

@app.route('/cv/<cv_id>')
def show_cv(cv_id):
    """Affiche un CV spécifique"""
    cv_path = get_cv_path(cv_id)
    if not cv_path:
        abort(404)
    
    cv_data = load_yaml_data(cv_path)
    if not cv_data:
        abort(500)
        
    photo_path = get_photo_path(cv_id)
    photo_base64 = get_base64_photo(photo_path)
    if not photo_base64:
        abort(500)
    
    # Get template choice from query parameter
    template_choice = request.args.get('template', 'standard')
    template_name = 'cv_ui_light_design.html' if template_choice == 'optimized' else 'cv_template.html'
    
    return render_template(
        template_name,
        cv=cv_data['cv'],
        cv_id=cv_id,
        photo=photo_base64,
        show_download=True
    )

@app.route('/download/<cv_id>')
def download_cv(cv_id):
    """Télécharge le CV au format PDF"""
    cv_path = get_cv_path(cv_id)
    if not cv_path:
        abort(404)
    
    cv_data = load_yaml_data(cv_path)
    if not cv_data:
        abort(500)
        
    photo_path = get_photo_path(cv_id)
    photo_base64 = get_base64_photo(photo_path)
    if not photo_base64:
        abort(500)
        # Get template choice from query parameter, same as show_cv
    template_choice = request.args.get('template', 'standard')
    template_name = 'cv_ui_light_design.html' if template_choice == 'optimized' else 'cv_template.html'
    
    # Générer le HTML avec le bon template
    html_content = render_template(
        template_name,
        cv=cv_data['cv'],
        cv_id=cv_id,
        photo=photo_base64,
        show_download=False  # Pour ne pas afficher le bouton dans le PDF
    )
    
    # Use absolute path for base_url and normalize it
    base_url = os.path.normpath(os.path.dirname(os.path.abspath(__file__)))
    html = HTML(string=html_content, base_url=base_url)
    pdf_file = BytesIO()
    html.write_pdf(pdf_file)
    pdf_file.seek(0)
    
    # Sanitize filename for both Windows and Linux
    template_suffix = '_light' if template_choice == 'optimized' else ''
    safe_filename = f'cv_{cv_id}{template_suffix}.pdf'.replace(' ', '_')
    
    return send_file(
        pdf_file,
        download_name=safe_filename,
        as_attachment=True,
        mimetype='application/pdf'
    )

if __name__ == '__main__':
    app.run(debug=True)