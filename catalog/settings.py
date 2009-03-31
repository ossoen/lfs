from django.utils.translation import gettext_lazy as _

STANDARD_PRODUCT = "0"
PRODUCT_WITH_VARIANTS = "1"
VARIANT = "2"

PRODUCT_TYPE_LOOKUP = {
    STANDARD_PRODUCT : _(u"Standard"),
    PRODUCT_WITH_VARIANTS : _(u"Product with variants"),
    VARIANT : _(u"Variant"),
}

PRODUCT_TYPE_CHOICES = [
    (STANDARD_PRODUCT, _(u"Standard")),
    (PRODUCT_WITH_VARIANTS, _(u"Product with variants")),
    (VARIANT, _(u"Variant")),
]

PRODUCT_TYPE_FORM_CHOICES = [
    (STANDARD_PRODUCT, _(u"Standard")),
    (PRODUCT_WITH_VARIANTS, _(u"Product with variants")),
]


LIST = 0
SELECT = 1
VARIANTS_DISPLAY_TYPE_CHOICES = [
    (LIST, _(u"List")),
    (SELECT, _(u"Select")),
]

CONTENT_PRODUCTS = 1
CONTENT_CATEGORIES = 2

CONTENT_CHOICES = (
    (CONTENT_PRODUCTS, _(u"Products")),
    (CONTENT_CATEGORIES, _(u"Categories")),
)

DELIVERY_TIME_UNIT_HOURS  = 1
DELIVERY_TIME_UNIT_DAYS   = 2
DELIVERY_TIME_UNIT_WEEKS  = 3
DELIVERY_TIME_UNIT_MONTHS = 4

DELIVERY_TIME_UNIT_CHOICES = (
    (DELIVERY_TIME_UNIT_HOURS, _(u"hours")),
    (DELIVERY_TIME_UNIT_DAYS, _(u"days")),
    (DELIVERY_TIME_UNIT_WEEKS, _(u"weeks")),
    (DELIVERY_TIME_UNIT_MONTHS, _(u"months")),
)

DELIVERY_TIME_UNIT_SINGULAR = {
    DELIVERY_TIME_UNIT_HOURS : _(u"hour"),
    DELIVERY_TIME_UNIT_DAYS : _(u"day"),
    DELIVERY_TIME_UNIT_WEEKS : _(u"week"),
    DELIVERY_TIME_UNIT_MONTHS : _(u"month"),
}

PROPERTY_NUMBER_FIELD = 1
PROPERTY_TEXT_FIELD = 2
PROPERTY_SELECT_FIELD = 3

PROPERTY_TYPE_CHOICES = (
    (PROPERTY_NUMBER_FIELD, _(u"Number field")),
    (PROPERTY_TEXT_FIELD, _(u"Text field")),
    (PROPERTY_SELECT_FIELD, _(u"Select field")),
)