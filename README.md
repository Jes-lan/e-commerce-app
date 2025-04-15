# e-commerce-app

## Overview

The `e-commerce-app` is a modern web application designed to provide a seamless online shopping experience. It includes features such as product browsing, user authentication, shopping cart management, and order processing.

## Features

- **User Authentication**: Secure login and registration system.
- **Product Management**: Browse, search, and filter products.
- **Shopping Cart**: Add, update, and remove items from the cart.
- **Order Processing**: Place orders and view order history.
- **Responsive Design**: Optimized for both desktop and mobile devices.

## Technologies Used

- **Frontend**: React, Redux, Tailwind CSS
- **Backend**: Node.js, Express.js
- **Database**: MongoDB
- **Authentication**: JSON Web Tokens (JWT)
- **Payment Integration**: Stripe API

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Jes-lan/e-commerce-app.git
   ```
2. Navigate to the project directory:
   ```bash
   cd e-commerce-app
   ```
3. Install dependencies for both frontend and backend:
   ```bash
   npm install
   cd client && npm install
   ```
4. Set up environment variables:

   - Create a `.env` file in the root directory.
   - Add the required variables (e.g., database URI, JWT secret, Stripe keys).

5. Start the development server:
   ```bash
   npm run dev
   ```

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
