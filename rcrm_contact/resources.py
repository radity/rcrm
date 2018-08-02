from import_export.fields import Field
from import_export.resources import ModelResource

from rcrm_contact.models import Address, Contact, Email, Phone, SocialProfile


# Create Your Resources Here


class ContactResource(ModelResource):
    emails = Field()
    phones = Field()
    instagram = Field()
    twitter = Field()
    facebook = Field()
    skype = Field()
    website = Field()
    linkedin = Field()
    addresses = Field()

    class Meta:
        model = Contact
        fields = (
            'id', 'account', 'first_name', 'last_name', 'gender', 'title',
            'date_of_birth', 'description', 'emails', 'phones', 'addresses',
            'instagram', 'twitter', 'skype', 'facebook', 'linkedin', 'website'
        )
        export_order = fields

    def dehydrate_emails(self, obj):
        emails = Email.objects.filter(contact=obj).values_list('email', flat=True)
        emails = ' & '.join(emails)
        return emails

    def dehydrate_phones(self, obj):
        phones = Phone.objects.filter(contact=obj).values_list('phone', flat=True)
        phones = ' & '.join(phones)
        return phones

    def dehydrate_addresses(self, obj):
        addresses = Address.objects.filter(contact=obj)
        address_list = []
        for address in addresses:
            full_address = address.address + ' - ' + address.city + ' - ' + address.state + ' - ' + address.postcode + ' - ' + address.get_country_display() + ' & '
            address_list.append(full_address)
        return address_list

    def dehydrate_instagram(self, obj):
        instagram = SocialProfile.objects.filter(contact=obj).values_list('instagram', flat=True)
        instagram = ' & '.join(instagram)
        return instagram

    def dehydrate_twitter(self, obj):
        twitter = SocialProfile.objects.filter(contact=obj).values_list('twitter', flat=True)
        twitter = ' & '.join(twitter)
        return twitter

    def dehydrate_facebook(self, obj):
        facebook = SocialProfile.objects.filter(contact=obj).values_list('facebook', flat=True)
        facebook = ' & '.join(facebook)
        return facebook

    def dehydrate_skype(self, obj):
        skype = SocialProfile.objects.filter(contact=obj).values_list('skype', flat=True)
        skype = ' & '.join(skype)
        return skype

    def dehydrate_website(self, obj):
        website = SocialProfile.objects.filter(contact=obj).values_list('website', flat=True)
        website = ' & '.join(website)
        return website

    def dehydrate_linkedin(self, obj):
        linkedin = SocialProfile.objects.filter(contact=obj).values_list('linkedin', flat=True)
        linkedin = ' & '.join(linkedin)
        return linkedin


class ContactImportResource(ModelResource):

    class Meta:
        model = Contact
        import_id_fields = ('id',)
