from django.test import TestCase, Client
from django.urls import reverse
from base.models import UploadedDocument
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile

class TestViews(TestCase):

    def setUp(self) -> None:
        self.client = Client()
        self.base_url = reverse('base')
        self.test_file_details_url = reverse('doc', args=[13])

        self.user = User.objects.create_user(
            username='test_user',
            email='test@example.com',
            password='test_password',
            first_name='testFirt',
            last_name='testLast'
        )

        self.participant1 = User.objects.create_user(
            username='participant1',
            email='participant1@example.com',
            password='participant_password1'
        )

        self.participant2 = User.objects.create_user(
            username='participant2',
            email='participant2@example.com',
            password='participant_password2'
        )


        self.uploaded_document = UploadedDocument.objects.create(
            id = 13,
            user=self.user,
            file='/home/siham/Desktop/Collaborative Document/media/uploaded_documents/Attribution_services_candidature_3TLLixQ.docx'
        )
        self.uploaded_document.participants.add(self.participant1, self.participant2)






    def test_base_POST(self):
        user = User.objects.create_user(
            username='test_user1',
            email='test1@example.com',
            password='test_password',
            first_name='testFirst1',
            last_name='testLast1'
        )

        participant3 = User.objects.create_user(
            username='participant13',
            email='participant3@example.com',
            password='participant_password1'
        )

        participant4 = User.objects.create_user(
            username='participant4',
            email='participant4@example.com',
            password='participant_password2'
        )

        uploaded_file = UploadedDocument.objects.create(
            user=user,
            file='/home/siham/Desktop/Collaborative Document/media/uploaded_documents/Attribution_services_candidature_3TLLixQ.docx',
        )
        uploaded_file.participants.add(participant3, participant4)

        response = self.client.post(self.base_url,{
            'id': uploaded_file.id,
            'user': user.id,
            'file': uploaded_file.file.name,
            'participants': [participant3.id, participant4.id]
        })

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base/upload_file.html')



        
    def test_file_details_GET(self):
        response = self.client.get(self.test_file_details_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'base/document_detail.html')



    def test_file_details_GET_no_id(self):
        response = self.client.get(self.test_file_details_url)
        self.assertEquals(response.status_code, 404) 



