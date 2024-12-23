# Airline-booking-system---ADM-161416-

## Setup Instructions

1. **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd Airline-booking-system---ADM-161416-
    ```

2. **Create a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Apply migrations:**
    ```bash
    python manage.py migrate
    ```

5. **Run the development server:**
    ```bash
    python manage.py runserver
    ```

6. **Access the application:**
    Open your web browser and go to `http://127.0.0.1:8000/`

## Models

### Flight
Represents a flight with the following attributes:
- `flight_number`: Unique identifier for the flight.
- `departure`: Departure date and time.
- `arrival`: Arrival date and time.
- `origin`: Origin of the flight.
- `destination`: Destination of the flight.
- `capacity`: Capacity of the flight.

### Passenger
Represents a passenger with the following attributes:
- `first_name`: First name of the passenger.
- `last_name`: Last name of the passenger.
- `email`: Unique email of the passenger.
- `phone_number`: Phone number of the passenger.
- `flight`: Foreign key linking to the `Flight` model.

## Serializers

### FlightSerializer
Serializes the `Flight` model, including all fields.

### PassengerSerializer
Serializes the `Passenger` model, including all fields. It also includes nested serialization for the `Flight` model and custom validation to ensure a valid flight ID is provided.

## Views/ViewSets

### FlightViewSet
Provides CRUD operations for the `Flight` model using Django REST Framework's `ModelViewSet`.

### PassengerViewSet
Provides CRUD operations for the `Passenger` model using Django REST Framework's `ModelViewSet`.

## Notable Design Decisions

- **Nested Serialization:** The `PassengerSerializer` includes a nested `FlightSerializer` to provide detailed flight information within passenger data.
- **Custom Validation:** The `PassengerSerializer` includes custom validation to ensure that a valid flight ID is provided when creating a passenger.
- **ViewSets and Routers:** The use of `ModelViewSet` and `DefaultRouter` simplifies the creation of RESTful APIs by automatically providing standard actions (list, create, retrieve, update, destroy) for the models.
