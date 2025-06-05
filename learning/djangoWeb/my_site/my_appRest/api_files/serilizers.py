from rest_framework import serializers
from my_app.models.customer import customer
from my_app.models.address import address

class AddressNewSerializer(serializers.ModelSerializer):
    class Meta:
        model = address
        fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):
    system_email = serializers.SerializerMethodField()
    #addresses = AddressNewSerializer(many=True)
    #addresses = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    addresses = serializers.SlugRelatedField(many=True, read_only=True, slug_field='city')

    class Meta:
        model = customer
        fields = '__all__'
        #exclude = ['password']
        #fields = ['fname', 'email', 'id']

    def get_system_email(self, object):
        systemEmail = object.fname + "mail.com"
        return systemEmail

class CustomerBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = customer
        fields = ['id', 'fname', 'email'] 

class AddressSerializer(serializers.ModelSerializer):
    customer = CustomerBasicSerializer()
    class Meta:
        model = address
        fields = '__all__'



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