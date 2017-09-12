class AdminUserRouter(object):

    def db_for_read(self, model, **hints):
        """
        Attempts to read auth models go to auth_db.
        """
        if model._meta.app_label == 'product':
            return 'default'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write default models go to default.
        """
        if model._meta.app_label == 'product':
            return 'default'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the default app is involved.
        """
        if obj1._meta.app_label == 'product' or \
           obj2._meta.app_label == 'product':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the default app only appears in the 'default'
        database.
        """
        if app_label == 'product':
            return True
        return None