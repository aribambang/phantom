from typing import TypeVar, Generic, List, Optional
import logging

logger = logging.getLogger(__name__)

T = TypeVar('T')

class BaseRepository(Generic[T]):
    def __init__(self, model: T):

        """
        Initializes the BaseRepository with the specified model.

        Args:
            model (T): The model class for database operations.
        """
        self.model = model
    

    def find_by_id(self, id: int) -> Optional[T]:
        """
        Finds an entity by its ID.

        Args:
            id (int): The ID of the entity to find.

        Returns:
            Optional[T]: The found entity or None if not found.
        """
        from app import db
        return db.session.query(self.model).filter(self.model.id == id).first()
    

    def find_all(self) -> List[T]:
        """
        Finds all entities of the model.

        Returns:
            List[T]: A list of all entities.
        """
        from app import db
        return db.session.query(self.model).all()
    

    def create(self, entity: T) -> T:
        """
        Creates a new entity in the database.

        Args:
            entity (T): The entity to create.

        Returns:
            T: The created entity.
        """
        from app import db
        db.session.add(entity)
        db.session.commit()
        return entity

    def update(self, entity: T) -> T:
        """
        Updates an existing entity in the database.

        Args:
            entity (T): The entity to update.

        Returns:
            T: The updated entity.
        """
        from app import db
        db.session.merge(entity)
        db.session.commit()
        return entity

    def delete(self, id: int) -> None:
        """
        Deletes an entity by its ID.

        Args:
            id (int): The ID of the entity to delete.
        """
        from app import db
        entity = db.session.query(self.model).filter_by(id=id).first()
        if entity:
            try:
                db.session.delete(entity)
                db.session.commit()
            except Exception as e:
                logger.error(f"Error deleting entity with ID {id}: {e}")
                raise e
        else:
            logger.error(f"Entity with ID {id} not found.")
            raise ValueError(f"Entity with ID {id} not found.")