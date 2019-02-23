from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import *


class CategoryTest(TestCase):

    def simpleTest(self):
        Category.objects.create(
            name='test',
            imgpath='/test/test'
        )

    def TestCategoryName(self):
        category = Category.objects.get(name='test')
        self.assertEqual(
            category_one.name, 'test'
        )


class CourseTest(TestCase):

    def simpleTest(self):
        categ = Category.objects.create(
            name='test',
            imgpath='/test.jpg'
        )

        Course.objects.create(
            category=categ,
            name="Test Name",
            description="It's simple test.",
            logo="/logo.img",
        )

    def TestCourseName(self):
        course_one = Course.objects.get(name='Test Name')
        self.assertEqual(
            course_one.description, 'Simple Test.'
        )



class BranchTest(TestCase):
    def setUp(self):
        Branch.objects.create(
            latitude="Das",
            longitude="asd",
            address="DDDD",
        )

    def test_branch(self):
        branch = Branch.objects.get(latitude='Das')
        self.assertEqual(
            branch.longitude, 'asd'
        )

class ContactTest(TestCase):

    def simpleTest(self):
        Contact.objects.create(
            type = 1,
            value = '4555'
        )

    def test_contact(self):
        cont = Contact.objects.get(value='4555')
        self.assertEqual(
            cont.type, 1
        )



class CoursePostTest(APITestCase):

    def test_create_course(self):
        #url = reverse('courses')
        data = {
            "name": "Das",
            "description": "Das course",
            "category": 1,
            "logo": "http://www.answersfrom.com/wp-content/uploads/2011/09/Not-talanted-but-curious.jpg",
            "contacts": [
                {
                    "type": "PHONE",
                    "value": "+996772675462"
                },
                {
                    "type": "FACEBOOK",
                    "value": "dastan.mazhiotov"
                },
                {
                    "type": "EMAIL",
                    "value": "dastan.majitov1@gmail.com"
                }
            ],
            "branches": [
                {
                    "latitude": "asdsfs",
                    "longitude": "fddfss",
                    "address": "fdfdgfg"
                }
            ]
        }
        response = self.client.post('courses/', data, format='json')
        print()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Course.objects.count(), 1)
        self.assertEqual(Course.objects.get().name, 'Das')


class CourseGetTest(APITestCase):


    def test_get_course(self):
       #url = reverse('courses/')
        response = self.client.get('/courses/')
       # print("Get: " + str(response.status_code))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class CourseGetByIdTest(APITestCase):

    def test_get_by_id(self):
        response = self.client.get('/courses/1/')
        print("Get By Id STATUS: " + str(response.status_code))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class CourseDeleteByIdTest(APITestCase):

    def test_delete_by_id(self):
        response = self.client.delete('/courses/1/')
        print("Delete By Id STATUS: " + str(response.status_code))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
