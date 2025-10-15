from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from accounts.models import Tenant, Membership, Roles

class Command(BaseCommand):
    help = "Create initial tenant and SuperAdmin membership"

    def add_arguments(self, parser):
        parser.add_argument("--tenant-name", default="Skoga")
        parser.add_argument("--tenant-slug", default="skoga")
        parser.add_argument("--domain", default="")
        parser.add_argument("--email", required=True)
        parser.add_argument("--password", required=True)

    def handle(self, *args, **opts):
        User = get_user_model()

        tenant, _ = Tenant.objects.get_or_create(
            slug=opts["tenant_slug"],
            defaults={"name": opts["tenant_name"], "domain": opts["domain"]},
        )
        self.stdout.write(self.style.SUCCESS(f"Tenant ready: {tenant}"))

        user, created = User.objects.get_or_create(
            email=opts["email"],
            defaults={"username": opts["email"].split("@")[0]},
        )
        if created:
            user.set_password(opts["password"])
            user.is_staff = True
            user.is_superuser = True
            user.save()
            self.stdout.write(self.style.SUCCESS(f"Created user: {user.email}"))

        Membership.objects.get_or_create(user=user, tenant=tenant, role=Roles.SUPERADMIN)
        self.stdout.write(self.style.SUCCESS("SuperAdmin membership ensured."))
