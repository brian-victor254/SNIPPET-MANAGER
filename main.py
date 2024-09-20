import click
from cli.commands import (
    add_user,
    edit_user,
    delete_user,
    add_snippet,
    edit_snippet, 
    delete_snippet,
    add_category, 
    edit_category, 
    delete_category,
    add_tag,
    edit_tag, 
    delete_tag,
    list_users,
    list_snippets,
    list_tags,
    
)


def main():
    print("Welcome to Snippet Manager")
    while True:
        menu()
        choice = input("Enter a command number (or '0' to logout): ").strip()
        if choice.lower() == "0":
            click.echo("Goodbye!")
            break
        elif choice == "1":
            username = input("Enter username: ").strip()
            password = input("Enter password: ").strip()
            email = input("Enter email: ").strip()
            try:
                add_user(username, password, email)
                click.echo("Oper>>> successfully.")
            except ValueError as ve:
                click.echo(f"Error: {ve}")
            except Exception as e:
                click.echo(f"An unexpected error occurred: {e}")
        elif choice == "2":
            user_id = input("Enter user ID: ").strip()
            username = input("Enter new username (leave empty to skip): ").strip()
            password = input("Enter new password (leave empty to skip): ").strip()
            email = input("Enter new email (leave empty to skip): ").strip()
            try:
                edit_user(user_id, username, password, email)
                click.echo("User edited successfully.")
            except Exception as e:
                click.echo(f"An unexpected error occurred: {e}")
        elif choice == "3":
            user_id = input("Enter user ID: ").strip()
            try:
                delete_user(user_id)
                click.echo("User deleted successfully.")
            except Exception as e:
                click.echo(f"An unexpected error occurred: {e}")
        elif choice == "4":
            title = input("Enter snippet title: ").strip()
            content = input("Enter snippet content: ").strip()
            language = input("Enter snippet language: ").strip()
            user_id = input("Enter user ID: ").strip()
            category_id = input("Enter category ID (leave empty to skip): ").strip()
            try:
                add_snippet(title, content, language, user_id, category_id)
                click.echo("Snippet added successfully.")
            except Exception as e:
                click.echo(f"An unexpected error occurred: {e}")
        elif choice == "5":
            snippet_id = input("Enter snippet ID: ").strip()
            title = input("Enter new title (leave empty to skip): ").strip()
            content = input("Enter new content (leave empty to skip): ").strip()
            language = input("Enter new language (leave empty to skip): ").strip()
            try:
                edit_snippet(snippet_id, title, content, language)
                click.echo("Snippet edited successfully.")
            except Exception as e:
                click.echo(f"An unexpected error occurred: {e}")
        elif choice == "6":
            snippet_id = input("Enter snippet ID: ").strip()
            try:
                delete_snippet(snippet_id)
                click.echo("Snippet deleted successfully.")
            except Exception as e:
                click.echo(f"An unexpected error occurred: {e}")
        elif choice == "7":
            name = input("Enter category name: ").strip()
            description = input("Enter category description (leave empty to skip): ").strip()
            try:
                add_category(name, description)
                click.echo("Category added successfully.")
            except Exception as e:
                click.echo(f"An unexpected error occurred: {e}")
        elif choice == "8":
            category_id = input("Enter category ID: ").strip()
            name = input("Enter new name (leave empty to skip): ").strip()
            description = input("Enter new description (leave empty to skip): ").strip()
            try:
                edit_category(category_id, name, description)
                click.echo("Category edited successfully.")
            except Exception as e:
                click.echo(f"An unexpected error occurred: {e}")
        elif choice == "9":
            category_id = input("Enter category ID: ").strip()
            try:
                delete_category(category_id)
                click.echo("Category deleted successfully.")
            except Exception as e:
                click.echo(f"An unexpected error occurred: {e}")
        elif choice == "10":
            name = input("Enter tag name: ").strip()
            try:
                add_tag(name)
                click.echo("Tag added successfully.")
            except Exception as e:
                click.echo(f"An unexpected error occurred: {e}")
        elif choice == "11":
            tag_id = input("Enter tag ID: ").strip()
            name = input("Enter new name (leave empty to skip): ").strip()
            try:
                edit_tag(tag_id, name)
                click.echo("Tag edited successfully.")
            except Exception as e:
                click.echo(f"An unexpected error occurred: {e}")
        elif choice == "12":
            tag_id = input("Enter tag ID: ").strip()
            try:
                delete_tag(tag_id)
                click.echo("Tag deleted successfully.")
            except Exception as e:
                click.echo(f"An unexpected error occurred: {e}")
        elif choice == "13":  # New option to list users
            try:
                list_users()
            except Exception as e:
                click.echo(f"An unexpected error occurred: {e}")
        elif choice == "14":
            try:
                list_snippets()  # Calling the list_snippets function
            except Exception as e:
                click.echo(f"An unexpected error occurred: {e}")
        elif choice == "15":
            list_tags()  
        else:
            click.echo("Invalid command. Please try again.")


        
        


def menu():
    click.echo("""
    Hello! Welcome to the Snippet Management Program.
    ================================================

    Please choose from the following options:

    1. Add a user
    2. Edit a user
    3. Delete a user
    4. Add a snippet
    5. Edit a snippet
    6. Delete a snippet
    7. Add a category
    8. Edit a category
    9. Delete a category
    10. Add a tag
    11. Edit a tag
    12. Delete a tag
    13. list_users
    14. list_snippets 
    15. list_tags                       
    0. Logout
    --------------------------------                                       
    | By Brian |
    --------------------------------          
    """)


if __name__ == '__main__':
    main()
