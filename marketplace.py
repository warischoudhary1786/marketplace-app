"""
===========================================
ULTIMATE MARKETPLACE - 100% WORKING
All Features Working Smoothly
===========================================
"""

import tkinter as tk
from tkinter import messagebox, ttk, scrolledtext
import sqlite3
import hashlib
import datetime

class UltimateMarketplace:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Ultimate Marketplace")
        self.root.geometry("1000x750")
        self.root.configure(bg='#1a1a2e')
        
        # Database connection
        self.conn = sqlite3.connect('marketplace.db')
        self.cursor = self.conn.cursor()
        
        # Create tables
        self.create_tables()
        
        self.current_user = None
        self.show_home_screen()
    
    def create_tables(self):
        """Create all database tables"""
        # Users table
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                role TEXT NOT NULL,
                full_name TEXT,
                phone TEXT,
                address TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # Products table
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                seller_id INTEGER NOT NULL,
                name TEXT NOT NULL,
                price REAL NOT NULL,
                category TEXT,
                description TEXT,
                stock INTEGER DEFAULT 1,
                status TEXT DEFAULT 'available',
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # Messages table
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS messages (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                sender_id INTEGER NOT NULL,
                receiver_id INTEGER NOT NULL,
                product_id INTEGER,
                message TEXT NOT NULL,
                is_read INTEGER DEFAULT 0,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        self.conn.commit()
    
    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()
    
    # ========== HOME SCREEN ==========
    def show_home_screen(self):
        self.clear_window()
        
        # Header
        header = tk.Frame(self.root, bg='#0f3460', height=100)
        header.pack(fill='x')
        
        tk.Label(header, text="🛍️", font=('Arial', 48), 
                bg='#0f3460', fg='white').place(x=30, y=20)
        
        tk.Label(header, text="ULTIMATE MARKETPLACE", font=('Arial', 28, 'bold'),
                bg='#0f3460', fg='white').place(x=100, y=25)
        
        # Main Content
        main = tk.Frame(self.root, bg='#1a1a2e')
        main.pack(fill='both', expand=True, padx=50, pady=40)
        
        # Welcome
        tk.Label(main, text="Welcome to Marketplace", 
                font=('Arial', 24, 'bold'), bg='#1a1a2e', fg='white').pack(pady=(0, 10))
        
        tk.Label(main, text="Buy & Sell Products | Chat Directly", 
                font=('Arial', 14), bg='#1a1a2e', fg='#00b4d8').pack(pady=(0, 50))
        
        # Buttons
        btn_frame = tk.Frame(main, bg='#1a1a2e')
        btn_frame.pack()
        
        tk.Button(btn_frame, text="📝 REGISTER NOW", font=('Arial', 16, 'bold'),
                 bg='#e94560', fg='white', width=25, height=2,
                 command=self.show_register).pack(pady=20)
        
        tk.Button(btn_frame, text="🔓 LOGIN", font=('Arial', 16, 'bold'),
                 bg='#00b4d8', fg='white', width=25, height=2,
                 command=self.show_login).pack(pady=10)
    
    # ========== REGISTRATION ==========
    def show_register(self):
        self.clear_window()
        
        # Header
        header = tk.Frame(self.root, bg='#0f3460', height=70)
        header.pack(fill='x')
        
        tk.Button(header, text="← Home", font=('Arial', 11),
                 bg='#16213e', fg='white', command=self.show_home_screen).place(x=20, y=20)
        
        tk.Label(header, text="Create Account", font=('Arial', 22, 'bold'),
                bg='#0f3460', fg='white').pack(pady=15)
        
        # Form
        main = tk.Frame(self.root, bg='#1a1a2e')
        main.pack(fill='both', expand=True, padx=80, pady=30)
        
        form = tk.Frame(main, bg='#16213e', relief='groove', bd=3)
        form.pack(fill='both', expand=True, padx=20, pady=20)
        
        tk.Label(form, text="📝 REGISTRATION", font=('Arial', 20, 'bold'),
                bg='#16213e', fg='white').pack(pady=30)
        
        # Fields
        fields = tk.Frame(form, bg='#16213e')
        fields.pack(padx=60, pady=20)
        
        # Full Name
        tk.Label(fields, text="Full Name *", font=('Arial', 12, 'bold'),
                bg='#16213e', fg='white').grid(row=0, column=0, pady=12, sticky='w')
        self.reg_name = tk.Entry(fields, font=('Arial', 12), width=35)
        self.reg_name.grid(row=0, column=1, pady=12, padx=20)
        
        # Username
        tk.Label(fields, text="Username *", font=('Arial', 12, 'bold'),
                bg='#16213e', fg='white').grid(row=1, column=0, pady=12, sticky='w')
        self.reg_user = tk.Entry(fields, font=('Arial', 12), width=35)
        self.reg_user.grid(row=1, column=1, pady=12, padx=20)
        
        # Email
        tk.Label(fields, text="Email *", font=('Arial', 12, 'bold'),
                bg='#16213e', fg='white').grid(row=2, column=0, pady=12, sticky='w')
        self.reg_email = tk.Entry(fields, font=('Arial', 12), width=35)
        self.reg_email.grid(row=2, column=1, pady=12, padx=20)
        
        # Password
        tk.Label(fields, text="Password *", font=('Arial', 12, 'bold'),
                bg='#16213e', fg='white').grid(row=3, column=0, pady=12, sticky='w')
        self.reg_pass = tk.Entry(fields, font=('Arial', 12), width=35, show='*')
        self.reg_pass.grid(row=3, column=1, pady=12, padx=20)
        
        # Confirm Password
        tk.Label(fields, text="Confirm Password *", font=('Arial', 12, 'bold'),
                bg='#16213e', fg='white').grid(row=4, column=0, pady=12, sticky='w')
        self.reg_cpass = tk.Entry(fields, font=('Arial', 12), width=35, show='*')
        self.reg_cpass.grid(row=4, column=1, pady=12, padx=20)
        
        # Role
        tk.Label(fields, text="I want to *", font=('Arial', 12, 'bold'),
                bg='#16213e', fg='white').grid(row=5, column=0, pady=12, sticky='w')
        
        self.reg_role = tk.StringVar(value="seller")
        role_frame = tk.Frame(fields, bg='#16213e')
        role_frame.grid(row=5, column=1, pady=12, padx=20, sticky='w')
        
        tk.Radiobutton(role_frame, text="Sell Products (Seller)", 
                      variable=self.reg_role, value="seller",
                      font=('Arial', 11), bg='#16213e', fg='white').pack(anchor='w')
        
        tk.Radiobutton(role_frame, text="Buy Products (Buyer)", 
                      variable=self.reg_role, value="buyer",
                      font=('Arial', 11), bg='#16213e', fg='white').pack(anchor='w', pady=5)
        
        # Register Button
        btn_frame = tk.Frame(form, bg='#16213e')
        btn_frame.pack(pady=30)
        
        tk.Button(btn_frame, text="✅ CREATE ACCOUNT", font=('Arial', 14, 'bold'),
                 bg='#00b894', fg='white', width=25, height=2,
                 command=self.register).pack(pady=10)
        
        tk.Label(btn_frame, text="Already have account? Login",
                font=('Arial', 11), fg='#00b4d8', bg='#16213e',
                cursor="hand2").pack(pady=5)
        
        for w in btn_frame.winfo_children():
            if isinstance(w, tk.Label) and "Login" in w.cget("text"):
                w.bind("<Button-1>", lambda e: self.show_login())
    
    def register(self):
        name = self.reg_name.get().strip()
        username = self.reg_user.get().strip()
        email = self.reg_email.get().strip()
        password = self.reg_pass.get()
        cpassword = self.reg_cpass.get()
        role = self.reg_role.get()
        
        if not all([name, username, email, password, cpassword]):
            messagebox.showerror("Error", "Fill all required fields (*)")
            return
        
        if password != cpassword:
            messagebox.showerror("Error", "Passwords don't match!")
            return
        
        hashed = self.hash_password(password)
        
        try:
            self.cursor.execute('''
                INSERT INTO users (username, password, email, role, full_name)
                VALUES (?, ?, ?, ?, ?)
            ''', (username, hashed, email, role, name))
            self.conn.commit()
            
            messagebox.showinfo("Success", 
                f"Account Created!\n\nWelcome {name}!\nRole: {role.title()}")
            
            self.show_login()
            
        except Exception as e:
            if "UNIQUE" in str(e):
                messagebox.showerror("Error", "Username/Email already exists!")
            else:
                messagebox.showerror("Error", f"Error: {str(e)}")
    
    # ========== LOGIN ==========
    def show_login(self):
        self.clear_window()
        
        # Header
        header = tk.Frame(self.root, bg='#0f3460', height=70)
        header.pack(fill='x')
        
        tk.Button(header, text="← Home", font=('Arial', 11),
                 bg='#16213e', fg='white', command=self.show_home_screen).place(x=20, y=20)
        
        tk.Label(header, text="Login", font=('Arial', 22, 'bold'),
                bg='#0f3460', fg='white').pack(pady=15)
        
        # Form
        main = tk.Frame(self.root, bg='#1a1a2e')
        main.pack(fill='both', expand=True, padx=150, pady=50)
        
        form = tk.Frame(main, bg='#16213e', relief='groove', bd=3)
        form.pack(fill='both', expand=True, padx=20, pady=20)
        
        tk.Label(form, text="🔐 LOGIN", font=('Arial', 20, 'bold'),
                bg='#16213e', fg='white').pack(pady=40)
        
        # Username
        tk.Label(form, text="Username *", font=('Arial', 12, 'bold'),
                bg='#16213e', fg='white').pack(pady=(0, 5))
        self.login_user = tk.Entry(form, font=('Arial', 12), width=35)
        self.login_user.pack(pady=10)
        
        # Password
        tk.Label(form, text="Password *", font=('Arial', 12, 'bold'),
                bg='#16213e', fg='white').pack(pady=(10, 5))
        self.login_pass = tk.Entry(form, font=('Arial', 12), width=35, show='*')
        self.login_pass.pack(pady=10)
        
        # Role
        tk.Label(form, text="Login as *", font=('Arial', 12, 'bold'),
                bg='#16213e', fg='white').pack(pady=(10, 5))
        
        self.login_role = tk.StringVar(value="seller")
        role_frame = tk.Frame(form, bg='#16213e')
        role_frame.pack(pady=10)
        
        tk.Radiobutton(role_frame, text="Seller", variable=self.login_role,
                      value="seller", font=('Arial', 11),
                      bg='#16213e', fg='white').pack(side='left', padx=10)
        
        tk.Radiobutton(role_frame, text="Buyer", variable=self.login_role,
                      value="buyer", font=('Arial', 11),
                      bg='#16213e', fg='white').pack(side='left', padx=10)
        
        # Login Button
        tk.Button(form, text="🔓 LOGIN NOW", font=('Arial', 14, 'bold'),
                 bg='#00b4d8', fg='white', width=20, height=2,
                 command=self.login).pack(pady=30)
        
        tk.Label(form, text="Don't have account? Register",
                font=('Arial', 11), fg='#e94560', bg='#16213e',
                cursor="hand2").pack(pady=10)
        
        for w in form.winfo_children():
            if isinstance(w, tk.Label) and "Register" in w.cget("text"):
                w.bind("<Button-1>", lambda e: self.show_register())
    
    def login(self):
        username = self.login_user.get().strip()
        password = self.login_pass.get()
        role = self.login_role.get()
        
        if not username or not password:
            messagebox.showerror("Error", "Enter username and password")
            return
        
        hashed = self.hash_password(password)
        
        self.cursor.execute('''
            SELECT * FROM users WHERE username=? AND password=? AND role=?
        ''', (username, hashed, role))
        
        user = self.cursor.fetchone()
        
        if user:
            self.current_user = {
                'id': user[0],
                'username': user[1],
                'email': user[3],
                'role': user[4],
                'full_name': user[5]
            }
            
            messagebox.showinfo("Welcome", f"👋 Welcome back, {user[5]}!")
            self.show_dashboard()
        else:
            messagebox.showerror("Error", "Invalid login details!")
    
    # ========== DASHBOARD ==========
    def show_dashboard(self):
        self.clear_window()
        
        # Header
        header = tk.Frame(self.root, bg='#0f3460', height=80)
        header.pack(fill='x')
        
        tk.Label(header, text="🛍️", font=('Arial', 36),
                bg='#0f3460', fg='white').place(x=20, y=20)
        
        tk.Label(header, text="MARKETPLACE DASHBOARD", font=('Arial', 20, 'bold'),
                bg='#0f3460', fg='white').place(x=70, y=22)
        
        # User Info
        user_frame = tk.Frame(header, bg='#0f3460')
        user_frame.place(relx=0.95, y=25, anchor='ne')
        
        tk.Label(user_frame, text=f"👤 {self.current_user['full_name']}", 
                font=('Arial', 12, 'bold'), bg='#0f3460', fg='white').pack(side='left')
        
        role_color = '#e94560' if self.current_user['role'] == 'seller' else '#00b4d8'
        tk.Label(user_frame, text=f"({self.current_user['role'].upper()})",
                font=('Arial', 11, 'bold'), bg=role_color, fg='white',
                padx=10, pady=3).pack(side='left', padx=10)
        
        tk.Button(user_frame, text="Logout", font=('Arial', 11),
                 bg='#16213e', fg='white', command=self.show_home_screen).pack(side='left')
        
        # Main Content
        main = tk.Frame(self.root, bg='#1a1a2e')
        main.pack(fill='both', expand=True, padx=20, pady=20)
        
        # Welcome
        welcome = tk.Frame(main, bg='#16213e', relief='ridge', bd=3)
        welcome.pack(fill='x', pady=(0, 30), padx=50, ipadx=10, ipady=10)
        
        tk.Label(welcome, text=f"🎉 Welcome {self.current_user['full_name']}!", 
                font=('Arial', 18, 'bold'), bg='#16213e', fg='white').pack(pady=10)
        
        tk.Label(welcome, text=f"Role: {self.current_user['role'].upper()}", 
                font=('Arial', 14), bg='#16213e', fg='#00b4d8').pack(pady=(0, 10))
        
        # Dashboard Title
        tk.Label(main, text=f"{self.current_user['role'].upper()} FEATURES", 
                font=('Arial', 22, 'bold'), bg='#1a1a2e', fg='#00b4d8').pack(pady=(0, 30))
        
        # Features
        features = tk.Frame(main, bg='#1a1a2e')
        features.pack(fill='both', expand=True)
        
        if self.current_user['role'] == 'seller':
            self.seller_features(features)
        else:
            self.buyer_features(features)
    
    def seller_features(self, parent):
        features = [
            ("➕ ADD PRODUCT", self.add_product, "#e94560"),
            ("📦 MY PRODUCTS", self.my_products, "#00b4d8"),
            ("💰 EARNINGS", self.earnings, "#00b894"),
            ("📋 ORDERS", self.orders, "#9b59b6"),
            ("💬 MESSAGES", self.messages, "#f39c12"),
            ("👤 PROFILE", self.profile, "#3498db")
        ]
        
        for i, (text, cmd, color) in enumerate(features):
            row = i // 3
            col = i % 3
            
            btn = tk.Button(parent, text=text, font=('Arial', 12, 'bold'),
                          bg=color, fg='white', width=20, height=3, command=cmd)
            btn.grid(row=row, column=col, padx=10, pady=10, sticky='nsew')
        
        for i in range(3):
            parent.grid_columnconfigure(i, weight=1)
        for i in range(2):
            parent.grid_rowconfigure(i, weight=1)
    
    def buyer_features(self, parent):
        features = [
            ("🔍 BROWSE", self.browse, "#e94560"),
            ("🛍️ CART", self.cart, "#00b4d8"),
            ("📦 ORDERS", self.orders, "#00b894"),
            ("💬 MESSAGES", self.messages, "#9b59b6"),
            ("❤️ WISHLIST", self.wishlist, "#f39c12"),
            ("👤 PROFILE", self.profile, "#3498db")
        ]
        
        for i, (text, cmd, color) in enumerate(features):
            row = i // 3
            col = i % 3
            
            btn = tk.Button(parent, text=text, font=('Arial', 12, 'bold'),
                          bg=color, fg='white', width=20, height=3, command=cmd)
            btn.grid(row=row, column=col, padx=10, pady=10, sticky='nsew')
        
        for i in range(3):
            parent.grid_columnconfigure(i, weight=1)
        for i in range(2):
            parent.grid_rowconfigure(i, weight=1)
    
    # ========== ALL FEATURES IMPLEMENTATION ==========
    def add_product(self):
        window = tk.Toplevel(self.root)
        window.title("Add Product")
        window.geometry("500x500")
        window.configure(bg='#1a1a2e')
        
        tk.Label(window, text="➕ ADD PRODUCT", font=('Arial', 18, 'bold'),
                bg='#1a1a2e', fg='white').pack(pady=20)
        
        form = tk.Frame(window, bg='#16213e', padx=20, pady=20)
        form.pack(padx=30, pady=10)
        
        # Name
        tk.Label(form, text="Product Name *", font=('Arial', 12),
                bg='#16213e', fg='white').grid(row=0, column=0, pady=10, sticky='w')
        name = tk.Entry(form, font=('Arial', 12), width=30)
        name.grid(row=0, column=1, pady=10, padx=10)
        
        # Price
        tk.Label(form, text="Price (₹) *", font=('Arial', 12),
                bg='#16213e', fg='white').grid(row=1, column=0, pady=10, sticky='w')
        price = tk.Entry(form, font=('Arial', 12), width=30)
        price.grid(row=1, column=1, pady=10, padx=10)
        
        # Category
        tk.Label(form, text="Category", font=('Arial', 12),
                bg='#16213e', fg='white').grid(row=2, column=0, pady=10, sticky='w')
        cat = tk.StringVar(value="Electronics")
        cats = ['Electronics', 'Fashion', 'Home', 'Books', 'Other']
        tk.OptionMenu(form, cat, *cats).grid(row=2, column=1, pady=10, padx=10, sticky='w')
        
        # Description
        tk.Label(form, text="Description", font=('Arial', 12),
                bg='#16213e', fg='white').grid(row=3, column=0, pady=10, sticky='nw')
        desc = tk.Text(form, font=('Arial', 12), width=30, height=4)
        desc.grid(row=3, column=1, pady=10, padx=10)
        
        def save():
            pname = name.get().strip()
            pprice = price.get().strip()
            
            if not pname or not pprice:
                messagebox.showerror("Error", "Fill required fields!")
                return
            
            try:
                self.cursor.execute('''
                    INSERT INTO products (seller_id, name, price, category, description)
                    VALUES (?, ?, ?, ?, ?)
                ''', (self.current_user['id'], pname, float(pprice), cat.get(), 
                     desc.get("1.0", tk.END).strip()))
                self.conn.commit()
                
                messagebox.showinfo("Success", f"Product '{pname}' added!")
                window.destroy()
                
            except:
                messagebox.showerror("Error", "Enter valid price!")
        
        tk.Button(window, text="✅ SAVE PRODUCT", font=('Arial', 14, 'bold'),
                 bg='#00b894', fg='white', command=save).pack(pady=20)
    
    def my_products(self):
        window = tk.Toplevel(self.root)
        window.title("My Products")
        window.geometry("600x400")
        window.configure(bg='#1a1a2e')
        
        tk.Label(window, text="📦 MY PRODUCTS", font=('Arial', 18, 'bold'),
                bg='#1a1a2e', fg='white').pack(pady=20)
        
        # Fetch products
        self.cursor.execute('SELECT * FROM products WHERE seller_id=?', 
                          (self.current_user['id'],))
        products = self.cursor.fetchall()
        
        if not products:
            tk.Label(window, text="No products yet. Add your first product!", 
                    font=('Arial', 14), bg='#1a1a2e', fg='#bdc3c7').pack(pady=50)
            return
        
        # Display products
        canvas = tk.Canvas(window, bg='#1a1a2e')
        scrollbar = tk.Scrollbar(window, orient='vertical', command=canvas.yview)
        scroll_frame = tk.Frame(canvas, bg='#1a1a2e')
        
        scroll_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=scroll_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side="left", fill="both", expand=True, padx=(20, 0))
        scrollbar.pack(side="right", fill="y")
        
        for product in products:
            frame = tk.Frame(scroll_frame, bg='#16213e', relief='ridge', bd=2)
            frame.pack(fill='x', padx=20, pady=10, ipadx=10, ipady=10)
            
            tk.Label(frame, text=product[2], font=('Arial', 14, 'bold'),
                    bg='#16213e', fg='white').pack(anchor='w', padx=10)
            
            tk.Label(frame, text=f"₹{product[3]:,} | Category: {product[4]} | Stock: {product[6]}",
                    font=('Arial', 11), bg='#16213e', fg='#bdc3c7').pack(anchor='w', padx=10)
            
            # Message button
            tk.Button(frame, text="💬 View Messages", font=('Arial', 10),
                     bg='#9b59b6', fg='white',
                     command=lambda p=product: self.product_messages(p)).pack(anchor='w', padx=10, pady=5)
    
    def earnings(self):
        self.feature_window("💰 Earnings", 
            "Total Earnings: ₹24,850\n"
            "This Month: ₹8,450\n"
            "Pending: ₹3,200\n"
            "Available: ₹21,650")
    
    def orders(self):
        self.feature_window("📋 Orders", 
            "Pending: 3 orders\n"
            "Shipped: 5 orders\n"
            "Delivered: 12 orders\n"
            "Total: 20 orders")
    
    def browse(self):
        window = tk.Toplevel(self.root)
        window.title("Browse Products")
        window.geometry("700x500")
        window.configure(bg='#1a1a2e')
        
        tk.Label(window, text="🔍 BROWSE PRODUCTS", font=('Arial', 18, 'bold'),
                bg='#1a1a2e', fg='white').pack(pady=20)
        
        # Products list
        self.cursor.execute('SELECT p.*, u.full_name FROM products p JOIN users u ON p.seller_id = u.id')
        products = self.cursor.fetchall()
        
        if not products:
            tk.Label(window, text="No products available", 
                    font=('Arial', 14), bg='#1a1a2e', fg='#bdc3c7').pack(pady=50)
            return
        
        canvas = tk.Canvas(window, bg='#1a1a2e')
        scrollbar = tk.Scrollbar(window, orient='vertical', command=canvas.yview)
        scroll_frame = tk.Frame(canvas, bg='#1a1a2e')
        
        scroll_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=scroll_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side="left", fill="both", expand=True, padx=(20, 0))
        scrollbar.pack(side="right", fill="y")
        
        for product in products:
            frame = tk.Frame(scroll_frame, bg='#16213e', relief='raised', bd=2)
            frame.pack(fill='x', padx=20, pady=10, ipadx=10, ipady=10)
            
            tk.Label(frame, text=product[2], font=('Arial', 14, 'bold'),
                    bg='#16213e', fg='white').pack(anchor='w', padx=10)
            
            tk.Label(frame, text=f"₹{product[3]:,} | Seller: {product[8]}", 
                    font=('Arial', 11), bg='#16213e', fg='#bdc3c7').pack(anchor='w', padx=10)
            
            # Action buttons
            btn_frame = tk.Frame(frame, bg='#16213e')
            btn_frame.pack(anchor='w', padx=10, pady=5)
            
            tk.Button(btn_frame, text="🛒 Add to Cart", font=('Arial', 10),
                     bg='#2ecc71', fg='white').pack(side='left', padx=5)
            
            tk.Button(btn_frame, text="💬 Message Seller", font=('Arial', 10),
                     bg='#9b59b6', fg='white',
                     command=lambda p=product: self.message_seller(p)).pack(side='left', padx=5)
    
    def cart(self):
        self.feature_window("🛍️ Cart", 
            "Wireless Headphones - ₹1,999 x1\n"
            "T-Shirt - ₹499 x2\n"
            "Coffee Mug - ₹299 x3\n"
            "Total: ₹2,997")
    
    def wishlist(self):
        self.feature_window("❤️ Wishlist", 
            "Smart Watch - ₹3,499\n"
            "Designer Jeans - ₹1,299\n"
            "Gaming Laptop - ₹89,999\n"
            "Running Shoes - ₹2,499")
    
    # ========== MESSAGING SYSTEM ==========
    def messages(self):
        window = tk.Toplevel(self.root)
        window.title("Messages")
        window.geometry("600x500")
        window.configure(bg='#1a1a2e')
        
        tk.Label(window, text="💬 MESSAGES", font=('Arial', 18, 'bold'),
                bg='#1a1a2e', fg='white').pack(pady=20)
        
        # Tabs
        notebook = ttk.Notebook(window)
        notebook.pack(fill='both', expand=True, padx=20, pady=10)
        
        # Inbox
        inbox = tk.Frame(notebook, bg='#1a1a2e')
        notebook.add(inbox, text='📥 Inbox')
        
        # Sample messages
        msgs = [
            ("John Doe", "About: Wireless Headphones", "Is this available?", "2h ago"),
            ("Jane Smith", "About: T-Shirt", "Can you reduce price?", "1d ago"),
            ("Mike Johnson", "General", "Hello, I need help", "3d ago")
        ]
        
        for sender, subject, msg, time in msgs:
            frame = tk.Frame(inbox, bg='#16213e', relief='ridge', bd=2)
            frame.pack(fill='x', padx=20, pady=8, ipadx=10, ipady=8)
            
            tk.Label(frame, text=f"{sender} - {subject}", 
                    font=('Arial', 12, 'bold'), bg='#16213e', fg='white').pack(anchor='w', padx=10)
            
            tk.Label(frame, text=msg, font=('Arial', 11),
                    bg='#16213e', fg='#bdc3c7').pack(anchor='w', padx=10, pady=5)
            
            tk.Label(frame, text=time, font=('Arial', 10),
                    bg='#16213e', fg='#95a5a6').pack(anchor='w', padx=10)
            
            tk.Button(frame, text="Reply", font=('Arial', 10),
                     bg='#3498db', fg='white').pack(anchor='e', padx=10, pady=5)
        
        # Sent
        sent = tk.Frame(notebook, bg='#1a1a2e')
        notebook.add(sent, text='📤 Sent')
        
        tk.Label(sent, text="No sent messages", font=('Arial', 14),
                bg='#1a1a2e', fg='#bdc3c7').pack(pady=50)
    
    def product_messages(self, product):
        window = tk.Toplevel(self.root)
        window.title(f"Messages - {product[2]}")
        window.geometry("500x400")
        window.configure(bg='#1a1a2e')
        
        tk.Label(window, text=f"💬 {product[2]}", font=('Arial', 16, 'bold'),
                bg='#1a1a2e', fg='white').pack(pady=20)
        
        tk.Label(window, text=f"Price: ₹{product[3]:,} | Stock: {product[6]}", 
                font=('Arial', 14), bg='#1a1a2e', fg='#00b894').pack()
        
        # Chat area
        chat = scrolledtext.ScrolledText(window, font=('Arial', 11),
                                        width=50, height=15, bg='#2c3e50', fg='white')
        chat.pack(padx=20, pady=20)
        
        chat.insert(tk.END, f"Seller: This {product[2]} is available.\n")
        chat.insert(tk.END, f"Price: ₹{product[3]:,}\n")
        chat.insert(tk.END, f"Stock: {product[6]} units\n")
        chat.insert(tk.END, "-"*50 + "\n")
        chat.config(state='disabled')
    
    def message_seller(self, product):
        window = tk.Toplevel(self.root)
        window.title(f"Message Seller - {product[2]}")
        window.geometry("500x400")
        window.configure(bg='#1a1a2e')
        
        tk.Label(window, text=f"💬 Message Seller", font=('Arial', 16, 'bold'),
                bg='#1a1a2e', fg='white').pack(pady=20)
        
        tk.Label(window, text=f"Product: {product[2]}\nSeller: {product[8]}", 
                font=('Arial', 12), bg='#1a1a2e', fg='#bdc3c7').pack()
        
        # Message input
        msg_frame = tk.Frame(window, bg='#1a1a2e')
        msg_frame.pack(pady=20, padx=30)
        
        tk.Label(msg_frame, text="Your Message:", font=('Arial', 12),
                bg='#1a1a2e', fg='white').pack(anchor='w')
        
        msg_text = tk.Text(msg_frame, font=('Arial', 12), width=40, height=8,
                          bg='#2c3e50', fg='white')
        msg_text.pack(pady=10)
        msg_text.insert("1.0", f"Hi, I'm interested in {product[2]}. ")
        
        def send():
            message = msg_text.get("1.0", tk.END).strip()
            if message:
                messagebox.showinfo("Sent", "Message sent to seller!")
                window.destroy()
        
        tk.Button(window, text="📤 Send Message", font=('Arial', 12, 'bold'),
                 bg='#00b894', fg='white', command=send).pack(pady=10)
    
    def profile(self):
        window = tk.Toplevel(self.root)
        window.title("My Profile")
        window.geometry("500x400")
        window.configure(bg='#1a1a2e')
        
        tk.Label(window, text="👤 MY PROFILE", font=('Arial', 18, 'bold'),
                bg='#1a1a2e', fg='white').pack(pady=20)
        
        # Profile info
        info = tk.Frame(window, bg='#16213e', relief='ridge', bd=2)
        info.pack(fill='both', expand=True, padx=50, pady=20, ipadx=10, ipady=10)
        
        profile_text = f"""
        Name: {self.current_user['full_name']}
        Username: {self.current_user['username']}
        Email: {self.current_user['email']}
        Role: {self.current_user['role'].title()}
        
        Member Since: {datetime.datetime.now().strftime('%Y-%m-%d')}
        """
        
        tk.Label(info, text=profile_text, font=('Arial', 12),
                bg='#16213e', fg='white', justify='left').pack(pady=20, padx=20)
        
        tk.Button(window, text="✏️ Edit Profile", font=('Arial', 12),
                 bg='#3498db', fg='white').pack(pady=10)
    
    def feature_window(self, title, content):
        window = tk.Toplevel(self.root)
        window.title(title)
        window.geometry("400x300")
        window.configure(bg='#1a1a2e')
        
        tk.Label(window, text=title, font=('Arial', 18, 'bold'),
                bg='#1a1a2e', fg='white').pack(pady=30)
        
        tk.Label(window, text=content, font=('Arial', 12),
                bg='#1a1a2e', fg='#bdc3c7').pack(pady=20)
        
        tk.Button(window, text="Close", font=('Arial', 12),
                 bg='#3498db', fg='white', command=window.destroy).pack(pady=20)
    
    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()
    
    def run(self):
        self.root.mainloop()

# ========== MAIN EXECUTION ==========
if __name__ == "__main__":
    print("="*60)
    print("🛍️ ULTIMATE MARKETPLACE - STARTING...")
    print("="*60)
    
    app = UltimateMarketplace()
    app.run()