from django.contrib import admin
from jobapp.models import hydjob,chenjob,bangjob

# Register your models here.
class hydjobAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phone_number']
admin.site.register(hydjob,hydjobAdmin)

class chenjobAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phone_number']    
admin.site.register(chenjob,chenjobAdmin)
class bangjobAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phone_number'] 
admin.site.register(bangjob,bangjobAdmin)    

