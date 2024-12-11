from rest_framework import serializers
from .models import Todo

class TodoSerializers(serializers.ModelSerializer):
    class Meta:
        model=Todo
        fields=['title','description','is_completed','created_at','due_date']
