# Setting Up GitHub Authentication on Your Local Machine

## Introduction

Securely authenticating with GitHub from your local machine is essential for pushing code, accessing private repositories, and performing other operations that require verification of your identity. This guide covers the most common authentication methods.

## Authentication Methods

GitHub supports several authentication methods for local development:

- **SSH Keys**: Secure, key-based authentication (recommended)
- **Personal Access Tokens**: Password replacement for HTTPS authentication
- **GitHub CLI**: Command-line tool with built-in authentication
- **Git Credential Manager**: Helper that stores credentials securely

## SSH Key Authentication

SSH keys provide a secure way to connect without entering your username and password each time.

### Generating an SSH Key

1. Open a terminal and check for existing SSH keys:

   ```bash
   ls -la ~/.ssh
   ```

2. Generate a new SSH key:

   ```bash
   ssh-keygen -t ed25519 -C "your_email@example.com"
   # Or for legacy systems:
   # ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
   ```

3. When prompted, press Enter to accept the default file location. Optionally enter a secure passphrase.

### Adding SSH Key to SSH Agent

1. Start the SSH agent:

   ```bash
   # macOS/Linux
   eval "$(ssh-agent -s)"
   
   # Windows (Git Bash)
   eval "$(ssh-agent -s)"
   # or PowerShell
   # Start-Service ssh-agent
   ```

2. Add your private key to the SSH agent:

   ```bash
   ssh-add ~/.ssh/id_ed25519
   # Or if you used RSA:
   # ssh-add ~/.ssh/id_rsa
   ```

### Adding SSH Key to Your GitHub Account

1. Copy your SSH public key to clipboard:

   ```bash
   # macOS
   pbcopy < ~/.ssh/id_ed25519.pub
   
   # Windows (Git Bash)
   cat ~/.ssh/id_ed25519.pub | clip
   
   # Linux
   xclip -sel clip < ~/.ssh/id_ed25519.pub
   # or
   cat ~/.ssh/id_ed25519.pub
   # then manually copy the output
   ```

2. Go to GitHub:
   - Click your profile photo → Settings
   - Select "SSH and GPG keys" from the sidebar
   - Click "New SSH key"
   - Add a descriptive title
   - Paste your key into the "Key" field
   - Click "Add SSH key"

3. Verify your connection:

   ```bash
   ssh -T git@github.com
   ```

### Using SSH URLs for Repositories

When cloning a repository, use the SSH URL:

```bash
git clone https://github.com/IvyLong/Temporary.git
```

For existing repositories, update the remote URL. For example:

```bash
git remote add origin git@github.com:IvyLong/DataCamp-Python.git
git branch -M main
git push -u origin main
```
