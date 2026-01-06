# Marketplace App

A modern, feature-rich marketplace application built with scalability and user experience in mind. This platform enables seamless buying and selling of products with a robust backend and intuitive frontend.

## Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation Instructions](#installation-instructions)
- [Usage Guide](#usage-guide)
- [Project Structure](#project-structure)
- [Configuration](#configuration)
- [API Endpoints](#api-endpoints)
- [Troubleshooting](#troubleshooting)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)

## Features

### Core Functionality

- **User Authentication & Authorization**
  - Secure user registration and login system
  - Role-based access control (Buyer, Seller, Admin)
  - JWT token-based authentication
  - Password encryption and reset functionality

- **Product Management**
  - Browse and search products across multiple categories
  - Advanced filtering and sorting options
  - Detailed product information with images and reviews
  - Inventory management for sellers
  - Product ratings and customer reviews

- **Shopping Experience**
  - Shopping cart functionality with persistent storage
  - Wishlist feature for saving favorite items
  - Multiple payment gateway integration
  - Order tracking and history
  - Invoice generation

- **Seller Features**
  - Seller dashboard with analytics and insights
  - Inventory management tools
  - Order fulfillment workflow
  - Sales reports and performance metrics
  - Customer communication system

- **Admin Features**
  - User management and moderation
  - Product approval workflow
  - Analytics and reporting dashboard
  - Payment reconciliation
  - System monitoring and logging

- **Additional Features**
  - Real-time notifications
  - Email and SMS notifications
  - User reviews and ratings system
  - Product recommendations engine
  - Customer support chat integration

## Tech Stack

### Frontend

- **Framework**: React.js
- **State Management**: Redux/Context API
- **UI Components**: Material-UI / Tailwind CSS
- **Build Tool**: Webpack / Vite
- **Testing**: Jest, React Testing Library

### Backend

- **Runtime**: Node.js
- **Framework**: Express.js
- **Database**: MongoDB / PostgreSQL
- **Authentication**: JWT (JSON Web Tokens)
- **API Documentation**: Swagger/OpenAPI
- **Testing**: Mocha, Chai, Jest

### DevOps & Infrastructure

- **Containerization**: Docker
- **Container Orchestration**: Kubernetes (optional)
- **CI/CD**: GitHub Actions / Jenkins
- **Cloud Hosting**: AWS / Azure / GCP
- **Database**: MongoDB Atlas / AWS RDS
- **Caching**: Redis

## Installation Instructions

### Prerequisites

- Node.js (v16.0.0 or higher)
- npm (v7.0.0 or higher) or yarn
- Git
- MongoDB (v4.4 or higher) or PostgreSQL (v12+)
- Docker (optional, for containerized setup)

### Setup Steps

#### 1. Clone the Repository

```bash
git clone https://github.com/warischoudhary1786/marketplace-app.git
cd marketplace-app
```

#### 2. Environment Configuration

Create a `.env` file in the root directory:

```env
# Server Configuration
NODE_ENV=development
PORT=5000
HOST=localhost

# Database Configuration
DB_HOST=localhost
DB_PORT=27017
DB_NAME=marketplace_db
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DATABASE_URL=mongodb://localhost:27017/marketplace_db

# Authentication
JWT_SECRET=your_jwt_secret_key
JWT_EXPIRE=7d
REFRESH_TOKEN_SECRET=your_refresh_token_secret

# Email Configuration
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=your_email@gmail.com
SMTP_PASSWORD=your_email_password
MAIL_FROM=noreply@marketplace.com

# Payment Gateway
STRIPE_PUBLIC_KEY=your_stripe_public_key
STRIPE_SECRET_KEY=your_stripe_secret_key
PAYPAL_CLIENT_ID=your_paypal_client_id
PAYPAL_SECRET=your_paypal_secret

# AWS S3 (for file uploads)
AWS_ACCESS_KEY_ID=your_aws_access_key
AWS_SECRET_ACCESS_KEY=your_aws_secret_key
AWS_REGION=us-east-1
AWS_S3_BUCKET=marketplace-uploads

# Redis Configuration
REDIS_HOST=localhost
REDIS_PORT=6379
REDIS_PASSWORD=optional_redis_password

# Logging
LOG_LEVEL=debug
```

#### 3. Backend Setup

```bash
cd backend
npm install

# Run database migrations (if applicable)
npm run migrate

# Seed initial data (optional)
npm run seed

# Start the development server
npm run dev

# For production
npm run build
npm start
```

#### 4. Frontend Setup

```bash
cd frontend
npm install

# Start development server
npm run dev

# For production build
npm run build
npm run preview
```

#### 5. Using Docker (Alternative)

```bash
# Build and run with Docker Compose
docker-compose up -d

# View logs
docker-compose logs -f

# Stop services
docker-compose down
```

### Verification

After installation, verify that:

- Backend server is running on `http://localhost:5000`
- Frontend is running on `http://localhost:3000` or `http://localhost:5173`
- Database connection is successful
- All environment variables are properly set

## Usage Guide

### For Users

#### 1. Registration & Login

```bash
# Visit the application
http://localhost:3000

# Sign up with email
- Navigate to Register page
- Fill in required details (name, email, password)
- Verify email via confirmation link
- Login with credentials
```

#### 2. Browsing Products

```
- Home page displays featured products
- Use search bar for specific products
- Apply filters: Category, Price Range, Rating
- Sort by: Newest, Price, Rating, Popularity
- View detailed product information
```

#### 3. Making a Purchase

```
- Add products to cart
- Review cart items
- Proceed to checkout
- Enter shipping address
- Select payment method
- Confirm order
- Receive order confirmation email
```

#### 4. Managing Account

```
- View and edit profile information
- Change password securely
- View order history
- Track active orders
- Manage address book
- Review saved wishlists
```

### For Sellers

#### 1. Seller Registration

```
- Complete seller onboarding process
- Provide business information
- Set up payment account
- Configure store settings
```

#### 2. Adding Products

```
API Endpoint: POST /api/v1/products
Content-Type: application/json

{
  "name": "Product Name",
  "description": "Detailed description",
  "price": 99.99,
  "category": "Electronics",
  "stock": 100,
  "images": ["url1", "url2"],
  "attributes": {
    "color": "Black",
    "size": "M"
  }
}
```

#### 3. Managing Orders

```
- View pending orders in dashboard
- Update order status (Processing, Shipped, Delivered)
- Generate shipping labels
- Communicate with customers
- Handle returns and refunds
```

### For Administrators

#### 1. Admin Dashboard

```
http://localhost:3000/admin
- Login with admin credentials
- Access dashboard for system overview
- View analytics and metrics
```

#### 2. User Management

```
- View all registered users
- Manage user roles and permissions
- Suspend/activate accounts
- View user activity logs
```

#### 3. Content Moderation

```
- Review and approve seller products
- Monitor user reviews and ratings
- Handle reported content
- Manage category taxonomy
```

## Project Structure

```
marketplace-app/
├── backend/
│   ├── src/
│   │   ├── config/              # Configuration files
│   │   ├── controllers/         # Request handlers
│   │   ├── models/              # Database schemas
│   │   ├── routes/              # API routes
│   │   ├── middleware/          # Custom middleware
│   │   ├── services/            # Business logic
│   │   ├── utils/               # Utility functions
│   │   ├── validators/          # Input validation
│   │   └── app.js               # Express app setup
│   ├── tests/                   # Test files
│   ├── .env.example             # Environment template
│   ├── package.json
│   └── server.js                # Entry point
│
├── frontend/
│   ├── src/
│   │   ├── components/          # Reusable React components
│   │   ├── pages/               # Page components
│   │   ├── hooks/               # Custom React hooks
│   │   ├── services/            # API service calls
│   │   ├── redux/               # State management
│   │   ├── styles/              # CSS/SCSS files
│   │   ├── utils/               # Utility functions
│   │   ├── App.jsx              # Main app component
│   │   └── main.jsx             # Entry point
│   ├── tests/                   # Test files
│   ├── public/                  # Static assets
│   ├── .env.example
│   └── package.json
│
├── docker-compose.yml           # Docker Compose configuration
├── README.md                    # This file
├── CONTRIBUTING.md              # Contributing guidelines
└── LICENSE                      # License file
```

## Configuration

### Database Configuration

#### MongoDB

```javascript
// config/database.js
const mongoose = require('mongoose');

const connectDB = async () => {
  try {
    await mongoose.connect(process.env.DATABASE_URL, {
      useNewUrlParser: true,
      useUnifiedTopology: true,
    });
    console.log('MongoDB connected');
  } catch (error) {
    console.error('MongoDB connection failed:', error);
    process.exit(1);
  }
};
```

#### PostgreSQL

```javascript
// config/database.js
const { Pool } = require('pg');

const pool = new Pool({
  connectionString: process.env.DATABASE_URL,
});

pool.on('error', (err) => console.error('Unexpected error', err));
```

### Redis Configuration

```javascript
// config/redis.js
const redis = require('redis');

const client = redis.createClient({
  host: process.env.REDIS_HOST,
  port: process.env.REDIS_PORT,
});

client.on('error', (err) => console.log('Redis Client Error', err));
```

## API Endpoints

### Authentication Endpoints

```
POST   /api/v1/auth/register         - User registration
POST   /api/v1/auth/login            - User login
POST   /api/v1/auth/refresh-token    - Refresh JWT token
POST   /api/v1/auth/logout           - User logout
POST   /api/v1/auth/forgot-password  - Request password reset
POST   /api/v1/auth/reset-password   - Reset password with token
```

### Products Endpoints

```
GET    /api/v1/products              - Get all products (with pagination/filtering)
GET    /api/v1/products/:id          - Get product details
POST   /api/v1/products              - Create new product (Seller)
PUT    /api/v1/products/:id          - Update product (Seller)
DELETE /api/v1/products/:id          - Delete product (Seller)
GET    /api/v1/products/search       - Search products
```

### Orders Endpoints

```
GET    /api/v1/orders                - Get user orders
GET    /api/v1/orders/:id            - Get order details
POST   /api/v1/orders                - Create new order
PUT    /api/v1/orders/:id            - Update order status
DELETE /api/v1/orders/:id            - Cancel order
```

### Cart Endpoints

```
GET    /api/v1/cart                  - Get user cart
POST   /api/v1/cart/add              - Add item to cart
PUT    /api/v1/cart/update           - Update cart item
DELETE /api/v1/cart/remove           - Remove item from cart
POST   /api/v1/cart/clear            - Clear entire cart
```

### User Endpoints

```
GET    /api/v1/users/profile         - Get user profile
PUT    /api/v1/users/profile         - Update user profile
GET    /api/v1/users/addresses       - Get user addresses
POST   /api/v1/users/addresses       - Add new address
DELETE /api/v1/users/addresses/:id   - Delete address
```

For complete API documentation, visit `/api-docs` after starting the server.

## Troubleshooting

### Common Issues and Solutions

#### Database Connection Failed

```bash
# Check MongoDB/PostgreSQL is running
# For MongoDB:
mongod

# For PostgreSQL:
psql -U your_user -d your_database

# Verify DATABASE_URL in .env file
```

#### Port Already in Use

```bash
# Kill process on port 5000
# Linux/Mac:
lsof -ti:5000 | xargs kill -9

# Windows:
netstat -ano | findstr :5000
taskkill /PID <PID> /F
```

#### CORS Errors

```javascript
// Ensure CORS is properly configured in backend
const cors = require('cors');
app.use(cors({
  origin: process.env.FRONTEND_URL,
  credentials: true,
}));
```

#### Authentication Token Expired

```bash
# Clear browser localStorage and cookies
# Re-login to obtain new tokens
```

#### File Upload Issues

```bash
# Verify AWS S3 credentials
# Check bucket permissions
# Ensure file size is within limits (max 10MB default)
```

### Debugging

```bash
# Enable debug logging
DEBUG=marketplace-app:* npm run dev

# Check server logs
tail -f logs/error.log

# MongoDB query logging
db.setProfilingLevel(1)
```

## Future Enhancements

### Phase 1 (Q2 2026)

- [ ] **Mobile Application**
  - Native iOS and Android apps
  - Offline mode for browsing
  - Push notifications integration

- [ ] **Advanced Search & Recommendations**
  - AI-powered product recommendations
  - Personalized search results
  - Machine learning-based demand prediction

- [ ] **Marketplace Analytics**
  - Comprehensive seller analytics dashboard
  - Buyer behavior insights
  - Revenue forecasting tools

### Phase 2 (Q3-Q4 2026)

- [ ] **Multi-Vendor Support**
  - Improved multi-vendor commission structure
  - Vendor collaboration features
  - Bulk vendor onboarding

- [ ] **Social Commerce**
  - Social sharing and referral system
  - Live shopping events
  - User-generated content integration
  - Influencer marketplace

- [ ] **International Expansion**
  - Multi-currency support
  - Multi-language interface
  - International payment gateways
  - Regional compliance handling

### Phase 3 (2027 onwards)

- [ ] **Advanced Features**
  - AR product preview
  - Voice search capability
  - Blockchain-based product authenticity
  - Cryptocurrency payment options
  - AI chatbot for customer service

- [ ] **Logistics Integration**
  - Real-time shipment tracking
  - Multiple carrier integration
  - Automated logistics optimization
  - Return management system

- [ ] **Marketplace Expansion**
  - Services marketplace integration
  - Subscription-based product support
  - B2B marketplace features
  - Wholesale trading platform

## Contributing

We welcome contributions from the community! Please follow these guidelines:

1. **Fork the repository**
2. **Create a feature branch** (`git checkout -b feature/AmazingFeature`)
3. **Commit changes** (`git commit -m 'Add AmazingFeature'`)
4. **Push to branch** (`git push origin feature/AmazingFeature`)
5. **Open a Pull Request**

For detailed contribution guidelines, see [CONTRIBUTING.md](CONTRIBUTING.md)

### Development Standards

- Follow ESLint and Prettier configurations
- Write unit tests for all new features
- Maintain >80% code coverage
- Update documentation for API changes
- Follow semantic versioning for releases

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

For support, please:

- Check the [Issues](https://github.com/warischoudhary1786/marketplace-app/issues) section
- Create a new issue with detailed information
- Contact: support@marketplace-app.com
- Documentation: [Wiki](https://github.com/warischoudhary1786/marketplace-app/wiki)

## Changelog

### Version 1.0.0 (2026-01-06)

- Initial release
- Core marketplace functionality
- User authentication system
- Product catalog and search
- Shopping cart and checkout
- Order management
- Admin dashboard
- Seller dashboard

---

**Last Updated**: 2026-01-06

**Maintainer**: [warischoudhary1786](https://github.com/warischoudhary1786)
