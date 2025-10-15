from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from accounts.models import Tenant, Membership, Roles

class Command(BaseCommand):
    help = "Create a Staff account for a given tenant"

    def add_arguments(self, parser):
        parser.add_argument("--tenant-slug", required=True)
        parser.add_argument("--email", required=True)
        parser.add_argument("--password", required=True)
        parser.add_argument("--username", help="Optional username, defaults to email prefix")

    def handle(self, *args, **opts):
        User = get_user_model()

        try:
            tenant = Tenant.objects.get(slug=opts["tenant_slug"])
        except Tenant.DoesNotExist:
            self.stderr.write(self.style.ERROR(f"Tenant '{opts['tenant_slug']}' not found."))
            return

        username = opts["username"] or opts["email"].split("@")[0]
        user, created = User.objects.get_or_create(
            email=opts["email"],
            defaults={"username": username}
        )

        if created:
            user.set_password(opts["password"])
            user.is_staff = True  # can log into Django admin if desired
            user.save()
            self.stdout.write(self.style.SUCCESS(f"Created staff user {user.email}"))

        Membership.objects.get_or_create(user=user, tenant=tenant, role=Roles.STAFF)
        self.stdout.write(self.style.SUCCESS(
            f"User {user.email} is now a Staff member for tenant {tenant.slug}"
        ))
