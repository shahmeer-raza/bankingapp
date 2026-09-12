# SR Bank - Banking Application

A secure command-line banking application built with Python and MySQL. Features user authentication, account management, and money transfers with security best practices.

## Features

- **User Authentication**: Secure signup and login with bcrypt password hashing
- **Account Management**: Create accounts with unique IDs and track balance
- **Money Transfers**: Transfer money between accounts with validation
- **Secure Credentials**: Environment variables for database configuration
- **Input Validation**: Comprehensive validation for passwords, amounts, and user inputs

## Security Features

-  Password hashing with bcrypt + salt
-  Parameterized SQL queries (SQL injection protection)
-  Environment variables for sensitive data (.env)
-  Password confirmation on signup
-  Transaction rollback on errors
-  Input validation (minimum 8-char passwords, positive amounts)

## Requirements

- Python 3.7+
- MySQL Server
- Dependencies: `bcrypt`, `mysql-connector-python`, `python-dotenv`

## Installation

1. **Clone the repository:**
```bash
git clone https://github.com/yourusername/banking-app.git
cd banking-app
```

2. **Install dependencies:**
```bash
pip install bcrypt mysql-connector-python python-dotenv
```

3. **Create `.env` file:**
```bash
cp .env.example .env
```

Edit `.env` with your database credentials:
```
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=srbank
```

4. **Set up database:**
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

### Menu Options

1. **Sign Up** - Create a new account
   - Enter name
   - Set password (minimum 8 characters)
   - Confirm password

2. **Login** - Login with existing account
   - Enter account ID
   - Enter password

3. **Dashboard** - After login
   - Check balance
   - Transfer money to another account
   - Logout

## Project Structure

```
banking-app/
├── app.py              # Main application entry point
├── user_mgmt.py        # Database operations
├── signup_page.py      # Signup logic
├── login_page.py       # Login logic
├── dashboard.py        # Dashboard UI and features
├── transfer_money.py   # Money transfer logic
├── .env                # Environment variables (not in git)
├── .gitignore          # Git ignore rules
└── README.md          # This file
```

## File Descriptions

- **app.py**: Main menu loop, handles signup/login/exit
- **user_mgmt.py**: Database connection and CRUD operations
- **signup_page.py**: User registration with password hashing
- **login_page.py**: Authentication with bcrypt verification
- **dashboard.py**: User dashboard with balance and transfer options
- **transfer_money.py**: Money transfer validation and execution

## Security Notes

- Never commit `.env` file to version control
- Use strong passwords (8+ characters recommended)
- For production, add rate limiting and logging
- Consider adding 2FA for production use

## Learning Outcomes

This project demonstrates:
- Secure password storage with bcrypt
- Database security with parameterized queries
- Environment variable management
- Exception handling and transaction management
- Input validation and error handling

## Future Improvements

- Add transaction history
- Implement rate limiting for login attempts
- Add logging system
- Implement 2FA
- Add unit tests
- Create API endpoints

## Author

Created as a practice project for learning database security and authentication.

## License

This project is open source and available under the MIT License.
