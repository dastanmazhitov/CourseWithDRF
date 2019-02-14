from rest_framework import serializers
from .models import *


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        exclude = ('id', )


class BranchSerializer(serializers.ModelSerializer):

    class Meta:
        model = Branch
        exclude = ('id', 'course')



class ContactSerializer(serializers.ModelSerializer):
    type = serializers.SerializerMethodField()

    def get_type(self, obj):
        return obj.get_type_display()

    class Meta:
        model = Contact
        exclude = ('id', 'course')


class CourseSerializer(serializers.ModelSerializer):
    branches = BranchSerializer(many=True)
    contacts = ContactSerializer(many=True)

    class Meta:
        model = Course
        fields = ('id', 'name', 'description', 'category', 'logo', 'contacts', 'branches')


    def create(self, validated_data):
        branches_data = validated_data.pop('branches')
        contacts_data = validated_data.pop('contacts')
        course = Course.objects.create(**validated_data)
        for contact in contacts_data:
            Contact.objects.create(course=course, **contact)
        for branch in branches_data:
            Branch.objects.create(course=course, **branch)

        return course
