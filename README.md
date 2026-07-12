# Installation

## 1. Clone the repository

```bash
git clone https://github.com/PurpleGraphite/python-task.git

cd python-task
```

---

## 2. Create a virtual environment

### Windows

```bash
python -m venv .venv

.venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv .venv

source .venv/bin/activate
```

---

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure environment variables

Create a `.env` file in the project root.

Example:

```env
DB_NAME=book_sales_db
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
```

---

## 5. Create PostgreSQL database

Create an empty PostgreSQL database matching the values provided in the `.env` file.

Example:

```
book_sales_db
```

---

## 6. Apply migrations

```bash
python manage.py migrate
```

---

## 7. Load sample data (Optional)

```bash
python manage.py loaddata book.json

python manage.py loaddata book_sale.json
```

---

## 8. Run the development server

```bash
python manage.py runserver
```

Visit

```
http://127.0.0.1:8000/
```
