# SR Bank - Banking Application

A secure command-line banking application built with Python and MariaDB. Features user authentication, account management, password change functionality, and money transfers with security best practices.

## Features

- **User Authentication**: Secure signup and login with bcrypt password hashing
- **Account Management**: Create accounts with unique 16-digit IDs and track balance
- **Money Transfers**: Transfer money between accounts with validation
- **Settings**: Change account password with secure verification
- **Secure Credentials**: Environment variables for database configuration
- **Input Validation**: Comprehensive validation for passwords, amounts, and user inputs

## Security Features

- Password hashing with bcrypt + salt (one-way hashing)
- Parameterized SQL queries (SQL injection protection)
- Environment variables for sensitive data (.env)
- Password confirmation on signup and password change
- Old password verification before allowing password change
- Prevention of reusing old password
- Transaction rollback on errors
- Input validation (minimum 8-character passwords, positive amounts)

## Requirements

- Python 3.8+
- MariaDB 10.5+ or MySQL 8.0+
- Dependencies:
  - `bcrypt==5.0.0`
  - `mysql-connector-python==8.0.33`
  - `python-dotenv==1.0.0`

## Installation

1. **Clone the repository:**
```bash
git clone https://github.com/shahmeer-raza/bankingapp.git
cd bankingapp
```

2. **Create virtual environment (recommended):**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies:**
```bash
pip install bcrypt mysql-connector-python python-dotenv
```

4. **Create `.env` file:**
```bash
cp _env .env
```

Edit `.env` with your database credentials:
```
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=srbank
```

5. **Set up database:**
```sql
CREATE DATABASE srbank;
USE srbank;

CREATE TABLE users (
    account_id VARCHAR(255) PRIMARY KEY,
    account_name VARCHAR(255) NOT NULL,
    account_balance INT DEFAULT 0,
    account_password VARCHAR(255) NOT NULL
);
```

## Usage

Run the application:
```bash
python app.py
```

### Main Menu

1. **Sign Up** - Create a new account
   - Enter your name
   - Set password (minimum 8 characters)
   - Confirm password (3 attempts)
   - Automatic 16-digit account ID generation

2. **Login** - Login with existing account
   - Enter account ID
   - Enter password
   - Secure bcrypt verification

3. **Exit** - Close the application

### Dashboard (After Login)

After logging in, you have access to:

1. **Check Balance** - View your current account balance
2. **Transfer Money** - Send money to another account
   - Validate recipient account exists
   - Confirm amount and recipient
   - Transaction validation and rollback on failure
3. **Settings** - Manage your account
   - Change password with old password verification
   - Prevent reusing old password
   - Secure new password confirmation
4. **Logout** - Exit dashboard and return to main menu

## Project Structure

```
sr-bank/
├── app.py              # Main application entry point
├── user_mgmt.py        # Database operations and queries
├── signup_page.py      # User registration logic
├── login_page.py       # Authentication with bcrypt
├── dashboard.py        # Dashboard UI and menu
├── transfer_money.py   # Money transfer logic and validation
├── settings.py         # Account settings (password change)
├── .env                # Environment variables (not in git)
├── _env                # Example env template
├── .gitignore          # Git ignore rules
└── README.md           # This file
```

## File Descriptions

| File | Purpose |
|------|---------|
| **app.py** | Main menu loop, handles signup/login/exit flow |
| **user_mgmt.py** | Database connection and all CRUD operations |
| **signup_page.py** | User registration with password hashing |
| **login_page.py** | Authentication with bcrypt password verification |
| **dashboard.py** | User dashboard with balance and transfer options |
| **transfer_money.py** | Money transfer validation and execution |
| **settings.py** | Account settings including password change functionality |

## Security Notes

⚠️ **Important:**
- Never commit `.env` file to version control (it's in `.gitignore`)
- Use strong passwords (8+ characters minimum)
- Always use parameterized queries (already implemented)
- For production, add:
  - Rate limiting on login attempts
  - Account lockout after failed attempts
  - Comprehensive logging and audit trail
  - Two-factor authentication (2FA)
  - HTTPS for client-server communication

## How It Works

### Password Hashing
```python
# Signup: hash password with salt
hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

# Login: verify password against hash
bcrypt.checkpw(entered_password.encode('utf-8'), stored_hash)
```

### Money Transfer
```
1. Validate recipient exists
2. Check sender has sufficient balance
3. Validate amount > 0
4. Prevent self-transfer
5. Execute transfer with transaction rollback on error
```

### Password Change
```
1. Verify old password (3 attempts)
2. Get new password with validation
3. Prevent reusing old password
4. Confirm new password (3 attempts)
5. Hash and store new password
```

## Learning Outcomes

This project demonstrates:
- Secure password storage with bcrypt hashing
- Database security with parameterized queries
- Environment variable management for sensitive data
- Exception handling and transaction management
- Input validation and error handling
- State management in CLI applications
- MySQL/MariaDB operations with Python

## Future Improvements

- [ ] Add transaction history with timestamps
- [ ] Implement login rate limiting
- [ ] Add comprehensive logging system
- [ ] Implement two-factor authentication (2FA)
- [ ] Add unit tests and integration tests
- [ ] Create REST API endpoints
- [ ] Add email verification on signup
- [ ] Implement account recovery system
- [ ] Add deposit/withdrawal functionality

## Troubleshooting

### "Cannot connect to database"
- Check `.env` file credentials are correct
- Ensure MariaDB/MySQL server is running
- Verify database name exists

### "Unknown column in where clause"
- Run database setup SQL commands
- Ensure `users` table exists with correct columns

### "Module not found"
- Ensure virtual environment is activated
- Run `pip install -r requirements.txt` or install dependencies manually

## License

This project is open source and available under the MIT License.

## Author

Created as a practice project for learning cybersecurity, authentication, and database security with Python.
