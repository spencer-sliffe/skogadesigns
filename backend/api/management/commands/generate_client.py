# api/management/commands/generate_client.py
from __future__ import annotations
import shutil
import subprocess
from pathlib import Path

from django.core.management.base import BaseCommand, CommandError
from drf_spectacular.generators import SchemaGenerator
from drf_spectacular.renderers import OpenApiJsonRenderer, OpenApiYamlRenderer


class Command(BaseCommand):
    help = (
        "Generate OpenAPI schema from DRF and optionally run frontend client/type generation.\n"
        "Clients supported:\n"
        "  - openapi-typescript (TS types only)\n"
        "  - orval (Axios client + React Query hooks)\n"
        "  - openapi-typescript-codegen (typed request functions; fetch/axios)"
    )

    def add_arguments(self, parser):
        # Schema
        parser.add_argument("--format", choices=["json", "yaml"], default="json",
                           help="Schema output format (default: json)")
        parser.add_argument("--schema-out", default="frontend/openapi.json",
                           help="Path to write the schema file (default: frontend/openapi.json)")
        parser.add_argument("--schema-url", default=None,
                           help="Override schema 'servers[0].url' (e.g., https://api.example.com)")

        # Frontend selection
        parser.add_argument("--client",
                            choices=["none", "openapi-typescript", "orval", "openapi-typescript-codegen"],
                            default="none",
                            help="Run a frontend generator after writing schema (default: none)")
        parser.add_argument("--frontend-dir", default="frontend",
                            help="Frontend working directory (default: ./frontend)")

        # openapi-typescript (types-only)
        parser.add_argument("--ts-out", default="src/api/types.gen.ts",
                            help="Types output path for openapi-typescript (relative to frontend dir)")

        # orval (axios + react-query)
        parser.add_argument("--orval-config", default="orval.config.ts",
                            help="Relative path to Orval config (inside frontend dir)")

        # openapi-typescript-codegen (functions)
        parser.add_argument("--output-dir", default="src/api/client",
                            help="Output dir for openapi-typescript-codegen (relative to frontend dir)")
        parser.add_argument("--codegen-client", choices=["fetch", "axios"], default="fetch",
                            help="HTTP client for openapi-typescript-codegen (default: fetch)")
        parser.add_argument("--use-union-types", action="store_true", default=True,
                            help="Use union types in openapi-typescript-codegen (default: true)")
        parser.add_argument("--force-clean", action="store_true",
                            help="Remove output dir for codegen client before generating")

    def handle(self, *args, **opts):
        fmt: str = opts["format"]
        schema_out = Path(opts["schema_out"])
        client: str = opts["client"]
        frontend_dir = Path(opts["frontend_dir"])
        orval_config = Path(opts["orval_config"])
        ts_out_rel = Path(opts["ts_out"])
        output_dir_rel = Path(opts["output_dir"])
        codegen_http_client: str = opts["codegen_client"]
        use_union_types: bool = bool(opts.get("use_union_types", True))
        force_clean: bool = bool(opts.get("force_clean", False))
        schema_url_override = opts["schema_url"]

        # 1) Generate schema
        self.stdout.write(self.style.NOTICE("Generating OpenAPI schema via drf-spectacular..."))
        generator = SchemaGenerator()
        schema = generator.get_schema(request=None, public=True)

        if schema is None:
            raise CommandError("drf-spectacular returned no schema. Check your DRF/URL conf.")

        # Optional: patch servers
        if schema_url_override:
            schema["servers"] = [{"url": schema_url_override}]

        # 2) Serialize to file
        schema_out.parent.mkdir(parents=True, exist_ok=True)
        if fmt == "json":
            payload = OpenApiJsonRenderer().render(schema)
        else:
            payload = OpenApiYamlRenderer().render(schema)

        schema_out.write_bytes(payload)
        self.stdout.write(self.style.SUCCESS(f"Schema written to {schema_out.resolve()}"))

        # 3) Optionally run frontend generators
        if client == "none":
            self.stdout.write(self.style.WARNING("Skipping frontend generation (client=none)."))
            return

        if not frontend_dir.exists():
            raise CommandError(f"Frontend directory not found: {frontend_dir.resolve()}")

        schema_abs = str(schema_out.resolve())

        if client == "openapi-typescript":
            # Types only
            ts_out_abs = (frontend_dir / ts_out_rel).resolve()
            ts_out_abs.parent.mkdir(parents=True, exist_ok=True)
            cmd = ["npx", "openapi-typescript", schema_abs, "-o", str(ts_out_abs)]
            self._run(cmd, cwd=frontend_dir, label="openapi-typescript")
            self.stdout.write(self.style.SUCCESS(f"Types generated at {ts_out_abs}"))

        elif client == "orval":
            # Axios + React Query hooks via config file
            cfg_path = (frontend_dir / orval_config).resolve()
            if not cfg_path.exists():
                raise CommandError(f"Orval config not found at: {cfg_path}")
            cmd = ["npx", "orval", "--config", str(cfg_path)]
            self._run(cmd, cwd=frontend_dir, label="orval")
            self.stdout.write(self.style.SUCCESS("Orval client generation complete."))

        elif client == "openapi-typescript-codegen":
            # Typed request functions (fetch/axios)
            output_dir_abs = (frontend_dir / output_dir_rel).resolve()
            if force_clean and output_dir_abs.exists():
                self.stdout.write(self.style.NOTICE(f"Cleaning output directory: {output_dir_abs}"))
                shutil.rmtree(output_dir_abs)

            output_dir_abs.mkdir(parents=True, exist_ok=True)

            cmd = [
                "npx", "openapi-typescript-codegen",
                "--input", schema_abs,
                "--output", str(output_dir_abs),
                "--client", codegen_http_client,
            ]
            if use_union_types:
                cmd.append("--useUnionTypes")

            self._run(cmd, cwd=frontend_dir, label="openapi-typescript-codegen")
            self.stdout.write(self.style.SUCCESS(f"Codegen client generated at {output_dir_abs}"))

        self.stdout.write(self.style.SUCCESS("Frontend generation complete."))

    def _run(self, cmd: list[str], cwd: Path, label: str):
        self.stdout.write(self.style.NOTICE(f"Running {label}: {' '.join(cmd)} (cwd={cwd.resolve()})"))
        try:
            subprocess.run(cmd, cwd=str(cwd), check=True)
        except FileNotFoundError:
            raise CommandError(
                f"{label}: command not found. Ensure Node.js is installed and `npx` is on PATH."
            )
        except subprocess.CalledProcessError as e:
            raise CommandError(f"{label} failed with exit code {e.returncode}")
