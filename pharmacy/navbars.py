from django.conf import settings
from edc_navbar import NavbarItem, site_navbars, Navbar


pharmacy = Navbar(name='pharmacy')

pharmacy.append_item(
    NavbarItem(
        name='patients',
        label='Patients',
        fa_icon='fa-user-plus',
        url_name=settings.DASHBOARD_URL_NAMES.get('patient_listboard_url')))

pharmacy.append_item(
    NavbarItem(
        name='dispensary',
        label='Dispensary',
        fa_icon='fa-medkit',
        url_name=settings.DASHBOARD_URL_NAMES['dispense_listboard_url'],))

site_navbars.register(pharmacy)
