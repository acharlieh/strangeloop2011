from django.contrib import admin
from yabl.entries.models import Entry

admin.site.register(Entry,
        prepopulated_fields = {'slug': ['headline']}
)
