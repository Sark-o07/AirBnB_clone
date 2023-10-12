```markdown
# Custom CLI for AirBnB Clone

## Description

This project is a fundamental component of the ALX School Full-Stack Software Engineer program, designed as the first phase in developing a comprehensive web application - an AirBnB clone. The main objective of this project is to construct a customized command-line interface (CLI) for efficient data management, alongside establishing the foundational classes for data storage. The system ensures data persistence through JSON serialization/deserialization.

## Usage

The console provides an interactive environment, akin to a Unix shell, and awaits user input at the prompt (hbnb). It offers support for a range of commands, including:

- `quit`: Terminate the console.
- `help <command>`: Retrieve detailed guidance on a specific command.
- `create <class>`: Generate an object and display its unique ID.
- `show <class> <id>` or `<class>.show(<id>)`: Display the attributes of an object.
- `destroy <class> <id>` or `<class>.destroy(<id>)`: Remove an object from the system.
- `all` or `all <class>`: List all objects or instances belonging to a specific class.
- `update <class> <id> <attribute name> "<attribute value>"` or `<class>.update(<id>, <attribute name>, "<attribute value>")`: Modify an attribute of an object.

### Non-interactive Mode Example

Non-interactive mode enables you to pipe commands to the console, allowing for automation:

```sh
$ echo "help" | ./console.py
(hbnb)
```

## Models

Inside the `models` directory, you'll find a collection of classes relevant to the project, each equipped with specific attributes:

- `base_model.py`: The BaseModel class, which serves as the foundation for other classes and encompasses attributes such as `id`, `created_at`, and `updated_at`.
- `user.py`: The User class, designed for handling future user information, featuring attributes like `email`, `password`, `first_name`, and `last_name`.
- `amenity.py`: The Amenity class, dedicated to future amenity information, with the `name` attribute.
- `city.py`: The City class, for future location information, equipped with attributes `state_id` and `name`.
- `state.py`: The State class, specializing in future location data, with the `name` attribute.
- `place.py`: The Place class, tailored for future accommodation data, housing attributes like `city_id`, `user_id`, `name`, `description`, `number_rooms`, `number_bathrooms`, `max_guest`, `price_by_night`, `latitude`, `longitude`, and `amenity_ids`.
- `review.py`: The Review class, targeted at future user/host review data, consisting of attributes like `place_id`, `user_id`, and `text`.

## File Storage

Data serialization and deserialization in JSON format is managed within the `engine` folder. It introduces the `FileStorage` class, which is equipped with methods for transforming objects to JSON and back. The `__init__.py` file initializes the `FileStorage` class as `storage` and invokes the `reload()` method, which facilitates the automatic reloading of serialized data.

## Tests

To ensure the reliability and accuracy of the code, comprehensive testing has been implemented using the `unittest` module. The test cases for the classes can be located within the `test_models` directory.

## Author

- Ugbala Kosisochukwu Nicholas
- Email: kosinick01@gmail.com

---

This project represents a solid starting point for building an AirBnB clone. It offers a versatile command-line interface for efficient data management and a robust data storage system using JSON. The comprehensive unit testing ensures its reliability and stability.
```
