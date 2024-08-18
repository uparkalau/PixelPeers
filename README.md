# PixelPeers

PixelPeers is a social network application for photographers, allowing them to create personalized galleries, connect with other photographers, and showcase their work through custom subdomains.

## Features

- User authentication and profile management
- Photo upload and gallery creation
- Custom template editor for personalized galleries
- Subdomain management for public-facing portfolios
- Social features (follow, like, comment)
- Admin panel for site management

## Tech Stack

- Frontend: Vue.js
- Backend: Python (Flask) microservices
- Database: PostgreSQL
- Caching: Redis
- Message Broker: RabbitMQ
- Containerization: Docker
- CI/CD: GitHub Actions

## Project Structure

The project follows a monorepo structure with the following main directories:

- `services/`: Contains all backend microservices
- `frontend/`: Vue.js frontend application
- `.github/workflows/`: CI/CD pipeline configurations
- `scripts/`: Utility scripts for development and deployment

## Setup Instructions

### Prerequisites

- Docker and Docker Compose
- Node.js and npm
- Python 3.8+

### Local Development

1. Clone the repository: git clone https://github.com/uparkalau/pixelpeers.git
 ```cd pixelpeers```
2. Create a `.env` file in the root directory with necessary environment variables (see `.env.example` for required variables).

3. Build and start the services: docker-compose up --build

4. The application should now be running:
- Frontend: http://localhost:8080
- API Gateway: http://localhost:5000

### Running Tests

To run tests for all services: 
```./scripts/run-tests.sh```

To run tests for a specific service:
```./scripts/run-tests.sh <service-name>```

### Deployment

The project uses GitHub Actions for CI/CD. Pushing to the `develop` branch will trigger a deployment to the staging environment, while pushing to `master` will deploy to production.

For manual deployment to staging:
```./scripts/deploy-staging.sh```

For manual deployment to production:
```./scripts/deploy-production.sh```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

uladzimir.parkalau@gmail.com

Project Link: [https://github.com/upakalau/pixelpeers](https://github.com/uparkalau/pixelpeers)