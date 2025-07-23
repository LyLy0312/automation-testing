import allure
import pytest
from tests.xno_gemini.conftest import BaseAgentTest


@allure.feature("Luồng chính XNO")
class TestXNOMainFlow(BaseAgentTest):

    @allure.story("Luồng chính")
    @allure.title("Thực hiện tất cả các thao tác chính trong XNO trong một phiên trình duyệt")
    @pytest.mark.asyncio
    async def test_main_flow(self, llm, browser_session):
        steps = [
            {
                "description": "Thực hiện toàn bộ luồng chính trong XNO",
                "task": (
                    "Go to https://xno.vn/giao-dich, "
                    "click on the 'Bảng giá' tab in the navigation bar, wait for the page to load, "
                    "click on the 'Lọc cổ phiếu' tab in the navigation bar, wait for the page to load, "
                    "click on the 'Gói dịch vụ' tab in the navigation bar, wait for the page to load, "
                    "click on the 'Sàn bot' tab in the navigation bar, wait for the page to load, "
                    "click on the 'XBot AI' tab, wait for the AI interface to load, "
                    "click on the 'Xbot TA' tab, wait for technical analysis charts to load, "
                    "click the search button (with aria-haspopup='dialog'), find the input with aria-label 'Tìm mã CK', type 'HNX', wait for the results to appear, click on the result with text 'HNX - Chỉ số HNX', "
                    "go to https://xno.vn/loc-co-phieu, click on the element with text 'Cổ phiếu giá trị', click on the element with text 'Nhóm thông dụng', click on the button with text 'Lọc', wait for the results to appear, click on the result with text 'BID', "
                    "return a confirmation that all actions were completed successfully"
                ),
                "expected": "all actions were completed successfully"
            }
        ]

        for step in steps:
            with allure.step(step["description"]):
                await self.validate_task(
                    llm,
                    browser_session,
                    step["task"],
                    expected_substring=step["expected"],
                    ignore_case=True
                )