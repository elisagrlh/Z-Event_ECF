class MyDatabaseRouter:
    def db_for_read(self, model, **hints):
        """Envoyer les opérations de lecture pour LiveStats à MongoDB."""
        if model._meta.model_name == 'livestats':
            return 'mongodb'
        return 'default'

    def db_for_write(self, model, **hints):
        """Envoyer les opérations d'écriture pour LiveStats à MongoDB."""
        if model._meta.model_name == 'livestats':
            return 'mongodb'
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        """Autoriser toutes les relations si sur la même base de données."""
        if obj1._state.db == obj2._state.db:
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """Assurer que les migrations pour LiveStats vont seulement à MongoDB."""
        if model_name == 'livestats':
            return db == 'mongodb'
        return db == 'default'
