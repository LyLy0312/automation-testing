from collections import defaultdict
import allure

class APIStatusTracker:
    def __init__(self, default_section="Default"):
        self.current_section = default_section
        self.status_counts = defaultdict(lambda: defaultdict(int))
        self.sections = []
        self.set_section(default_section)

    def set_section(self, name):
        self.current_section = name
        self.sections.append({"section": name, "status": None, "url": None})

    def handle_response(self, response):
        if response.request.resource_type in ["xhr", "fetch"]:
            status_group = (response.status // 100) * 100
            self.status_counts[self.current_section][status_group] += 1
            # Kiểm tra nếu sections không rỗng trước khi gán
            if self.sections:
                self.sections[-1]["status"] = response.status
                self.sections[-1]["url"] = response.url
            else:
                # Nếu sections rỗng, tạo một section mặc định
                self.sections.append({"section": self.current_section, "status": response.status, "url": response.url})
            print(f"[{self.current_section}] {response.status} - {response.url}")
            if response.status >= 400:
                print(f"[{self.current_section}] LỖI API: {response.status} - {response.url}")
                # Gắn lỗi API vào Allure
                with allure.step(f"Lỗi API trong section {self.current_section}"):
                    allure.attach(
                        f"Status: {response.status}\nURL: {response.url}",
                        name=f"Lỗi API: {response.status} - {self.current_section}",
                        attachment_type=allure.attachment_type.TEXT
                    )

    def print_summary(self):
        report = f"\n=== TỔNG KẾT TRẠNG THÁI API TAB {self.current_section.upper()} ===\n"
        for section, counts in self.status_counts.items():
            report += f"\nTab: {section}\n"
            for group in sorted(counts):
                report += f"  Status {group}: {counts[group]} requests\n"
                # Gắn chi tiết lỗi API (nếu có) cho trạng thái >= 400
                if group >= 400:
                    for sec in self.sections:
                        if sec["status"] and sec["status"] // 100 * 100 == group and sec["section"] == section:
                            report += f"    LỖI API: {sec['status']} - {sec['url']}\n"

            print(report)

            with allure.step(f"Tổng kết trạng thái API tab {self.current_section}"):
                allure.attach(
                    report,
                    name=f"API Status Summary - {self.current_section}",
                    attachment_type=allure.attachment_type.TEXT
                )