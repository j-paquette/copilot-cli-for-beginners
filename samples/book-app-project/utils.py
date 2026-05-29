from datetime import date

from books import Book


def _safe_input(prompt: str) -> str:
    try:
        return input(prompt).strip()
    except (EOFError, KeyboardInterrupt):
        print("\nInput cancelled. Exiting.")
        raise SystemExit(1)


def _get_non_empty_input(prompt: str, field_name: str) -> str:
    while True:
        value = _safe_input(prompt)
        if value:
            return value
        print(f"{field_name} cannot be empty. Please try again.")


def _get_valid_year() -> int:
    current_year = date.today().year

    while True:
        year_input = _safe_input("Enter publication year: ")

        if not year_input:
            print("Year cannot be empty. Please enter a valid year.")
            continue

        try:
            year = int(year_input)
        except ValueError:
            print("Year must be a whole number. Please try again.")
            continue

        if year < 1 or year > current_year:
            print(f"Year must be between 1 and {current_year}.")
            continue

        return year


def print_menu() -> None:
    print("\n📚 Book Collection App")
    print("1. Add a book")
    print("2. List books")
    print("3. Mark book as read")
    print("4. Remove a book")
    print("5. Exit")


def get_user_choice() -> str:
    while True:
        choice = _safe_input("Choose an option (1-5): ")

        if not choice:
            print("Choice cannot be empty. Please enter a number between 1 and 5.")
            continue

        if not choice.isdigit():
            print("Choice must be a number between 1 and 5.")
            continue

        if choice not in {"1", "2", "3", "4", "5"}:
            print("Invalid option. Please choose a number between 1 and 5.")
            continue

        return choice


def get_book_details() -> tuple[str, str, int]:
    """
    Prompt the user to enter details for a new book and validate the input.

    Prompts the user for the book's title, author, and publication year. Ensures that the title and author are non-empty strings
    (with additional whitespace checks), and that the year is a valid integer between 1 and the current year.

    Returns:
        tuple[str, str, int]:
            - title (str): The non-empty title of the book.
            - author (str): The non-empty author of the book.
            - year (int): The publication year of the book (1 <= year <= current year).
    """
    title = _get_non_empty_input("Enter book title: ", "Title")
    while not title.strip():
        print("Title cannot be empty. Please try again.")
        title = _get_non_empty_input("Enter book title: ", "Title")

    author = _get_non_empty_input("Enter author: ", "Author")
    while not author.strip():
        print("Author cannot be empty. Please try again.")
        author = _get_non_empty_input("Enter author: ", "Author")

    year = _get_valid_year()

    return title, author, year


def print_books(books: list[Book]) -> None:
    if not books:
        print("No books in your collection.")
        return

    print("\nYour Books:")
    for index, book in enumerate(books, start=1):
        status = "✅ Read" if book.read else "📖 Unread"
        print(f"{index}. {book.title} by {book.author} ({book.year}) - {status}")
