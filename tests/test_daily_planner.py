import unittest
from unittest.mock import patch, mock_open
import planner

class TestDailyPlanner(unittest.TestCase):

    def test_load_tasks_file_missing(self):
        with patch("os.path.exists", return_value=False):
            self.assertEqual(planner.load_tasks(), [])

    def test_load_tasks_with_content(self):
        mock_data = "8:00 AM - Breakfast [Everyday]\n10:00 AM - Coding [Work]\n"
        with patch("os.path.exists", return_value=True), \
             patch("builtins.open", mock_open(read_data=mock_data)):
            tasks = planner.load_tasks()
            self.assertEqual(tasks, [
                "8:00 AM - Breakfast [Everyday]",
                "10:00 AM - Coding [Work]"
            ])

    def test_save_tasks_writes_correctly(self):
        tasks = ["9:00 AM - Meeting [Work]", "6:00 PM - Gym [Personal]"]
        m = mock_open()
        with patch("builtins.open", m):
            planner.save_tasks(tasks)
        m().write.assert_any_call("9:00 AM - Meeting [Work]\n")
        m().write.assert_any_call("6:00 PM - Gym [Personal]\n")

    def test_add_task_formatting(self):
        with patch("planner.input", side_effect=["7:00 AM", "Jogging", "2"]), \
             patch("planner.save_tasks") as mock_save, \
             patch("planner.load_tasks", return_value=[]):
            planner.add_task()
            mock_save.assert_called_once_with(["7:00 AM - Jogging [Personal]"])

    def test_remove_task_valid(self):
        tasks = ["8:00 AM - Breakfast [Everyday]", "10:00 AM - Coding [Work]"]
        with patch("planner.input", return_value="2"), \
             patch("planner.load_tasks", return_value=tasks.copy()), \
             patch("planner.save_tasks") as mock_save:
            planner.remove_task()
            mock_save.assert_called_once_with(["8:00 AM - Breakfast [Everyday]"])

    def test_clear_tasks_confirmed(self):
        with patch("planner.input", return_value="y"), \
             patch("planner.save_tasks") as mock_save:
            planner.clear_tasks()
            mock_save.assert_called_once_with([])

    def test_clear_tasks_cancelled(self):
        with patch("planner.input", return_value="n"), \
             patch("planner.save_tasks") as mock_save:
            planner.clear_tasks()
            mock_save.assert_not_called()

if __name__ == "__main__":
    unittest.main()
