from import_export import resources
from .models import Person

class PersonResource(resources.ModelResource):
    class Meta:
        model = Person
        skip_unchanged = False
        report_skipped = True
        #exclude = ('id',)
        import_id_fields = ('email',)
        #fields = ()
        
