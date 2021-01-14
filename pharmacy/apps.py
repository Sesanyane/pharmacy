import os
from datetime import datetime
from dateutil.tz import gettz
from django.apps import AppConfig as DjangoAppConfig
from django.conf import settings
from django.core.management.color import color_style
from edc_base.apps import AppConfig as BaseEdcBaseAppConfig
from edc_data_manager.apps import AppConfig as BaseEdcDataManagerAppConfig
from edc_facility.apps import AppConfig as BaseEdcFacilityAppConfig
from edc_identifier.apps import AppConfig as BaseEdcIdentifierAppConfig
from edc_label.apps import AppConfig as BaseEdcLabelAppConfig
from edc_protocol.apps import AppConfig as BaseEdcProtocolAppConfig
from edc_visit_tracking.constants import SCHEDULED, UNSCHEDULED, LOST_VISIT

style = color_style()


class AppConfig(DjangoAppConfig):
    name = 'pharmacy'


class EdcProtocolAppConfig(BaseEdcProtocolAppConfig):
    protocol = 'BHP132'
    protocol_name = 'Pharmacy EDC'
    protocol_number = '045'
    protocol_title = ''
    study_open_datetime = datetime(
        2020, 3, 1, 0, 0, 0, tzinfo=gettz('UTC'))
    study_close_datetime = datetime(
        2025, 12, 1, 0, 0, 0, tzinfo=gettz('UTC'))


class EdcBaseAppConfig(BaseEdcBaseAppConfig):
    project_name = 'Pharmacy EDC'
    institution = 'Botswana-Harvard AIDS Institute'


class EdcIdentifierAppConfig(BaseEdcIdentifierAppConfig):
    identifier_prefix = '045'


class EdcLabelAppConfig(BaseEdcLabelAppConfig):
    default_cups_server_ip = 'localhost'
    default_printer_label = 'pharma_test_printer'
    extra_templates_folder = os.path.join(
        settings.STATIC_ROOT, 'pharmacy', 'label_templates')
