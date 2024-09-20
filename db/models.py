from sqlalchemy import create_engine, Column, Integer, String, Text, TIMESTAMP, ForeignKey, func, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker


engine = create_engine('sqlite:///snippet_manager.db', echo=True)


Base = declarative_base()

# association table for the many-to-many relationship between Snippets and Tags
snippet_tag = Table('snippet_tag', Base.metadata,
    Column('snippet_id', Integer, ForeignKey('snippet.snippet_id'), primary_key=True),
    Column('tag_id', Integer, ForeignKey('tag.tag_id'), primary_key=True)
)

class Category(Base):
    __tablename__ = 'category'

    category_id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, unique=True)
    description = Column(String(255))
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.current_timestamp())

    snippets = relationship('Snippet', backref='category')

    def __repr__(self):
        return f"<Category(category_id={self.category_id}, name={self.name})>"

class Snippet(Base):
    __tablename__ = 'snippet'

    snippet_id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    content = Column(Text, nullable=False)
    language = Column(String(50), nullable=False)
    user_id = Column(Integer, ForeignKey('user.user_id', ondelete='CASCADE'), nullable=False)
    category_id = Column(Integer, ForeignKey('category.category_id', ondelete='SET NULL'))

    created_at = Column(TIMESTAMP, server_default=func.now())

    tags = relationship('Tag', secondary=snippet_tag, back_populates='snippets')

    def __repr__(self):
        return f"<Snippet(snippet_id={self.snippet_id}, title={self.title}, language={self.language})>"

class Tag(Base):
    __tablename__ = 'tag'

    tag_id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, unique=True)
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.current_timestamp())

    snippets = relationship('Snippet', secondary=snippet_tag, back_populates='tags')

    def __repr__(self):
        return f"<Tag(tag_id={self.tag_id}, name={self.name})>"

class User(Base):
    __tablename__ = 'user'

    user_id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    created_at = Column(TIMESTAMP, server_default=func.now())

    snippets = relationship('Snippet', backref='author', cascade='all, delete-orphan')

    def __repr__(self):
        return f"<User(user_id={self.user_id}, username={self.username}, email={self.email})>"


Base.metadata.create_all(engine)


Session = sessionmaker(bind=engine)


session = Session()
