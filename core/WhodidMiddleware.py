from django.db.models import signals
from django.utils.functional import curry
from django.utils.deprecation import MiddlewareMixin


class WhodidMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if not request.method in ('GET', 'HEAD', 'OPTIONS', 'TRACE'):
            if hasattr(request, 'user') and request.user.is_authenticated():
                user = request.user
            else:
                user = None

            mark_whodid = curry(self.mark_whodid, user)
            signals.pre_save.connect(mark_whodid,  dispatch_uid=(
                self.__class__, request,), weak=False)

    def process_response(self, request, response):
        signals.pre_save.disconnect(dispatch_uid=(self.__class__, request,))
        return response

    def mark_whodid(self, user, sender, instance, **kwargs):
        if 'created_by' in instance._meta.fields and not instance.created_by:
            instance.created_by = user
        if 'modified_by' in instance._meta.fields:
            instance.modified_by = user
