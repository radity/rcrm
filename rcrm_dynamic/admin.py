from django.contrib.admin import register

from rcrm_dynamic.models import Dynamic,\
    CharfieldModel, TextboxModel, ImageModel,\
    FileModel, DateModel, DateTimeModel,\
    TimeModel, URLModel, BooleanModel

from import_export.admin import ImportExportModelAdmin

# Register your models here.


@register(Dynamic)
class AdminDynamic(ImportExportModelAdmin):
    pass


@register(CharfieldModel)
class AdminDynamic(ImportExportModelAdmin):
    pass


@register(TextboxModel)
class AdminDynamic(ImportExportModelAdmin):
    pass


@register(ImageModel)
class AdminDynamic(ImportExportModelAdmin):
    pass


@register(FileModel)
class AdminDynamic(ImportExportModelAdmin):
    pass


@register(DateModel)
class AdminDynamic(ImportExportModelAdmin):
    pass


@register(DateTimeModel)
class AdminDynamic(ImportExportModelAdmin):
    pass


@register(TimeModel)
class AdminDynamic(ImportExportModelAdmin):
    pass


@register(URLModel)
class AdminDynamic(ImportExportModelAdmin):
    pass


@register(BooleanModel)
class AdminDynamic(ImportExportModelAdmin):
    pass