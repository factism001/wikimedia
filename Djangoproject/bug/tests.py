from django.test import TestCase, Client
from django.utils import timezone
from .models import Bug
from django.urls import reverse
from .forms import BugForm
from .views import index, register_bug, view_bug

# Create your tests here.

class BugModelTestCase(TestCase):
    def test_bug_creation(self):
        """
        Test the creation of a bug.

        This function creates a new bug object with the following attributes:
        - description: "Test Bug"
        - bug_type: "error"
        - report_date: the current date and time
        - status: "todo"

        The function then asserts the following conditions:
        - The bug's description is "Test Bug"
        - The bug's bug_type is "error"
        - The bug's report_date is not None
        - The bug's status is "todo"
        """
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
        """
        Test the `str` method of the `Bug` model.

        Creates a new `Bug` object with a description, bug type, report date, and status.
        Asserts that the `str` method of the `Bug` object returns the correct string representation.

        Parameters:
            self (TestCase): The current test case.

        Returns:
            None
        """
        bug = Bug.objects.create(
            description="Another Bug",
            bug_type="new_feature",
            report_date=timezone.now(),
            status="inprogress"
        )
        self.assertEqual(str(bug), "Another Bug")

    def test_bug_type_choices(self):
        """
        Test the bug type choices.

        This function creates bug objects with different bug types and asserts that the bug types are correctly
        stored in the database.

        Parameters:
            self (TestCase): The current test case object.

        Returns:
            None
        """
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
        """
        Test the status choices of the Bug model.

        This function creates Bug instances with different status choices and then 
        checks if the distinct status choices in the database match the expected 
        choices.

        Parameters:
        - self: The reference to the current instance of the test class.

        Returns:
        - None
        """
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
        """
        Set up the test environment before running each test case.

        This function creates a Bug object with the following attributes:
            - description: a string representing the description of the bug.
            - bug_type: a string representing the type of the bug.
            - report_date: a string representing the date the bug was reported.
            - status: a string representing the current status of the bug.

        This function does not have any parameters.

        This function does not return anything.
        """
        self.bug = Bug.objects.create(
            description="Test Bug",
            bug_type="error",
            report_date="2023-10-01",
            status="todo"
        )

    def test_index_view(self):
        """
        Function to test the index view.
        """
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        self.assertContains(response, self.bug.description)

    def test_register_bug_view_get(self):
        """
        Test the GET request for the register_bug view.

        This function sends a GET request to the register_bug view and checks
        that the response status code is 200. It also asserts that the
        'bug_register.html' template is used and that the context contains a
        'form' instance of the BugForm class.

        Parameters:
            self (TestCase): The current test case instance.

        Returns:
            None
        """
        response = self.client.get(reverse('register_bug'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bug_register.html')
        self.assertIsInstance(response.context['form'], BugForm)

    def test_register_bug_view_post(self):
        """
        Test the functionality of the `register_bug` view when making a POST request.

        This function sends a POST request to the `register_bug` endpoint with a test bug
        payload. It then asserts that the response status code is 302, indicating a
        successful redirect after the POST request. Additionally, it checks if a new bug
        was created by asserting that the count of `Bug` objects is 2.

        Returns:
            None
        """
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
        """
        Test the view_bug_view function.
        
        This function tests the behavior of the view_bug_view function by making a GET request to the 
        'view_bug' URL with the bug ID as a parameter. It checks that the response status code is 200, 
        that the 'bug_detail.html' template is used, and that the bug object in the response context is 
        equal to the self.bug object.
        """
        response = self.client.get(reverse('view_bug', args=[self.bug.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bug_detail.html')
        self.assertEqual(response.context['bug'], self.bug)

