import click
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager
from db.models import engine, User, Snippet, Category, Tag

# Create a new session
Session = sessionmaker(bind=engine)
session = Session()

@contextmanager
def session_scope():
    session = Session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()


def add_user(username, password, email):
    """Add a new user."""
    existing_user = session.query(User).filter(User.username == username).first()
    if existing_user:
        print()
        click.echo(f"User with username '{username}' already exists.")
        return
    
    new_user = User(username=username, password=password, email=email)
    session.add(new_user)
    session.commit()
    print()
    click.echo(f'User {username} added successfully.')


def edit_user(user_id, username=None, password=None, email=None):
    """Edit an existing user."""
    with session_scope() as session:
        user = session.query(User).get(user_id)
        if not user:
            click.echo("User not found.")
            return

        if username:
            user.username = username
        if password:
            user.password = password
        if email:
            user.email = email
        print()
        click.echo(f'User {user.username} updated successfully.')


@click.argument('user_id')
def delete_user(user_id):
    """Delete an existing user."""
    session = Session()
    user = session.query(User).get(user_id)
    if not user:
        click.echo("User not found.")
        return

    session.delete(user)
    session.commit()
    session.close()
    print()
    click.echo(f'User {user.username} deleted successfully.')

# Snippet commands
@click.argument('title')
@click.argument('content')
@click.argument('language')
@click.argument('user_id')
@click.argument('category_id', required=False)
def add_snippet(title, content, language, user_id, category_id=None):
    """Add a new snippet."""
    session = Session()
    new_snippet = Snippet(title=title, content=content, language=language, user_id=user_id, category_id=category_id)
    session.add(new_snippet)
    session.commit()
    session.close()
    print()
    click.echo(f'Snippet {title} added successfully.')

@click.argument('snippet_id')
@click.argument('title', required=False)
@click.argument('content', required=False)
@click.argument('language', required=False)
def edit_snippet(snippet_id, title, content, language):
    """Edit an existing snippet."""
    session = Session()
    snippet = session.query(Snippet).get(snippet_id)
    if not snippet:
        click.echo("Snippet not found.")
        return

    if title:
        snippet.title = title
    if content:
        snippet.content = content
    if language:
        snippet.language = language

    session.commit()
    session.close()
    print()
    click.echo(f'Snippet {snippet.title} updated successfully.')

@click.argument('snippet_id')
def delete_snippet(snippet_id):
    """Delete an existing snippet."""
    session = Session()
    snippet = session.query(Snippet).get(snippet_id)
    if not snippet:
        click.echo("Snippet not found.")
        return

    session.delete(snippet)
    session.commit()
    session.close()
    print()
    click.echo(f'Snippet {snippet.title} deleted successfully.')

# Category commands
@click.argument('name')
@click.argument('description', required=False)
def add_category(name, description=None):
    """Add a new category."""
    session = Session()
    new_category = Category(name=name, description=description)
    session.add(new_category)
    session.commit()
    session.close()
    print()
    click.echo(f'Category {name} added successfully.')

@click.argument('category_id')
@click.argument('name', required=False)
@click.argument('description', required=False)
def edit_category(category_id, name, description):
    """Edit an existing category."""
    session = Session()
    category = session.query(Category).get(category_id)
    if not category:
        click.echo("Category not found.")
        return

    if name:
        category.name = name
    if description:
        category.description = description

    session.commit()
    session.close()
    print()
    click.echo(f'Category {category.name} updated successfully.')

@click.argument('category_id')
def delete_category(category_id):
    """Delete an existing category."""
    session = Session()
    category = session.query(Category).get(category_id)
    if not category:
        click.echo("Category not found.")
        return

    session.delete(category)
    session.commit()
    session.close()
    print()
    click.echo(f'Category {category.name} deleted successfully.')

# Tag commands
@click.argument('name')
def add_tag(name):
    """Add a new tag."""
    session = Session()
    new_tag = Tag(name=name)
    session.add(new_tag)
    session.commit()
    session.close()
    print()
    click.echo(f'Tag {name} added successfully.')

@click.argument('tag_id')
@click.argument('name', required=False)
def edit_tag(tag_id, name):
    """Edit an existing tag."""
    session = Session()
    tag = session.query(Tag).get(tag_id)
    if not tag:
        click.echo("Tag not found.")
        return

    if name:
        tag.name = name

    session.commit()
    session.close()
    click.echo(f'Tag {tag.name} updated successfully.')

@click.argument('tag_id')
def delete_tag(tag_id):
    """Delete an existing tag."""
    session = Session()
    tag = session.query(Tag).get(tag_id)
    if not tag:
        click.echo("Tag not found.")
        return

    session.delete(tag)
    session.commit()
    session.close()
    click.echo(f'Tag {tag.name} deleted successfully.')
def list_users():
    """List all users."""
    session = Session()
    users = session.query(User).all()
    session.close()

    if users:
        print()
        print("List of Users:")
        for user in users:
            print(f"ID: {user.user_id}, Username: {user.username}, Email: {user.email}")
    else:
        print("No users found.")
def list_snippets():
    """List all snippets."""
    session = Session()
    snippets = session.query(Snippet).all()
    session.close()

    if snippets:
        print()    
        print()
        print()
        for snippet in snippets:
            print(f"ID: {snippet.snippet_id}, Title: {snippet.title}, Language: {snippet.language}, User ID: {snippet.user_id}")
            print(f"Content: {snippet.content}")
            print("-" * 60) 
    else:
        print("No snippets found.")
def list_tags():
    """List all tags and their associated snippets."""
    session = Session()
    tag_name = input("Enter the name of the tag: ").strip()

    # Check if the tag name matches any snippet language
    matching_snippets = session.query(Snippet).filter(Snippet.language == tag_name).all()

    if matching_snippets:
        print()
        print(f"Snippets with language '{tag_name}':")
        for snippet in matching_snippets:
            print()
            print(f" - {snippet.title}")
            print()
            print(f"Content: {snippet.content}")

    else:
        # No matching snippets found, list all tags and their associated snippets
        tags = session.query(Tag).all()
        if tags:
            print()
            print("List of Tags:")
            for tag in tags:
                print()
                print(f"Tag ID: {tag.tag_id}, Name: {tag.name}")
                print("Associated Snippets:")
                if tag.snippets:
                    for snippet in tag.snippets:
                        print(f" - ID: {snippet.snippet_id}, Title: {snippet.title}, Language: {snippet.language}, User ID: {snippet.user_id}")
                else:
                    print("No snippets associated with this tag.")
                print("=" * 50)  # Adding a separator line for better readability
        else:
            print("No tags found.")



if __name__ == '__main__':
    print("Welcome to the Snippet Manager!")
    
 