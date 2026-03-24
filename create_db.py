# check_admin.py
import sqlite3

print("=" * 50)
print("CHECKING ADMIN DATABASE")
print("=" * 50)

try:
    # Connect to database
    conn = sqlite3.connect("quiz.db")
    cur = conn.cursor()
    
    # Check if admin table exists
    cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='admin'")
    table_exists = cur.fetchone()
    
    if table_exists:
        print("✅ Admin table exists")
        
        # Check if there are any admin records
        cur.execute("SELECT * FROM admin")
        admins = cur.fetchall()
        
        if admins:
            print(f"✅ Found {len(admins)} admin record(s):")
            print("-" * 30)
            for admin in admins:
                print(f"ID: {admin[0]}")
                print(f"Username: {admin[1]}")
                print(f"Password: {admin[2]}")
                print("-" * 30)
        else:
            print("❌ No admin users found in the table")
            print("   Run reset_admin.py to create default admin")
    else:
        print("❌ Admin table does not exist")
        print("   Run reset_admin.py to create the table and admin user")
    
    # Also check users table
    print("\n" + "=" * 50)
    print("CHECKING USERS TABLE")
    print("=" * 50)
    
    cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='users'")
    if cur.fetchone():
        cur.execute("SELECT COUNT(*) FROM users")
        user_count = cur.fetchone()[0]
        print(f"✅ Users table exists with {user_count} user(s)")
    else:
        print("❌ Users table does not exist")
    
    conn.close()
    
except Exception as e:
    print(f"❌ Error: {e}")

print("\n" + "=" * 50)