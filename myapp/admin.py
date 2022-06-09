from dataclasses import fields
from django.contrib import admin
from myapp.models import usercomplaints, customer, transfer

'''contact page'''

admin.site.site_header = "GHB DataBase"
# filter 1
# class userAdmin(admin.ModelAdmin):     #only those field will appear to be filled in admin panel
#   fields=["name",'email',"di"]
# admin.site.register(user,userAdmin)

# filter 2 show the data in the form of the table


class usercomplaitsAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "di", "sub", "comp", "addedon"]
    search_field = ["name", "di", "sub"]  # adds a search field to the table
    list_filter = ["sub"]  # filter 3, adds a box with all the names
    # list_editable=["name"]               #filter 4 allows admin to change the fields through the table itself


# allow admin to add dAta to the fileds
admin.site.register(usercomplaints, usercomplaitsAdmin)
# admin.site.register(userprof)


admin.site.register(customer)
admin.site.register(transfer)
