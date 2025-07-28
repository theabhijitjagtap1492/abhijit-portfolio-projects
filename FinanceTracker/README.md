# Financial Tracker

A Flask-based web application for tracking personal income and expenses, visualizing financial data, and exporting transaction records. This app is designed for individuals who want a simple, no-authentication-required way to manage their finances.

## Features

- **Add, edit, and delete transactions** (income and expenses)
- **Category management** for both income and expenses
- **Dashboard** with interactive charts (income vs. expenses, expenses by category)
- **Data export** to PDF
- **Responsive UI** using Bootstrap 5
- **No authentication required**
- **Smart validation**: Users must add income before expenses

## Technology Stack

- **Backend:** Flask, Flask-SQLAlchemy
- **Database:** MySQL (via SQLAlchemy ORM)
- **Forms:** Flask-WTF, WTForms
- **Frontend:** Bootstrap 5, Chart.js
- **Data Processing:** pandas
- **PDF Export:** reportlab

## Project Structure

```
Expemses/
├── app/
│   ├── __init__.py         # Flask app factory and initialization
│   ├── models.py           # SQLAlchemy models (Transaction)
│   ├── forms.py            # WTForms definitions (TransactionForm)
│   └── routes.py           # Application routes and logic
├── templates/
│   ├── base.html           # Base template
│   ├── index.html          # Home page (transaction list)
│   ├── add_transaction.html# Add transaction form
│   ├── edit_transaction.html# Edit transaction form
│   └── dashboard.html      # Dashboard with charts
├── static/
│   └── css/
│       └── style.css       # Custom styles
├── config.py               # App configuration (dev/prod)
├── requirements.txt        # Python dependencies
├── run.py                  # Application entry point
├── view_data.py            # CLI script to view database data
└── instance/               # (Empty, for Flask instance configs)
```

## Installation & Setup

### 1. Clone the repository
```bash
git clone <your-repo-url>
cd Expemses
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Set up MySQL database
- Create a MySQL database and user:
```sql
CREATE DATABASE finance_tracker CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER 'finance_user'@'%' IDENTIFIED BY 'your_password';
GRANT ALL PRIVILEGES ON finance_tracker.* TO 'finance_user'@'%';
FLUSH PRIVILEGES;
```

### 4. Configure environment variables
Set the following environment variables for your environment:

**Linux/Mac:**
```bash
export MYSQL_HOST=localhost
export MYSQL_PORT=3306
export MYSQL_USER=finance_user
export MYSQL_PASSWORD=your_password
export MYSQL_DATABASE=finance_tracker
```

**Windows (PowerShell):**
```powershell
$env:MYSQL_HOST='localhost'
$env:MYSQL_PORT='3306'
$env:MYSQL_USER='finance_user'
$env:MYSQL_PASSWORD='your_password'
$env:MYSQL_DATABASE='finance_tracker'
```

### 5. Run the application
```bash
python run.py
```
Visit [http://localhost:5000](http://localhost:5000) in your browser.

## Usage
- **Add transactions**: Click "Add Transaction" to record income or expenses.
- **Dashboard**: View charts and summaries on the dashboard page.
- **Export**: Download all transactions as a PDF from the dashboard.
- **Edit/Delete**: Use the edit and delete buttons on the transaction list.

## Main Modules
- `app/models.py`: Defines the `Transaction` model (id, amount, category, type, description, date)
- `app/forms.py`: Defines the `TransactionForm` for adding/editing transactions
- `app/routes.py`: All web routes (add, edit, delete, dashboard, export, reset)
- `view_data.py`: CLI script to print all transactions and summaries to the console
- `config.py`: Development and production configuration classes

## Database Schema

The application uses a single `Transaction` table. Here is the SQL schema:

```sql
CREATE TABLE Transaction (
    id INT AUTO_INCREMENT PRIMARY KEY,
    amount FLOAT NOT NULL,
    category VARCHAR(50) NOT NULL,
    type VARCHAR(10) NOT NULL, -- 'income' or 'expense'
    description VARCHAR(200),
    date DATE NOT NULL
);
```

- **Transaction**
  - `id`: Integer, primary key
  - `amount`: Float, required
  - `category`: String, required
  - `type`: String ('income' or 'expense'), required
  - `description`: String, optional
  - `date`: Date, required

## Troubleshooting
- **MySQL connection errors**: Ensure MySQL is running and credentials are correct
- **No transactions showing**: Add income first (required by app logic)
- **PDF export issues**: Ensure `reportlab` is installed

## License
MIT License (add your own license if needed)

---

*This project is a simple, no-auth, personal financial tracker built with Flask. Contributions and suggestions are welcome!* 