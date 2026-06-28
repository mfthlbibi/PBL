import numpy as np
from PIL import Image
import time
import os

def compress_channel(channel, num_components):
    """
    Fungsi untuk mereduksi dimensi satu channel warna menggunakan PCA.
    """
    # 1. Menghitung mean dan memusatkan data
    mean = np.mean(channel, axis=0)
    centered_data = channel - mean
    
    # 2. Menghitung Covariance Matrix
    cov_matrix = np.cov(centered_data, rowvar=False) 
    
    # 3. Menghitung eigenvalue dan eigenvector
    eigenvalues, eigenvectors = np.linalg.eigh(cov_matrix)
    
    # 4. Mengurutkan eigenvalue secara descending
    sorted_idx = np.argsort(eigenvalues)[::-1]
    sorted_eigenvectors = eigenvectors[:, sorted_idx]
    
    # 5. Menghasilkan dataset baru dengan n komponen utama
    eigenvectors_subset = sorted_eigenvectors[:, :num_components]
    transformed = np.dot(centered_data, eigenvectors_subset)
    
    # Rekonstruksi citra
    reconstructed = np.dot(transformed, eigenvectors_subset.T) + mean
    return reconstructed

def run_pca_compression(input_path, output_path, k):
    """
    Menjalankan kompresi pada gambar RGB dan menghitung waktu eksekusi.
    """
    start_time = time.time()
    
    # Buka gambar menggunakan PIL
    img = Image.open(input_path).convert('RGB')
    img_array = np.array(img)
    
    # Pisahkan channel warna Red, Green, Blue
    r, g, b = img_array[:,:,0], img_array[:,:,1], img_array[:,:,2]
    
    # Kompresi tiap channel
    r_comp = compress_channel(r, k)
    g_comp = compress_channel(g, k)
    b_comp = compress_channel(b, k)
    
    # Gabungkan kembali channel warna
    reconstructed_img = np.dstack((r_comp, g_comp, b_comp))
    reconstructed_img = np.clip(reconstructed_img, 0, 255).astype(np.uint8)
    
    # Simpan hasil
    compressed_img = Image.fromarray(reconstructed_img)
    compressed_img.save(output_path)
    
    end_time = time.time()
    runtime = round(end_time - start_time, 4)
    
    # Hitung persentase perbedaan pixel (kompresi)
    original_size = os.path.getsize(input_path)
    compressed_size = os.path.getsize(output_path)
    pixel_diff_percentage = round((1 - (compressed_size / original_size)) * 100, 2)
    
    return runtime, pixel_diff_percentage