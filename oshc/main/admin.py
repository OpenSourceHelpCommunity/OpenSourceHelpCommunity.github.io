# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from main.models import chatSession, Contest, Journey


class chatSessionAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date')


class journeyAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date')


class contestAdmin(admin.ModelAdmin):
    list_display = ('name', 'link', 'description', 'start_date', 'end_date',
                    'approved')
    actions = ['approve_contest']

    def approve_contest(self, request, queryset):
        contest_approved = queryset.update(approved=True)
        if contest_approved == 1:
            message_bit = "1 contest"
        else:
            message_bit = "{} contests were".format(contest_approved)
        self.message_user(request, "{} approved.".format(message_bit))

    approve_contest.short_description = "Approve"


admin.site.register(chatSession, chatSessionAdmin)
admin.site.register(Journey, journeyAdmin)
admin.site.register(Contest, contestAdmin)
