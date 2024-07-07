# Iris Flower Classification with Django and Scikit-learn

This project is a web application built with Django and Scikit-learn to classify Iris flowers based on sepal length, sepal width, petal length, and petal width. The application uses a machine learning model trained on the Iris dataset to predict the species of the flower.

## Features

- User input for sepal length, sepal width, petal length, and petal width
- Predicts the species of the Iris flower (setosa, versicolor, virginica)
- Easy-to-use web interface

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/YOUR_USERNAME/iris-django-model.git
    cd iris-django-model
    ```

2. **Create and activate a virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required dependencies:**
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

6. **Navigate to the application:**
    Open your browser and go to `http://127.0.0.1:8000/`.

## Usage

1. **Enter the sepal length, sepal width, petal length, and petal width** in the input form on the home page.
2. **Submit the form** to get the predicted species of the Iris flower.

## Project Structure

- `iris_django_model/`: Main Django project folder.
- `iris_model/`: Django app containing the model, views, and templates.
- `static/`: Static files for the project.
- `templates/`: HTML templates for the project.
- `manage.py`: Django's command-line utility.

## Machine Learning Model

The machine learning model is built using Scikit-learn and the Iris dataset. The model is trained to classify the species of an Iris flower based on the following features:

- Sepal Length
- Sepal Width
- Petal Length
- Petal Width

The trained model is saved using `joblib` and loaded in the Django application for making predictions.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes.

## License

This project is licensed under the MIT License.

## Acknowledgements

- [Scikit-learn](https://scikit-learn.org/)
- [Django](https://www.djangoproject.com/)
- [Iris Dataset](https://archive.ics.uci.edu/ml/datasets/iris)

