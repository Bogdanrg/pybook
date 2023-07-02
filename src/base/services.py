class BaseCRUD:
    """ Base CRUD class for inheriting
    """
    CRUD_MODEL = None

    def safe_get(self, *args, **kwargs) -> CRUD_MODEL:
        try:
            obj = self.CRUD_MODEL.objects.get(**kwargs)
        except self.CRUD_MODEL.DoesNotExist:
            return None
        return obj
