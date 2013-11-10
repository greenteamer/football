# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'News.subtext'
        db.add_column(u'news_news', 'subtext',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=100),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'News.subtext'
        db.delete_column(u'news_news', 'subtext')


    models = {
        u'news.news': {
            'Meta': {'object_name': 'News'},
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'subtext': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'text': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['news']