# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from main.models import chatSession


class chatSessionAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date')


admin.site.register(chatSession, chatSessionAdmin)
