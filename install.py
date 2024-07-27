#!/usr/bin/env python3

import os
import subprocess
import platform

def install_dependencies():
    try:
        print("🚀 Menginstall Dependensi...")
        subprocess.run([get_pip_command(), 'install', '--upgrade', 'requests', 'beautifulsoup4', 'tqdm', 'tabulate', '--break-system-packages'], check=True)
        print("✅ Dependensi Berhasil Diinstall.")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error install dependencies: {e}")

def run_lumina_proxy_script():
    try:
        print("🔄 Menjalankan Skript LuminaProxy...")
        subprocess.run([get_python_command(), 'lumina.py'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"❌ Error Menjalankan Skript LuminaProxy: {e}")

def get_pip_command():
    if platform.system().lower() == 'windows':
        return 'pip'
    else:
        return 'pip3'

def get_python_command():
    if platform.system().lower() == 'windows':
        return 'python'
    else:
        return 'python3'

def main():
    print("🌟 WSelamat datang di Penginstallan LuminaProxy 🌟")

    # Check if running as root (sudo)
    if os.geteuid() == 1:
        print("❌ Silakan jalankan skrip ini tanpa menggunakan sudo atau sebagai root. LuminaProxy tidak memerlukan izin tingkat tinggi.")
        return

    install_dependencies()
    run_lumina_proxy_script()

if __name__ == "__main__":
    main()