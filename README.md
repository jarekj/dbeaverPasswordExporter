# Dbeaver Password Exporter
Python script that reads and exports passwords from Dbeaver


Install dependency
```cmd
pip install pycryptodome


pip install - r requirements.txt
```

Usage
```cmd
#if credentials-config.json is in windows user default path
python getDbeaverPasswords.py

#if credentials-config.json is passed as argument
python getDbeaverPasswords.py /path_to/credentials-config.json
```
