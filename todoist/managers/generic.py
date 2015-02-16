# -*- coding: utf-8 -*-


class Manager(object):

    # should be re-defined in a subclass
    state_name = None
    object_type = None

    def __init__(self, api):
        self.api = api
        # shortcuts
        self.state = self.api.state
        self.queue = self.api.queue


class AllMixin(object):
    def all(self, filt=None):
        return filter(filt, self.state[self.state_name])


class GetByIdMixin(object):

    def get_by_id(self, obj_id):
        """
        Finds and returns the object based on its id.
        """
        for obj in self.state[self.state_name]:
            if obj['id'] == obj_id or obj.temp_id == str(obj_id):
                return obj

        obj = eval('self.api.get_' + self.object_type)(obj_id)
        if self.object_type in obj and 'error' not in obj[self.object_type]:
            return obj[self.object_type]

        return None
