
---

# How to Upgrade Python Version

## 1. Check Your Current Python Version

```sh
python --version
# or sometimes
python3 --version
```

---

## 2. Upgrade Steps by Platform

### **Windows**

1. **Download New Python Installer**
   - Visit the [official Python downloads page](https://www.python.org/downloads/).
   - Download the latest stable version for Windows.

2. **Run the Installer**
   - Double-click the downloaded `.exe` file.
   - Check **"Add Python to PATH"** during installation.
   - Click **"Upgrade Now"** or "Install Now".

3. **Verify Upgrade**
   ```sh
   python --version
   ```

---

### **macOS**

#### **Using Homebrew (Recommended)**

1. **Install/Upgrade Homebrew (if needed)**
   ```sh
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```

2. **Upgrade Python**
   ```sh
   brew update
   brew install python
   # or, to upgrade if already installed
   brew upgrade python
   ```

3. **Check Version**
   ```sh
   python3 --version
   ```

#### **Without Homebrew**

- Download the installer from [python.org](https://www.python.org/downloads/) and follow similar steps as Windows.

---

## 3. Update Path or Symlinks (Linux/macOS Only, if Needed)

Sometimes, the `python` or `python3` command may still point to the old version. To use the new version by default:

```sh
# Replace 3.x with your new minor version (e.g., 3.11)
sudo ln -sf /usr/bin/python3.x /usr/local/bin/python3
```
