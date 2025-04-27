# CuraSense - Disease Prediction Backend API
## Overview

**CuraSense** is a powerful backend application designed to provide medical disease prediction based on user-provided symptoms. This API leverages machine learnings models (coming soon) to predcit possible diseases and assit in medical decision-making.

---

## Features

- **Root Endpoint (`GET /`)**: A simple welcome message.
- **Disease Prediction Endpoint (`POST /predict_disease`)**: Accepts user symptoms and returns a disease prediction (currently a placeholder response).

---

## Technologies Used
- **FastAPI**: A modern, fast (high-performance) web framework for building APIs
- **Uvicorn**: ASGI server for FastAPI.
- **Pydantic**: Data validation and settings management.
- **Dotenv**: Load environment variables from `.env` files.
- **Python**: The backend logic is powered by Python.

---