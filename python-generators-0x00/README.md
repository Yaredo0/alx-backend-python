# 📦 Python Generators: Streaming SQL Rows

This project demonstrates how to use Python generators to stream rows from a PostgreSQL database one by one. It includes full setup for database creation, table definition, CSV import, and efficient row-by-row iteration.

---

## 🧠 Objectives

- Set up a PostgreSQL database named `alx_prodev`
- Create a table `user_data` with the following fields:
  - `user_id` (UUID, Primary Key, Indexed)
  - `name` (VARCHAR, NOT NULL)
  - `email` (VARCHAR, NOT NULL)
  - `age` (DECIMAL, NOT NULL)
- Import sample data from `user_data.csv`
- Stream rows using a Python generator

---

## 🗂️ Project Structure

