from datetime import datetime

from dateutil.tz import gettz
from django.apps import AppConfig as DjangoAppConfig
from django.core.management.color import color_style
from edc_base.apps import AppConfig as BaseEdcBaseAppConfig
from edc_data_manager.apps import AppConfig as BaseEdcDataManagerAppConfig
from edc_facility.apps import AppConfig as BaseEdcFacilityAppConfig
from edc_identifier.apps import AppConfig as BaseEdcIdentifierAppConfig
# from edc_metadata.apps import AppConfig as BaseEdcMetadataAppConfig
from edc_protocol.apps import AppConfig as BaseEdcProtocolAppConfig
# from edc_visit_tracking.apps import AppConfig as BaseEdcVisitTrackingAppConfig
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


# class EdcVisitTrackingAppConfig(BaseEdcVisitTrackingAppConfig):
#     visit_models = {
#         'pharma_subject': ('subject_visit', 'pharma_subject.subjectvisit')}
# 
# 
# class EdcFacilityAppConfig(BaseEdcFacilityAppConfig):
#     country = 'botswana'
#     definitions = {
#         '7-day clinic': dict(days=[MO, TU, WE, TH, FR, SA, SU],
#                              slots=[100, 100, 100, 100, 100, 100, 100]),
#         '5-day clinic': dict(days=[MO, TU, WE, TH, FR],
#                              slots=[100, 100, 100, 100, 100])}
# 
# 
# class EdcMetadataAppConfig(BaseEdcMetadataAppConfig):
# 
#     reason_field = {'pharma_subject.subjectvisit': 'reason'}
#     other_visit_reasons = [ 'off study', 'deferred', 'death']
#     other_create_visit_reasons = [
#         'initial_visit/contact', 'fu_visit/contact',
#         'unscheduled_visit/contact', 'missed_visit']
#     create_on_reasons = [SCHEDULED, UNSCHEDULED] + other_create_visit_reasons
#     delete_on_reasons = [LOST_VISIT] + other_visit_reasons
# 
# 
# class EdcDataManagerAppConfig(BaseEdcDataManagerAppConfig):
#     identifier_pattern = subject_identifier
# 
# 
# class EdcSmsAppConfig(BaseEdcSmsAppConfig):
#     locator_model = 'pharma_subject.subjectlocator'
#     consent_model = 'pharma_subject.subjectconsent'
#     sms_model = 'pharma_subject.sms'
