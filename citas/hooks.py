# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "citas"
app_title = "Citas"
app_publisher = "César DiMartino"
app_description = "Citas a Clientes"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "cesardimartino@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/citas/css/citas.css"
# app_include_js = "/assets/citas/js/citas.js"

# include js, css files in header of web template
# web_include_css = "/assets/citas/css/citas.css"
# web_include_js = "/assets/citas/js/citas.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "citas.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "citas.install.before_install"
# after_install = "citas.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "citas.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"citas.tasks.all"
# 	],
# 	"daily": [
# 		"citas.tasks.daily"
# 	],
# 	"hourly": [
# 		"citas.tasks.hourly"
# 	],
# 	"weekly": [
# 		"citas.tasks.weekly"
# 	]
# 	"monthly": [
# 		"citas.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "citas.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "citas.event.get_events"
# }

