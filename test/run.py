"""
🧭 This test file turns each JSON case into its own unittest so every
scenario gets clear pass/fail reporting, plus a small timeout guard.

Instead of putting all cases inside one big `test()` loop, we generate
one real test method per case. That way, `unittest` can show exactly
which scenario passed or failed in verbose mode. 
"""

import sys
import json
import os
import time
import unittest
from typing import Dict, List, Optional
from timeout_decorator import TimeoutError, timeout
from source.solution import Solution
from treenode import TreeNode

def _to_test_name(title: str) -> str:
    # 🏷️ Convert each friendly title into a safe unittest method name.
    sanitized   = ''.join(char.lower() if char.isalnum() else '_' for char in title)
    compact     = '_'.join(part for part in sanitized.split('_') if part)
    return f'test_{compact}'

def _create_binary_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    """🌳 Build a binary tree from its level-order representation."""

    # 🌱 An empty list represents an empty tree.
    if not values:
        return None

    # 🏠 Create the root node from the first value.
    root: TreeNode = TreeNode(val=values[0])

    # 🚶 Keep track of nodes whose children are yet to be assigned.
    queue: List[TreeNode] = [root]

    index: int = 1
    n: int = len(values)

    while index < n:
        # 👨‍👦 Get the next parent waiting for its children.
        parent: TreeNode = queue.pop(0)

        # ◀️ Create the left child when a value exists.
        if index < n and values[index] is not None:
            parent.left = TreeNode(val=values[index])
            queue.append(parent.left)

        index += 1

        # ▶️ Create the right child when a value exists.
        if index < n and values[index] is not None:
            parent.right = TreeNode(val=values[index])
            queue.append(parent.right)

        index += 1

    return root

def _make_testcase(testcase):
    # 🧱 Build one real unittest method per JSON case for better test output.
    def test_method(self):
        title: str = testcase['title']
        p: List[int]   = testcase['input']['p']
        q: List[int]   = testcase['input']['q']
        expected_output: List[int] = testcase['output']
        description    : str       = testcase.get('description', 'No description provided.')
        
        self._case_title        = title
        self._case_description  = description

        print('\n' + '=' * 60)
        print(f'🧪 Test Case : {title}')
        print(f'🤔 Scenario  : {description}')
        print(f'📝 Input : p={p}, q={q}')
        print('⏳ Starting soon...')
        time.sleep(self.DISPLAY_DELAY_SECONDS)

        try:
            ptree: Optional[TreeNode] = _create_binary_tree(p)
            qtree: Optional[TreeNode] = _create_binary_tree(q)
            actual_output: bool = self._run_case(p=ptree, q=qtree)
        except TimeoutError:
            print(f'⏱️ Result    : Time Limit Exceeded in {title}')
            print('=' * 60)
            self.fail(f'⏱️ Time Limit Exceeded: {title}')

        if actual_output == expected_output:
            print(f'✅ Result    : Passed with answer {actual_output}')
        else:
            print(f'❌ Result    : Expected {expected_output}, got {actual_output}')

        print('=' * 60)
        time.sleep(self.DISPLAY_DELAY_SECONDS)

        self.assertEqual(
            actual_output,
            expected_output,
            f'❌ Value Mismatch in {title}\n'
            f'Expected = {expected_output}\n'
            f'Actual   = {actual_output}'
        )

    return test_method


class TestSolution(unittest.TestCase):
    # 🎛️ Tweak this to make the test run faster or more cinematic.
    DISPLAY_DELAY_SECONDS = 2
    CASE_RESULTS: List[Dict[str, str]] = []

    def setUp(self):
        # 🛠️ Each test gets a fresh solution instance to keep runs predictable.
        self.__solution = Solution()
        return super().setUp()

    @timeout(1)
    def _run_case(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # ⚡ Give every testcase its own timeout instead of timing the whole file.
        return self.__solution.isSameTree(p=p, q=q)

class SameTreeTestResult(unittest.TextTestResult):
    # 🧾 Capture each testcase outcome so we can print one final summary.
    def addSuccess(self, test):
        super().addSuccess(test)
        TestSolution.CASE_RESULTS.append(
            {
                'title': getattr(test, '_case_title', test._testMethodName),
                'status': '✅ Passed',
            }
        )

    def addFailure(self, test, err):
        super().addFailure(test, err)
        TestSolution.CASE_RESULTS.append(
            {
                'title': getattr(test, '_case_title', test._testMethodName),
                'status': '❌ Failed',
            }
        )

    def addError(self, test, err):
        super().addError(test, err)
        TestSolution.CASE_RESULTS.append(
            {
                'title': getattr(test, '_case_title', test._testMethodName),
                'status': '💥 Error',
            }
        )

    def stopTestRun(self):
        super().stopTestRun()

        print('\n' + '🧾' + '=' * 58)
        print('📚 Partition List Final Summary')

        if not TestSolution.CASE_RESULTS:
            print('No test cases were executed.')
            print('=' * 60)
            return

        passed_count    = sum(result['status'] == '✅ Passed' for result in TestSolution.CASE_RESULTS)
        failed_count    = sum(result['status'] == '❌ Failed' for result in TestSolution.CASE_RESULTS)
        error_count     = sum(result['status'] == '💥 Error' for result in TestSolution.CASE_RESULTS)
        success_rate    = (passed_count / len(TestSolution.CASE_RESULTS)) * 100
        title_width     = max(len('Test Case'), *(len(result['title']) for result in TestSolution.CASE_RESULTS))
        status_width    = max(len('Status'), *(len(result['status']) for result in TestSolution.CASE_RESULTS))

        divider = f"+-{'-' * title_width}-+-{'-' * status_width}-+"
        header  = f"| {'Test Case'.ljust(title_width)} | {'Status'.ljust(status_width)} |"

        print(divider)
        print(header)
        print(divider)
        for result in TestSolution.CASE_RESULTS:
            print(f"| {result['title'].ljust(title_width)} | {result['status'].ljust(status_width)} |")
        print(divider)

        print(
            f'🏁 Total: {len(TestSolution.CASE_RESULTS)} | '
            f'✅ Passed: {passed_count} | '
            f'❌ Failed: {failed_count} | '
            f'💥 Errors: {error_count}'
        )
        print(f'📈 Success Rate: {success_rate:.2f}%')
        print('=' * 60)

is_pr_run = '--pr' in sys.argv

if is_pr_run:
    sys.argv.remove('--pr')

_CURRENT_DIRECTORY  = os.path.dirname(os.path.abspath(__file__))
_FILE_NAME = 'cases_pr.json' if is_pr_run else 'cases.json'
_FILE_PATH = os.path.join(_CURRENT_DIRECTORY, _FILE_NAME)


with open(_FILE_PATH, mode='r', encoding='utf-8') as read_file:
    all_testcases = json.load(read_file)

    # 🧪 Register every case as a standalone test so verbose mode is meaningful.
    for testcase in all_testcases:
        setattr(TestSolution, _to_test_name(testcase['title']), _make_testcase(testcase))


if __name__ == '__main__':
    unittest.main(
        verbosity=2,
        testRunner=unittest.TextTestRunner(resultclass=SameTreeTestResult)
    )
