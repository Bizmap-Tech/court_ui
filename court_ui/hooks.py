app_name = "court_ui"
app_title = "Court UI"
app_publisher = "Your Company"
app_description = "Modern UI Theme for Court Management System"
app_icon = "octicon octicon-law"
app_color = "blue"
app_email = "your@email.com"
app_license = "MIT"

# Include custom CSS
app_include_css = [
    "/assets/court_ui/css/court_theme.css"
]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
app_include_css = "/assets/court_ui/css/court_theme.css"

# Desk Notifications
# ---------------
notification_config = "court_ui.notifications.get_notification_config"

# Fixtures
fixtures = [
    {
        "doctype": "Custom Field",
        "filters": [
            ["name", "in", [
                "Case-custom_status",
                "Hearing-custom_priority"
            ]]
        ]
    }
]

# Additional Page Configurations
calendars = [
    {
        "doctype": "Court Hearing",
        "field_map": {
            "start": "hearing_date",
            "end": "hearing_end_date",
            "id": "name",
            "title": "case_number",
            "allDay": "all_day"
        }
    }
]

# Override Frappe Web Theme
website_theme_templates = [
    {
        "name": "Court Theme",
        "template": "templates/court_theme.html"
    }
]