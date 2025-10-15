from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from accounts.models import Tenant, Membership, Roles


class Command(BaseCommand):
    help = "Create an Owner account for a given tenant"

    def add_arguments(self, parser):
        parser.add_argument("--tenant-slug", required=True, help="Slug of the tenant (e.g. 'skoga')")
        parser.add_argument("--email", required=True, help="Owner's email")
        parser.add_argument("--password", required=True, help="Owner's password")
        parser.add_argument("--username", help="Optional username, defaults to email prefix")

    def handle(self, *args, **opts):
        User = get_user_model()

        # Get tenant
        try:
            tenant = Tenant.objects.get(slug=opts["tenant_slug"])
        except Tenant.DoesNotExist:
            self.stderr.write(self.style.ERROR(f"Tenant '{opts['tenant_slug']}' not found."))
            return

        # Create or get user
        username = opts["username"] or opts["email"].split("@")[0]
        user, created = User.objects.get_or_create(
            email=opts["email"],
            defaults={"username": username}
        )

        if created:
            user.set_password(opts["password"])
            user.is_staff = True   # give Django admin access
            user.save()
            self.stdout.write(self.style.SUCCESS(f"Created user {user.email}"))
        else:
            self.stdout.write(f"User {user.email} already exists, skipping creation.")

        # Create membership
        Membership.objects.get_or_create(
            user=user,
            tenant=tenant,
            role=Roles.OWNER
        )
        self.stdout.write(self.style.SUCCESS(
            f"User {user.email} is now an Owner for tenant {tenant.slug}"
        ))
