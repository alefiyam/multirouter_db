# class UserProductsRouter(object):
#     """
#     A router to control all database operations on models in the
#     auth application.
#     """
#     def db_for_read(self, model, **hints):
#         """
#         Attempts to read auth models go to auth_db.
#         """
#         if model._meta.app_label == 'product':
#             return 'database3'
#         return None

#     def db_for_write(self, model, **hints):
#         """
#         Attempts to write database3 models go to database3.
#         """
#         if model._meta.app_label == 'product':
#             return 'database3'
#         return None

#     def allow_relation(self, obj1, obj2, **hints):
#         """
#         Allow relations if a model in the database3 app is involved.
#         """
#         if obj1._meta.app_label == 'product' or \
#            obj2._meta.app_label == 'product':
#            return True
#         return None

#     def allow_migrate(self, db, app_label, model_name=None, **hints):
#         """
#         Make sure the database3 app only appears in the 'database3'
#         database.
#         """
#         if app_label == 'product':
#             return db == 'database3'
#         return None

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


# class UserProductsRouter(object):

#     def db_for_read(self, model, **hints):
#         return getattr(Product, "_DATABASE", "database3")

#     def db_for_write(self, model, **hints):
#         return getattr(Product, "_DATABASE", "database3")

#     def allow_relation(self, obj1, obj2, **hints):
#         """
#         Relations between objects are allowed if both objects are
#         in the master/slave pool.
#         """
#         db_list = ('database3')
#         return obj1._state.db in db_list and obj2._state.db in db_list

#     def allow_migrate(self, db, model):
#         """
#         All non-auth models end up in this pool.
#         """
#         return True 