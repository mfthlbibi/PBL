from flask import Flask, render_template, request, jsonify
import os
import time
import webbrowser
from threading import Timer
from pca_compressor import run_pca_compression

# --- PERBAIKAN: Mengunci rute folder secara absolut ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_FOLDER = os.path.join(BASE_DIR, 'static')

# Memaksa Flask untuk selalu menunjuk ke folder static yang benar
app = Flask(__name__, static_folder=STATIC_FOLDER)
app.config['UPLOAD_FOLDER'] = STATIC_FOLDER
os.makedirs(STATIC_FOLDER, exist_ok=True)
# --------------------------------------------------------

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/compress', methods=['POST'])
def compress():
    if 'file' not in request.files:
        return jsonify({'error': 'Tidak ada file'})
        
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'File belum dipilih'})
        
    k_value = int(request.form.get('k_value', 50))
    
    input_path = os.path.join(app.config['UPLOAD_FOLDER'], 'input.jpg')
    output_path = os.path.join(app.config['UPLOAD_FOLDER'], 'output.jpg')
    
    file.save(input_path)
    
    orig_size_kb = os.path.getsize(input_path) / 1024
    
    start_time = time.time()
    run_pca_compression(input_path, output_path, k_value)
    end_time = time.time()
    
    comp_size_kb = os.path.getsize(output_path) / 1024
    
    runtime_ms = int((end_time - start_time) * 1000)
    size_saved_kb = orig_size_kb - comp_size_kb
    size_saved_percent = (size_saved_kb / orig_size_kb) * 100 if orig_size_kb > 0 else 0
    pixel_diff = abs((1 - (comp_size_kb / orig_size_kb)) * 100)
    
    timestamp = int(time.time())
    
    return jsonify({
        'original_url': f'/static/input.jpg?t={timestamp}',
        'compressed_url': f'/static/output.jpg?t={timestamp}',
        'orig_size': f"{orig_size_kb:.1f}",
        'comp_size': f"{comp_size_kb:.1f}",
        'runtime_ms': runtime_ms,
        'size_saved_percent': f"{size_saved_percent:.1f}",
        'size_saved_kb': f"{size_saved_kb:.1f}",
        'pixel_diff': f"{pixel_diff:.2f}"
    })

def open_browser():
    webbrowser.open_new("http://127.0.0.1:5000/")

if __name__ == '__main__':
    Timer(1.25, open_browser).start()
    app.run(debug=True, port=5000, use_reloader=False)