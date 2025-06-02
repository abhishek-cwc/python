from rest_framework import serializers
from my_app.models.customer import customer

class CustomerSerializer(serializers.ModelSerializer):
    system_email = serializers.SerializerMethodField()
    class Meta:
        model = customer
        #fields = '__all__'
        exclude = ['password']
        #fields = ['fname', 'email', 'id']

    def get_system_email(self, object):
        systemEmail = object.fname + "mail.com"
        return systemEmail

        

# class CustomerSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only= True)
#     fname = serializers.CharField()
#     email = serializers.CharField()

#     def create(self, validated_data):
#         return customer.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.fname = validated_data.get('fname', instance.fname)
#         instance.email = validated_data.get('email', instance.email)
#         instance.save()
#         return instance