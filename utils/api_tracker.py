from collections import defaultdict

class APIStatusTracker:
    def __init__(self, default_section="Default"):
        self.current_section = default_section
        self.status_counts = defaultdict(lambda: defaultdict(int))
        self.sections = []
        # Khởi tạo section mặc định để tránh IndexError
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

    def print_summary(self):
        print(f"\n=== TỔNG KẾT TRẠNG THÁI API TAB {self.current_section.upper()} ===")
        for section, counts in self.status_counts.items():
            print(f"\nTab: {section}")
            for group in sorted(counts):
                print(f"  Status {group}: {counts[group]} requests")