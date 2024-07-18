from myapp.models import MyModel

encodings = MyModel.objects.all().values('encoding').distinct()
sort_fields = MyModel._meta.get_all_field_names()

print("Encodings:", encodings)
print("Sort Fields:", sort_fields)
