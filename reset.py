import os
import glob
import shutil

print("--- STARTING CLEANUP ---")

# 1. Delete the database
if os.path.exists("db.sqlite3"):
    try:
        os.remove("db.sqlite3")
        print("✅ Deleted db.sqlite3")
    except PermissionError:
        print("❌ ERROR: Close the server! (Ctrl+C in terminal)")
        exit()
else:
    print("ℹ️ db.sqlite3 was already gone.")

# 2. Delete migration files (Keep __init__.py)
migrations_path = os.path.join("core", "migrations")
if os.path.exists(migrations_path):
    files = glob.glob(os.path.join(migrations_path, "*.py"))
    for f in files:
        if "__init__" not in f:
            os.remove(f)
            print(f"✅ Deleted migration file: {f}")

# 3. Delete compiled python files (__pycache__)
for root, dirs, files in os.walk("."):
    for d in dirs:
        if d == "__pycache__":
            shutil.rmtree(os.path.join(root, d))
            print(f"✅ Cleaned cache: {os.path.join(root, d)}")

print("--- CLEANUP COMPLETE ---")
print("Now run: python manage.py makemigrations")