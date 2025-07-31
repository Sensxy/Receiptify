# Receiptify

AI-powered expense tracking application that automatically processes receipt photos, extracts data via OCR, and categorizes expenses with intelligent analytics.

## Features

- **Smart OCR Processing**: Upload receipt photos and extract merchant, amount, and date automatically
- **Intelligent Categorization**: Rule-based expense categorization with user feedback collection
- **Real-time Processing**: Async background processing with status updates
- **Analytics Dashboard**: Interactive spending visualizations and reports
- **Future-Ready**: Built with ML integration capabilities for improved categorization

## Tech Stack

**Backend:**
- **FastAPI** - Modern Python web framework with auto-documentation
- **SQLAlchemy** - Database ORM with SQLite for development
- **Celery** - Background task processing
- **OpenAI Vision API** - OCR text extraction from receipts
- **Redis** - Task queue and caching 

**Frontend:**
- **React** with TypeScript - Modern UI framework
- **Tailwind CSS** - Utility-first styling
- **Chart.js/Recharts** - Data visualization

**Infrastructure:**
- **Docker** - Containerization for easy deployment
- **SQLite** - Development database (PostgreSQL for production)
- **Local Storage** - Development file storage (AWS S3 for production)

## Roadmap

### Week 1: Foundation & Core Backend
- [x] FastAPI setup with auto-documentation
- [x] Database models with SQLAlchemy
- [x] SQLite database configuration
- [ ] File upload endpoints (Days 3-4)
- [ ] Authentication system (Days 5-7)

### Week 2: OCR Integration & Background Processing
- [ ] OpenAI Vision API integration
- [ ] Celery setup for async processing
- [ ] Rule-based categorization system
- [ ] User feedback collection for future ML

### Week 3: Frontend Development
- [ ] React setup with TypeScript
- [ ] File upload interface with drag-and-drop
- [ ] Receipt dashboard and analytics
- [ ] Category management interface

### Week 4: Analytics, Testing & Deployment
- [ ] Advanced data visualizations
- [ ] PDF export functionality
- [ ] Unit tests and error handling
- [ ] Production deployment setup

## Installation & Setup

### Prerequisites
- Python 3.8+
- Docker Desktop
- Node.js 16+ (for frontend in Week 3)

### Backend Setup

1. **Clone and setup project:**
   ```bash
   git clone <your-repo-url>
   cd receipt-analyzer/backend
   
   # Create virtual environment
   python -m venv venv
   
   # Activate virtual environment
   # Windows:
   venv\Scripts\activate
   # Mac/Linux:
   source venv/bin/activate
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Create database:**
   ```bash
   python create_tables.py
   ```

4. **Run the development server:**
   ```bash
   uvicorn main:app --reload
   ```

5. **Access the application:**
   - API: http://localhost:8000
   - Documentation: http://localhost:8000/docs
   - Database: `receipts.db` file in backend folder

## API Documentation

FastAPI automatically generates interactive API documentation:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

### Current Endpoints

- `GET /` - Health check
- `GET /receipts` - List all receipts
- `POST /receipts/test` - Create test receipt

## Database Schema

### Receipts Table
```sql
CREATE TABLE receipts (
    id INTEGER PRIMARY KEY,
    merchant_name VARCHAR,
    amount DECIMAL(10,2),
    date DATE,
    category VARCHAR,
    image_url VARCHAR,
    raw_ocr_text TEXT,
    status VARCHAR DEFAULT 'processing',
    created_at DATETIME DEFAULT NOW()
);
```

### Users Table
```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    email VARCHAR UNIQUE,
    password_hash VARCHAR,
    created_at DATETIME DEFAULT NOW()
);
```

### Switching to Production Services:

1. **Database**: SQLite → PostgreSQL
   ```python
   DATABASE_URL = "postgresql://user:pass@host:5432/db"
   ```

2. **File Storage**: Local → AWS S3
   ```python
   # Will use boto3 for S3 integration
   ```

3. **Background Tasks**: Local → Redis + Celery Workers
4. **Deployment**: Docker containers on AWS/DigitalOcean

This is a learning project built to demonstrate modern Python web development practices. Key learning objectives:

- **FastAPI**: Modern async Python web framework
- **Database Design**: SQLAlchemy ORM with proper relationships
- **Background Processing**: Async task handling with Celery
- **API Integration**: Working with external services (OpenAI)
- **System Architecture**: Designing for scalability and maintainability

## Notes

- **Development Focus**: Currently using SQLite and local storage for simplicity
- **Production Ready**: Architecture supports easy migration to production services
- **Learning Oriented**: Code includes comments and explanations for educational purposes
- **Scalable Design**: Built with future enhancements and ML integration in mind


---

**Current Status**: Week 1 (Days 1-2) Complete ✅  
**Next Steps**: File upload implementation (Days 3-4)
