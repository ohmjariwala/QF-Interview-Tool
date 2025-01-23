# Quantitative Finance Interview Tool

A full-stack application designed to help quantitative researchers and traders prepare for technical interviews. Features dynamic problem generation in quantitative finance domains and real-time mental math exercises.

## Features

- **Problem Generator**: Dynamically generates problems in:
  - Option Pricing (Black-Scholes, Exotic Options)
  - Portfolio Optimization (Markowitz, Risk Parity)
  - Stochastic Processes (Brownian Motion, Martingales)
  - Probability & Statistics

- **Practice Mode**: Curated collection of interview problems with detailed solutions (updated with problems that I encounter over time and will eventually be scaled to web-scrape and update)

- **Mental Math Challenge**: 120-second arithmetic challenge for developing quick numerical intuition (0-100 +-*/)

## Technical Stack

### Frontend
- **Framework**: React 18 with Vite
- **State Management**: React Hooks
- **Routing**: React Router v6
- **HTTP Client**: Axios
- **Deployment**: GitHub Pages (will be translated to Vercel)

### Backend
- **Framework**: FastAPI (Python)
- **Mathematical Libraries**:
  - NumPy: Numerical computations
  - Pandas: Data manipulation
  - SciPy: Statistical functions
  - Scikit-learn: Machine learning utilities

## Architecture

The application follows a modern client-server architecture:

```
Frontend (React) <--HTTP/REST--> Backend (FastAPI)
     |                               |
     |                               |
UI Components                    Problem Generation
State Management                 Mathematical Models
API Integration                  Data Processing
```

- Frontend makes RESTful API calls to the backend
- Backend generates problems using mathematical models
- Real-time problem generation and validation
- Responsive design for all devices

## Development

1. Start the backend:
```bash
cd backend/python/src
python -m venv venv
source venv/bin/activate  # or `venv\Scripts\activate` on Windows
pip install -r requirements.txt
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

2. Start the frontend:
```bash
cd frontend
npm install
npm run dev
```

## Skills Demonstrated

- **Quantitative Finance**: Option pricing, portfolio theory, stochastic calculus
- **Mathematics**: Probability, statistics, numerical methods
- **Software Engineering**: Full-stack development, API design, state management

## Future Enhancements

- Monte Carlo simulations for option pricing
- Integration with market data APIs for live data problems
- Machine learning-based problem difficulty adjustment
- Coding IDE for programming questions (similar to projecteuler.net -> reference my Project-Euler repository for some solutions!)

## Author
Ohm Jariwala - ohmjariwala@gmail.com

## License
MIT License 
