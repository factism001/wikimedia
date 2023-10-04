from django.test import TestCase, Client
from django.utils import timezone
from .models import Bug
from django.urls import reverse
from .forms import BugForm
from .views import index, register_bug, view_bug

# Create your tests here.

class BugModelTestCase(TestCase):
    def test_bug_creation(self):
        bug = Bug.objects.create(
            description="Test Bug",
            bug_type="error",
            report_date=timezone.now(),
            status="todo"
        )
        self.assertEqual(bug.description, "Test Bug")
        self.assertEqual(bug.bug_type, "error")
        self.assertIsNotNone(bug.report_date)
        self.assertEqual(bug.status, "todo")

    def test_bug_str_method(self):
        bug = Bug.objects.create(
            description="Another Bug",
            bug_type="new_feature",
            report_date=timezone.now(),
            status="inprogress"
        )
        self.assertEqual(str(bug), "Another Bug")

    def test_bug_type_choices(self):
        for choice in Bug.BUG_TYPES:
            Bug.objects.create(
                description=f"Bug with type {choice[1]}",
                bug_type=choice[0],
                report_date=timezone.now(),
                status="done"
            )
        bug_types = Bug.objects.values_list('bug_type', flat=True).distinct()
        self.assertCountEqual(bug_types, [choice[0] for choice in Bug.BUG_TYPES])

    def test_status_choices(self):
        for choice in Bug.STATUS_CHOICES:
            Bug.objects.create(
                description=f"Bug with status {choice[1]}",
                bug_type="other",
                report_date=timezone.now(),
                status=choice[0]
            )
        statuses = Bug.objects.values_list('status', flat=True).distinct()
        self.assertCountEqual(statuses, [choice[0] for choice in Bug.STATUS_CHOICES])


class BugViewTests(TestCase):
    def setUp(self):
        self.bug = Bug.objects.create(
            description="Test Bug",
            bug_type="error",
            report_date="2023-10-01",
            status="todo"
        )

    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        self.assertContains(response, self.bug.description)

    def test_register_bug_view_get(self):
        response = self.client.get(reverse('register_bug'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bug_register.html')
        self.assertIsInstance(response.context['form'], BugForm)

    def test_register_bug_view_post(self):
        data = {
            'description': 'New Test Bug',
            'bug_type': 'error',
            'report_date': '2023-10-02',
            'status': 'todo'
        }
        response = self.client.post(reverse('register_bug'), data)
        self.assertEqual(response.status_code, 302)  # Should redirect after a successful POST
        self.assertEqual(Bug.objects.count(), 2)  # Check if a new bug was created

    def test_view_bug_view(self):
        response = self.client.get(reverse('view_bug', args=[self.bug.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bug_detail.html')
        self.assertEqual(response.context['bug'], self.bug)

