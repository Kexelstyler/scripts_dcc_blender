# Wheels

Bundle third-party Python dependencies here as `.whl` files, then list each one
in the top-level `wheels = [...]` array of `blender_manifest.toml` (one directory up).

Example manifest entry:

    wheels = [
        "./wheels/requests-2.32.3-py3-none-any.whl",
    ]

Download a wheel with pip:

    pip wheel <package-name> -w ./wheels

Blender Probe extracts and mounts these wheels automatically when you run or debug
the add-on, so imports work in development exactly as they will once the extension
is installed. Wheels built for other platforms are skipped, and extracted wheels are
cached under `.blender_probe/`.

See: https://docs.blender.org/manual/en/latest/advanced/extensions/python_wheels.html