from rest_framework import serializers
from db.task import Task

class TaskSerializer(serializers.ModelSerializer):
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.eta = validated_data.get('eta' , instance.eta)
        instance.save()
        return instance

    class Meta:
        model = Task
        fields = '__all__'


class TaskPointCalc(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = '__all__'
